# Content Delivery network (CDN)

Content Delivery Networks are a bunch of servers spread across the globe to serve information. 
These networks are available on rent to deliver static content quickly to nearby users.
Some examples of CDNs are Amazon CloudFront and the Akamai CDN. 
They are (relatively) cheap to rent and have high availability. 
They also provide pluggable algorithms to invalidate and fetch data.


# Why do we need a CDN?

Lets say you have a web-app.
When people try to open your website, their browser will hit your server,
and your server will respon with html for your web page (static files).

Now, lets say you have users from all around the globe.
Your server, even a cloud server, is actually hosted at a physical location.
So some users that are nearby this server will get the response pretty fast. 
But for some users, the data path will be long, and response time will be comparatively slower.


# A practical example of a CDN
In a practical application, you may want ther server to only deal with dynamic data (API hits that involve the database)
The static data request, like serving back the webpages, can be done using a cache.
You can create a write once, never delete cache.
Let's say your app servers 3 web-pages, one for mobile, one for tabs, one for desktops, and does this for 5 countries.
So, you have 3*5 = 15 static html web-pages stored in the cache.
The load web-page requests are directed to the cache instead of the server, reducing load on the server.

However, the cache would then be a SPOF.
So, you want to have replication, by making it a distributed cache.
You don't have to do it yourself, you can leverage services like RAFT/PAXOS.

Next, you have 3 caches, that all have 15 pages. 
But you might not need such big caches.
As the pages for one country are local to that country and people from other country would not see them.
So, then you can have multiple small caches, one for each country.
(Basically, sharding the cache horizontally based on location).

However, the entire network is still located at one place.
Requests from all countries travel to that place and then go back
This is not needed. 
So, you can have the server/cache, in the countries where your app is used.
However, this makes managing it difficult, and different countries have different data regulations.
So, we can use leverage a pre-build CDN service, like Akamai, or AWS CDN.
These services manages the servers/caches automatically, by hosting them closer to the users,
updating periodiaclly, and managing data regulations. 


# Extra info
when the user of a country let's say India makes a request, to what exactly will he be making a request? How do we know which CDN box we have to hit? We have the user's location but who determines the routing? Will there be an intermediate gateway or something like that in each country?

Well, there can be two ways the client gets routed to the CDN. 
First, when the client sends the request, it is sent to the server. 
After the first request, the client gets the address of the CDN from the server. 

Second, the ISP can map the domain to the IP Address of the nearest CDN. So when a client sends a request, he/she is first redirected to the CDN


