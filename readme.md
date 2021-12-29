# Setup Cognito Hosted UI and Google Auth Provider 
**Hai Tran 29 DEC 2021**
This note goes through how to setup authentication using cognito hosted ui with Google Authe Provider. Step 1. create clientID and clientSecret from Google Credential. Step 2. Setp cognito domain, redirectSignIn and redirectSignOut in the AWS Cognito Console or via Amplify CLI. Step 3. Configure the aws-export.json with the same redirectSignIn and redirectSignOut in the step 3. 

### Cognito hosted ui and fedreated auth with Google Auth Provider 
Setup google credential 
![147643131-93e7f070-f30a-4044-af5a-424d412b5e92](https://user-images.githubusercontent.com/20411077/147668791-e027c0bc-5c2b-4092-802b-29106ff3c12d.png)
Setup cognito domain 
![147643149-fa6f0e80-89f2-4541-8a2e-9f2290773bad](https://user-images.githubusercontent.com/20411077/147668853-0009dc9e-7190-4e26-a503-98f987f97fa2.png)
Setup cognito client app 
![147643160-5cea6893-d123-4ce0-9537-0f87c064bb48](https://user-images.githubusercontent.com/20411077/147669007-d5318fc7-63dd-4f58-bf5c-de65d3424396.png)
Cognito auth window launched from hosted UI 
![cognito_auth_window](https://user-images.githubusercontent.com/20411077/147643758-9b047be5-94ff-4ee7-bb15-86112aa88cb1.png)

```
<Button
  colorScheme='green'
  mb={6}
  onClick={() => {
    Auth.federatedSignIn({
      provider: CognitoHostedUIIdentityProvider.Cognito
    })
  }}
>
  Sign In with Cognito 
</Button>
<Button
  colorScheme='orange'
  mb={6}
  onClick={() => {
    Auth.federatedSignIn({
      provider: CognitoHostedUIIdentityProvider.Google
    })
  }}
>
  Sign In with Google
</Button>
<Button

```

Configure redirect url in aws-config.json
```
"redirectSignIn": "https://www.example.io/",
"redirectSignOut": "https://www.example.io/signout/",
``` 

### Note 
Seperate backend and frontend in AWS Amplify Console  <br/>
















