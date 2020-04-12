#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import pickle 
import uuid 
  

TCP_IP = '127.0.0.1'
TCP_PORT = 1234
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("Server is Running And Listening for connection")
conn, addr = s.accept()
print ('Connection address:', addr)
f=open("Users_Data.txt","a+")
while 1:
    data = conn.recv(40960)
    ans_recv=pickle.loads(data)
    if not data: 
        break
        print("error")
    print ("Survey Answer Recieved:", ans_recv)  
    userid = uuid.uuid4() 
    id =str(userid)
    age=ans_recv[0]
    gender=ans_recv[1]
    temperature=ans_recv[2]
    symptoms=ans_recv[3]
    addsymptoms=ans_recv[4]
    travel=ans_recv[5]
    history=ans_recv[6]
    country=ans_recv[7]
    points=0
    tot_points=0;
    tot_points=tot_points+10;
    if(age<=20):
        points=points+3;
    elif(age<=50 and age>=21):
        points=points+5; 
    elif(age<=65 and age>=51):
        points=points+3;
    else:
        points=points+8;
    tot_points=tot_points+10;
    if(gender==1):
        points=points+9;
    else:
        points=points+8;
    tot_points=tot_points+10;
    if(temperature==1):
        points=points+4;   
    elif(temperature==2):
        points=points+7;
    elif(temperature==3):
        points=points+9;
    else:
        points=points+5;
    symp=len(symptoms)
    tot_points=tot_points+10;
    for i in range(symp):
        if(symptoms[i]==1):
            points=points+5;       
        elif(symptoms[i]==2):
            points=points+5;
        elif(symptoms[i]==3):
            points=points+8;
        elif(symptoms[i]==4):
            points=points+6;
        elif(symptoms[i]==5):
            points=points+6;      
        elif(symptoms[i]==6):
            points=points+4;
    addsymp=len(addsymptoms)
    tot_points=tot_points+10;
    for i in range(addsymp):
        if(addsymptoms[i]==1):
            points=points+2;       
        elif(addsymptoms[i]==2):
            points=points+2;
        elif(addsymptoms==3):
            points=points+3;
        elif(addsymptoms[i]==4):
            points=points+3;
        elif(addsymptoms[i]==5):
            points=points+3; 
        elif(addsymptoms[i]==6):
            points=points+3;
        elif(addsymptoms[i]==7):
            points=points+1;
    tot_points=tot_points+10;
    if(travel==1):
        points=points+4;   
    elif(travel==2):
        points=points+4; 
    elif(travel==3):
        points=points+7; 
    else:
        points=points+8;
    hist=len(history)
    tot_points=tot_points+10;
    for i in range(hist):
        if(history[i]==1):
            points=points+5;       
        elif(history[i]==2):
            points=points+5;
        elif(history[i]==3):
            points=points+6;
        elif(history[i]==4):
            points=points+6;
        elif(history[i]==5):
            points=points+6; 
        elif(history[i]==6):
            points=points+6;
        elif(history[i]==7):
            points=points+6;
        elif(history[i]==8):
            points=points+4;
    tot_points=tot_points+10;
    if(country=='IN'):
        points=points+5;
        # print('Your located Country: INDIA')
    elif(country=='IE'):
        points=points+6;
        #print('Your located Country: IRELAND')
    elif(country=='GB'):
        points=points+8; 
        #print('Your located Country: UNITED KINGDOM')
    elif(country=='US'):
        points=points+8;
            #print('Your located Country: UNITED STATES OF AMERICA')
    elif(country=='FR'):
        points=points+8;
            #print('Your located Country: FRANCE')
    elif(country=='IT'):
        points=points+10;
            #print('Your located Country: ITALY')
    elif(country=='CN'):
        points=points+10;
            #print('Your located Country: CHINA')
    else:
        points=points+6;
        print('SORRY!! WE ARE UNABLE TO LOCATE THE USER COUNTRY')

    calc=points/tot_points
    if(calc<=0.2):
        chance="LOW"
    elif(calc<=0.5 and calc>0.2):
        chance=("MEDIUM")
    elif(calc<=0.7 and calc>0.5):
        chance=("HIGH")
    else:
        chance=("VERY HIGH : YOU SHOULD SEE SOME DOCTOR")
    conn.send(chance.encode())
    conn.send(id.encode())
    print("Results are successfully send. ")
    L = ["User ID : ",id,"\tChances: ",chance,"\tLocation: ",country,"\n"]    
    f.writelines(L)  
   # print(f.read())
    f.close()
    chance_status=conn.recv(1024)
    chance_s=chance_status.decode("utf-8")
    print(chance_s,"\n\n")
    
conn.close()


# In[2]:





# In[1]:





# In[ ]:




