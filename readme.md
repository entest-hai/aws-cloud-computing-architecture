# Codepipeline to Deploy A Lambda API Gateway 
**03 JAN 2021 Hai Tran**
### Description 
This note goes through how to create a AWS Codepipeline for a Lambda based API endpint. Below diagram illustrates how things work.</br>
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

### 1. Setup a git repository, lambda code, template.yaml, buildspec.yaml
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
```
### 3. Create a codepipeline 
- 3.1 Source stage </br>
Connect to GitHub version 2. 
- 3.2 Build stage </br>
Create a CodeBuild and configure, need to assign a policy to enable CodeBuild read/write the S3 bucket. 
- 3.3 Deploy stage </br>

### 4. Check results 
Go to AWS API Gateway console, find the new created API endpoint and curl to check. 


