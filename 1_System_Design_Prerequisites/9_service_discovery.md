# Service Discovery

Service Discovery is a crucial part of deploying and maintaining systems. 

Let's say you follow a microservice architecture. You have 100 servers and 20 services running across them.
These can be services A, B, C, D, and E, running on servers S1, S2, ... S100.

Let's say S1 to S15 run the service A 
and S40 to S50 run the service C

Now service C needs to talk to service A,
so servers in service C need to talk to servers in service A.
So, all servers in Service C need to store the details of all servers in Service A.
Further, every time a server is added/removed/down, this information needs to be updated in all servers in service C.
In reality, all services may need to talk to all other services. 
Maintaining this information on every server and updating it so frequently is costly and inefficient.

This is where service discovery comes into the picture. 
Service discovery is nothing but a snapshot of a service.
let's say service A has S1 to S15. 
The load balancer takes a snapshot of service A.
This snapshot has all the information of service A, like how many servers it has, the IP address of the servers, the ports occupied by the servers, and the status of the servers

Now, every time a server in service C needs to talk to a server in service A, 
they can simply poll the load balancer for the IP address and the port (service discovery)

# How does the load-balancer know when to update itself
The load balancer is regularly updated using heartbeats. Every service will send a snapshot hash in each heartbeat. Every time a server is added or removed or marked dead by the heartbeat service, there will be a hash mismatch, and the load balancer discards the earlier snapshot of the service and take/request a new snapshot.
Now when other servers query the load balancer, they get the updated snapshot


# Extra information on Service-Discovery Mechanism
Service discovery is a critical component in distributed systems and cloud computing, enabling applications and services to find and communicate with each other. Here are some of the common approaches:

DNS-Based Service Discovery:
This method uses the Domain Name System (DNS) to locate services. Each service is assigned a DNS name, and the DNS server is updated dynamically as services are added, removed, or changed.

Example: In a Kubernetes cluster, when a new pod is created as part of scaling out a service, its IP address is automatically registered with the cluster's DNS service. Other services can then discover the new instance using its DNS name.

Service Registry/Discovery Agents:
Services register themselves with a central registry upon startup, and clients query this registry to find services.

Example: Using a tool like Consul or Eureka, when a service instance is launched, it registers its address with the central service registry. Clients then query the registry to discover the address of the available service instances.

Server-Side Service Discovery:
The client requests an intermediate router or load balancer, which is responsible for directing the request to an available service instance.

Example: When new instances of a service are added, a load balancer like NGINX or HAProxy is updated to include these instances. The load balancer then directs incoming client requests to these new instances based on its load-balancing algorithm.

Self-Announcing Services:
Services publish their availability on a common message bus or distributed system like Apache ZooKeeper, where clients can discover them.

Example: When a service instance is scaled out, it announces its presence on a message bus like Kafka or a distributed system like ZooKeeper. Other services listen on these channels and update their records of available services.
