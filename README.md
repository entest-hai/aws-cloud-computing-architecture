## Multi-Region NextJS Deployment using Route 53 and EC2
**04 DEC 2021 TRAN MINH HAI**  
### Abstract 
When users click in this web [entest](http://test.entest.io) they will be routed based on their ip **geolocation**
- Users in Signapore are routed to aws ap-southest-1 Asia Pacific Singapore
- Users in USA, India, Vietnam are routed to aws us-east-1 US East N.Virginia 
- Noted: support **http** only [http://test.entest.io](http://test.entest.io). No **https** for this demo. 
- Based on your location, you will see different things as the end of this note
### 1. Architecture 
![Picture1](https://user-images.githubusercontent.com/20411077/144642634-ce323da2-8064-44ce-8c57-35389b1feb73.png)
### 2. Use cases 
- Disaster recovery RPO & RTO
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
- **Users in USA, India, Vietnam will see**
![usa](https://user-images.githubusercontent.com/20411077/146625043-e4de7341-cf86-4398-a009-69c6e303b8a2.png)

- **Users in Singapore will see** 

![singapore](https://user-images.githubusercontent.com/20411077/146625247-79f2c79c-3c3b-4d9c-86af-09a10d7d5e9d.png)

