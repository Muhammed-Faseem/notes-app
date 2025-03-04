import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

try:
    # Specify the AWS profile to use
    session = boto3.Session(profile_name='faseem')

    # Use this session to create the DynamoDB resource
    dynamodb = session.resource('dynamodb')

    # Print credentials for debugging
    credentials = session.get_credentials()
    print("Credentials:", credentials.get_frozen_credentials())

    # Example: Create the table
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
                'AttributeType': 'S'  # String type for ID
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait for the table to be created
    table.meta.client.get_waiter('table_exists').wait(TableName='Note')
    print("Table created successfully!")

except NoCredentialsError:
    print("Error: No credentials found. Please configure your AWS credentials.")
except PartialCredentialsError:
    print("Error: Incomplete credentials. Please check your AWS credentials file.")
except ClientError as e:
    print(f"Error: {e.response['Error']['Message']}")