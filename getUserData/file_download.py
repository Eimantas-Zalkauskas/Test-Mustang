import boto3
import botocore
import json


def file_download_lambda(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Test-Table-Project-Eimantas')

    # Getting path parameter from json into string
    pathPar = json.dumps(event['pathParameters'])
    strPar = json.loads(pathPar)
    resp = strPar['messageID']

    dbResp = table.get_item(
        Key={
            'Message_Id': resp
        }
    )
    key = dbResp['Item']['key']

    s3 = boto3.resource('s3')
    output = "/tmp/" + key

    try:
        s3.Bucket('aws-earth-mo-atmospheric-ukv-prd').download_file(key, output)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    return {
        'statusCode': 200,
        'body': json.dumps({
            "Message_Id": dbResp['Item']['Message_Id'],
            "forecast_reference_time": dbResp['Item']['forecast_reference_time'],
            "model": dbResp['Item']['model'],
            "name": dbResp['Item']['name']
        })
    }
