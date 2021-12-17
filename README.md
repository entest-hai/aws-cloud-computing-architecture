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
