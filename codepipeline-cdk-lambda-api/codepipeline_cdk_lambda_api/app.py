from aws_cdk import App
from pipeline import Pipeline
from base import Base 

props = {'namespace': 'cdk-example-pipeline'}

app = App()

base = Base(app, "{0}-base".format(props['namespace']), props)

pipeline = Pipeline(app, props['namespace'], base.output_props)

pipeline.add_dependency(base)

app.synth()

