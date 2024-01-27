from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the seed value
seed_value = 0

@app.route('/', methods=['GET'])
def get_seed():
    return str(seed_value)

@app.route('/', methods=['POST'])
def update_seed():
    global seed_value
    data = request.get_json()
    seed_value = data.get('num', seed_value)  # Update if 'num' is in the JSON body, else keep existing
    return jsonify(success=True), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run on all interfaces on port 5000
