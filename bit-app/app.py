from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv # for API keys
import requests # for connection to Airtable API
import json

AIRTABLE_KEY = os.getenv('AIRTABLE_KEY')
print(AIRTABLE_KEY)

app = Flask(__name__)

@app.route('/')
def index():
    """
    Route for landing page
    """
    print("LOADING HERE")
    return render_template('index.html')

@app.route('/api/subscribe/', methods=['POST'])
def subscribe():
    """
    API that retrieves submitted form data for a new subscriber
    """
    email = request.form['email']

    headers = {
        'Authorization': 'Bearer {}'.format(AIRTABLE_KEY),
        'Content-Type': 'application/json',
    }
    data = { "records": [ { "fields": { "Email": email } } ] }

    r = requests.post('https://api.airtable.com/v0/app1Gt3CaYpphpsGV/Table%201', headers=headers, data=json.dumps(data))

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)