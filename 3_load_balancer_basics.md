# Load Balancing

Load balancing is a technique used in computing to distribute workloads uniformly across multiple servers or other resources to optimize resource usage, reduce latency, and ensure that no single server is overwhelmed with too much demand. This helps improve responsiveness and availability of applications, websites, databases, and other IT services.

There are several methods used for load balancing, including:

- **Round Robin:** This simple method involves distributing requests sequentially to servers in a list. When the end of the list is reached, the load balancer starts again at the top.

- **Least Connections:** This method directs new requests to the server that is currently handling the fewest active connections.

- **IP Hash:** This method uses the client's IP address to determine which server to direct the request to. This can help ensure that a client always connects to the same server.

- **Least Time:** This method combines both the shortest queue length and the fastest server response time to direct traffic.

## Hashing

Hashing is a technique used in computer science to convert a large amount of data into a smaller fixed size. It is primarily used to facilitate rapid data lookup and access in data structures such as hash tables. A 'hash function' performs the operation to convert the input data into a smaller fixed size, often referred to as a hash code.

## Load on Servers

In the context of load balancing and servers, the "load" refers to the amount of computational work that a server is currently performing. This can be measured in various ways, such as the number of active connections, CPU usage, memory usage, network bandwidth, or a combination of these and other factors.

## Load Factors

In the context of a hash table, the load factor is a measure that determines when to resize the table. It's calculated as the number of entries in the hash table divided by the number of slots or buckets. 

## Uneven Distribution

Uneven distribution occurs when a hash function does not distribute data uniformly across the range of possible hash values. This can lead to certain servers receiving more requests than others, which is undesirable in a load balancing scenario because it defeats the purpose of evenly distributing the load to optimize resource utilization.

## Adding More Servers

When you add more servers to your server pool, the distribution of load needs to be recalculated. With a simple hash function, adding a new server often requires rehashing and redistributing all the existing data, which can be computationally expensive and disruptive to a system in operation. Plus, if all requests are mapped to different servers suddenly, all the useful information cache is suddenly a waste.

## Consistent Hashing

Consistent hashing is a strategy that's often used to mitigate these issues. With consistent hashing, when a new server is added, only a small fraction of keys get remapped, minimizing disruption and load spikes. Similarly, when a server is removed, its load is smoothly redistributed among the remaining servers.
