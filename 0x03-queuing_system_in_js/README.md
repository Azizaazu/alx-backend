0. Install a redis instance
Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - https://redis.io/downloads/):

$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
Start Redis in the background with src/redis-server
$ src/redis-server &
Make sure that the server is working with a ping src/redis-cli ping
PONG
Using the Redis client again, set the value School for the key Holberton
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
Kill the server with the process id of the redis-server (hint: use ps and grep)
$ kill [PID_OF_Redis_Server]
Copy the dump.rdb from the redis-5.0.7 directory into the root of the Queuing project.
Requirements:
Running get Holberton in the client, should return School
1. Node Redis Client
Install node_redis using npm

Using Babel and ES6, write a script named 0-redis_client.js. It should connect to the Redis server running on your machine:

It should log to the console the message Redis client connected to the server when the connection to Redis works correctly
It should log to the console the message Redis client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work .
.
.
.
11. Writing the test for job creation
Now that you created a job creator, let’s add tests:

Import the function createPushNotificationsJobs
Create a queue with Kue
Write a test suite for the createPushNotificationsJobs function:
Use queue.testMode to validate which jobs are inside the queue
etc.
12. In stock?
Data
Create an array listProducts containing the list of the following products:

Id: 1, name: Suitcase 250, price: 50, stock: 4
Id: 2, name: Suitcase 450, price: 100, stock: 10
Id: 3, name: Suitcase 650, price: 350, stock: 2
Id: 4, name: Suitcase 1050, price: 550, stock: 5
Data access
Create a function named getItemById:

It will take id as argument
It will return the item from listProducts with the same id
Server
Create an express server listening on the port 1245. (You will start it via: npm run dev 9-stock.js)

Products
Create the route GET /list_products that will return the list of every available product with the following JSON format:
