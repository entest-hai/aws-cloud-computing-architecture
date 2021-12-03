## 03 DEC 2021 Multi-Region NextJS Deployment using Route 53 and EC2  
### 1. Architecture 
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