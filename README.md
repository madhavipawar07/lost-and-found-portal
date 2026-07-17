# lost-and-found-portal

## Overview

The Lost & Found Portal is a cloud-based web application that enables users to report, search, view, and manage lost or found items through a simple web interface. The application is hosted as a static website on Amazon S3 and uses AWS serverless services to store and retrieve item information.

Users can submit details such as the item ID, item name, location, concern person, and an image of the lost or found object. Images are securely stored in Amazon S3
, while item details are stored in Amazon DynamoDB. AWS Lambda and Amazon API Gateway provide backend APIs for reporting, searching, displaying, and deleting records.

## Live Demo

http://lost-found-images-s.s3-website.ap-south-1.amazonaws.com

## Features

- Report lost and found items.
- Upload images of lost or found items.
- Search items by name.
- Display all reported items.
- Delete item records.
- Responsive web interface hosted on Amazon S3.
- Serverless backend using AWS Lambda.
- Fast data retrieval using Amazon DynamoDB.

## Technologies Used

- HTML
- CSS
- Python
- AWS SDK (Boto3)

## AWS Services Used

- **Amazon S3**
  - Hosts the static website.
  - Stores uploaded images of lost and found items.

- **Amazon DynamoDB**
  - Stores item details such as ID, item name, location, concern person, and image URL.

- **AWS Lambda**
  - Processes requests for reporting, searching, displaying, and deleting items.

- **Amazon API Gateway**
  - Exposes REST APIs used by the frontend to communicate with Lambda functions.

- **AWS IAM**
  - Provides secure permissions for Lambda to access AWS resources.

## Project Workflow

User

↓

Static Website (Amazon S3)

↓

Amazon API Gateway

↓

AWS Lambda

↓

Amazon DynamoDB (Item Details)

↓

Amazon S3 (Uploaded Images)

↓

Display Results on Website

## Output

<img width="1915" height="973" alt="Screenshot 2026-07-17 105513" src="https://github.com/user-attachments/assets/cb6795cd-5955-43ff-8ec8-a20fdb39bba6" />

<img width="1918" height="972" alt="Screenshot 2026-07-17 105526" src="https://github.com/user-attachments/assets/0af70cbe-d3c0-4001-84ef-e6b042d5c025" />

<img width="1917" height="906" alt="image" src="https://github.com/user-attachments/assets/7cfc7b3a-d800-44e4-93f9-b51ad23bd95f" />




