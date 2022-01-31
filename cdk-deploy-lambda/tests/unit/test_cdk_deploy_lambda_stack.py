import aws_cdk
from cdk_deploy_lambda.cdk_deploy_lambda_stack import CdkDeployLambdaStack

def test_lambda_stack():
    """
    Test lambda stack
    """
    # GIVEN
    app = aws_cdk.App()

    # WHEN
    CdkDeployLambdaStack(app, "Stack")

    # THEN 
    template = app.synth().get_stack_by_name("Stack").template
    functions = [resource for resource in template["Resources"].values()
                if resource["Type"] == "AWS::Lambda::Function"
            ]
    # ASSERT 
    print(functions[0])
