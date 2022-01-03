import json

def lambda_handler(event, context):
    # response 
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,GET"
        },
         'body': json.dumps({'filename': 'Hello Codepipeline'},  indent=4, sort_keys=True, default=str)
    }

