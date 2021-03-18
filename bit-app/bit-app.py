from flask import Flask, render_template, request

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
    print(email)
    return email