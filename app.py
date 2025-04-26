from flask import Flask, request

app = Flask(__name__)

# متغير عالمي لحفظ آخر إشارة وصلت
last_signal = None

@app.route('/')
def home():
    return "Telegram Signal Server is Running ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    global last_signal
    data = request.get_json()

    if not data or 'signal' not in data:
        return {"message": "Invalid payload"}, 400

    signal = data['signal']
    last_signal = signal  # تحديث الإشارة دائماً
    print(f"Received Signal: {signal}")

    return {"message": "Signal received successfully"}, 200

@app.route('/last-signal', methods=['GET'])
def get_last_signal():
    if last_signal:
        return {"last_signal": last_signal}, 200
    else:
        return {"last_signal": None}, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
