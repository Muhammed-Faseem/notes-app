import boto3
from botocore.exceptions import NoCredentialsError, ClientError

class DynamoDBService:
    def __init__(self, table_name):
        self.table_name = table_name
        self.dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id='AKIAW3MEDDOL7LK2T4D3',
            aws_secret_access_key='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',
            region_name='ap-southeast-2'
        )
        self.table = self.dynamodb.Table(table_name)

    def put_item(self, item):
        try:
            response = self.table.put_item(Item=item)
            return response
        except NoCredentialsError:
            return "Error: No credentials found."
        except ClientError as e:
            return f"Error: {e.response['Error']['Message']}"

    def get_item(self, key):
        try:
            response = self.table.get_item(Key=key)
            return response.get('Item')
        except NoCredentialsError:
            return "Error: No credentials found."
        except ClientError as e:
            return f"Error: {e.response['Error']['Message']}"

    def list_items(self):
        try:
            response = self.table.scan()
            return response.get('Items', [])
        except NoCredentialsError:
            return "Error: No credentials found."
        except ClientError as e:
            return f"Error: {e.response['Error']['Message']}"

    def delete_item(self, key):
        try:
            response = self.table.delete_item(Key=key)
            return response
        except NoCredentialsError:
            return "Error: No credentials found."
        except ClientError as e:
            return f"Error: {e.response['Error']['Message']}"