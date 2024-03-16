# What is a Messaging Queue?

Messaging Queues are widely used in "asynchronous" systems. 
Message processing in an asynchronous fashion allows the client to relieve itself from waiting for a task to complete and, 
hence, can do other jobs during that time. 
It also allows a server to process its jobs in the order it wants to.

(Better worded explanation)
Message Queues are designed to facilitate this kind of parallel execution.
Instead of executing the tasks right away, MQ queues up the tasks it receives therefore decoupling publisher from subscriber. 
The publisher does not wait for the task to be completed and continues with its execution knowing that the task will be executed in due course of time. 
The subscriber receives the tasks one by one based on its processing capacity. The key here is both publisher and subscriber are working at the same time, the publisher on its main task with the subscriber executing its assigned sub-task.

# What it means in simple terms.
It means that once the client sends a request, the server can send just a response "Okay".
Then add the query in the messaging queue along with other queries, and process them using any custom scheduling algorithm.
Once a clients query is processed, the actual response is then sent back to the client.
(E.g., A restaurant (system) takes multiple food orders (placed in a queue) simultaneously from customers (clients), while the chef (server) prepares an order. 
Once the order is ready, the chef moves to the new order in the queue, and the ready dish (response) is taken to the customer (client). 

# Additional benefit of MQ (Increased Resilience)
Messaging Queues provide useful features such as persistence, routing, and task management. 
E.g, you have multiple servers and a queue per server.
If a server goes down, you could send its queue to other available servers, and stop a total failure of the system. (increased resilience)
(Keep in mind, for this to work, the queue must be stored in a database ("MQ data must persist").
The actual flow would look like this,
You had 5 servers. Each server had its MQ.
All MQs are stored in one DB.
We will have a heartbeat service running.
As soon as a server is down, the heartbeat service will detect it.
The heartbeat service can then notify a new microservice that queries the common DB and fetches all unfinished jobs in the failed server's MQ.
These will be passed on to a load balance, in inturns routes them to existing and working servers. 
Popular services like RabbitMQ have the MQ, heartbeat, query service, and load balancer all built-in. 


# IMP Note
The 'queue' is just a name for this data structure. 
In practice, it could be storing messages using any policy. 
Some examples of message queues are Kafka, and RabbitMQ (very popular), and Zero MQ. 



