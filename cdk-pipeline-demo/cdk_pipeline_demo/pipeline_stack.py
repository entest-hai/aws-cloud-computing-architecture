# create CDK pipeline from aws_cdk.pipelines.CdkPipeline
# moved to aws_cdk.pipelines.CodePipeline
# different from aws_cdk.aws_codepipeline.Pipeline
# 23 JAN 2022 Hai Tran

from aws_cdk import (
    pipelines,
    aws_codepipeline,
    aws_codepipeline_actions,
    Stack
)
from constructs import Construct

class PipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        source_artifact = aws_codepipeline.Artifact()
        cloud_assembly_artifcat = aws_codepipeline.Artifact()

        # create a cdk pipeline
        pipeline = pipelines.CodePipeline(
            self,
            'Pipeline',
            pipeline_name='WebinarPipeline',
            synth=pipelines.ShellStep(
                'Synth',
                input=pipelines.CodePipelineSource.connection(
                    "entest-hai/aws-cloud-computing-architecture",
                    "codepipeline-lambda",
                    connection_arn="arn:aws:codestar-connections:ap-southeast-1:610770234379:connection/ae577773-a348-472d-96cd-0f3ceb656c09"
                ),
                commands=["pip install -r requirements.txt", "cdk synth"]
            )
        )
