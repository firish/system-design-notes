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
However, this is a bad practice as, 
a. It requires more bandwidth to transfer this data, so it could put stress on the network if the API is hit millions of times.
b. If the API is hosted on a cloud gateway, you most likely have to pay a data transfer fee, and this will increase your fee.
c. If these are not internal microservices, and you are charging a client per call, you may want to charge for the extra data you are returning in free.

The last important consideration is finding a balance about how many errors you want to define
You could define custom errors for every small thing, like invalid input param, wrong data type input param, unexpected input param value, etc.
Or, you may send a generic error for all of these problems.
It is best to define a custom error message for subtle mistakes (like the object you are querying for was deleted) or more frequent mistakes.

# Practical API Design Coniderations
