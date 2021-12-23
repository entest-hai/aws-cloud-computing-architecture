# 23 DEC 2021 TRAN MINH HAI 
# curl 
# add header to enable CORS form API Gateway and Lambda 
# tag key: 
import json
import boto3
import requests
# load configure 
with open("config.json") as file: 
    config = json.load(file)

def lambda_handler(event, context):
    # parse parameters 
    filename = event["queryStringParameters"]["filename"]
    # client s3 client to read an object from s3 
    s3Client = boto3.client("s3")
    items = s3Client.list_objects(
        Bucket='haitran-swinburne-2021'
    )
    # response 
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,GET"
        },
        'body': json.dumps({'filename': filename, 'item': items},  indent=4, sort_keys=True, default=str)    
    }


# ============================== TEST =================================
# test api endponit 
def testInvokeLambda():
    """
    """
    lambdaClient = boto3.client('lambda')
    res = lambdaClient.invoke(
            FunctionName='testLambdaReadS3Bucket',
            InvocationType="RequestResponse",
            Payload=json.dumps({'queryStringParameters': {'filename': 'STG_111.csv'}}))
    # parse api response 
    data = json.loads(res['Payload'].read())
    print(data)
    print(data['body'])
  


def testAPIEndopint():
    """
    """
    # 

    # configure url with parameter query 
    url = "{0}?filename={1}".format(config['apiEndpoint'],'STG111.csv')
    # call api 
    res = requests.get(url=url)
    # parse response 
    print(res.json())


# ============================== TEST =================================
if __name__=="__main__":
    # testInvokeLambda()
    testAPIEndopint()