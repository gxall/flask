from flask import Flask, jsonify
import os

app = Flask(__name__)

def nf_crypto_payment(amount, telegram_user_id):
    data = {"id": "", "price": amount, "currency": "USD", "store_id": "RUZcUraKvqVNWdKCMGreKFrWraLNIbtI", "products": "", "expiration": "", "promocode": "",
            "notification_url": "https://gcbot-production.up.railway.app/nfwcp", "redirect_url": "", "buyer_email": "",
            "order_id": "", "discount": "", "status": "", "tx_hashes": "", "exception_status": "",
            "shipping_address": "", "notes": "", "created": "", "payments": "", "metadata": {
            "tg_id": telegram_user_id
        }, "action": ""}

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',

    }
    url = "http://45.153.240.217/api/invoices"
    response = requests.post(url, headers=headers, data=json.dumps(data))
    r = response
    print("curl -X GET '" + url + "' -v -H 'User-Agent: " + r.request.headers['User-Agent'] + "' -H 'Accept: " +
          r.request.headers['Accept'] + "' -H 'Accept-Encoding: " + r.request.headers[
              'Accept-Encoding'] + "' -H 'Connection: " + r.request.headers['Connection'] + "' -H 'Cache-Control: " +
          r.request.headers['Cache-Control'] + "'")

    return {
        "price_amount": amount,
        "invoice_url": f"http://c8bc-37-19-221-160.ngrok.io/invoice/{response.json()['id']}",
        "payments": response.json()['payments']
    }


@app.route('/')
def index():
    return nf_crypto_payment(200, "2121)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
