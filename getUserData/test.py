import boto3
import json

def get_message_from_queue(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Met_Test')
    sqs = boto3.resource('sqs')
    queue = sqs.Queue('https://sqs.eu-west-2.amazonaws.com/998292383020/test-mustang-queue')
    resp = queue.receive_messages(
        MaxNumberOfMessages=1)

    for obj in resp:
      new_obj = json.loads(obj.body)
      new_dict = {'Message_Id': new_obj['MessageId']}
      for key, val in new_obj['MessageAttributes'].items():
            new_dict[key] = val['Value']

      entries = table.put_item(Item=new_dict)
    return "Done"


event = {
        "Messages": [
            {
                "MessageId": "11d528df-e12e-4a6b-8186-7a97aeecb2a7",
                "ReceiptHandle": "AQEBXS8Mt+rNF1xvTZANZvoZaEzux7bNVh5FIWWF/dSweZRAHR29Rw37LmWuZpRFpX9hzyfS1dwMJR37iDYkgS5Io1rxUxnUGsK5DfYobn4X/Ev4q9QAZgxR3Pt9peY+SOK//NIJe0h7qiOHVhNnD6cTjzZCqawAvuU0W87PPhSun29EmlIC3/24MgZwqPItYxkpE75Sbqb/hCoG8CP56hh1YXhpVRIJGlG70YKfBpvNsB1lIbl5KNpgy5AvDwvwfl0+ytQTKjRtRpwpqF6Vjs/uKCsQVQMrvOiwbxOQjFGapY8sCxI2MYurqCRq8E12D2rsAF+IeKrL8S2tWs3bVEbCIy/p4CWac4LquqmNtCFqfTaYqDHk4QqrWnFK7a4JiEjTA6/PfC1Wk89gL78B6olSkA==",
                "MD5OfBody": "786f6bb881e4b14a99ea340c7dd718f8",
                "Body": {
                    "Type": "Notification",
                    "MessageId": "17d3753c-7a77-580e-93da-2086290f27a9",
                    "TopicArn": "arn:aws:sns:eu-west-2:021908831235:aws-earth-mo-atmospheric-ukv-prd",
                    "Message": {
                        "model": "mo-atmospheric-ukv-prd",
                        "object_size": 1668568,
                        "forecast_reference_time": "2019-07-29T13:00:00",
                        "forecast_period": "25200",
                        "forecast_period_units": "seconds",
                        "ttl": 1565100980,
                        "time": "2019-07-29T20:00:00",
                        "bucket": "aws-earth-mo-atmospheric-ukv-prd",
                        "key": "ab01b82a46ce2963ec5a6d69a64cef9f2468d81d.nc",
                        "created_time": "2019-07-29T14:13:42",
                        "name": "surface_direct_downwelling_shortwave_flux_in_air"
                    },
                    "Timestamp": "2019-07-30T14:16:24.193Z",
                    "SignatureVersion": "1",
                    "Signature": "VNPUhBPRk9PkzbmHJXl6VG0FwnRH+hRTp+UeGA6b/SCu7uW6rtTyf31/N3TOFKPLIhIOCBavn0tD110E8zZTyOdcV+MO87G2kXKXdNoQgHPDJKXleJLBwxmTSWcZvB+lCxfFUK+5Thw3AB4dLp6mu77Zr4lKyBfeovowXQTX2uvzAAB1QtRIXbnFl7Hlo9kcb5nrdTj6XvUUaqBAFJEL0Lgbg2iwtjKxM3qU91jBwgf2lYdklwpAeOcUzk9F9UITm8T1HwoW6LSjNrZcpHpi9FaqKpAVEZ5PppTvWleltFVypvK20oWiRtHMEmtJBlK4IbB4JbjQ3/l5wy3JeHl3LQ==",
                    "SigningCertURL": "https://sns.eu-west-2.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem",
                    "UnsubscribeURL": "https://sns.eu-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-west-2:021908831235:aws-earth-mo-atmospheric-ukv-prd:2aea5180-e877-4f63-87fb-a3a344f1d5ba",
                    "MessageAttributes": {
                        "forecast_reference_time": {
                            "Type": "String",
                            "Value": "2019-07-29T13:00:00Z"
                        },
                        "name": {
                            "Type": "String",
                            "Value": "surface_direct_downwelling_shortwave_flux_in_air"
                        },
                        "Messages": [
                            {
                                "MessageId": "11d528df-e12e-4a6b-8186-7a97aeecb2a7",
                                "ReceiptHandle": "AQEBXS8Mt+rNF1xvTZANZvoZaEzux7bNVh5FIWWF/dSweZRAHR29Rw37LmWuZpRFpX9hzyfS1dwMJR37iDYkgS5Io1rxUxnUGsK5DfYobn4X/Ev4q9QAZgxR3Pt9peY+SOK//NIJe0h7qiOHVhNnD6cTjzZCqawAvuU0W87PPhSun29EmlIC3/24MgZwqPItYxkpE75Sbqb/hCoG8CP56hh1YXhpVRIJGlG70YKfBpvNsB1lIbl5KNpgy5AvDwvwfl0+ytQTKjRtRpwpqF6Vjs/uKCsQVQMrvOiwbxOQjFGapY8sCxI2MYurqCRq8E12D2rsAF+IeKrL8S2tWs3bVEbCIy/p4CWac4LquqmNtCFqfTaYqDHk4QqrWnFK7a4JiEjTA6/PfC1Wk89gL78B6olSkA==",
                                "MD5OfBody": "786f6bb881e4b14a99ea340c7dd718f8",
                                "Body": {
                                    "Type": "Notification",
                                    "MessageId": "17d3753c-7a77-580e-93da-2086290f27a9",
                                    "TopicArn": "arn:aws:sns:eu-west-2:021908831235:aws-earth-mo-atmospheric-ukv-prd",
                                    "Message": {
                                        "model": "mo-atmospheric-ukv-prd",
                                        "object_size": 1668568,
                                        "forecast_reference_time": "2019-07-29T13:00:00",
                                        "forecast_period": "25200",
                                        "forecast_period_units": "seconds",
                                        "ttl": 1565100980,
                                        "time": "2019-07-29T20:00:00",
                                        "bucket": "aws-earth-mo-atmospheric-ukv-prd",
                                        "key": "ab01b82a46ce2963ec5a6d69a64cef9f2468d81d.nc",
                                        "created_time": "2019-07-29T14:13:42",
                                        "name": "surface_direct_downwelling_shortwave_flux_in_air"
                                    },
                                    "Timestamp": "2019-07-30T14:16:24.193Z",
                                    "SignatureVersion": "1",
                                    "Signature": "VNPUhBPRk9PkzbmHJXl6VG0FwnRH+hRTp+UeGA6b/SCu7uW6rtTyf31/N3TOFKPLIhIOCBavn0tD110E8zZTyOdcV+MO87G2kXKXdNoQgHPDJKXleJLBwxmTSWcZvB+lCxfFUK+5Thw3AB4dLp6mu77Zr4lKyBfeovowXQTX2uvzAAB1QtRIXbnFl7Hlo9kcb5nrdTj6XvUUaqBAFJEL0Lgbg2iwtjKxM3qU91jBwgf2lYdklwpAeOcUzk9F9UITm8T1HwoW6LSjNrZcpHpi9FaqKpAVEZ5PppTvWleltFVypvK20oWiRtHMEmtJBlK4IbB4JbjQ3/l5wy3JeHl3LQ==",
                                    "SigningCertURL": "https://sns.eu-west-2.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem",
                                    "UnsubscribeURL": "https://sns.eu-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-west-2:021908831235:aws-earth-mo-atmospheric-ukv-prd:2aea5180-e877-4f63-87fb-a3a344f1d5ba",
                                    "MessageAttributes": {
                                        "forecast_reference_time": {
                                            "Type": "String",
                                            "Value": "2019-07-29T13:00:00Z"
                                        },
                                        "name": {
                                            "Type": "String",
                                            "Value": "surface_direct_downwelling_shortwave_flux_in_air"
                                        },
                                        "model": {
                                            "Type": "String",
                                            "Value": "mo-atmospheric-ukv-prd"
                                        }
                                    }
                                },
                                "               Attributes": {
                                    "SenderId": "AIDAIVEA3AGEU7NF6DRAG",
                                    "ApproximateFirstReceiveTimestamp": "1564496184232",
                                    "ApproximateReceiveCount": "6",
                                    "SentTimestamp": "1564496184232"
                                }
                            },
                            {
                                "MessageId": "16c11373-239b-4e97-b0fd-ef4bada6ff09",
                                "ReceiptHandle": "AQEBWOK08bCKOZwKNd/v18PD2kz6VCblPmV3xexK4bAxs1+Uj+oOjGQ76BtrpQ2DepEOHxIS8BZsLJRQELM4+H6Hltg1vsoIkJ6rfI3u5+rOe0Z8PxebXj7amQC7SRTQzRAAsqzVeiEI7VTrbaJ+CEyUTXcuvV/Zh6vqIEAxZanD/N6LqYWMQqzBn4CpinuV0zTTbJzL0j2q61XriOVXOShVQxj8gRDHgNPAuTyOwmQmSaRN8qMzEIDaxKekl1H8DF6Z+luyr6IWvMtGxvd68sjunlUZkdY5329sUmHv+++jx1drN36Y3WGq4Cy4+dVmdtWT+XEHQpcOP8oYzvCzWfUf6uIGojYgOX/8pRv+k1y45UGD9vf2Wqo5+d0yotqBbiOrBQbxjPoOCGd7Kdi1qfA+DA==",
                                "MD5OfBody": "e14eff2d1e9a01c44bc0e3c927b69a0e",
                                "Body": {
                                    "               Type": "Notification",
                                    "MessageId": "3e46938d-d0f9-52c4-95e4-c637834a7121",
                                    "TopicArn": "arn:aws:sns:eu-west-2:021908831235:aws-earth-mo-atmospheric-ukv-prd",
                                    "Message": {
                                        "   model": "mo-atmospheric-ukv-prd",
                                        "object_size": 138466,
                                        "forecast_reference_time": "2019-07-29T13:00:00               Z",
                                        "forecast_period": "36000",
                                        "forecast_period_units": "seconds",
                                        "ttl": 1565101039,
                                        "time": "2019-07-29T23:00:00 ",
                                        "bucket": "aws-earth-mo-atmospheric-ukv-prd",
                                        "key": "3e9643d83bbae35f2d82dd5345d75bd428675a5f.nc",
                                        "created_time": "2019-07-29T14:07:34               Z",
                                        "name": "deprecated_snowfall_fraction_of_precipitation_rate"
                                    },
                                    "Timestamp": "2019-07-30T14:17:23.135Z",
                                    "SignatureVersion": "1",
                                    "Signature": "nWbMx61soO5PAiXp/EvtHiZe4+FVaqzie0R2VvnmF1ERe3jgR7fKziTGyRUtIsBMkeIf305UKFJW0vUW/txEis1ty+zDZnDmvmnm4YAgJibobNjzXqOjOE9xtX9kiodsza7iNqNDW3SVW9eXBTRwWIUEnPqNQY5unxr79iL4AJIMHlLQBgQdWZh8oEbUyQeyGyF3LALeGtDbv8ZAS2eg14YGaXmZ/+fulBNnseLtgdaVAJjq9jAxIiSs3Qi2JE2ZhqtVeCdsQKcb7TI/LVnqMASBjP7wgSEGNNnvUGXD85FG+vIarGkhOfuNALai/bTOs6rRtVVRvKiX467B/otDhw==",
                                    "SigningCertURL": "https://sns.eu-west-2.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem",
                                    "UnsubscribeURL": "https://sns.eu-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-west-2:021908831235:aws-earth-mo-atmospheric-ukv-prd:2aea5180-e877-4f63-87fb-a3a344f1d5ba",
                                    "MessageAttributes": {
                                        "forecast_reference_time": {
                                            "Type": "String",
                                            "Value": "2019-07-29T13:00:00Z"
                                        },
                                        "name": {
                                            "Type": "String",
                                            "Value": "deprecated_snowfall_fraction_of_precipitation_rate"
                                        },
                                        "model": {
                                            "Type": "String",
                                            "Value": "mo-atmospheric-ukv-prd"
                                        }
                                    }
                                },
                                "Attributes": {
                                    "SenderId": "AIDAIVEA3AGEU7NF6DRAG",
                                    "ApproximateFirstReceiveTimestamp": "1564496243164",
                                    "ApproximateReceiveCount": "4",
                                    "SentTimestamp": "1564496243164"
                                }
                            }
                        ],
                        "ResponseMetadata": {
                            "RequestId": "d8651f30-1e29-55db-a2ac-4a8a4a26641f",
                            "HTTPStatusCode": 200,
                            "HTTPHeaders": {
                                "x-amzn-requestid": "d8651f30-1e29-55db-a2ac-4a8a4a26641f",
                                "date": "Tue, 30 Jul 2019 14:18:55 GMT",
                                "content-type": "text/xml",
                                "content-length": "6557"
                            },
                            "RetryAttempts": 0
                        }
                    }
                }
            }
        ]
    }
context = dict()
get_message_from_queue(event, context)
