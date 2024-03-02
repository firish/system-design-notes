# Sharding

How do you make sure that queries run fast when the database is HUGE?

A very basic option is to optimize the query logic
A second option is to have indexes on certain attributes
However, these options fail when the database is truly enormous.

At such times, we can use database sharding. Sharding is the horizontal partitioning of data according to a shard key (database attribute). This shard key determines which database the entry to be persisted is sent to.

One common method is to shard on id (user_id, record_id, etc). 
However, you can also shard based-on other attributes. Tinder shards based on location, so that all the records from a location are stored together. 
Similarly, Netflix could shard on "genre", and so on. 

However, like everything, sharding giveth and sharding taketh away.

Problems with sharding, 
1) Joining across shards - if we want data from two different shards (partitions) the query must go to both of them and then merge the retrieved records. This is a costly operation.
   
3) A second problem is that typically the number of shards is fixed. so, if you have one server shard, you will get stuck while adding or removing servers. This may be solved using consistent hashing and virtual servers. Another way to deal with this is to have hierarchical sharding. So that each shard is further sharded into smaller shards. So this gives you the flexibility to change the number of shards in a way by changing the number of sub-shards.

Sharding good practices
1) A good practice is to shard the database and then index different attributes in the shards.
Continuing with the Tinder example, Tinder shards based on location.
Then on each shard, you can index based on 'Age'
This allows the app to read/fetch match suggestions in similar locations and similar age group.

2) It is also a good practice to have a Master-slave type backup of each shard. 
A shard is the master. A copy/s of the shard are slave. read operations are distributed amongst master and slaves, while writes are applied only to the master. The slaves update themself by polling the master shard. If the master shard fails, one of the slave shard becomes the master shard.
