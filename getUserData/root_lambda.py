import boto3
import json


def api_root_lambda(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Test-Table-Project-Eimantas')
    pathPar = json.dumps(event['pathParameters'])
    newPar = json.loads(pathPar)

    dbResp = table.scan(
        AttributesToGet=[
            'Message_Id', 'forecast_reference_time', 'key', 'model', 'name'],
        Limit=10,
        Select='SPECIFIC_ATTRIBUTES'
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            "Items": dbResp['Items'],
            "LastEvaluatedKey": dbResp['LastEvaluatedKey']['Message_Id']
        })
    }


