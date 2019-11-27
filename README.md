# management_app_server

## Rest Api
An android application connect with sqlite database througt restful api. In our app the api accept the post request from android
application with user information and save it to database.

Django REST framework is used for making restful api.
For sending messages and email I used smtp server.

###end points
1) https://127.0.0.1.8000/checkin/
2) https://127.0.0.1.8000/checkout/

Server is currently local machine but for deployement we can deploy server on amazon web services.

## work flow of app_server

1) when user clicks on check_in button , the post request will occur and all information(also check_in time) is saved in database  and also mail will send to 
host with the help of smtp server.

2) when user clicks on check_out button , the post request will occur and all information(also check_out time) will send to user email_id.

check_in and check_out time will save in database by server_side with help of date_time method in python.
