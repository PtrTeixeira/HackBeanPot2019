from flask import Flask, request, jsonify, send_from_directory
import json

app = Flask(__name__, static_url_path = "")

@app.route("/api/load", methods=['POST'])
def get_text():
    # These get ignored for the moment :c
    usernames = request.get_json()['usernames']
    image_count = request.get_json()['imageCount']

    return jsonify([
        {
            "caption": "this is the caption\nBonusCaption",
            "image": "http://flask.pocoo.org/docs/1.0/_static/flask.png",
            "video": False
        },
        {
            "caption": "this is the caption\nBonusCaption",
            "image": "http://flask.pocoo.org/docs/1.0/_static/flask.png",
            "video": False
        },
        {
            "caption": "this is the caption\nBonusCaption",
            "image": "http://flask.pocoo.org/docs/1.0/_static/flask.png",
            "video": False
        }
    ])

@app.route("/")
def server_index():
    return send_from_directory('www', 'index.html')

@app.route("/static/<path:filename>")
def serve_static(filename):
    print(filename)
    return send_from_directory('www', filename)
