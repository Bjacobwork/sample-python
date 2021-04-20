from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    # Use this data in your application logic
    print(request.form['MessageSid'])
    print(request.form['SmsSid'])
    print(request.form['AccountSid'])
    print(request.form['MessagingServiceSid'])
    print(request.form['From'])
    print(request.form['To'])
    print(request.form['Body'])
    print(request.form['NumMedia'])
    

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("Did this work?")

    return str(resp)

app.run(debug=True, port=80, host=os.environ["DB_HOST"])
