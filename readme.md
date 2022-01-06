# Host a static website using AWS S3 
**16 DEC 2021 Hai Tran** <br>
[AWS reference ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html#step2-create-bucket-config-as-website)

### Create a S3 bucket 
[s3 cli mb](https://docs.aws.amazon.com/cli/latest/reference/s3/mb.html)
```
aws s3 mb s3://bucket-name --region ap-southeast-1
```
verify 
```
aws s3 ls 
```
### Copy web files to S3 
```
aws s3 cp . s3://bucket-name/ --recursive
```
verify 
```
aws s3 ls s3://bucket-name/ --recursive 
```
### 403 error 
By default, Amazon S3 blocks public access to your account and buckets. If you want to use a bucket to host a static website, you can use these steps to edit your block public access settings.

### Configure host a static website 
![enable_static_web_hosting_index](https://user-images.githubusercontent.com/20411077/146595602-22db6843-6282-45ba-814a-bca5040ef716.png)
### Configure bucket policy 
After you edit S3 Block Public Access settings, you can add a bucket policy to grant public read access to your bucket. When you grant public read access, anyone on the internet can access your bucket.

```
{
  "Id": "",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::bucket-name/*",
      "Principal": "*"
    }
  ]
}
```

### Block public bucket access 
Check **public access block** of an account  
```
aws s3control get-public-access-block --account id "your account id"
```
Check **public access block** of a bucket 
```
aws s3api get-public-access-block --bucket haitran-swinburne-2021
```
Result 
```
  "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": false,
        "RestrictPublicBuckets": false
    }
```
Update 
```
aws s3control put-public-access-block --public-access-block-configuration BlockPublicPolicy=true --account-id "your account id"
```

## TODO: Note on S3 
### S3 cost and best practice 
### Configure CORS 
Cross-origin resource sharing (CORS) defines a way for client web applications that are loaded in one domain to interact with resources in a different domain. You can build rich client-side web application with Amazon S3 and selective allow cross-origin access to your Amazon S3 resources. [AWS CORS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManageCorsUsing.html)
### Setup S3 VPC endpoint 
### Setup policies for S3 bucket 
### Setup IAM role to access S3 bucket 
### Setup S3 encryption and KMS key 