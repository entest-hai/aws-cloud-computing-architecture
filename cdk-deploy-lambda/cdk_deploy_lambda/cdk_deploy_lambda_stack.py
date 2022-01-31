import os 
from aws_cdk import (
    Stack,
    Duration,
    aws_lambda,
    aws_apigateway,
    CfnOutput
)
from constructs import Construct

class CdkDeployLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        dirname = os.path.dirname(__file__)
        handler = aws_lambda.Function(
                self,
                id="lamdba-deploy-demo",
                code=aws_lambda.Code.from_asset(os.path.join(dirname, "lambda")),
                handler="handler.lambda_handler",
                memory_size=512,
                timeout=Duration.seconds(90),
                runtime=aws_lambda.Runtime.PYTHON_3_8,
                )
        # create api gateway 
        api_gw = aws_apigateway.LambdaRestApi(
                self,
                id="api-lambda-deploy-demo",
                handler=handler
                )
        # get url 
        self.url_output = CfnOutput(self, "Url", value=api_gw.url)
