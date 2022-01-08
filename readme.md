# Setup AWS SES and Workmail with Custom Domain 
**08 JAN 2022 Hai Tran**
This note goes through how to setup SES (Simple Email Service) with a custom domain and receive emails in S3. Then also setup Workmail with the custom domain. 
## Part I. Setup AWS SES with Custom Domain and Receive Emails in S3 
We need to do five steps 1) verify identities which are the custom domain and emails. Why need to verify emails here? Because the SES is in a sandbox environment before AWS approval for production, and need to apply for approval. In this sandbox environment, to test sending emails to an email, the email need to be verified first. 2) Create a S3 bucket and a policy to allow SES write emails into it. 3) Need to set receiving rules, and action to tell SES write receiving emails into the S3 bucekt. 4) Need to create a MX record in DNS provider, in this case Route 53 because the custom domain registered with Route 53. At this moment, this step is needed. When setup workmail, this step is easier as records are automatically generated and updated to the Route 53 DNS records. We will need to review and fix conflics if they occurs. **Note that receiving email configuration is only avaiable in three regions {us-east-1, us-west-1, us-west-2}**
### Step 1. Create and verify identities 
Create and verify the custom domain.
</br>
![create_verify_domain](https://user-images.githubusercontent.com/20411077/148641713-bfb47c6d-7553-4d6d-add6-b3a10bd86ba5.png)
</br>
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
![create_rule_set](https://user-images.githubusercontent.com/20411077/148641724-d8fc963d-3ca6-44a7-a0ef-f79ef7f0ec43.png)
</br>
Add actions choose **Deliver to S3 bucket** and choose the bucket created in step 2.  
![create_set_rule_devliver_s3](https://user-images.githubusercontent.com/20411077/148641717-decda9ae-6c5d-49f5-bd23-d6d9a9724c3c.png)
</br>
### Step 4. Create an MX record in the Route 53 
Details in here [Publishing an MX record for SES email receiving](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-mx-record.html). In this case, the custom domain is registered with Route 53, so need to go to Route 53 console, create a MX record with following information. </br>
![create_mx_record](https://user-images.githubusercontent.com/20411077/148641743-eedd9956-5feb-4f7f-a1cc-a0eb638a38e1.png)
</br>
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
</br>
![send_test_email](https://user-images.githubusercontent.com/20411077/148641757-fac4c98d-2683-460e-9924-ba4c19d8364e.png)
</br>
## Part II. Setup Workmail with Custom Domain 
### Step 1. Create an organization
Goto AWS Workmail console and create an organization with the custom domain. Noted the default **{yourname}.awsapps.com**, we can go here to login. 
### Step 2. Create users like username@customdomain
### Step 3. Configure mail clients to receive it 
Usually, with any mail clients such as thunderbird, ios mail, we need to parameters [detail here](https://docs.aws.amazon.com/workmail/latest/userguide/using_IMAP.html) <br/>
IMAP server 
```
us-east-1.imap.mail.us-east-1.awsapps.com
```
SMTP server 
```
us-east-1.smtp.mail.us-east-1.awsapps.com
```

