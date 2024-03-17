# What is the Publisher-Subscriber Model?

Pub-Sub is an event-driven service model and provides the basis for event-driven systems.
In this model, events are produced by a publishing service and consumed by downstream services.
This model works great with Microservices, as they benefit from the loose data coupling that it provides.  
Designing the microservice interactions involves event handling and consistency checks. 


# Pub-Sub architecture vs a Request-Response architecture.

Pub-Sub architecture relies on message queues to ensure event passing. An example would be rabbitMQ or Kafka.
The architecture is very common in real-life scenarios. 
If no strong consistency guarantee is required for transactions, an event model is good to use in microservices.

Main advantages:
1. Decouples a system's services.
2. Easily add subscribers and publishers without informing the other.
3. Converts multiple points of failure to a single point of failure.
4. Interaction logic can be moved to services/message broker.

Main Disadvantages:
1. Can not be used in systems requiring strong consistency of data
2. An extra layer of interaction slows services
3. Additional cost to the team for redesigning, learning, and maintaining the message queues.



