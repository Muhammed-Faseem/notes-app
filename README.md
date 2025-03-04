# NotesApp

# A Django-based web application for managing notes, integrated with AWS DynamoDB for data storage.
# Features

   - Create, read, update, and delete notes.

   - RESTful API for backend communication.

   - AWS DynamoDB for scalable data storage.

# Prerequisites

# Before running the application, ensure you have the following installed:

  - Python 3.9 or higher

  - AWS CLI (optional, for DynamoDB setup)

  - Git (optional, for version control)

# Setup
### Clone the Repository

```
git clone https://github.com/your-username/notesapp.git
cd notesapp
```
### Set Up a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Set Up AWS Credentials

   # Create a .env file in the project root:
    ```
    touch .env
    ```
   # Add your AWS credentials to the .env file:
    ```
    AWS_ACCESS_KEY_ID=your-access-key-id
    AWS_SECRET_ACCESS_KEY=your-secret-access-key
    AWS_REGION=ap-southeast-2
    ```
   # Ensure the .env file is added to .gitignore to prevent it from being uploaded to GitHub:
   ``` 
    .gitignore
    .env
   ```
# Initialize DynamoDB
# Create the DynamoDB Table

### Run the following Python script to create the Note table in DynamoDB:
```
python initialize_dynamodb.py
```
### initialize_dynamodb.py Script
```
import boto3
import os

# Initialize DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION', 'ap-southeast-2')
)

# Create the table
table = dynamodb.create_table(
    TableName='Note',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'  # String type
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait for the table to be created
table.meta.client.get_waiter('table_exists').wait(TableName='Note')
print("DynamoDB table 'Note' created successfully!")
```
### Verify the Table

  # Go to the AWS DynamoDB Console.

  # Check that the Note table has been created.

# Run the Application
### Start the Django Development Server
```
python manage.py runserver
```

Deployment

To deploy the application to a production environment:

    Use AWS Elastic Beanstalk or Heroku for Django backend deployment.

    Use AWS Amplify or Vercel for React frontend deployment (if applicable).
