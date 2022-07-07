# Assignment_solution_Chezuba:
 A small application exposing the given endpoint through a REST API, in this project Flask framework is used:
 
# Prerequisite:
 I am assuming you have cloned and completed the setup of the project. 
 
 
# Lets start:
 ### Importing library and modules
 ```
 from flask import Flask, request
 import json
 import pandas as pd
 ```
 - request module is specified to get the access the data from the clientside like json or parameters<br>
 - json library imported to return our response as a json formated document to the client side<br>
 
 ```
 app = Flask(__name__)
 ```
 - initialize the app instance to the flask class
 
 ```
 @app.route("/1/queries/count/<DATE_PREFIX>", methods = ['GET'])
 ```
 - adding the route endpoint to access the specific function of the project<br>
 ### The main function:
 ```
 def fetch_data(DATE_PREFIX):
    prefix = DATE_PREFIX

    #creating the dataframe from the .tsv file and add the columns name
    df = pd.read_csv('hn_logs.tsv',sep = '\t', names=['date_time','url'])
    
    #converting the string date_time column to Date_time format by creating a new column
    df['Date'] = pd.to_datetime(df['date_time'])

    #setting the Date column as index of the dataframe
    df.set_index('Date', inplace=True)
      
    #counting the numbers of record according to our given date_time range  
    count = len(df[prefix].index)

    #adding the count value to the json object 
    result = {
        "count" : count
    }
    #print(result)

    return json.dumps(result)
        
```
# Description of the function:
In this project pandas library is used by re-implement some of its feature to achieve our goal.<br>
First of all we creating the dataframe by specifying the file type here is ".tsv" and adding some column name to it in the dataframe.<br>
Next we converting the column 'date_time' which is in string format to 'Date_time' format with "Date" column name,<br>
Then setting the "Date" column as the index of the dataframe.<br>
Next fetched the records which are satisfying our data_time range and storing the length of the dataframe to a variable named "count".<br>
After that created a json object called result and initialize the count key.<br>
Finally returning the json object to the client side.

# Run the project:
Open any favorite IDE, open the terminal
install the virtual enviornment package in the computer by following command:
```
pip install virtualenv
```
after that create the virtual env by below command:
```
virtualenv venv
```
Here "venv" is our current enviornment name.<br>
After that need to activate our virtual enviornment by the command:
```
> .\venv\Scripts\activate 
```
#### Good to go our virtual enviornment is now activated.<br>
install the required dependencies like flask, pandas etc.<br>
## Dependencies:
 Install the flask framework by following commands:<br>
 ```
 pip install flask
 ```
 Install pandas to re-implement its features to make our task complete<br>
 ```
 pip install pandas
 ```
Or we can install all our required packages in a single go by this command:
```
pip3 install -r requirements.txt
```
It will install all the project's dependencies to the virtual enviornment.<br>
Next need to activate our flask enviornment variable.<br>
```
setx FLASK_APP "app.py"
```
finally run the project by the last but not the least command:<br>
```
flask run
```
### Congatulations the project is running now on the local server
# Access the endpoint:
To make our functionality work we have to send request to the server using any browser or we can use postman.<br>
Simply paste the request url by selecting the method 'GET' and pass the date range like given below:

Examples<br>
Distinct queries done in 2015: GET /1/queries/count/2015: <br>
Distinct queries done in Aug: GET /1/queries/count/2015-08: <br>
Distinct queries done on Aug 3rd: GET /1/queries/count/2015-08-03: <br>
Distinct queries done on Aug 1st between 00:04:00 and 00:04:59: GET /1/queries/count/2015-08-01 00:04: <br>

# Summary:
The application will works fine as per the task, but as per my research this is not the efficient way to do the application run effectively because its taking a small time gape to get the record count this is because its quering all through the record in the dataframa which will increase everytime the record numbers increase.<br>
As per my knowladge ELASTIC-SEARCH could be a perfect solution to make this functionality efficient if we use in the storage procedure.



# System Design digram:

 ![system_design_backend](https://user-images.githubusercontent.com/80528499/177852768-fd141860-64e7-4cf5-a0b2-8261290d41d9.JPG)

# System Design Description:
Here i used the AWS EC2 instance to host my application. <br>
After creating the EC2 instance on AWS need to logon to the instance by using the IP address of the instance.<br>
Then we ready to go with the instance by installing the Nginx the wsgi webserver and Gunicorn to communicate with the application and instance.<br>
Also need to install all the application's dependencies the instance. Here we can use the loadbalancer feature to redirect and balance our requests to the application endpoint. 
Finally the server configured with the DNS service and it will expose to all the users over the world to serve them throw internet.

# Scalability:
AWS or GCP provides the basic auto scalling feature to balance the getting requests and work on the server, but according to the service demand we can add vertical and horizontal scalling to the system .<br>
Also for now we are dealing with a single service to serve in this application if we expanding our services we can implement the microservice architecture to the system.
## Thank You So Much for giving the time to evaluate the project
