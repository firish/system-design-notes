# What is the Publisher-Subscriber Model?

Pub-Sub is an event-driven service model and provides the basis for event-driven systems.
In this model, events are produced by a publishing service and consumed by downstream services.
This model works great with Microservices, as they benefit from the loose data coupling that it provides.  
Designing the microservice interactions involves event handling and consistency checks. 


# Pub-Sub architecture vs a Request-Response architecture.

Pub-Sub architecture relies on message queues to ensure event passing. An example would be rabbitMQ or Kafka.
The architecture is very common in real-life scenarios. 
If no strong consistency guarantee is required for transactions, an event model is good to use in microservices.

# Main advantages:
## 1. Decouples a system's services.
E.g, If S1 receives a request it must do some work and make three more calls to S2, S3, and S4.
In the Pub-Sub model, S1 can do so in any order.
It sends a successful response to the client immediately after publishing to S2, S3, and S4.
The requests to each of these servers are stored in an MQ to that server.
Once the server completes the request, the response is sent back to the client directly by the MQ.
This makes S1 free from any requirements and results of call to S2, S3, or S4, achieving decoupling.
This enhances the system's responsiveness and scalability.

In contrast, in a REST architecture, this cascading would be achieved through asynchronous calls by S1 to S2, S3, and S4. 
However, S1 might still need to manage the coordination, error handling, and aggregation of responses from S2, S3, and S4. 
This maintains a level of coupling and can affect the system's scalability and fault tolerance.

## 2. Lower failure latency
In request-response architecture(REST), assume that there is a multi-layer request hierarchy.
I.e. S1 calls S2 and S2 calls S3 and S4.
Given that each server processes requests to other servers asynchronously, a failure to process requests in S4 will have to be propagated to S2 through callbacks or notifications(email, SMS, or push messages).
Similarly, this failure is again propagated to S1 through callbacks or notifications.
S1 again forwards this failure to the original requesting user through callbacks or notifications.
Because of the limitations of this architecture, failure messages will have to flow through the strict hierarchy(S4 to S2 to S1 to the user) to reach the user.
The total delay in getting the failure message to the client is failure latency.

In an event-driven architecture using Pub-Sub, the failure handling is more localized.  
S1 does not care about what happens in S2 and S2 does not care about processing in S3 and S4. 
All servers will have a message broker/message queue in between them.
These queues have data persistence.
If S4 encounters an issue, it can handle the failure locally, potentially retrying the operation or moving the message to a Dead Letter Queue (DLQ). 
DLQ is a Dead-Letter Queue, which houses messages that the system can't process owing to any error.
This DLQ can then be monitored, and notifications can be sent directly to the client or an administrator, bypassing the need for upstream services to be involved in the error-handling process. 
This setup can significantly reduce the time it takes for a failure to be communicated back to the client.
The benefit is even greater in systems where the calling hierarchy has many levels. 

 
4. Easily add subscribers and publishers without informing the other.
5. Converts multiple points of failure to a single point of failure.
6. Interaction logic can be moved to services/message broker.

Main Disadvantages:
1. Can not be used in systems requiring strong consistency of data
2. An extra layer of interaction slows services
3. Additional cost to the team for redesigning, learning, and maintaining the message queues.



