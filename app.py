from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
last_signal = None

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Latest Signal</title>
    <meta http-equiv="refresh" content="3"> <!-- يحدث الصفحة تلقائياً كل 3 ثواني -->
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding-top: 50px; }
        h1 { font-size: 2em; }
    </style>
</head>
<body>
    <h1>📢 Latest Signal:</h1>
    <h2>{{ signal }}</h2>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HTML_TEMPLATE, signal=last_signal if last_signal else "No signal yet")

@app.route('/update', methods=['POST'])
def update_signal():
    global last_signal
    data = request.get_json()
    if data and 'signal' in data:
        last_signal = data['signal']
        return jsonify({"message": "Signal updated successfully"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
