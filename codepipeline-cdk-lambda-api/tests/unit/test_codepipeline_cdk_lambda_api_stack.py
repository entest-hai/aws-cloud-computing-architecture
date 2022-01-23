import aws_cdk as core
import aws_cdk.assertions as assertions

from codepipeline_cdk_lambda_api.codepipeline_cdk_lambda_api_stack import CodepipelineCdkLambdaApiStack

# example tests. To run these tests, uncomment this file along with the example
# resource in codepipeline_cdk_lambda_api/codepipeline_cdk_lambda_api_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CodepipelineCdkLambdaApiStack(app, "codepipeline-cdk-lambda-api")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
