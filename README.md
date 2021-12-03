## 03 DEC 2021 Multi-Region NextJS Deployment using Route 53 and EC2  
### 1. Architecture 
Noted: [http://test.entest.io](http://test.entest.io) the demo does not supported yet **https**
![Picture1](https://user-images.githubusercontent.com/20411077/144642634-ce323da2-8064-44ce-8c57-35389b1feb73.png)
### 2. Use cases 
- Fail-over handle 
- Better user experience per region 
### 3. Key component route 53 and routing policy
- Geolocation based on location of users 
- Geoproximity based on location of resources 
- Failover active-passive failover 
- Latency bassed on latency round-trip
- Weighted 
- Multivalue answer 
- Simple 
### 4. Simple example 
- A web [http://test.entest.io](http://test.entest.io) 
- Code repo for the web [web repo](https://github.com/tranminhhaifet/haitran-homepage)
- Users in USA, Vietnam, India will be routed to the **aws us-east-1** US-East(N.Virignia)
- Users in Sigapore, Asia will be routed to **aws ap-southeast-1** Asia Pacific (Singapore)
### 5. Configure 
Singapore 
![biorithm_singapore_route_53](https://user-images.githubusercontent.com/20411077/144639096-a9df76b3-d990-4709-9c2c-c536bf69d984.png)
USA
![biorithm_usa_route_53](https://user-images.githubusercontent.com/20411077/144639108-683fc242-567a-4a55-84ab-a010722ae5a0.png)
India
![biorithm_india_route_53](https://user-images.githubusercontent.com/20411077/144639121-0c32d07b-0f79-4fcd-8d6e-90c0a30f0da2.png)
Vietnam
![biorithm_vietnam_route_53](https://user-images.githubusercontent.com/20411077/144639135-ba4c299c-e1ae-4f71-b2bb-950aecfe00b2.png)
### 6. Result
- Users in Singapore will see 
![users_singapore](https://user-images.githubusercontent.com/20411077/144644064-dbb0f5c7-f3c0-43ee-b98d-5ad9efe1bd44.PNG)
- Users in USA, India, Vietnam will see 
