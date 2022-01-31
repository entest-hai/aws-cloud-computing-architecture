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

## Option 1. handler.py without dependencies 
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
aws_lambda.Function(
    self,
    id="lambda",
    code=lambda_.Code.from_asset(os.path.join(dirname, "lambda")),
    handler=aws_lambda.Handler.FROM_IMAGE,
    runtime=aws_lambda.Runtime.FROM_IMAGE,
    memory_size=512,
    timeout=Duration.seconds(90),
    architecture=aws_lambda.Architecture.ARM_64
)
```
## Option 2. handler.py with dependencies 
need to install dependencies into a package togeter with handler.py [reference](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html). Install dependencies in to lambda
```
python -m pip install --user --target lambda
```
local test lambda import 

## Option 3. existing ecr docker image 
```
aws_lambda.Function(
    self,
    id="lambda",
    code=aws_lambda.EcrImageCode.from_ecr_image(
        repository=aws_ecr.Repository.from_repository_name(
            self,
            id="lambda-demo",
            repository_name="lambda-image-demo"
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
project structure 
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
