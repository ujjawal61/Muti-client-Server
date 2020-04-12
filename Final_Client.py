#!/usr/bin/env python
# coding: utf-8

# In[9]:


import socket
import os
import subprocess
import json

s = socket.socket()
host = '127.0.0.1'
port = 1234
final_ans=[]
s.connect((host, port))
print("Voila! You are connected to " + host  )
print('Please Enter your age: ')
age=int(input());
final_ans.append(age)
print("\n")

print('Please enter your Gender: 1.Male 2.Female');
gender=int(input());
final_ans.append(gender)
print("\n")

print('Please let us know your current body temperature in degree Fahrenheit (Normal body temperature is 98.6°F): \n1.Normal(96°F-98.6°F) 2.Fever(98.6°F-102°F) \n3.High Fever(>102°F) 4.Don’t know');
temperature=int(input());
final_ans.append(temperature)
print("\n")

print('Are you experiencing any of the symptoms(Enter all those applicable): \n1.Dry Cough  2.Loss or diminished sense of smell \n3.Sore Throat 4.Weakness  5.Change in Appetite \n6.None of these');
temp=int(input())
symptoms=()
temp_symp=list(symptoms)
temp_symp.append(temp)
while True:
    if(temp==6):
        print('You have selected NONE OF THESE ')
        break;
    else:    
        print('Do you want to select more:1.Yes 2.No')
        yn=int(input());
        if(yn==1):
            temp_symp.append(int(input('Next One:')))    
        else:
            break;
symptoms=tuple(temp_symp)
final_ans.append(symptoms)
print("\n")

print('Additionally, please verify if you are experiencing any of the symptoms below (Enter all those applicable): \n1.Moderate to Severe Cough 2.Feeling Breathless\n3.Difficulty in Breathing 4.Drowsiness\n5.Persistant Pain and Pressure in Chest 6.Severe Weakness\n7.None of these');
temp2=int(input())
addsymptoms=()
temp_addsymp=list(addsymptoms)
temp_addsymp.append(temp2)
while True:
    if(temp2 == 7):
        print('You have selected NONE OF THESE ')
        break;
    else:    
        print('Do you want to select more:1.Yes 2.No')
        yn=int(input());
        if(yn==1):
            temp_addsymp.append(int(input('Next One:')))    
        else:
            break;

addsymptoms=tuple(temp_addsymp)
final_ans.append(addsymptoms)
print("\n")

print('Please select your travel and exposure details(Enter all those applicable):\n1.No Travel History \n2.No contact with anyone with Symptoms\n3.History of travel or meeting in affected geographical area in last 14 days\n4.Close Contact with confirmed COVID in last 14 days');
travel=int(input());
final_ans.append(travel)
print("\n")

print('Do you have a history of any of these conditions (Enter all those applicable):\n1.Diabetes 2.High Blood Pressure\n3.Heart Disease 4.Kidney Disease\n5.Lung disease 6.Stroke \n7.Reduced Immunity 8.None of these');
temp3=int(input())
history=()
temp_hist=list(history)
temp_hist.append(temp3)
while True:
    if(temp3 == 8):
        print('You have selected NONE OF THESE ')
        break;
    else:    
        print('Do you want to select more:1.Yes 2.No')
        yn=int(input());
        if(yn==1):
            temp_hist.append(int(input('Next One:')))    
        else:
            break;
history=tuple(temp_hist)
final_ans.append(history)

import requests
import json
url = 'http://ipinfo.io/json'
data = requests.get(url).json()
country=data['country']
final_ans.append(country)


# In[ ]:


import pickle
data=pickle.dumps(final_ans)
s.send(data)
chances_recv = s.recv(1024)
id_recv=s.recv(1024)
id=id_recv.decode("utf-8")
print("\n")
chances = chances_recv.decode("utf-8")
print("---------------------------------------------------------------------------")
print("                          YOUR RESULT               ")
print("                   Your User ID :",id)
print("                       Respiratory Illness: ",chances)
print("-----------------------------------------------------------------------------")
print("\n")
s.send(str.encode("Chances Successfully Recieved"))


# In[1]:


preventions="""

                  TAKE SOME PREVENTIONS
Prevention and Precautions - Basic protective measures
Be aware or Educate yourself with the latest updates on the following websites : WHO & MoHFW

Most people who become infected experience mild illness and recover, but it can be more severe for others. Take care of your health and protect others by doing the following:

Wash your hands frequently
Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water.

Maintain social distancing
Maintain at least 2 metre (6 feet) distance between yourself and anyone who is coughing or sneezing.

Avoid touching eyes, nose and mouth
Our hands touch many surfaces and can pick up viruses. Once contaminated, hands can transfer the virus to your eyes, nose or mouth.

Practice respiratory hygiene
Make sure you and the people around you, follow good respiratory hygiene. This means covering your mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately.

If you have fever, cough and difficulty in breathing, seek medical care early
Stay home if you feel unwell. If you have a high fever, moderate to severe cough and difficulty in breathing and it is worsening in short period of time, seek medical asistance and call in advance.
"""
print(preventions)
print("\n-----------------Our Previous Users Statistics--------------------")
f=open("Users_Data.txt","r+")
print(f.read())
f.close()

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "700f3e17b4msh819a49f52fa61b8p166850jsn65f14fa2e45b"
    }

x = requests.request("GET", url, headers=headers).json()
print("---------------------------------------------------------------------")
print("      Currently Top 4 Countries in Number of Cases for COVID 19") 
print("Country   Cases          Deaths    \tCases per Million")
for i in range(4):
    country=x['countries_stat'][i]['country_name']
    cases=x['countries_stat'][i]['cases']
    deaths=x['countries_stat'][i]['deaths']
    casesperm=x['countries_stat'][i]['total_cases_per_1m_population']
    print(country,"\t",cases,"\t",deaths,"\t",casesperm)




