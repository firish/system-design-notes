# Service Discovery

Service Discovery is a crucial part of deploying and maintaining systems. 

Lets say you follow a microservice architecture. You have 100 servers 20 services running across them.
These can be service A, B, C, D, E, running on servers S1, S2, ... S100

Lets say S1 to S15 run the service A 
and S40 to S50 run the service C

Now service C needs to talk to service A
so servers in service C need to talk to servers in service A
so all servers in service C need to store the details of all servers in service A
Further, everytime a server is added/removed/down, this information needs to be updated in all servers in service C
In reality, all serverices may need to talk to all other services. 
Maintaining this information on every server and updating it so frequently in costly and inefficient

This is where service discovery comes into the picture. 
Service discovery is nothing but a snapshot of a service
lets say service A has S1 to S15. 
The load balancer takes a snapshot of service A
this snapshot has all the information of service A, like how many servers it has, the IP address of the servers, and the ports occupied by the servers, and the status of the servers

Now, everytime a server in service C needs to talk to a server in service A
they can simply poll the load balancer for the ip address and the port (service discovery)

Updating and keep the service information relevant also becomes easier
every time a server is added or removed or marked dead by the heartbeat service
the load balancer discards the earlier snapshot of the service and take a new snapshot.
Now when other servers query the load balancer, they get the updated snapshot
