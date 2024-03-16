# Messaging Queue

Messaging Queues are widely used in "asynchronous" systems. 
Message processing in an asynchronous fashion allows the client to relieve itself from waiting for a task to complete and, 
hence, can do other jobs during that time. 
It also allows a server to process its jobs in the order it wants to.

It means that once the client sends a request, the server can send just a response "Okay".
Then add the query in the messaging queue along with other queries, and process them using any custom scheduling algorithm.
Once a clients query is processed, the actual response is then sent back to the client.
(E.g., A restaurant (system) takes multiple food orders (placed in a queue) simultaneously from customers (clients), while the chef (server) prepares an order. 
Once the order is ready, the chef moves to the new order in the queue, and the ready dish (response) is taken to the customer (client). 

Messaging Queues provide useful features such as persistence, routing, and task management. 
E.g, you have multiple servers and a queue per server.
If a server goes down, you could send its queue to other available servers, and stop a total failure of the system. (increased persistence)
(Keep in mind, for this to work, the queue must be stored in a database).

A system having a message queue can move to higher-level requirements
while abstracting implementation details of message delivery and event handling to the messaging queue.

Note: The 'queue' is just a name for this data structure. 
In practice, it could be storing messages using any policy. 
Some examples of message queues are Kafka and RabbitMQ (very popular). 
They are widely used for various purposes such as command query request segregation (CQRS) and event sourcing.

