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

## 1. Availability
EDA often involves components that operate independently, communicating through events. 
This means if one part of the system fails, the others can continue working. 
For example, in an e-commerce system, the checkout service might fail, but the browsing and cart services can still function, allowing users to browse products and add them to their carts.

## 2. Easy Roll-back (IMP)
The concept of "easy roll-back" in the context of Event-Driven Architecture (EDA) refers to the ability to quickly revert or undo changes in the system without causing significant disruption. 
This is particularly important in systems where updates or changes are frequently made, and there is a need to maintain stability and continuous operation.
This also helps with debugging and rapid recovery.

Imagine a scenario where a new version of a service is deployed, and it unexpectedly starts to malfunction. 
In an EDA system, you can quickly revert to the previous version of the service. 
This roll-back can be done without needing to undo changes across the entire system, minimizing downtime and impact on users. 
For instance, if an update to a payment processing service introduces bugs, you can roll back to the previous version of just that service, while the rest of the system (like order processing, inventory management, etc.) continues to operate normally.
Similar to how version control systems like Git allow developers to revert to previous code states, EDA supports reverting service changes. 
This is because each service in an EDA can be versioned and managed independently, much like code in version control.

## 3. Service Replacement
EDA allows easy replacement or upgrading of services without affecting the entire system. 
For example, if you want to replace an inventory management service with a new one, you can do so seamlessly as long as the new service emits and consumes the same events as the old one.
You can also use the events stored in the previous service to bring the new service up-to-speed on the current state of the system.

## 4. Transactional Guarantee
EDA can ensure that events are processed at least once or at most once, depending on the system’s requirements. 
"At least once" means every event will be processed, but there might be duplicates, suitable for scenarios where missing an event is unacceptable. 
"At most once" means events are processed only once, suitable for cases where duplicating actions is problematic. 
For example, in a billing system, "at least once" ensures every purchase triggers invoicing, but "at most once" prevents charging a customer twice for the same purchase.

## 5. Intent of the Data
Events in EDA carry the "intent" or the purpose behind the data change, not just the data itself. 
This means the system understands why a change occurred, enabling more intelligent and context-aware processing. 
For instance, an event stating "user added product to cart" carries more intent than just updating the cart's total count, allowing the system to trigger additional processes like recommendations or inventory checks based on the user's action.


# Disadvantages

## Consistency
Maintaining data consistency across distributed services can be challenging in EDA. 
Since events are processed asynchronously, ensuring that all parts of the system are synchronized and reflect the latest state can be difficult, especially in systems requiring strong consistency.

## Not Applicable to Gateways
EDA is less effective for processes that require immediate, synchronous responses, such as API gateways or direct user interactions, where a request/response model is more appropriate.

## Less Control
In EDA, the flow of execution is driven by events. 
This can lead to less control over the process flow, as the system's behavior is determined by the occurrence and handling of events, which can be unpredictable.

## Hidden Flow
The logic and flow of the application can become hidden or obscured in the interactions between event producers and consumers. 
This can make it hard to trace the path of execution and understand how data moves through the system.

## Migration
Migrating an existing system in an EDA to a normal architecture is difficult.
So, this may cause an architecture lock-in.


# How to enable the Roll-back of Events?

## Replay All from Start
One way to return to a previous state is to replay all events from the beginning. 
This can be time-consuming and resource-intensive, especially for systems with a long history of events.

## Store the Diff/Intermediate Results
Storing snapshots or intermediate states of the system can help in quickly reverting to a previous state without replaying all events. 
This approach balances storage cost against recovery speed.

## Undo
Implementing an "undo" functionality by emitting compensating events can revert the effects of previous operations, allowing the system to return to an earlier state.
E.g., add/sub/mult/division changes.
However, some events can not be undone easily, like sending an email/text.

## Event Sourcing
Event sourcing is a related concept where all changes to the application state are stored as a sequence of events. 
This not only allows for event replay but also for checking out the state of the system at any point in time by replaying events up to that point.

## Compacting or Squashing/Merging Events
Event Compacting
In systems with a large number of events, it can be beneficial to compact or squash events over time. This involves merging multiple events into a single event or snapshot that represents the final state after those events have occurred.
For example, if a record has been updated 100 times, instead of keeping all 100 update events, you could compact these into a single event representing the final state.
The main purpose of compacting is to reduce the number of events that need to be stored or replayed, making the system more efficient and quicker to restore or analyze.
This can be achieved through techniques like snapshotting (storing the current state at a point in time) or event merging (combining multiple events into one after every n events, or after t time), which can significantly reduce the load during event replay and state reconstruction.


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
