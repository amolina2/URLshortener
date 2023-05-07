from flask import Flask, request, redirect
import string
import random
import json


#creates app
app = Flask(__name__)
urls = {}

#generates short URL code 
def generate_short_code():
    options = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(options) for _ in range(6))

#Response to HTTP POST request (long url --> code for short URL)
@app.route('/short', methods=['POST'])
def shorten_url():
    req_data = request.get_json() #long_URL data || JSON-->python
    long_url = req_data['long_url']
    code = generate_short_code() #calls previous function to generate unique code
    short_url = 'http://127.0.0.1:5000/' + code #generates short URL 
                                                    #by adding IP address and code 
    urls[code] = long_url #adds key to dictionary
    return json.dumps({'short_url': short_url}) #short URL || python-->JSON

#Response to HTTP GET request
#From short URL to orignal URL (when using in browser)
@app.route('/<short_code>')
def redirect_url(short_code):
    if short_code in urls: 
        return redirect(urls[short_code]) #from short URL to long URL 
    else:
        return f"Short URL '{short_code}' not found"

        

#Starts flask
if __name__ == '__main__':
    app.run(debug=True)
