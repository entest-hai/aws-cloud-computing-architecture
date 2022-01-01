# Creat a S3 Bucket using CDK 
**01 JAN 2021 TRAN MINH HAI**
### Step 1. install cdk cli and python lib
Before this, need to configure aws cli with IAM
```
aws configure 
~/.aws/credentials
```
```
npm install -g aws-cdk
```
check 
```
cdk --version 
```
cdk python 
```
python -m pip install aws-cdk-lib
import aws_cdk as cdk
```

### Step 2. init cdk app in an empty directory 
```
cdk init app --language python 
```
activate venv which auto generated 
```
source .venv/bin/activate
```
pip install dependencies 
```
python -m pip install -r requirements.txt 
```

### Step 3. Specify env including region and s3 bucket name 
edit app.py 
```
env=cdk.Environment(account='123456789012', region='ap-southeast-1'),
```
edit cdk_s3/cdk_s3_stack.py
```
bucket = s3.Bucket(self, "MyFirstBucket", versioned=False)
```
Deploy 
```
cdk deploy 
```
### Step 4. Check result 
```
aws s3 ls 
```
and should see 
```
cdks3stack-MyFirstBucket606e0bb0-1jzfg4uw6ica7
```

