from flask import Flask, request
import requests
import base64

app = Flask(__name__)

@app.route('/maxicode', methods=['POST'])
def maxicode():
    if request.is_json:
        data = request.get_json()
        imgdata = create_maxicode(data)
        return imgdata
    else:
        return jsonify({'error': 'Invalid request'}), 400

def encode_data(data):
    data = data['maxicode']
    data = data.replace("\\x1e", "%5Cx1e")
    data = data.replace("\\F", "%5CF")
    data = data.replace("\\F0", "%5CF0")
    data = data.replace("\\F1", "%5CF1")
    data = data.replace("\\F4", "%5CF4")
    data = data.replace("\\FN", "%5CFN")
    data = data.replace("\\FB", "%5CFB")
    data = data.replace("+", "%2B")
    data = data.replace(" ", "+")
    return "data=" + data + "&code=MaxiCode&translate-esc=true&dpi=600&imagetype=Png&base64=true"


def create_maxicode(data):
    url = "https://barcode.tec-it.com/barcode.ashx"

    data = encode_data(data=data)

    headers = {
        'authority': 'barcode.tec-it.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '__RequestVerificationToken=EpNxhZXq7xYAYIzWh1144QIYmJwYp7sQhsVMEqQqz1C3612Uh6TljNinr-cxY2PmEkuDzwjykiCb2QAqBSlLeLGig1yTRwKf8MbYhYcF8781',
        'origin': 'https://barcode.tec-it.com',
        'pragma': 'no-cache',
        'referer': 'https://barcode.tec-it.com/en/MaxiCode?data=This%20is%20a%20MaxiCode%20by%20TEC-IT',
        'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="112", "Google Chrome";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 11.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5529.219 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.post(url, headers=headers, data=data)

    return response.text

if __name__ == '__main__':
    app.run()
