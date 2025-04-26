from flask import Flask, request, jsonify

app = Flask(__name__)

# خزّن آخر إشارة في متغير جلوبال
last_signal_data = {"last_signal": None}

@app.route("/", methods=["GET"])
def home():
    return jsonify(last_signal_data)

@app.route("/update_signal", methods=["POST"])
def update_signal():
    data = request.get_json()
    if data and "signal" in data:
        last_signal_data["last_signal"] = data["signal"]
        return jsonify({"message": "Signal updated successfully"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
