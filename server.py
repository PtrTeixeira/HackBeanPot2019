from flask import Flask, request, jsonify, send_from_directory
import json

app = Flask(__name__, static_url_path = "")

@app.route("/load", methods=['POST'])
def get_text():
    usernames = request.get_json()['usernames']
    image_count = request.get_json()['imageCount']

    print(usernames)
    return jsonify({ "generated_caption": "this is two people sitting in a tree" })

@app.route("/")
def serve_static():
    return send_from_directory('www', 'index.html')


