# CloudFront to Deliver Static Web Hosted on S3 
**06 JAN 2022 Hai Tran** <br>
## References 
- [CloudFront deliver static and dyanmic content](https://aws.amazon.com/blogs/networking-and-content-delivery/deliver-your-apps-dynamic-content-using-amazon-cloudfront-getting-started-template/)
- [CloudFront S3 origin](https://aws.amazon.com/getting-started/hands-on/deliver-content-faster/)
- [Route 53 alias record CloudFront domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html)

## Part I Host a static web using S3 
### 1. Create a S3 bucket 
[s3 cli mb](https://docs.aws.amazon.com/cli/latest/reference/s3/mb.html)
```
aws s3 mb s3://bucket-name --region ap-southeast-1
```
verify 
```
aws s3 ls 
```
### 2. Copy web files to S3 
```
aws s3 cp . s3://bucket-name/ --recursive
```
verify 
```
aws s3 ls s3://bucket-name/ --recursive 
```
### 3. 403 error 
By default, Amazon S3 blocks public access to your account and buckets. If you want to use a bucket to host a static website, you can use these steps to edit your block public access settings.

### 4. Configure host a static website 
![enable_static_web_hosting_index](https://user-images.githubusercontent.com/20411077/146595602-22db6843-6282-45ba-814a-bca5040ef716.png)
### 5. Configure bucket policy 
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

### 6. Block public bucket access 
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
## Part II Deliver the S3 hosted web with CloudFront
### 1. Create a CloudFront distribution with the S3 bucket as an origin
![cloudfront_distribution](https://user-images.githubusercontent.com/20411077/148347041-12b265b4-22e9-4cfd-9137-56a702623e9a.png)
### 2. Request a SSL certificate with the custom domain
![request_cerfiticate_ssl](https://user-images.githubusercontent.com/20411077/148347068-71ae43bc-2893-4503-b192-3407d5df7f37.png)
### 3. Create an alternate domain
Use the certificate to add/update an alternate domain to the CloudFormation distribution in step 1. 
### 4. Create an Route 53 alias record with the CloudFront auto-gen domain
![route_53_cloudfront_alias_record](https://user-images.githubusercontent.com/20411077/148347117-817e2e50-c136-4739-b922-7d97fa47abe5.png)
