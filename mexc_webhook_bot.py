from flask import Flask, request, jsonify
import time
import hmac
import hashlib
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
BASE_URL = 'https://api.mexc.com'

def place_order(symbol, side, quantity=10.0, order_type='MARKET'):
    path = '/api/v3/order'
    timestamp = int(time.time() * 1000)

    params = {
        'symbol': symbol,
        'side': side.upper(),
        'type': order_type,
        'quantity': quantity,
        'timestamp': timestamp
    }

    query_string = '&'.join([f"{key}={params[key]}" for key in sorted(params)])
    signature = hmac.new(SECRET_KEY.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    headers = {
        'X-MEXC-APIKEY': API_KEY
    }

    params['signature'] = signature
    response = requests.post(BASE_URL + path, params=params, headers=headers)
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(f"تم الاستلام: {data}")

    try:
        action, symbol = data['message'].split(',')
        result = place_order(symbol.upper(), action.lower())
        return jsonify({'status': 'تم التنفيذ', 'response': result})
    except Exception as e:
        return jsonify({'status': 'خطأ', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
