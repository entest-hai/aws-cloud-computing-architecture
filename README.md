
# FHR API Demo with CDK CodePipeline
## 1. Architecture
 It is a simple Lambda based API
 - Lambda function to process FHR 
 - API gateway 
 - S3 bucket to store ECG 
 - Role to enable Lambda to access the S3 bucket 
 - API endpoint open mode for demo  <br/>
 ![pipeline](https://user-images.githubusercontent.com/20411077/151143026-bf89073a-5e3a-409c-8bcf-33a8a48c190f.png)
 <br/>
## 2. Show the FHR API 
Go to this link to try the FHR API [biorithm-fhr-api](https://test.bio-rithm.io/). Optional, walkthrough how the web is built using [AWS Amplify](https://docs.amplify.aws/lib/q/platform/js/), ReactJS, [material UI](https://mui.com/), and the TypeScript code. 

## 3. Load test the API 
##### 3.1 Configuration of the FHR lambda function 
- memory 10240MB RAM 
- timeout 90 seconds 
- reserved concurrency 380
- run time PYTHON 3.8  
- deploy method ecr image  
 
 ##### 3.2 Concurrent requets 
 350 concurrent requests are sent from terminal by **concurrent.futures** a type of thread
```
with concurrent.futures.ThreadPoolExecutor(max_workers=numWorker) as execute:
    execute.map(callApi, ecgS3Paths)
```

##### 3.3 Testing data 
Testing data already uploaded to a S3 bucket with about 350 data records, each limited to 30 minutes of ECG data 
```
aws s3 ls s3://biorithm-testing-data/lambda-batch-load-test/ | wc -l 
```
Let run the test script and analyse the log. Check python environment before running  
```
./run 
```
##### 3.4 Results 
It is important to note that sometimes it can be upto 10% of the requests are timeout. 
- total 350 records within few minutes (less than 5)
- average 26 seconds per data record 
- aws lambda concurrency execution 360 
- success rate can be 10% fail the first time request 
- need queue, retry, and optimisation 

## 4. CDK CodePipeline WalkThrough 
- Create Lambda, Role, Policy, and API from CDK python code 
- Create CDK CodePipeline from CDK python code 
- Add pre-product, product, and manual approval stages <br/>
![stage](https://user-images.githubusercontent.com/20411077/151143670-b859887f-ba65-4781-b75b-88b335abe093.png)
<br/>
## 5. Troubleshooting
```
{
  "queryStringParameters": {
    "filename": "s3://biorithm-testing-data/racer-06-octg/A202.csv"
  }
}
```
test lambda API by curl 
```
curl https://l4n8zxz15h.execute-api.ap-southeast-1.amazonaws.com/prod/?filename=s3://biorithm-testing-data/racer-06-oct/A202.csv

```
