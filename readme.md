# Host a static website using AWS S3 
**16 DEC 2021 Hai Tran** <br>
[AWS reference ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html#step2-create-bucket-config-as-website)

### Create a S3 bucket 
[s3 cli mb](https://docs.aws.amazon.com/cli/latest/reference/s3/mb.html)
```
aws s3 mb s3://haitran-swinburne-2021 --region ap-southeast-1
```
verify 
```
aws s3 ls 
```

### Copy web files to S3 
```
aws s3 cp . s3://haitran-swinburne-2021/swin-coffee-web/ --recursive
```
verify 
```
aws s3 ls s3://haitran-swinburne-2021/ --recursive 
```

### Configure host a static website 
