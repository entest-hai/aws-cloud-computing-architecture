# Setup AWS ECS Faragte with Application Load Balancer
**18 JAN 2022 Hai Tran**
#### Summary 
This note goes through how to setup AWS ECS Fargate with an ALB to run an Flask Python app in multiple tasks, each tasks configured with 1 CPU and 2048MB RAM. It is noted that we should configure ALB **inbound** from all IP with port 80, and configure **ECS inbound** from the ALB on port 8081 in this case. The ALB will forward requests to ECS tasks. Role can be assigned to the tasks to grant access to DynamoDB or S3 bucket. This is low level than Lambda, like go backward from python to C. 

<br/>
![aws-ecs](https://user-images.githubusercontent.com/20411077/149967893-3e23b343-64f4-4c0e-b157-9c292053c09f.png)
<br/>


#### Step 1. Prepare a Docker script 
```
FROM python:3.7-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8081 

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

```
local build 
```
docker build -t flask-app . 
```
local run to test 
```
docker run -d -p 56733:8081 flask-app:latest 
```
check containers ID runnings 
```
docker ps  
```
go to browser and check the web server flask is running 
```
http://localhost:56733
```
push docker image to aws ecr [follow this](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) <br/>
authenticate with a profile noted 
```
aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
```
tag 
```
sudo docker tag dc73321f7fab aws_account_id.dkr.ecr.ap-southeast-1.amazonaws.com/flask-app:latest
```
push 
```
sudo docker push aws_account_id.dkr.ecr.ap-southeast-1.amazonaws.com/flask-app:latest
```
go to aws console and take note the image id
```
aws_account_id.dkr.ecr.ap-southeast-1.amazonaws.com/flask-app:latest
```
#### Step 2. Setup an ECS cluster and task definition
go to aws console ecs service and create a cluster named **FhrProcessingCluster** <br/>
create a cluster 
<br/> 
![create_cluster](https://user-images.githubusercontent.com/20411077/149961773-9db384ff-ef68-4ca1-8e5e-83ef234a5573.png)
<br/> 
create a task definition 
<br/>
![create_task](https://user-images.githubusercontent.com/20411077/149961838-f29d8462-5238-45bb-9a3b-d90f79dd098c.png)
<br/>
view task definition 
<br/>
![create_fargate_task](https://user-images.githubusercontent.com/20411077/149961888-d0160b91-02d9-459d-9b15-5e0dfabf7ac9.png)
<br/>
add container 
</br>
![add_container](https://user-images.githubusercontent.com/20411077/149962000-e2dfcd44-5b33-47ff-8f34-c2e9742aa280.png)
</br>
create load balancer as step 4. 
<br/>
![create_load_balancer](https://user-images.githubusercontent.com/20411077/149962043-a31739e5-d71f-4ec0-9f14-81196b0ae131.png)
<br/>

create a service 
<br/> 
![configure_ecs_service_container](https://user-images.githubusercontent.com/20411077/149962079-4539d0d7-af0b-4936-856c-13fef75aca49.png)
<br/> 
configure network for the ecs service 
<br/>
![configure_network_service](https://user-images.githubusercontent.com/20411077/149962130-b2a3e2d2-245a-4d3f-ac48-0e2ef830bd85.png)
<br/>
configure container for the ecs service 
<br/>
![configure_ecs_service_container](https://user-images.githubusercontent.com/20411077/149962199-f6d43403-6ba3-4df6-ae94-4b8f0948d7cb.png)
<br/>
**important configure security for ecs service so that inbound from the ALB enabled**
<br/>
![configure_security_group_for_ecs_inbound_from_alb](https://user-images.githubusercontent.com/20411077/149962339-ceae5ced-e1c1-4260-82fd-28ec513fd0f4.png)
<br/>

#### Step 3. Setup an Application Load Balancer
go to ec2 service and choose load balancer <br/>

create a load balancer 
<br/>
![create_load_balancer](https://user-images.githubusercontent.com/20411077/149961558-389953e9-958e-496c-b150-2c3ae32ae91e.png)
<br/>

setup security group inbound open 80 from all 
<br/>
![create_fhr_alb](https://user-images.githubusercontent.com/20411077/149962450-c7da9c2b-1c2c-418d-a7a6-5b9daa01c541.png)
<br/>

forward to port 8081 of the target group ecs <br/>

setup target group with ecs fargate <br/>

#### Step 4. Check security group and connection 

