# Setup NextJS with Typescript and ChakraUI 
**07 DEC 2021**
### Init project with npm 
This will create package.json
```
npm init -y
```
### Update package.json 
```
npm i @chakra-ui/react @emotion/react @emotion/styled framer-motion next react react-dom react-table react-icons @chakra-ui/icons
```
To support typescript 
```
npm i -D typescript
```
package.json content 
```
{
  "name": "typescript-test",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "keywords": [],
  "author": "Hai",
  "license": "ISC",
  "dependencies": {
    "@chakra-ui/icons": "^1.1.1",
    "@chakra-ui/react": "^1.7.2",
    "@emotion/react": "^11.7.0",
    "@emotion/styled": "^11.6.0",
    "framer-motion": "^5.4.3",
    "next": "^12.0.7",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-icons": "^4.3.1",
    "react-table": "^7.7.0"
  },
  "devDependencies": {
    "eslint": "^8.4.1",
    "eslint-config-next": "^12.0.7",
    "prettier": "^2.5.1",
    "typescript": "^4.5.2"
  }
}
```
### First page 
```
./pages/index.js 
```
```
function HomePage() {
  return <div>Welcome to Next.js!</div>
}

export default HomePage
```

### Eslint and prettier configuration 
```
npm i -D eslint eslint-config-next prettier 
```
.eslintrc.json
```
{
    "root": true,
    "extends": "next",
    "rules": {
      "quotes":[
        "error",
        "single"
      ],
      "indent":[
        "error",
        2
      ],
      "no-unused-vars": [
        "error",
        {
          "argsIgnorePattern": "^_",
          "varsIgnorePattern": "^_"
        }
      ],
      "react/display-name": 0
    }
  }
```
prettier.config.js
```
const options = {
    arrowParens: 'avoid',
    singleQuote: true,
    bracketSpacing: true,
    endOfLine: 'lf',
    semi: false,
    tabWidth: 2,
    trailingComma: 'none'
  }
  
  module.exports = options
```

# Connect with AWS Amplify 
### Init a aws amplify project using cli 
```
amplify init 
```
Help 
```
amplify add -help 
```
Add auth 
```
amplify add auth 
```
Add storage
```
amplify add storage
```
Add api graphql and dynamo db
```
amplify add api 
```
Push create backend in cloud 
```
amplify push 
```
### Simple data model 
```
type User @model @auth(rules: [{allow: public}]) {
  id: ID!
  username: String
  email: String
  phone: String
  address: String
  profileImageUrl: String
}

type Message @model @auth(rules: [{allow: public}]){
  id: ID! 
  userID: ID!
  content: String
  createdTime: AWSTimestamp! 
}
```
### Configure a primary key 
```
type Message @model @auth(rules: [{allow: public}]){
  id: ID! @primaryKey(sortKeyFields: ["userID"])
  userID: ID! 
  content: String
  createdTime: AWSTimestamp! 
}
```

### Configure a secondary index
```
type Message @model @auth(rules: [{allow: public}]){
  id: ID!
  userID: ID! @index(name: "byUserID", queryField: "messagesByUserID")
  content: String
  createdTime: AWSTimestamp! 
}
```
More complicated by using composition sortKeyFields
```
type Message @model @auth(rules: [{allow: public}]){
  id: ID!
  userID: ID! @index(name: "byUserByByCreatedTime", sortKeyFields: ["createdTime"])
  content: String
  createdTime: AWSTimestamp! 
}
```

**Advanced flow admin** 

### Pull backend with amplify cli 
```
amplify pull 
```
### Update _app.js 
```
import Amplify from 'aws-amplify';
import config from '../src/aws-exports';
Amplify.configure({
  ...config, ssr: true
})
```
### Update aws-amplify javascript lib 
```
npm install aws-amplify
```

