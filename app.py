from flask import Flask

app = Flask(__name__)

latest_signal = ""

@app.route('/signal', methods=['GET'])
def signal():
    return latest_signal

@app.route('/set/<sig>', methods=['GET'])
def set_signal(sig):
    global latest_signal
    if sig.lower() in ["buy", "sell"]:
        latest_signal = sig.lower()
        return f"Signal set to {latest_signal}"
    else:
        return "Invalid signal", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
