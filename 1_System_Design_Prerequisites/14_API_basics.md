# API Basics

API (Application Programming Interface).
It is how two software/programs talk with each other. 
It is a software contract that defines the expectations and interactions of a piece of code being exposed externally. 
This includes the parameters, response, errors, API name, and sometimes, a key.

Note: API is not supposed to explain how your system (code/codebase) works.
It is supposed to explain how users interact with the system.
Hence, it serves as an "interface" to your codebase.

# Good API Design Practices
When designing an API, keep in mind,
1. What will the API be called? (Name it properly)
2. What input parameters will it expect? (along with their data types)
3. What will the API return? (along with the data type)
4. What can be a source of error? (try listing all possible errors)

Typically, we should not take unnecessary optional parameters.
An exception is when you could take additional optional parameters that could help you query less data and increase API performance.

Also, the API should only return what is expected (acc. to API name)
Many times people return multiple parameters thinking it is good to return excess information as it was already fetched.
However, this is a bad practice because:

1. It requires more bandwidth to transfer this data, so it could put stress on the network if the API is hit millions of times.
2. If the API is hosted on a cloud gateway, you most likely have to pay a data transfer fee, and this will increase your fee.
3. If these are not internal microservices, and you are charging a client per call, you may want to charge for the extra data you are returning in free.

The last important consideration is finding a balance about how many errors you want to define
You could define custom errors for every small thing, like invalid input param, wrong data type input param, unexpected input param value, etc.
Or, you may send a generic error for all of these problems.
It is best to define a custom error message for subtle mistakes (like the object you are querying for was deleted) or more frequent mistakes.


# Practical API Design Considerations


1. Designing endpoints?
A good API endpoint format is:

<base_url><file/page/service><API_name><Version>
www.firish/notes/getSystemDesignNotes/v2

For get requests, you can pass in parameters as a part of the query.
www.firish/notes/getSystemDesignNotes/v2?chapter=2
For post requests, you typically pass a full-fledged payload.



2. Side Effects
Lets say you are making a Whatsapp API, called "setAdmins" that is responsible for making a user admin of a chat group.
Now, what if this member is not in the group? You may add this member and then make them the group admin.
Now, what if the group does not exist? You would create a group, add the members, and then make them admin.
This will keep cascading.
This is not a good practice.
Your setAdmin API should only make someone the admin. There should be no "side effects". 

Another problem with Side Effects is that you risk losing the "Atomocity". Let's say you were doing everything in one API, and you create a group, but due to wrong parameters, logical error, network error, database error, or any random error, your API fails without setting admins, the group will already have been created. 
Now, if you were doing 4 things in the API and it fails midway, you don't have atomicity in the API. 



3. Dealing with long responses
Sometimes, you write an API that fetches some data from a table without filtering.
This is generally not a good practice. 
However, sometimes, this would be required.
In this case, the two best ways to deal with this problem are,

A. Paginations: Have a limit on a number of records returned by the API, and accept an offset from the client. If the offset is 20k and the limit is 10k, then you would return records 20k to 30k.
This approach delegates extra responsibility to the client and may not be an optimal solution.

B. Fragmentation: Let's say that the total response size is 100KB. 
But the limit for transmitting data is 10KB.
You could break your response down into 10 responses of 10KB and send them sequentially with a serial number that would then be used to reconstruct the responses in a sensible manner. 


4. API Degradation.
This refers to the consistency vs. performance tradeoff.
If you require extremely high consistency, you would hold strict locks even while reading, direct every API call to the server, and send the response back. Eg., An API that reads a person's account balance before doing some action. 
On the other hand, if consistency is not crucial, you could introduce a cache that is being refreshed after x time, and direct APIs to the cache, to decrease read time and reduce load on the server.
Eg., Getting the admins of a WhatsApp group. 
