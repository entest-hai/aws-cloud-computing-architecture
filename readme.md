# Codepipeline to Deploy A Lambda API Gateway 
**03 JAN 2021 Hai Tran**
### Description 
This note goes through how to create a AWS Codepipeline for a Lambda based API endpoint. Below diagram illustrates how things work.</br>
![codepipeline_api_gateway](https://user-images.githubusercontent.com/20411077/147917263-f555608d-ef22-454b-9a62-1b76fc94218a.png)
Let's summary roles of each component: 
- **Repository** can be GitHub, Bibucket, AWS CodeCommit 
- **CodeBuild** 
  - We need to create and configure a CodeBuild 
  - We write buildspec.yaml to tell what CodeBuild does
    - Run tests 
    - Build template.yaml and upload to a S3 bucket (need assigned an IAM role)
- **CodeDeploy** 
    - Choose ClodFormation as the deploy provider 
    - Need assigned IAM role to create stacks/resources 

### 1. Setup a git repository, lambda code, template.yaml, buildspec.yaml, a S3 bucket 
Here is a hello **lambda handler** in python 
```
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

```
Here is **buildspec.yml**, it package template.yaml and upload to a S3 bucket. 
```
version: 0.2
phases:
  install:
  build:
    commands:
      - export BUCKET=example-codepipeline-lambda-demo
      - aws cloudformation package --template-file template.yaml --s3-bucket $BUCKET --output-template-file outputtemplate.yaml
artifacts:
  type: zip
  files:
    - template.yaml
    - outputtemplate.yaml
```
Here is **tempalte.yaml** for CodeDeploy to create stacks. This template is to build a simple Lambda function and a API endpoint with API Gateway. Note that there are two way 1) normal cloudformation template or 2) SAM 
```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: Demo codepipeline with lambda api 
Resources:
  TimeFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: lambda_function.lambda_handler
      Runtime: python3.8
      CodeUri: ./
      Events:
        MyTimeApi:
          Type: Api
          Properties:
            Path: /TimeResource
            Method: GET

```
Create a S3 bucket for CodeBuild 
```
example-codepipeline-lambda-demo
```
### 2. Create a IAM role for the codepipeline and cloudformation 
Create an IAM role to allow the CodePipeline to do things 
```
{
    "Statement": [
        {
            "Action": [
                "apigateway:*",
                "codedeploy:*",
                "lambda:*",
                "cloudformation:CreateChangeSet",
                "iam:GetRole",
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:PutRolePolicy",
                "iam:AttachRolePolicy",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy",
                "iam:PassRole",
                "s3:GetObjectVersion",
                "s3:GetBucketVersioning"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ],
    "Version": "2012-10-17"
}
```
Assign a policy to the CodeBuild so it can access the S3 bucket 
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": "arn:aws:s3:::example-codepipeline-lambda-demo/*"
        }
    ]
}
```
### 3. Create a codepipeline 
- 3.1 Source stage </br>
Connect to GitHub version 2. 
- 3.2 Build stage </br>
Create a CodeBuild and configure, need to assign a policy to enable CodeBuild read/write the S3 bucket. 
- 3.3 Deploy stage </br>

### 4. Check results 
Go to AWS Lambda console to check the new created lambd fuction, its names should be 
```
LambdaPipelineDemoStack-TimeFunction-{id}
```
Go to AWS API Gateway console, find the new created API endpoint and curl to check, its name should be 
```
 https://{id}.execute-api.ap-southeast-1.amazonaws.com/Prod/TimeResource
``` 
### 5. There are two S3 bucket 
first one is created by the AWS CodePipeline with this policy <br/>
![bucket_policy](https://user-images.githubusercontent.com/20411077/150976031-38a617eb-a189-4d4e-b8e2-a3501f0e22b0.png)
<br/>
second we need to creaet a S3 bucket to store the outputtemplate.yaml

### 6. Need to add deploy action
before deploy action need to manually execute change set like this <br/>
![deploy_chage_set_execute](https://user-images.githubusercontent.com/20411077/150976232-5cce834d-8870-442e-809d-a32487fc7007.png)

