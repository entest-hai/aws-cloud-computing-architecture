# Create an AWS CodePipeline by using CDK 
# 22 JAN 2022 Hai Tran 
# 
from aws_cdk import (
        App,
        CfnOutput,
        aws_codepipeline, 
        aws_codepipeline_actions,
        Stack
        )

class Pipeline(Stack):
    """
    This create a stack for the aws codepipeline wanted to create 
    """
    def __init__(self, app:App, id: str, props, **kwargs) -> None: 
        super().__init__(app, id, **kwargs)
        # define the s3 artifact 
        source_output = aws_codepipeline.Artifact(artifact_name="source")
        # define the pipeline
        pipeline = aws_codepipeline.Pipeline(
                self, "Pipeline",
                pipeline_name=props['namespace'],
                artifact_bucket=props['bucket'],
                stages=[
                    aws_codepipeline.StageProps(
                        stage_name='Source',
                        actions=[
                            aws_codepipeline_actions.S3SourceAction(
                                bucket=props['bucket'],
                                bucket_key='source.zip',
                                action_name='S3Source',
                                run_order=1,
                                output=source_output,
                                trigger=aws_codepipeline_actions.S3Trigger.POLL
                                )
                            ]
                        ),
                    aws_codepipeline.StageProps(
                        stage_name='Build',
                        actions=[
                            aws_codepipeline_actions.CodeBuildAction(
                                action_name='DockerBuildImages',
                                input=source_output, 
                                project=props['cb_docker_build'],
                                run_order=1
                                )
                            ]
                        )
                    ]
                )
        # give pipeline read write to the bucket 
        props['bucket'].grant_read_write(pipeline.role)

        # pipeline param to get the 
        
        # ctf output 
        CfnOutput(
                self, "PipelineOut",
                description='Pipeline',
                value=pipeline.pipeline_name
                )


