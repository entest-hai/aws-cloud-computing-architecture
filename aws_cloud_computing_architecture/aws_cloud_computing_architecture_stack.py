# create CDK pipeline from aws_cdk.pipelines.CdkPipeline
# moved to aws_cdk.pipelines.CodePipeline
# different from aws_cdk.aws_codepipeline.Pipeline
# 23 JAN 2022 Hai Tran

from aws_cdk import (
    pipelines,
    Stack
)
from constructs import Construct
from .lambda_api_stage import LambdaApiStageDemo

class AwsCloudComputingArchitectureStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # create a cdk pipeline
        pipeline = pipelines.CodePipeline(
            self,
            'Pipeline',
            pipeline_name='CdkPipelineLambdaApiDemo',
            synth=pipelines.ShellStep(
                'Synth',
                input=pipelines.CodePipelineSource.connection(
                    "entest-hai/aws-cloud-computing-architecture",
                    "cdk-pipeline-lambda-api-demo",
                    connection_arn="arn:aws:codestar-connections:ap-southeast-1:610770234379:connection/ae577773-a348-472d-96cd-0f3ceb656c09"
                ),
                commands=["pip install -r requirements.txt", "npm install -g aws-cdk", "cdk synth"]
            )
        )

        # add pre-prod stage
        pipeline.add_stage(
            LambdaApiStageDemo(
                self,
                "pre-prod"
            )
        )

        # add manual review stage with email notification

        # add prod-stage