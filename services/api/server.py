from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/data")
def get_data():
    return jsonify({
        "suhu": random.randint(20, 35)
    })

app.run(host="0.0.0.0", port=5000)