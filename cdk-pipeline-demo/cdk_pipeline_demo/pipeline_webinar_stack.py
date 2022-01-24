# create a CDK stack constructing a Lambda API
# 23 JAN 2022 Hai Tran

from os import path
from aws_cdk import (
    Stack,
    aws_lambda,
    aws_apigateway,
    aws_codedeploy,
    aws_cloudwatch,
    CfnOutput
)

from constructs import Construct

class PipelinesWebinarStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # get dirname supported by aws
        this_dir = path.dirname(__file__)

        # create lambda
        hander = aws_lambda.Function(
            self,
            "Handler",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            handler='handler.handler',
            code=aws_lambda.Code.from_asset(path.join(this_dir, 'lambda'))
        )

        # create lambda alias
        alias = aws_lambda.Alias(
            self,
            'HandlerAlias',
            alias_name='Current',
            version=hander.current_version
        )

        # create api gateway
        gw = aws_apigateway.LambdaRestApi(
            self,
            "Gateway",
            description='Endpoint for a simple Lambda',
            handler=alias
        )

        # get url of the api endpoint
        self.url_output = CfnOutput(
            self,
            'Url',
            value=gw.url
        )


