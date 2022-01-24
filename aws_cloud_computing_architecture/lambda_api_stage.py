from constructs import Construct
from aws_cdk import (
  Stage
)

from .lambda_api_stack import LambdaApiStackDemo

class LambdaApiStageDemo(Stage):
  def __init__(self, scope: Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    service = LambdaApiStackDemo(self, 'LambdaApiStackDemo')

    self.url_output = service.url_output