import boto3
import logging

print('Loading function')


def lambda_handler(event):
    print('Calling LAmbda handler')
    logging.info('Lambda Handler Triggered')
    if event is not None:
        address_name = event['Address']
        return create_dynamoDB(address_name)


def create_dynamoDB(address):

    logging.info('create_dynamoDB method called')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Contact')
    try:
        response = table.put_item(
            Item={
                'Address': address
            }
        )
        print('Response: ', response)
        return 'Success'
    except Exception as e:
        logging.error('Error occurred with Exception')
        return e



