# What is DNS?

DNS stands for Domain Name Service.
In Computer Networks, machines don't go by names, instead they go by IP addresses. 
However, it is inconvenient to remember the IP address of every machine/server.
The DNS resolves names to IP addresses. 
So, if you type "Yahoo.com", the DNS will convert it to 74.125.44.25, and direct you to that address.

# How does a DNS work?

DNS is like a look-up database that maps domain names to their respective IP addresses. 
Many IP addresses that a person frequents, are stored in the browser's cache.
So, first, the entered domain name is searched in the cache and retrieves the IP from the cache if it is a hit.

If the browser cache check is a miss, the next query is sent to a resolver. 
A resolver is also known as an ISP (internet service provider).
The ISP has a cache of its own which has the most frequent domains that the ISP's customers are using.
The entered domain name is searched is retrieved from the ISP cache if it is a hit.

If the ISP cache check is a miss, the query is forwarded to a "Root server".
A Root server is at the top of the DNS hierarchy.
There are ONLY 13 sets of DNS Root servers in the world and they are placed at different geographical/physical locations.
These are maintained by 12 different organizations.
Each set has its unique IP address.

The next question is how does the ISP decide which DNS Root server to redirect the request to?
The DNS Root servers use anycast routing.
This allows all of them to share the same IP address.
When the request is redirected, a networking protocol like BCG (Border-Control-Protocol) is employed to route the request nearest, least busy Root server.

The DNS does not directly have the IP address of all the domain names.
However, the DNS Root server knows where exactly this particular domain fetch request should be routed to.
The DNS will respond to the ISP with the IP address of the appropriate TLD (Top-Level-Domain) server.
In www.yahoo.com, the .com part is called the top-level domain. 
There are two types of top-levels, gTLDs and ccTLDs.
gTLD stands for generic top-level domains, like .com, .org, .net, etc. 
ccTLD stands for country code top-level domain, like .in, .uk, .js, etc. 
Combining the gTLDs and ccTLDs, there are 1500+ top-level domains. 
The DNS Root server will send back the IP address of the TLD server that is responsible for fetching the requested domain name.

After receiving the TLD's IP address, the ISP will direct the domain name query to the TLD (here the TLD that is responsible for .com).
The .com TLD will not know the IP address of yahoo.com directly.
However, the .com TLD will know the IP address of ANSs (Authoritative Name Servers) that are authoritative for yahoo.com.  

An  (ANS) is a server that holds the complete and definitive database of domain names and their corresponding IP addresses.
An ANS will typically be authoritative for many domain names, and upon the inception/registry of the ANS, it will tell the TLD about the domains it is authoritative on.

For each domain, there are at least 2 different ANS that are authoritative on it. (There is deliberate redundancy in case an ANS fails). 
Famous domains can have multiple ANSs.
On getting queries for yahoo.com, the .com TLD will check the registry and find the ANSs that are authoritative on yahoo.com.
It will then return the IP address of these ANSs to the ISP.

Now, the ISP will query the ANS for yahoo.com.
An ANS is the eventual step in the DNS graph. 
The ANS will look up the IP address assigned to yahoo.com and return the IP address to the ISP.
The ISP returns the IP address to the browser, which can then fetch yahoo.com's webpage. 

The top-to-end DNS graph looks like this,
local browser -> ISP -> DNS root server -> ISP -> TLD server -> ISP -> ANS -> ISP -> local browser.
The entire process can be long, and introduce latency, hence, the ISP and the local browser both maintain a cache system to minimize traversing the entire DNS graph. 
