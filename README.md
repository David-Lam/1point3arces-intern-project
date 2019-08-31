# 1point3arces-intern-project

**Login with username and password**  
sample http request: `127.0.0.1:5000/login`  
params: `username=tester1&password=testering1`  
method: `POST`  
sample response: 
```json

```
sample error response (Invalid username or password):
```json

```
sample error response (User already logged in):
```json

```

**Register with username, password, and email**  
sample http request: `127.0.0.1:5000/register`  
params: `username=david&password=password&&email=testemail@gmail.com`  
method: `POST`

sample response:
```json

```
sample error response (Username, password, or email are too long):
```json

```
sample error response (Username had been taken):
```json

```
sample error response (Email had been taken):
```json

```
sample error response (Invalid email):
```json

```

**Confirm email**  
sample http request: `127.0.0.1:5000/posts`   
params: `token`  
method: `POST`

sample email:

sample response:
```json

```
sample error response (Token expired):
```json

```
sample error response (Invalid token):
```json

```
sample error response (Account already created):
```json

```

**Get user profile**  
sample http request: `127.0.0.1:5000/profile`   
method: `GET`  

sample response:
```json

```
sample error response (Login needed):
```json

```

**Get user messages**  
sample http request: `127.0.0.1:5000/messages`    
method: `GET`  

sample response:
```json

```
sample error response (Login needed):
```json

```

**Get posts**  
sample http request: `127.0.0.1:5000/posts`     
method: `GET`  

sample response:  
```json

```

**Logout**  
sample http request: `127.0.0.1:5000/logout`    
method: `POST`  

sample response:
```json

```
sample error response (User already logged out):
```json

```
