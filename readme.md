# Setup AWS ECS Faragte with Application Load Balancer
**18 JAN 2022 Hai Tran**
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
sudo docker tag dc73321f7fab 717869305038.dkr.ecr.ap-southeast-1.amazonaws.com/flask-app:latest
```
push 
```
sudo docker push 717869305038.dkr.ecr.ap-southeast-1.amazonaws.com/flask-app:latest
```
go to aws console and take note the image id
```
717869305038.dkr.ecr.ap-southeast-1.amazonaws.com/flask-app:latest
```
#### Step 2. Setup an ECS cluster 
go to aws console ecs service and create a cluster named **FhrProcessingCluster** <br/>
create a cluster <br/> 

create a task definition <br/>

view task definition <br/>

create load balancer as step 4. <br/>

create a service <br/> 

#### Step 3. Define a Fargate task 
#### Step 4. Setup an Application Load Balancer
go to ec2 service and choose load balancer <br/>

create a load balancer <br/>

setup security group inbound open 80 from all<br/>

forward to port 8081 of the target group ecs <br/>

setup target group with ecs fargate <br/>

#### Step 5. Check security group and connection 

