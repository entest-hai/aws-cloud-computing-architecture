# Setup AWS SES and Workmail with Custom Domain 
**08 JAN 2022 Hai Tran**
This note goes through how to setup SES (Simple Email Service) with a custom domain and receive emails in S3. Then also setup Workmail with the custom domain. 
## Part I. Setup AWS SES with Custom Domain and Receive Emails in S3 
We need to do five steps 1) verify identities which are the custom domain and emails. Why need to verify emails here? Because the SES is in a sandbox environment before AWS approval for production, and need to apply for approval. In this sandbox environment, to test sending emails to an email, the email need to be verified first. 2) Create a S3 bucket and a policy to allow SES write emails into it. 3) Need to set receiving rules, and action to tell SES write receiving emails into the S3 bucekt. 4) Need to create a MX record in DNS provider, in this case Route 53 because the custom domain registered with Route 53. At this moment, this step is needed. When setup workmail, this step is easier as records are automatically generated and updated to the Route 53 DNS records. We will need to review and fix conflics if they occurs. **Note that receiving email configuration is only avaiable in three regions {us-east-1, us-west-1, us-west-2}**
### Step 1. Create and verify identities 
Create and verify the custom domain.
Similar verify emails which will be used for send test email. 
### Step 2. Create S3 bucket to store email 
This is policy to allow SES write email into it. 
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSESPuts",
            "Effect": "Allow",
            "Principal": {
                "Service": "ses.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::BUCKET_NAME/*",
            "Condition": {
                "StringEquals": {
                    "aws:Referer": "ACCOUNT_ID"
                }
            }
        }
    ]
}
```
### Step 3. Set up a receipt rule 
Add actions choose **Deliver to S3 bucket** and choose the bucket created in step 2.  

### Step 4. Create an MX record in the Route 53 
Details in here [Publishing an MX record for SES email receiving](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-mx-record.html). In this case, the custom domain is registered with Route 53, so need to go to Route 53 console, create a MX record with following information. </br>
MX record Name
```
the custom domain 
```
Value 
```
10 inbound-smtp.us-east-1.amazonaws.com
```
#### Step 5. Send test email 
Now we can send test emails from the custom domain to verified email in step 1. Then we go to the S3 bucket to check received emails, need to refresh or waits for few minutes somtimes. 

## Part II. Setup Workmail with Custom Domain 