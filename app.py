from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MOCK_DATA = [
    {"name": "IKEA Sofa", "price": 15000},
    {"name": "Amazon Lights", "price": 2000},
    {"name": "Zomato Cake", "price": 1200}
]

@app.route('/')
def home():
    return "PocketSmart AI Running!"

@app.route('/generate-home', methods=['POST'])
def home_p():
    return jsonify({"message": "Home plan ready", "products": MOCK_DATA})

@app.route('/generate-party', methods=['POST'])
def party_p():
    return jsonify({"message": "Party plan ready", "products": MOCK_DATA})

@app.route('/generate-jewelry', methods=['POST'])
def jew_p():
    return jsonify({"message": "Jewelry ready", "products": MOCK_DATA})

if __name__ == '__main__':
    app.run()
