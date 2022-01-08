# CloudFormation Week 1
**08 JAN 2022 Hai Tran**
### What is CloudFormation 
- Template 
- Stacks 
- Change sets 
### How does it works? 
[Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.html)
</br>
[<img src="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/create-stack-diagram.png">](ref)
</br>
- Use IAM to give permissions to create resources 
- Template example  
```
AWSTemplateFormatVersion: '2010-09-09'
Description: A simple EC2 instance
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-0ff8a91507f77f867
      InstanceType: t2.micro
```
- Create a stack by console, API, or AWS CLI 
- Update changes 
</br>
[<img src="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/update-stack-diagram.png">](ref)
</br>
- Delete a stack 

### Template to create a S3 bucket for static web hosting 
```
AWSTemplateFormatVersion: "2010-09-09"
Description: Create a S3 bucket
Resources:
  TestCreateS3BucketWithCloudFormation:
    Type: AWS::S3::Bucket
    Properties:
      AccessControl: PublicRead
      WebsiteConfiguration:
        IndexDocument: index.html
        ErrorDocument: error.html
    DeletionPolicy: Delete
  BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref TestCreateS3BucketWithCloudFormation
      PolicyDocument:
        Id: MyPolicyForS3StaticWeb
        Version: 2012-10-17
        Statement:
          - Sid: PublicReadForGetBucketObjects
            Effect: Allow
            Principal: "*"
            Action: "s3:GetObject"
            Resource: !Join
              - ""
              - - "arn:aws:s3:::"
                - !Ref TestCreateS3BucketWithCloudFormation
                - /*
Outputs:
  WebsiteURL:
    Value: !GetAtt
      - TestCreateS3BucketWithCloudFormation
      - WebsiteURL
    Description: URL for website hosted on S3
  S3BucketSecureURL:
    Value: !Join
      - ""
      - - "https://"
        - !GetAtt
          - TestCreateS3BucketWithCloudFormation
          - DomainName
    Description: Name of S3 bucket to hold website content

```

### Template to create an EC2 instance inside a security group 
```
Resources:
  Ec2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      SecurityGroups:
        - !Ref InstanceSecurityGroup
      KeyName: mykey
      ImageId: ''
  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
```

### The Ref function 
```
Parameters:
  KeyName:
    Description: The EC2 Key Pair to allow SSH access to the instance
    Type: 'AWS::EC2::KeyPair::KeyName'
Resources:
  Ec2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      SecurityGroups:
        - !Ref InstanceSecurityGroup
        - MyExistingSecurityGroup
      KeyName: !Ref KeyName
      ImageId: ami-7a11e213
  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
```

### The Fn::GetAtt function 
This is how domain name is obtained by GetAtt function given bucket name
```
"DomainName": {
                "Fn::GetAtt": [
                  "myBucket",
                  "DomainName"
                ]
              },
```
```
Resources:
  myBucket:
    Type: 'AWS::S3::Bucket'
  myDistribution:
    Type: 'AWS::CloudFront::Distribution'
    Properties:
      DistributionConfig:
        Origins:
          - DomainName: !GetAtt 
              - myBucket
              - DomainName
            Id: myS3Origin
            S3OriginConfig: {}
        Enabled: 'true'
        DefaultCacheBehavior:
          TargetOriginId: myS3Origin
          ForwardedValues:
            QueryString: 'false'
          ViewerProtocolPolicy: allow-all

```
### Receiving user input using input parameters 
Define parameters. You declare parameters in a template's Parameters object. If no default given, users must specify a key name value at **stack creation**
```
Parameters:
  KeyName:
    Description: Name of an existing EC2 KeyPair to enable SSH access into the WordPress web server
    Type: AWS::EC2::KeyPair::KeyName
  WordPressUser:
    Default: admin
    NoEcho: true
    Description: The WordPress database admin account user name
    Type: String
    MinLength: 1
    MaxLength: 16
    AllowedPattern: "[a-zA-Z][a-zA-Z0-9]*"
  WebServerPort:
    Default: 8888
    Description: TCP/IP port for the WordPress web server
    Type: Number
    MinValue: 1
    MaxValue: 65535
```

### Mappings Fn::FindInMap
Note that the **AWS::Region pseudo parameter** is a value that CloudFormation resolves as the region where the stack is created. Pseudo parameters are resolved by CloudFormation when you create the stack.
```
Parameters:
  KeyName:
    Description: Name of an existing EC2 KeyPair to enable SSH access to the instance
    Type: String
Mappings:
  RegionMap:
    us-east-1:
      AMI: ami-76f0061f
    us-west-1:
      AMI: ami-655a0a20
    eu-west-1:
      AMI: ami-7fd4e10b
    ap-southeast-1:
      AMI: ami-72621c20
    ap-northeast-1:
      AMI: ami-8e08a38f
Resources:
  Ec2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      KeyName: !Ref KeyName
      ImageId: !FindInMap 
        - RegionMap
        - !Ref 'AWS::Region'
        - AMI
      UserData: !Base64 '80'
```

### Constructed values and output values with Fn::Join
Parameters and mappings are way to pass values at stack creation time, but there can be situtations wehre a value from a parameter or other resource attributes is only part of the value you need. Constructued values by **Join**
```
Resources:
  ElasticLoadBalancer:
    Type: 'AWS::ElasticLoadBalancing::LoadBalancer'
    Properties:
      AvailabilityZones: !GetAZs ''
      Instances:
        - !Ref Ec2Instance1
        - !Ref Ec2Instance2
      Listeners:
        - LoadBalancerPort: '80'
          InstancePort: !Ref WebServerPort
          Protocol: HTTP
      HealthCheck:
        Target: !Join 
          - ''
          - - 'HTTP:'
            - !Ref WebServerPort
            - /
        HealthyThreshold: '3'
        UnhealthyThreshold: '5'
        Interval: '30'
        Timeout: '5'
```
And outputs, the Outputs object in the template contains declarations for the values that you want to have **available after the stack is created.**
```
Outputs:
  InstallURL:
    Value: !Join 
      - ''
      - - 'http://'
        - !GetAtt 
          - ElasticLoadBalancer
          - DNSName
        - /wp-admin/install.php
    Description: Installation URL of the WordPress website
  WebsiteURL:
    Value: !Join 
      - ''
      - - 'http://'
        - !GetAtt 
          - ElasticLoadBalancer
          - DNSName
```

### Inspect a CodePipeline stack 
[Create a CodePipeline](https://s3.amazonaws.com/cloudformation-examples/user-guide/continuous-deployment/basic-pipeline.yml)
