import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_deploy_lambda.cdk_deploy_lambda_stack import CdkDeployLambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_deploy_lambda/cdk_deploy_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkDeployLambdaStack(app, "cdk-deploy-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
