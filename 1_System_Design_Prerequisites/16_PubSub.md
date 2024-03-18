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

## 3. Ease of Interaction logic.

Interaction Logic:
In a REST architecture, interaction logic is often embedded within each service, which can lead to complex interdependencies and make the system harder to manage and scale.
In a Pub-Sub model, the interaction logic can be somewhat decoupled from the services themselves. 
The services publish and subscribe to messages without needing to know the details of other service implementations. 
This decoupling simplifies the interaction logic.

Failure Points:
Shifting to a Pub-Sub model can help in identifying and isolating failures because it centralizes message handling. 
While it can simplify the debugging process because there's a central place where message flows can be monitored, it also introduces a critical dependency on the message broker itself. 
If the MQ becomes a single point of failure, then its reliability becomes crucial for the entire system's stability.

To avoid this, Messaging services encapsulate load balancers, health services, etc. 
Hence chances of failure are low.
However, the MQ is a software application, and similar to any other backend server application, it can still fail.
To make them fail-proof, we can make them highly available across single or multiple regions(Disaster recovery). 
For a single region, high availability is achieved by deploying to multiple zones in a clustered environment with messages duplicated across brokers. 

## 4. Easily add subscribers and publishers without informing (Improving Scalability).
In a Pub-Sub (Publish-Subscribe) model, scalability is enhanced because you can add new publishers or subscribers without needing to inform or modify the existing components of the system.

In the Pub-Sub model, publishers and subscribers are decoupled. 
That is, they do not have direct knowledge of each other. 
Publishers send messages to a message queue or broker, and subscribers listen for messages they are interested in, without knowing who the original publisher is.
Subscribers can dynamically subscribe to topics or message queues of interest. 
When a new subscriber is added, it simply registers its interest with the message broker. 
There is no need to change the publisher’s code or configuration, as the publisher continues to send messages to the same queue.

Similarly, new publishers can start sending messages to a queue without affecting existing subscribers. 
As long as the messages conform to the expected format, existing subscribers can process them, enabling seamless scalability.

This decoupling allows the system to scale horizontally with ease. 
As the number of messages or the volume of data increases, you can add more publishers or subscribers to handle the load without significant changes to the system architecture or needing extensive coordination between components.
Additionally, the message broker or queue in the middle can manage load balancing and ensure messages are evenly distributed among subscribers, enhancing the system's overall fault tolerance and reliability.

## 5. Offers a loose consistency guarantee. 
The term "loose consistency" generally refers to the idea that all nodes in a distributed system will eventually become consistent but do not necessarily need to be consistent at all times.

In a REST architecture, if a server (e.g., S3) crashes during a request chain (S1 → S2 → S3), the ongoing request might be lost if not properly handled, and state consistency can be compromised unless there are mechanisms in place to retry or recover the transaction.
In an MQ system, messages are typically persisted in the queue. 
If a consumer (like S3) fails while processing a message, the MQ can retain the message and deliver it again when the consumer is back online. This persistence ensures that messages are not lost due to server crashes, enhancing fault tolerance and providing a form of consistency guarantee.

At-Least-Once Delivery:
Many MQ systems support "at-least-once delivery," meaning that messages are guaranteed to be delivered at least once to a consumer. If a consumer fails to process a message (due to crashing or other issues), the MQ system can redeliver the message, ensuring that the processing attempt is made again, which contributes to system consistency.


# Main Disadvantages:

## 1. Can not be used in systems requiring strong consistency of data
Let's say you have a banking service.
There are 3 microservices, S0, S1, and S2. 
S0 is a payment gateway, S1 is a bank commission calculator, and S2 is a fund transfer.
A has 1000 in his account. B has 0. The Bank commission is 50 flat.

A makes a request to S0 for transferring 950 into B.
A makes a second request to S0 for transferring 800 into C.
After the transaction, A should have 0, B should have 950, and Bank should be +50. (1st transaction executes)
(The second transaction fails due to insufficient funds).

Now, S0 sends the message in MQ of S1 and S2.
S1 takes the message and charges a fee of 50. A now has 950, and Bank has +50.
S2 has a high load, is experiencing downtime, or has crashed. 
So, the request to transfer stays in MQ.
The second transaction is called by A.
S0 calls S1 and S2 again by placing the request on the respective MQ.
S1 sees that there is 950 in A and transactions for 800 can go through.
Now, A has 900, and the Bank has +100.
Now S2 is up.
The first request of 950 comes, and fails as A only has 900. 
The second request of 800 comes and executes.

After the sequence, A has 100, B has 0, C has 800, and Bank has +100.
This is different than what should have happened.
Hence, when we decouple services, consistency of data always takes a hit.
We can avoid some of this with good design practices, but still, consistency is never perfect, as there is no 100% atomicity of transactions.

2. An extra layer of interaction slows services
3. Additional cost to the team for redesigning, learning, and maintaining the message queues.
4. Actual fiscal cost to MQ Brokers.
   
## 5. Idempotency
Idempotency means that performing the same operation multiple times has the same effect as doing it once. 
In the context of message queues (MQ), idempotency ensures that processing a message more than once does not lead to duplicate actions or changes.

Many MQ systems do not provide idempotency by default, meaning they don't automatically prevent the same message from being processed more than once. 
If a message is delivered multiple times, perhaps due to a network issue or service retry, it could result in repeated actions, like charging a customer twice for the same transaction.

Therefore, developers need to implement idempotency logic in their applications to check if a message has been processed before and avoid repeating actions. 
This often involves tracking which messages have been processed and ensuring that processing a message multiple times does not result in duplicated effects or data inconsistencies.



# Additional

## Common MQ Architecture
The concepts of push-based and pull-based models are central to understanding how MQs manage message delivery to consumers. 
Here's a comparison of the two models:

## Push-Based Model
Initiation: In a push-based model, the server (or broker) takes the initiative to send messages to the client (or consumer) as soon as they become available.
Control: The control over the message flow lies primarily with the server.
Latency: Typically offers lower latency since messages are sent immediately after they become available.
Resource Utilization: This can lead to high resource utilization on the client side, especially if the rate of incoming messages is high.
Examples and Usage:
RabbitMQ primarily uses a push-based model. 
It pushes messages to consumers as they arrive in the queue. 
This model is efficient in scenarios where it is critical to process messages as soon as they arrive and where consumers can handle the incoming message load effectively.


## Pull-Based Model
Initiation: In a pull-based model, the client (or consumer) requests or polls for messages from the server (or broker) when it is ready to process them.
Control: The control over the message flow is more on the client's side, allowing it to manage its own workload and fetch messages at its own pace.
Latency: This model can have higher latency compared to push-based, as there might be a delay between message availability and consumer polling.
Resource Utilization: Generally leads to more controlled and efficient use of client resources.
Examples and Usage: 
Kafka uses a pull-based model. 
Consumers poll Kafka for messages, which allows them to control the rate at which they process messages. 
This model is particularly effective in scenarios involving "large data streams (NBA, Spotify, Netflix, Live TV)" where consumers might need to manage a heavy load and require control over the rate of message processing.


## Comparison in Summary
Push-Based (e.g., RabbitMQ): Better for scenarios where immediate processing of each message is crucial, and consumers can keep up with the pace of message arrival.
Pull-Based (e.g., Kafka): More suitable for scenarios with high volume data streams (NBA, Spotify, Netflix, Live TV) where consumers require control over the processing rate to manage resource utilization and handle large data efficiently.

