# Codepipeline to Deploy A Lambda API Gateway 
**03 JAN 2021 TRAN MINH HAI**
### Description 
- When a code commit happens, it will triggers CodeCommit to run tests and output template.yaml for deploy stage. In this case, deploy provider is cloudformation, so the the template.yaml is used to build a stack. The missing part is the manual approval step?
- Source code can be stored in GitHub, Bitbucket, or CodeCommit
- CodeBuild need to be setup via buildspec.yaml
  - Ubuntu environment
  - Python, Nodejs environment
  - Command to run tests 
  - Output template.yaml and upload to a S3 bucket
  - Where th S3 bucket name specified? 
  - Artifacts
  - Therefore, CodeBuild need to be assigned an IAM role to allow writing in to the S3 bucket 
- CodeDeploy in this case has cloudformation as a deploy provider
  - Build a stack given the template.yaml 

### 1. Setup a git repository, lambda code, template.yaml, buildspec.yaml
lambda handler python. This is just a hello lambda function in python. 
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
buildspec.yml, need to provide a S3 bucket where template.yaml will be uploaded to. 
```
version: 0.2
phases:
  install:
  build:
    commands:
      - export BUCKET=haitran-codepipeline-lambda-demo
      - aws cloudformation package --template-file template.yaml --s3-bucket $BUCKET --output-template-file outputtemplate.yaml
artifacts:
  type: zip
  files:
    - template.yaml
    - outputtemplate.yaml

```
template.yaml, there are two options 1) using normal cloudformation template or 2) using SAM. This template is for a lambda function and a API endpoint.  
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

### 3. Create a codepipeline 
- 3.1 Source stage 
- 3.2 Build stage 
- 3.3 Deploy stage 


