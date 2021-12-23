# API Gateway - Lambda - EFS - S3 
**23 DEC 2021 Hai Tran**

#### Objective  
Create an REST API with API Gateway which trigger a Lambda function to read a object from S3. In addition, 
the Lambda can load large library dependencies from a EFS endpoint. 

#### Step 1. Create a simple hello world function python handler 
```
def lambda_handler(event, context):
    # parse parameters 
    params = event["queryStringParameters"]["filename"]
    # 
    return {
        'statusCode': 200,
        'body': json.dumps({'filename': params})
    }
```

#### Step 2. Configure  API Gatway to trigger the Lambda function 

#### Step 3. Check CORS for Lambda and curl 
Need to add HEADER to the lambda handler 
```
def lambda_handler(event, context):
    # parse parameters 
    filename = event["queryStringParameters"]["filename"]
    # client s3 client to read an object from s3 
    s3Client = boto3.client("s3")
    items = s3Client.list_objects(
        Bucket='bucketname'
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
```
#### Step 4. Configure Lambda access a S3 bucket 
- Need a VPC endpoint. 
- IAM role for the Lambda function to access S3 [reference](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-execution-role-s3-bucket/)
```

  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ExampleStmt",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": [
        "arn:aws:s3:::AWSDOC-EXAMPLE-BUCKET/*"
      ]
    }
  ]
}
```

#### Step 5. Create a EFS endpoint 

#### Step 6. Configure Lambda load dependencies from EFS 

#### Step 7. Lambda write to EFS 

#### Step 8. Test from web application 