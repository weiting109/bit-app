## Project structure
The app is created with the Flask microframework, and HTML and CSS for styling with the help of Bootstrap.

## Instructions

To run the app:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ flask run
```

Environment variables:
In a `.env` file in the root directory of the project, include:
```
# API KEYS
AIRTABLE_KEY = YOUR_AIRTABLE_API_KEY_HERE
AIRTABLE_API_URL = YOUR_AIRTABLE_BASE&TABLE_API_URL_HERE
```