import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cloud_computing_architecture.aws_cloud_computing_architecture_stack import AwsCloudComputingArchitectureStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cloud_computing_architecture/aws_cloud_computing_architecture_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCloudComputingArchitectureStack(app, "aws-cloud-computing-architecture")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
