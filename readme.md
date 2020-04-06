# MultiClient-Sever
Every country reacts differently to the COVID-19 pandemic. Some governments may make late decisions to protect their people. This problem is due to the long incubation time of the virus (few weeks), but also to the lack of screenings. The tests are expensive and may take time, so in order to be more efficient in the fight against the virus, some countries neglect them.

So we built an application where any user could signal if they have any symptom related to the COVID-19 disease. Anonymously, an user informs his age, gender, travel history and symptoms. This information, plus their geolocation identified by their IP address, are transmitted to a server. This server is a database that gather all users information and their location, and, thanks to an algorithm, computes the chance that a given user is infected. 

## Requirements
Our project will run on Python 3.8.2 .If you dont have the required version.You can download it via cmd (as administrator) ,just run following coommand:
```
python -m pip install --upgrade pip
```
We also workign with "pickle", "requests" , "json" libraries. to install these libraries use following commands on comamand prompt by firstly adding the path of python script 
```
python -m pip install requests
python -m pip install json
python -m pip install pickle

```
## How to run the project
First we have to get the server running ,so that it can listen different connection ffrom different clients. To run the server, open your command prompt and type the command
```
python server.py
```
If you have the required version and libraries, then it should be run properly and will show
```
Server is running and listening for connections.

```
Now for client side, run the client flie by typing
```
python client.py
```
If everything works fine, then fist step of establishing the connection will be done . And we can proceed to next step of filling out the survey on client side.
User will fill out the answer question asked on terminal . Also client side will also automatically detects the Location of the user. After filling out the survey, all the answer will be sent to Server side for calculation part.

After all the answer will be recieved on server side, next step of the process is Calculation of chances of having the Virus.
Server will segregate all the answer received and start calculating the chances.

##Algorithm for chances
This section needs alot of improvement for more accurate answers.
Well, We have created a pool for every answer , in pool there are different conditions based on the research. Whenever any of the condition will be satisfied for given answer, it will add points related to that condition to a global point variable .This will be done for every answer(age,travel-history,etc) and keeps updating the point variable.In the end,it will divides the point variable by 80( 80 because there are 8 parameter).
Calculated answer will get through another if-else conditon , that will finally generate the chances based on answer calculated.

Then after this ,chances will be transferred to client side and will be shown alongside with some precautions and prevention tips.
