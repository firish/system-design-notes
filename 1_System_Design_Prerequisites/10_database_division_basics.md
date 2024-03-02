# Basic Information of data division


There are several types of data “distribution”:

First: Every instance is a clone of every other, 
with only minimal inconsistency tolerated during broadcasting of updates to all the instances. 
In terms of storage, the main purpose of this type of distribution is redundancy and optimizing read performance in the case of widely distributed db’s such as blockchain, 
as you can read an instance “near you” in terms of networking.

Second: Each instance, or each instance group (more typically the latter), has a distinct set of data. 
Instances within groups may be clones of each other, or have data-slices that are in common in a sort of RAID-ish fashion (ie, Cassandra rings), 
but in most types of distribution, a particular piece of data may reside in only one group.
If you have any sort of distribution where each instance or group isn’t a complete copy, 
you need some sort of rules for sending a particular piece of data to a particular storage pool in your distributed world.
This is where sharding comes in.

Partitioning:
This is a generic term that just means dividing your logical entities into different physical entities for performance, availability, or some other purpose. 

"Sharding" (sometimes used replacibly with horizontal partitioning): 
This is replicating the schema, and then dividing the data.
Consistent hashing is an algorithm for assigning a set of keys to machines with a few properties.
You can think of sharding as the decision to put your data on multiple machines, and consistent hashing as one of many methods of determining which machine any particular piece of data goes to.
Amazon shards the databse and then uses a Merkel Tree for heirarchial sharding. 
A Merkel tree is just like a B+ tree, where every node has the hash (of the shard key) of the sub shard,
and the leaf shards are the actual shards with data. 

# What is the difference between replication, partitioning, clustering, and sharding?
1. Replication - Copying an entire table or database onto multiple servers. 
Used for improving speed of access to reference records such as master data.

2. Partitioning - Splitting up a large monolithic database into multiple smaller databases based on data cohesion.
Example - splitting a large ERP database into modular databases like accounts database, sales database, materials database etc.

3. Clustering - Using multiple application servers to access the same database.
Used for computation-intensive, parallelized, analytical applications that work on nonvolatile data.

4. Sharding - Splitting up a large table of data horizontally i.e. row-wise.
A table containing 100s of millions of rows may be split into multiple tables containing 1 million rows each.
Each of the tables resulting from the split will be placed into a separate database/server.
Sharding is done to spread the load and improve access speed.