### Update UI 
### Update index.js 
```
import styles from '../styles/Home.module.css'
import { DataStore } from 'aws-amplify'
import { useState, useEffect } from 'react'
import Link from 'next/link'
import { Post } from '../src/models'
```
```

export default function Home() {
  const [posts, setPosts] = useState([])

  useEffect(() => {
    fetchPosts()
    async function fetchPosts() {
      const postData = await DataStore.query(Post)
      setPosts(postData)
    }
    const subscription = DataStore.observe(Post).subscribe(() => fetchPosts())
    return () => subscription.unsubscribe()
  }, [])
  ```
  ```
  
  return (
    <div className={styles.container}>
      <h1>Posts</h1>
      {
        posts.map(post => (
          <Link href={`/posts/${post.id}`}>
            <a>
              <h2>{post.title}</h2>
            </a>
          </Link>
        ))
      }
    </div>
  )
}
```

### Simple auth 
```
{ Amplify } from 'aws-amplify';
import { withAuthenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';

import awsExports from './aws-exports';
import React from 'react';
Amplify.configure(awsExports);


function App({ signOut, user }) {
  return (
    <div>
      <h1>Hello {user.username}</h1>
      <button onClick={signOut}>Sign out</button>
      </div>
  );
}

export default withAuthenticator(App);
```

### Custom auth ui
```
import {
  Authenticator,
  Flex,
  Grid,
  Image,
  useTheme,
  View
} from "@aws-amplify/ui-react";

import { Header } from "./Header";
import { Footer } from "./Footer";
import { SignInHeader } from "./SignInHeader";
import { SignInFooter } from "./SignInFooter";

const components = {
  Header,
  SignIn: {
    Header: SignInHeader,
    Footer: SignInFooter
  },
  Footer
};

export function Login() {
  const { tokens } = useTheme();

  return (
    <Grid templateColumns={{ base: "1fr 0", medium: "1fr 1fr" }}>
      <Flex
        backgroundColor={tokens.colors.background.secondary}
        justifyContent="center"
      >
        <Authenticator components={components}>
          {({ signOut, user }) => (
            <main>
              <h1>Hello {user.username}</h1>
              <button onClick={signOut}>Sign out</button>
            </main>
          )}
        </Authenticator>
      </Flex>
      <View height="100vh">
        <Image
          src=""
          width="100%"
          height="100%"
          objectFit="cover"
        />
      </View>
    </Grid>
  );
}
```

# Test backend from aws console 
cerate a user 
```
mutation MyMutation {
  createUser(input: {address: "", email: "", id: "", phone: "", username: "", profileImageUrl: ""}) {
    email
    id
    phone
    username
    profileImageUrl
  }
}

```
create a message 
```
mutation MyMutation {
  createMessage(input: {content: "Hello, this is firsrt message from demo", userID: "", createdTime: ""}) {
    content
    createdTime
    userID
  }
}

```

# Debug
### tsx ignore an error 
```
// @ts-ignore
  <Sidebar 
    signOut={signOut}
    user={user}
  >
  </Sidebar>
```

### Noted for nextjs ssr 
```
import Amplify from 'aws-amplify';
import config from '../src/aws-exports';
Amplify.configure({
  ...config, ssr: true
});
```
### References 
1. [aws ssr realtime](https://aws.amazon.com/blogs/mobile/host-a-next-js-ssr-app-with-real-time-data-on-aws-amplify/)
2. [aws amplify docs](https://docs.amplify.aws/lib/ssr/q/platform/js/)
3. [aws amplify custom auth](https://aws.amazon.com/blogs/mobile/amplify-uis-new-authenticator-component-makes-it-easy-to-add-customizable-login-pages-to-your-react-angular-or-vue-app/)

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
"redirectSignIn": "https://cognito-hosted-ui.d1kr0cdjwf92am.amplifyapp.com/",
"redirectSignOut": "https://cognito-hosted-ui.d1kr0cdjwf92am.amplifyapp.com/signout/",
``` 
Configure redirect uri in AWS Cognito console 





















