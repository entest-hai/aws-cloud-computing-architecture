## Application Load Balancer EC3 Port Fordward 
**28 DEC 2021 TRAN MINH HAI**  
### Discussion 
Before routing users to different servers using route 53, I need to deploy a web with Application Load Balancer. This take note two things 1) run a web on port 80 by port forwarding 2) configure Application Load Balancer. 

### 1. Setup nodejs for aarch64
aarch64 needs to download node for  ARMv8 from [](https://nodejs.org/en/download/)

### 2. Run a web on port 80 by port forwarding 
forward to port 80 
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 3000
sudo iptables -t nat -I OUTPUT -p tcp -d 127.0.0.1 --dport 80 -j REDIRECT --to-ports 3000
```
configure security grouop 
```
inbound port: 80, 3000 
from: all ip 
```
```
outbound: all port 
destination: all ip 
```

### 3. Setup application load balancer 

