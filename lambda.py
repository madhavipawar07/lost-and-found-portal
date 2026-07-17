import json
import boto3
import uuid
from boto3.dynamodb.conditions import Attr

TABLE_NAME = "lost-found-items"
BUCKET_NAME = "lost-found-images-s"

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)
s3 = boto3.client("s3")


def response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }


def lambda_handler(event, context):

    method = event["requestContext"]["http"]["method"]
    path = event["requestContext"]["http"]["path"]

    # ---------------- GET /upload-url ----------------

    if method == "GET" and path == "/upload-url":

        params = event.get("queryStringParameters") or {}

        extension = params.get("ext", "jpg")

        filename = f"{uuid.uuid4()}.{extension}"

        content_type = {
            "jpg": "image/jpeg",
            "jpeg": "image/jpeg",
            "png": "image/png",
            "webp": "image/webp"
        }.get(extension, "image/jpeg")

        upload_url = s3.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": BUCKET_NAME,
                "Key": filename,
                "ContentType": content_type
            },
            ExpiresIn=300
        )

        return response(200, {
            "uploadURL": upload_url,
            "imageURL": f"https://{BUCKET_NAME}.s3.ap-south-1.amazonaws.com/{filename}"
        })

    # ---------------- POST /report ----------------

    elif method == "POST" and path == "/report":

        body = json.loads(event["body"])

        table.put_item(
            Item={
                "itemId": body["itemId"],
                "item": body["item"],
                "location": body["location"],
                "concernPerson": body["concernPerson"],
                "image": body["image"]
            }
        )

        return response(
            200,
            {"message": "Item Added Successfully"}
        )

    # ---------------- GET /items ----------------

    elif method == "GET" and path == "/items":

        data = table.scan()

        return response(
            200,
            data["Items"]
        )

    # ---------------- GET /item ----------------

    elif method == "GET" and path == "/item":

        name = event["queryStringParameters"]["name"]

        data = table.scan(
            FilterExpression=Attr("item").eq(name)
        )

        return response(
            200,
            data["Items"]
        )

    # ---------------- DELETE /item ----------------

    elif method == "DELETE" and path == "/item":

        name = event["queryStringParameters"]["name"]

        data = table.scan(
            FilterExpression=Attr("item").eq(name)
        )

        if len(data["Items"]) > 0:

            table.delete_item(
                Key={
                    "itemId": data["Items"][0]["itemId"]
                }
            )

            return response(
                200,
                {"message": "Item Deleted Successfully"}
            )

        return response(
            404,
            {"message": "Item Not Found"}
        )

    return response(
        404,
        {"message": "Invalid Request"}
    )