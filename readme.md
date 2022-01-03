# Codepipeline to Deploy A Lambda API Gateway 
**03 JAN 2021 TRAN MINH HAI**
### Description 
- When a code commit happens, it will triggers CodeCommit to run tests and output template.yaml for deploy stage. In this case, deploy provider is cloudformation, so the the template.yaml is used to build a stack. The missing part is the manual approval step?
- Source code can be stored in GitHub, Bitbucket, or CodeCommit
- CodeBuild need to be setup via buildspec.yaml
  - Ubuntu environment
  - Python, Nodejs environment
  - Command to run tests 
  - Output template.yaml and upload to a S3 bucket
  - Where th S3 bucket name specified? 
  - Artifacts
  - Therefore, CodeBuild need to be assigned an IAM role to allow writing in to the S3 bucket 
- CodeDeploy in this case has cloudformation as a deploy provider
  - Build a stack given the template.yaml 

### 1. Setup a git repository, lambda code, template.yaml, buildspec.yaml

### 2. Create a IAM role for the codepipeline and cloudformation 

### 3. Create a codepipeline 
- 3.1 Source stage 
- 3.2 Build stage 
- 3.3 Deploy stage 


