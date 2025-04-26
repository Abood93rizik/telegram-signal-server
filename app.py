from flask import Flask, request, jsonify

app = Flask(__name__)

last_signal = None  # تخزين آخر إشارة هنا

@app.route('/', methods=['GET'])
def home():
    return jsonify({'last_signal': last_signal})

@app.route('/update_signal', methods=['POST'])
def update_signal():
    global last_signal
    data = request.get_json()
    signal = data.get('signal')
    if signal:
        last_signal = signal
        return jsonify({'message': 'Signal updated successfully'}), 200
    else:
        return jsonify({'error': 'No signal provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
