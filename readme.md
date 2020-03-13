# MultiClient-Sever
Its a simple multi-client server that runs on various devices . Server can select the particular client from the list shown . Client can input the data asked by server and will write that data into the output.txt.

## Requirements
Our project will run on Python 3.8.2 .If you dont want have the required version.You can download it via cmd (as administrator) ,just run following coommand:
```
python -m pip install --upgrade pip
```
## Server
Well, we have provided the server.py file. Open cmd prompt , run ```python server.py``` or ``` python3 server.py```(if showing some error) .This is will create your server and if doesnt show any error(i hope it doesnt) ,then your server is up and listening for different connection from different IPs.

## Client
We have also provided you the client.py file. You have to change the ip address in client file.You can know your ip address by typing ```ipconfig``` for windows. And update the ip address in client file.
Now open as many cmd propmt as you want. And run the client.py using ```python client.py``` or ``` python3 client.py```(if showing some error) on each cmd.
And you can see, connection estabilished will be shown on server window. And thats how you can know your client server is running perfect.


## Lets Run some command
### list
As, you have already seen that Connection Established will be shown on server windows.Now, you press the enter it will start Custom Interactive Shell on Seerver side. We'll take about Custom Interactive Shell little bit later. Now when you type ``` list``` besides ```coronavirus->```,and press enter, it will show the list of clients that are connected to the server. Format for the list will be like,for eg: ```0  10.8.6.22  50456``` 
here,"0" is unique id assigned by the server to each client.
     "10.8.6.22" is the ip address of the client
     "50456" is the port number

### select 0
Now, when you type ```select <id>```, for eg, "select 0" , it will select the 0th client and start sending data. 
on Client side, it will ask for different information from the user like "Name , Age, Profession , Message". and sending the data to Server. on server side, it will show " Writing data to file". and client side it will show "Done!!You are good to go"

### printdata
If you want you can select different client and get their data too!!
Now, if you want to check for the data that written to file. Just type,```printdata``` and press enter. It will show you all the data written to text file. 