from flask import Flask, render_template, request, redirect, url_for
import os
import requests # for connection to Airtable API
import json

AIRTABLE_KEY = os.getenv('AIRTABLE_KEY')
AIRTABLE_API_URL = os.getenv('AIRTABLE_API_URL')

app = Flask(__name__)

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

    headers = {
        'Authorization': 'Bearer {}'.format(AIRTABLE_KEY),
        'Content-Type': 'application/json',
    }
    data = { "records": [ { "fields": { "Email": email } } ] }

    r = requests.post(AIRTABLE_API_URL, headers=headers, data=json.dumps(data))

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)