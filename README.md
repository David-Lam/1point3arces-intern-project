# 1point3arces-intern-project

## Login with username and password
sample http request: `127.0.0.1:5000/login`  
params: `username=tester1&password=testering1`  
method: `POST`  
sample response: 
```json
{
  "message": "Logged in successfully."
}
```
sample error response (Invalid username or password):
```json
{
  "error": "Invalid username or password."
}
```
sample error response (User already logged in):
```json
{
  "error": "You are already logged in."
}
```

## Register with username, password, and email 
sample http request: `127.0.0.1:5000/register`  
params: `username=username&password=password&email=testemail@gmail.com`  
method: `POST`

sample response:
```json
{
  "message": "The email confirmation was sent."
}
```
sample error response (Username, password, or email are too long):
```json
{
  "error": "The length of information can't excess 255 characters."
}
```
sample error response (Username had been taken):
```json
{
  "error": "Username had been taken."
}
```
sample error response (Email had been taken):
```json
{
  "error": "Email had been taken."
}
```
sample error response (Invalid email):
```json
{
  "error": "Invalid email."
}
```

## Confirm email 
sample http request: `127.0.0.1:5000/register/confirmEmail/token`   
params: `token`  
method: `GET`

sample email:
**Click on the link:http://127.0.0.1:5000/register/emailConfirmation/token to confirm your email.**

sample response:
```json
{
  "message": "Account created successfully."
}
```
sample error response (Token expired):
```json
{
  "error": "Token expired."
}
```
sample error response (Invalid token):
```json
{
  "error": "Token is invalid."
}
```
sample error response (Account already created):
```json
{
  "error": "Account is already created."
}
```

## Get user profile  
sample http request: `127.0.0.1:5000/profile`   
method: `GET`  

sample response:
```json
{
  "user": {
    "posts": [
      {
        "id": 1,
        "title": "title1",
        "content": "Content1 by tester1",
        "dateCreated": "2019-08-31T19:43:13",
        "dateUpdated": "2019-08-31T19:43:13"
      },
      {
        "id": 2,
        "title": "title2",
        "content": "Content2 by tester1",
        "dateCreated": "2019-08-31T19:43:13",
        "dateUpdated": "2019-08-31T19:43:13"
      }
    ],
    "sentMessages": [
      {
        "id": 1,
        "content": "Hello Tester2",
        "date": "2019-08-31T19:43:13",
        "receiver": {
          "username": "tester2"
        }
      }
    ],
    "receivedMessages": [
      {
        "id": 2,
        "content": "Hello Tester1",
        "date": "2019-08-31T19:43:13",
        "sender": {
          "username": "tester2"
        }
      },
      {
        "id": 3,
        "content": "Hello Tester1",
        "date": "2019-08-31T19:43:13",
        "sender": {
          "username": "tester3"
        }
      }
    ],
    "id": 1,
    "username": "tester1",
    "password": "testing1",
    "email": "tester1@email.com"
  }
}
```
sample error response (Login needed):
```json
{
    "message": "The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required."
}
```

## Get user messages
sample http request: `127.0.0.1:5000/messages`    
method: `GET`  

sample response:
```json
{
  "messages": [
    {
      "id": 1,
      "content": "Hello Tester2",
      "date": "2019-08-31T19:43:13",
      "sender": {
        "username": "tester1"
      },
      "receiver": {
        "username": "tester2"
      }
    },
    {
      "id": 2,
      "content": "Hello Tester1",
      "date": "2019-08-31T19:43:13",
      "sender": {
        "username": "tester2"
      },
      "receiver": {
        "username": "tester1"
      }
    },
    {
      "id": 3,
      "content": "Hello Tester1",
      "date": "2019-08-31T19:43:13",
      "sender": {
        "username": "tester3"
      },
      "receiver": {
        "username": "tester1"
      }
    }
  ]
}
```
sample error response (Login needed):
```json
{
    "message": "The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required."
}
```

## Get posts  
sample http request: `127.0.0.1:5000/posts`     
method: `GET`  

sample response:  
```json
{
  "posts": [
    {
      "id": 1,
      "title": "title1",
      "content": "Content1 by tester1",
      "dateCreated": "2019-08-31T19:43:13",
      "dateUpdated": "2019-08-31T19:43:13",
      "poster": {
        "username": "tester1"
      }
    },
    {
      "id": 2,
      "title": "title2",
      "content": "Content2 by tester1",
      "dateCreated": "2019-08-31T19:43:13",
      "dateUpdated": "2019-08-31T19:43:13",
      "poster": {
        "username": "tester1"
      }
    },
    {
      "id": 3,
      "title": "title3",
      "content": "Content2 by tester2",
      "dateCreated": "2019-08-31T19:43:13",
      "dateUpdated": "2019-08-31T19:43:13",
      "poster": {
        "username": "tester2"
      }
    }
  ]
}
```

## Logout
sample http request: `127.0.0.1:5000/logout`    
method: `POST`  

sample response:
```json
{
  "message": "Logged out successfully."
}
```
sample error response (User already logged out):
```json
{
    "message": "The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required."
}
```
