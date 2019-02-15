from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__)

VERIFY_URL_PROD = 'https://ipnpb.paypal.com/cgi-bin/webscr'
VERIFY_URL_TEST = 'https://ipnpb.sandbox.paypal.com/cgi-bin/webscr'
VERIFY_URL = VERIFY_URL_TEST


def get_current_user_id():
    return '77777'


@app.route("/")
def buy_page():
    return render_template('index.html', user_id=get_current_user_id())


@app.route("/paypal_ipn", methods=['POST', 'GET'])
def paypal_ipn_listener():
    print("IPN event received.")

    # Sending message as-is with the notify-validate request
    params = request.form.to_dict()
    params['cmd'] = '_notify-validate'
    headers = {'content-type': 'application/x-www-form-urlencoded',
               'user-agent': 'Paypal-devdungeon-tester'}
    response = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)
    response.raise_for_status()

    # See if PayPal confirms the validity of the IPN received
    if response.text == 'VERIFIED':
        print("Verified IPN response received.")
        try:
            user_id_of_buyer = params['custom'].split(":")[1]
            print("User who bought item: " + str(user_id_of_buyer))

            # Take action, e.g. update database to give user 1000 tokens

        except Exception as e:
            print(e)

    elif response.text == 'INVALID':
        # Don't trust
        print("Invalid IPN response.")
    else:
        print("Some other response.")
        print(response.text)
    return ""


@app.route("/paypal_cancel")
def paypal_cancel():
    return "PayPal cancel"


@app.route("/paypal_success")
def paypal_success():
    return "Paypal success"






















