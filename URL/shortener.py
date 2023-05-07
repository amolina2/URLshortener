import requests
import json

urls={}

#Creates a txt file to store URLs

#check if txt file is NOT empty.
#If file is empty it creates a new dictionary
#if it's not it reads the info and adds it to urls(dictionary)
try:
    with open('dictionary.txt','r') as file:
        urls=json.load(file)
except FileNotFoundError: 
    urls={}


#user input 
long_url=input('Enter long link: ')
#converting long_url into a JSON string 
datap = json.dumps({'long_url': long_url})
#specifies data is JSON and sends HTTP post request
#             --> generates short URL & saves relation bw short and long URL
headersp = {'Content-type': 'application/json'}
response = requests.post("http://127.0.0.1:5000/short", data=datap, headers=headersp)

#Short URL JSON format --> python
short_url=response.json()['short_url']
#adds to dictionary
urls[short_url]=long_url

#adds new short URL to the dictionary/txt file
with open('dictionary.txt','w')as file:
    file.write(json.dumps(urls))

#prints short URL 
print(short_url)

