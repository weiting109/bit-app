from flask import Flask, render_template, request, redirect, url_for
import os
import requests     # for connection to Airtable API
import json         # for reading responses
import logging      # for logging messages
from bitapp import app

# importing environment variables 
AIRTABLE_KEY = os.getenv('AIRTABLE_KEY')
AIRTABLE_API_URL = os.getenv('AIRTABLE_API_URL')

# configure logger
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def index():
    """
    Route for landing page
    """
    return render_template('index.html')

@app.route('/api/subscribe/', methods=['POST'])
def subscribe():
    """
    API that retrieves submitted form data for a new subscriber
    """
    email = request.form['email']

    # formatting and sending request via Airtable API to create record
    headers = {
        'Authorization': 'Bearer {}'.format(AIRTABLE_KEY),
        'Content-Type': 'application/json',
    }
    data = { "records": [ { "fields": { "Email": email } } ] }
    res = requests.post(AIRTABLE_API_URL, headers=headers, data=json.dumps(data))

    # logging errors - log subscriber emails for manual input 
    if isinstance(res,requests.models.Response) is False: # no response received
        app.logger.error(f"Response not received with email:{email}")
    elif not res.ok:                                      # if errors received
        app.logger.error(f"Error for {email} with {res.json()['error']}")

    # redirect to landing page
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)