# API Gateway - Lambda - EFS - S3 
**23 DEC 2021 Hai Tran**

#### Objective  
Create an REST API with API Gateway which trigger a Lambda function to read a object from S3. In addition, 
the Lambda can load large library dependencies from a EFS endpoint. 

#### Architecture 
![aws-s3-vpc-endpoint](https://user-images.githubusercontent.com/20411077/147256007-ac158516-dc0e-4899-9552-ee2030aa1efb.png)
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
- create a EFS file system 
[Reference](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/)
- create an access point 
[Reference](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/)
- CloudFormation template 
```
  AccessPointResource:
    Type: 'AWS::EFS::AccessPoint'
    Properties:
      FileSystemId: !Ref FileSystemResource
      PosixUser:
        Uid: "1000"
        Gid: "1000"
      RootDirectory:
        CreationInfo:
          OwnerGid: "1000"
          OwnerUid: "1000"
          Permissions: "0777"
        Path: "/efs"
```
#### Step 6. Mount EFS access point to EC2 
- Install efs-utils for ubuntun [git repo](https://github.com/aws/efs-utils)
- mount the access point on an EC2 [mount](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html)
- [mount access point command](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html)
- ensure that EC2 and EFS is in the default security group 
```
mount -t efs -o tls,accesspoint=fsap-12345678 fs-12345678: /localmountpoint
```
#### Step 7. Add polcies for Lambda 
- add VPC endpoint S3 because now this is the only way for Lambda to access S3
- policy to add the VPC 
- policy to read and write the EFS 
- policy to read the S3 bucket (just double check) 
- test 
```
import json
import boto3

def lambda_handler(event, context):
    # test read write EFS
    with open("/mnt/efs/data.txt", "w") as file: 
        file.write("Hello from Lambda")
    # test lamba access s3 
    s3Client = boto3.client("s3")
    items = s3Client.list_objects(
        Bucket='haitran-swinburne-2021'
    )
    # parse parameters 
    filename = event["queryStringParameters"]["filename"]
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

#### Step 8. Configure Lambda load dependencies from EFS 
- [recommendation and performance from AWS](https://docs.aws.amazon.com/lambda/latest/dg/services-efs.html)

#### Step 10. Test from web application 
