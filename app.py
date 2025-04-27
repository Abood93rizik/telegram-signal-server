from flask import Flask, request, jsonify

app = Flask(__name__)

# تخزين آخر إشارة تم استقبالها
last_signal = None

@app.route('/', methods=['GET'])
def home():
    return f"<h1>Latest Signal:</h1><h2>{last_signal if last_signal else 'No signal yet.'}</h2>"

@app.route('/update', methods=['POST'])
def update_signal():
    global last_signal
    data = request.get_json()
    if not data or 'signal' not in data:
        return jsonify({"error": "Missing 'signal' in request"}), 400
    last_signal = data['signal']
    return jsonify({"message": "Signal updated successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
