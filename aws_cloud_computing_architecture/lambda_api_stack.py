from os import path
from constructs import Construct
from aws_cdk import (
    Stack,
    Duration,
    CfnOutput
)
import aws_cdk.aws_lambda as lmb
import aws_cdk.aws_apigateway as apigw

class LambdaApiStackDemo(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        this_dir = path.dirname(__file__)

        handler = lmb.Function(self, 'Handler',
            runtime=lmb.Runtime.PYTHON_3_7,
            handler='handler.handler',
            code=lmb.Code.from_asset(path.join(this_dir, 'lambda')))

        alias = lmb.Alias(self, 'HandlerAlias',
            alias_name='Current',
            version=handler.current_version)

        gw = apigw.LambdaRestApi(self, 'Gateway',
            description='Endpoint for a simple Lambda-powered web service',
            handler=alias)

        self.url_output = CfnOutput(self, 'Url',
            value=gw.url)