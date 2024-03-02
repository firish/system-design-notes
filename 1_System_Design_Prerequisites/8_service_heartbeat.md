# Service Discovery and heartbeat

This basically means checking if the service is always up and running.
Assuring Up-time and reducing service Down-time

Servers crash due to various reasons like hardware faults and software bugs. 
Service Discovery and Health Checks are essential for maintaining a service ecosystem's availability and reliability. 
E.g., A heartbeat service can be used to maintain system state and help the load balancer decide where to direct requests. 
Now when a server crashes, the heartbeat service cand identify that and restart the service immediately on the server.

# How does the heartbeat service look in practice?
It could be fairly simple or fairly involved.
A simple service could be a poling machine that polls all the servers every 5s
If it receives a response without latency, the service is up and running
This cycle repeats every 5s
If a server respons late, or doesn't respond to the poll, the service may change the status of the server to something like 'overloaded'
If the server misses multiple polls (2-3), it can be marked as critical
and if it misses another poll, it is marked as dead.

At this point the heartbeat service will inform this to the load balancer, so more requests aren't routed to the dead server
The service heartbeat can also be responsible for sending a message to another service that is responsible for restarting the server

# A 2-way heartbeat
Sometimes the server may be alive but the service running on the server may be dead
This can not be detected properly by the heartbeat service
so we use a 2-way heartbeat

In this, the heartbeat service polls the sever every 5 seconds (expecting a response from the server)
and the service on the server polls/sends a message (without expecting a response) to the heartbeat service
with this the heartbeat service can be sure that both the server and the service on it are up and running.

However, this method increases complexity and adds up communication (data transfer overhead)
(Most cloud platforms also charge a data transfer fee, which is very low, but can build up fast if we have such a service running for hundreds of servers)

# Zombie servers
When a server is alive, but the service running on it is dead, the server is called a Zombie
This is a very big problem

Servers typically have cron jobs running on them
These cron jobs may talk to other servers and influence data on them
However, since the service on a zombie is dead, the zombie has stale data and its cron jobs can mess the entire systems data management
A two-way heartbeat service can help reduce the risk of zombie servers

# what if the health service goes down?
The health services are lightweight and made fault tolerant (by replication), making this unlikely. However, there is a possibility of any service going down. In that case, we try to bring it back as soon as possible.


# Extra relevant information
In Kubernetes this is implemented as a liveliness check where Kubernetes service queries each pod or each pod sends its liveness rule result back to Kubernetes and the replica set/deployment object could restart these pods that have dead service.

In Kafka, I think consumer groups have 2-way heartbeat mechanisms where group coordinators and consumer threads send heartbeat signals. So, Kafka heartbeat interval.ms is generally 1/3rd of session timeout and if no heartbeat signal is received by the co-ordinator till the end of the session timeout, the consumer instance is replaced. 
