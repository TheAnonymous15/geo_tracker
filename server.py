from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global variable to store the client's location
client_location = {'latitude': None, 'longitude': None}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_location', methods=['POST'])
def update_location():
    global client_location
    data = request.json
    client_location['latitude'] = data['latitude']
    client_location['longitude'] = data['longitude']
    return jsonify(success=True)

@app.route('/get_location', methods=['GET'])
def get_location():
    return jsonify(client_location)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
