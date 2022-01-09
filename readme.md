# Getting started with EC2, Apache Web Server and PHP Application 
**08 JAN 2022 Hai Tran**

I choose ap-southest-1 region, but for assignment, you should check is this required to choose us-east-1 region.

# Task 1. Launch an EC2 and get Apache up running 
### Step 1. Install LAMP stack on EC2 Linux 2 AMI 
- Launch free tier EC2 Linux 2 AMI 
- Install LAM by following commands 
- [Reference here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.html)
```
sudo yum update -y
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
sudo yum install -y httpd mariadb-server
```
start the Apache web server 
```
sudo systemctl start httpd
```
use the systemctl to configure the Apache web server to start each system boot 
```
sudo systemctl enable httpd
```
verify that the httpd is on by this command 
```
sudo systemctl is-enabled httpd
```

### Step 2. Configure a security group 
- Port 22 for SSH 
- Port 443 for HTTPS 
- Port 3000 for testing 

### Step 3. Enalbe ec2-user write contents to the Apache document root /var/www/
Type this public IP of the instance in a web browser to see the apache web server is running, you should see the Test Page. To develop your app, you need permission to write files in /var/www/html where the Apache server files located. The following commands will give ec2-user permission to write into this directory. <br/>

Add your user (ec2-user) to apache group 
```
sudo usermod -a -G apache ec2-user
```
Log out and back in again 
```
exit
```
Log in SSH again 
```
groups
ec2-user adm wheel apache systemd-journal
```
Change the group ownershop of /var/www and its content to the apache group 
```
sudo chown -R ec2-user:apache /var/www
```
Add group write permission
```
sudo chmod 2775 /var/www && find /var/www -type d -exec sudo chmod 2775 {} \;
```
Add group write permission recursively 
```
find /var/www -type f -exec sudo chmod 0664 {} \;
```

### Step 4. Develop a HelloWorld PHP application 
Create a PHP file in the Apache document root 
```
echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php
```
Go to web browser enter this address to check, please replace {ec2-public-ip} with your ec2 public ip. 
```
http://{ec2-public-ip}/phpinfo.php
```
You should see a page as below picture. Further optional step. Copy and paste **hello.html** into /var/www/html/, then go to web-browser to check 
```
http://{ec2-public-ip}/index.html
```

# Task 2. Create a PHP web page 
Folder structure as 
```
/var/www/html/cos20019/photoalbum/upload.php 
```


### Bonus 
scp copy from ec2 to local with pem key 
```
scp -r -i ~/aws/haitran-swin-free-ec2.pem ec2-user@13.213.5.166:/var/www/html/cos20019/photoalbum/ . 

```
