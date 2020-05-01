## Restful APIs development with Python Flask.
- A RESTFUL API is an application program interface - *API*.
- RESTful APIs are used to provide the communication between two parties over the network.
- RESTful APIs are developed using REST rules.
- REST rules are set of rules to develop modern web applications to send and receive data over the network.
- REST APIs are not used to serve any web applications, instead of that they are used as an interface between two parties to provide communication between them over the network with its URL.


## REST (Representational State Transfer).
- we have to know some concepts before understanding about what is *REST*?
- E.g.: GitHub REST API:
  - *https://api.github.com/users/{username}/repos*
- *Client*:
  - The client is the person or software who uses the API.
  - Here: curl/browser/program/script/any application
- *Resource*:
  - A resource can be any object that API can provide information about.
  - Here: GitHub account repos.

#### REST means when a RESTful API is called, the server will transfer the representation of the state of the requested resource to the client.

- It's better to know how to use existing REST APIs then develop APIs on our own.
- Execution of existing REST APIs can be done by using:
  - curl command
  - postman
  - requests module (python)
- Implementation of REST APIs:
  - flask, flask restful, flask restplus.
  - Integration with swagger UI.
  - Dockerizing our Python REST APIs and deploy them for production.

## Basic Concepts of REST applications.
- **Concepts**:
  - Base URL
  - Endpoints
  - Resource
  - HTTP verbs/methods/operations

#### Base URL:
- Just consider dummy REST APIs from: http://dummy.restapiexample.com/
  - http://dummy.restapiexample.com/api/v1/employees
  - http://dummy.restapiexample.com/api/v1/employee/1
  - http://dummy.restapiexample.com/api/v1/create
  - http://dummy.restapiexample.com/api/v1/update/21
  - http://dummy.restapiexample.com/api/v1/delete/2
- Here the Base URL or the Root Endpoint is: http://dummy.restapiexample.com
- Remaining parts are called Endpoints/Routes
- They are:
  - /api/v1/employees
  - /api/v1/employee/1
  - /api/v1/create
  - /api/v1/update/21
  - /api/v1/delete/2
- So REST API URL is : **Base URL + Endpoint**

#### Resource and HTTP Verbs:
- Resource is simply data in web application.
- Simply Endpoints are useful to work with resource(s).
- SO, we have to execute different operations/methods on endpoints based on requirement.
- Those methods/operations are called HTTP verbs.
- The different HTTP verbs are: **GET, POST, PUT** & **DELETE** etc...
- GET method is used to get existing resource info/data from web application.
- POST method is to send a data resource in web application.
- PUT method is to update existing resource in web application.
- DELETE method is to delete resource in web application.
- Note: *Most of the cases REST API's response is in the form of csv/json/xml and rarely text*.

## HTTP Status Codes.
- HTTP Status code represents the status of a request on REST APIs.
  - curl -x GET {url}
  - curl -i -x GET {url}
- We can get the HTTP status code from the header of a response.
- The status code is a 3 digit integer where the first digit of the status code defines the class of response and the last two digits don't have any categorization role.
- Status Codes:
  - 1xx - *Informational*
  - 2xx - *Success*
  - 3xx - *Redirection*
  - 4xx - *Client Error*
  - 5xx - *Server Error*
