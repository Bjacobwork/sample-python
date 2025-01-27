from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os
import time

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    # Use this data in your application logic
    for key in request.form.keys():
        print(key)
        time.sleep(1)
        print(request.form[key])
        print("")
    for key in request.values.keys():
        print(key)
        time.sleep(1)
        print(request.values[key])
        print("")
     

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("Did this work?")

    return str(resp)

app.run(debug=True, port=80, host=os.environ["DB_HOST"])
