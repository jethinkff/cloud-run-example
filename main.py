# import os
# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return jsonify({"message": "Welcome to the Flask API!"})

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     data = {
#         "name": "John Doe",
#         "age": 30,
#         "occupation": "Software Engineer"
#     }
#     return jsonify(data)

# @app.route('/api/data', methods=['POST'])
# def post_data():
#     new_data = request.json
#     return jsonify({"message": "Data received", "data": new_data}), 201

# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 8080))  # Use PORT from environment or default to 8080
#     app.run(host='0.0.0.0', port=port)


import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))