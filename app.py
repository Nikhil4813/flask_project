from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/api/greet', methods=['GET'])
def greet_user():
    # Get the 'name' query parameter from the request
    name = request.args.get('name', 'Guest')
    
    # Create a response dictionary
    response = {
        'message': f'Hello, {name}!'
    }
    
    # Return the response as a JSON object
    return jsonify(response)

@app.route('/api/farewell', methods=['POST'])
def farewell_user():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify({'message': f'Goodbye, {name}!'})

@app.route('/api/square/<int:number>', methods=['GET'])
def square_number(number):
    return jsonify({'number': number, 'square': number ** 2})

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Resource not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
