## Graphql

### Definition:

It is an API query language that allows reading and mutating data in APIs, created by Facebook to solve the problems of Under Fetching and Over Fetching.

### Particularities

It attacks the problems of Under Fetching and Over Fetching.
GraphQL can be tested with a tool called graphiql or with postman.

+ **Under Fetching:** In an application, multiple entities and data may be needed at a single given time. Under the Rest concept, it is normal that in order to obtain this information, multiple requests are made to obtain the desired information.

+ **Over Fetching:** Obtaining a lot of data when requests are made and not using all of it. Which means that the requests can be very heavy.

### Traits

+ It needs dependencies for its use.
+ It uses 3 terms to differentiate the types of queries that can be made to the backend: Queries, Mutations and Subscriptions.

**Queries:** Queries to request data from the client, equivalent to GET requests.
**Mutations:** Send requests to the server to modify data, equivalent to a POST, PUT, DELETE.
**Subscriptions:** develop real-time connections between client and server based on Websockets.

### Differences between REST API and GraphQL:

**REST API:** Uses multiple endpoints and HTTP methods, can cause over-fetching/under-fetching issues, and often requires versioning.
**GraphQL:** Uses a single endpoint and dynamic queries, solves over-fetching/under-fetching issues, and generally avoids the need for versioning.

### Graphql on Python

#### How to use Graphql with Python:

+ Install ```graphene```
+ Install ```starlette_graphene3```
+ Install ```fastapi```
+ Install ```uvicorn```

#### Execute app ```uvicorn 1_intro:app --reload --port 8081```


### What is ObjectType

A Graphene **ObjectType** is the building block used to define the relationship between **Fields** in your **Schema** and how their data is retrieved.

#### Basics:

+ Each ObjectType is a Python class that inherits from ```graphene.ObjectType```
+ Each attribute of the ObjectType represent a Field.
+ Each Field has a resolver method to fetch data (or Default Resolver)