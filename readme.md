# CDK Deploy Lambda 
**29 JAN 2022 Hai Tran**

## Setup CDK project 
create an empty dir
```
mkdir cdk-deploy-lambda
```
init cdk 
```
cdk init --language python 
```
the most simple handler 
```
import json 


def lambda_handler(event, context):
    """
    Lambda handler
    """
    # response
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,GET"
        },
         'body': json.dumps({"message": "Hello Lambda"},
                            indent=4,
                            sort_keys=True,
                            default=str)
    }

```

## Option 1. handler without dependencies 
project structure 
```
cdk-deploy-lambda
    - cdk_deploy_lambda
        - cdk_deploy_lambda_stack.py
        - lambda
            - handler.py
    - app.py
```
aws_cdk.aws_lambda.Function 
```
dirname = os.path.dirname(__file__)
```
```
handler = aws_lambda.Function(
  self,
  id="lamdba-deploy-demo",
  code=aws_lambda.Code.from_asset(os.path.join(dirname, "lamdba")),
  handler="handler.handler",
  memory_size=512,
  timeout=Duration.seconds(90),
  runtime=aws_lambda.Runtime.PYTHON_3_8,
) 
```
## Option 2. handler with dependencies 
need to install dependencies into a package togeter with handler.py [reference](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html). Install dependencies in to lambda
```
python -m pip install --user --target lambda
```
local test lambda import 

## Option 3. existing ecr docker image 
review how to build a docker image, it can be built from local or from AWS CodeBuild 
```
sudo docker build -t lambda-image . 
```
tag 
```
sudo docker tag 095b14bf4a04 717869305038.dkr.ecr.ap-southeast-1.amazonaws.com/lambda-image:latest

```
authenticate 
```
aws ecr get-login-password --region ap-southeast-1 | sudo docker login --username AWS --password-stdin 717869305038.dkr.ecr.ap-southeast-1.amazonaws.com

```
create a ecr repository from AWS console, then push to the ecr repository,
```
sudo docker push 717869305038.dkr.ecr.ap-southeast-1.amazonaws.com/lambda-image:latest

```
aws_cdk.aws_lambda.Function 
```
aws_lambda.Function(
    self,
    id="lambda",
    code=aws_lambda.EcrImageCode.from_ecr_image(
        repository=aws_ecr.Repository.from_repository_name(
            self,
            id="lambda-demo",
            repository_name="lambda-image"
        )
    ),
    handler=aws_lambda.Handler.FROM_IMAGE,
    runtime=aws_lambda.Runtime.FROM_IMAGE,
    memory_size=512,
    timeout=Duration.seconds(90),
    architecture=aws_lambda.Architecture.ARM_64
)
```

## Option 4. build ecr docker image 
in this case, an docker image will be built from local asset code and pushed to aws ecr. Here is the project structure. Can be built by local machine or by AWS CodeBuild inside a AWS CDK CodePipeline. 
```
cdk-deploy-lambda
    - cdk_deploy_lambda
        - Dockerfile
        - .dockerignore
        - requirements.txt
        - cdk_deploy_lambda_stack.py
        - lambda
            - handler.py
    - app.py
```

aws_cdk.aws_lambda.Function 
```
aws_lambda.Function(
    self,
    id="lambda",
    code=aws_lambda.EcrImageCode.from_asset_image(
                directory=os.path.join(dirname, "lambda")
            ),
    handler=aws_lambda.Handler.FROM_IMAGE,
    runtime=aws_lambda.Runtime.FROM_IMAGE,
    memory_size=512,
    timeout=Duration.seconds(90),
    architecture=aws_lambda.Architecture.ARM_64
)
```
