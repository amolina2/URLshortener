import json

#opens txt file with dictionary info
with open('dictionary.txt','r') as file:
    urls=json.loads(file.read())

#user input 
input_short_url = input('Enter short link: ')

#if statment to give backt the URL if there's a match 
if input_short_url in urls:
    long_url = urls[input_short_url]
    print(long_url)
else:
    print("URL not found")
