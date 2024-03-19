# Event Driven Architecture


Event-driven architecture (EDA) is a design paradigm in which components or services of a system communicate with each other through the production, detection, consumption, and reaction to events. 
An event is a significant change in state or an important occurrence that other parts of the system need to be aware of and potentially respond to.
Imp: Events are typically accompanied by timestamps. This allows the processing of events in sequence. 

Event-driven systems pass and persist events. 
They have evolved from the publisher-subscriber model, and the design has some advantages. 
Famous examples of systems using this architecture are Git, Node, React, and a LOT of gaming engines.

# The basic working of an EDA
Here's how event-driven architecture works:

Event Producers: These are sources of events in the system. 
An event producer generates an event whenever something notable happens within the system, like a user action, a change in data, or an external trigger. 
For example, a sensor could produce an event when it detects a temperature change.

Events: Events are the core of an EDA. 
They are data records that represent something that happened in the system. 
An event contains information about what occurred and any relevant context. 
Events are typically lightweight and designed to be processed quickly.

Event Consumers: 
These are components or services that listen for and react to events. When an event occurs, interested consumers are notified and can take appropriate action. 
The action taken in response to an event can vary widely, from updating a database to triggering a complex workflow.

Message Broker / Event Bus: 
To facilitate the communication between producers and consumers, EDA often uses a message broker or an event bus. 
This intermediary component decouples the event producers from the consumers, allowing them to operate independently. 
The broker routes events from producers to the appropriate consumers, managing the distribution and delivery of messages.

Asynchronous Communication: One of the key characteristics of EDA is that it's primarily asynchronous. 
Producers send events without needing to wait for a response from the consumers. 
This non-blocking behavior enables high levels of scalability and flexibility in the system.


# Advantages of EDA
1. Availiblity
2. Easy Roll-back (Git example?)
3. Service replacement
4. Transactional guarantee (atleast 1 or atmost 1)
5. Intent of the data


# Disadvantages
1. Consistaincy 


Events are immutable and can be replayed to allow the systems to take snapshots of their behavior. 
This allows services to 'self-heal'.

A lot of transaction issues are alleviated once idempotency and retrial logic are added to a system. 
The system can retry messages an infinite number of times to the recipient till there is a message acceptance and acknowledgment from the receiver.

Event-driven systems are closely related to event sources and CQRS. 
Greg Young and Martin Fowler have been talking about these systems for a while. 
Events are persisted in something like a message queue, and hence the responsibility for retrial and persistence is moved to it.

These abstractions enable the programmer to focus on the business logic of a system and add subscribers to events with minimum coupling with other services. 
Decoupling the system is one of the advantages of event-driven systems.

One major disadvantage of this system is that it is difficult to reason about the flow of a request. 
Services can independently register for an event and consume it without the publisher being aware of it.


# Extra Information

## Why is EDA used in multiple game engines?
Consider the example of a game like Counter-Strike
Player 1 is shooting and player 2 is jumping to evade.
In a regular architecture, till the time the shot of player 1 is processed, position of player 2 may have changed slightly causing the shot to miss.

In an EDA,
Imagine you have the game state based on a series of actions.
So, a shot, as well as any movement is an event.

Time - Action - Result State.
T1 - A - S1
T2 - B - S2
T3 - C - S3
T4 - D - S4

To recreate any point in the game up to timestamp Ts, you just need to run through the events from T1 to Ts.
Assume you have a new event.

new event:
Ts - E
What should be the result state? 
If Ts < T4, you want to check the effect of action E with S3, not S4.

How do you get S3? Three options:
1. Replay all events from the initial state up to all actions with timestamp < Ts.
2. Undo the events with timestamps >= Ts (the system must know how to undo any action).
3. Store the intermediate states of the game (S1, S2, S3).

Once you make the action E, play the action D and broadcast the new state to all clients.
