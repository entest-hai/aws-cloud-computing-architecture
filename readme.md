# Setup Cognito Hosted UI and Google Auth Provider 
**Hai Tran 29 DEC 2021**

### Cognito hosted ui and fedreated auth with Google Auth Provider 
Setup google credential 
![google_credential_configuration](https://user-images.githubusercontent.com/20411077/147643131-93e7f070-f30a-4044-af5a-424d412b5e92.png)
Seup cognito domain 
![cognito_domain_name](https://user-images.githubusercontent.com/20411077/147643149-fa6f0e80-89f2-4541-8a2e-9f2290773bad.png)
Setup cognito client app 
![cognito_app_client_settings](https://user-images.githubusercontent.com/20411077/147643160-5cea6893-d123-4ce0-9537-0f87c064bb48.png)
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

### Note 
Seperate backend and frontend in AWS Amplify Console  <br/>
Configure redirect url in aws-config.json
```
"redirectSignIn": "https://{projectname}.{project-id}.amplifyapp.com/",
"redirectSignOut": "https://{projectname}.{project-id}}amplifyapp.com/signout/",
``` 
Configure redirect uri in AWS Cognito console 





















