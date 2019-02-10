from flask import Flask, request, jsonify, send_from_directory
import json

from start import get_media_list

app = Flask(__name__, static_url_path = "")

@app.route("/api/load", methods=['POST'])
def get_text():
    # These get ignored for the moment :c
    usernames = request.get_json()['usernames']
    image_count = request.get_json()['imageCount']


    result = []
    for item in get_media_list(usernames):
        for index, url in enumerate(item["urls"]):
            result.append({
                "caption": item["text"],
                "image": url,
                "video": item["is_video"][index]
            })

    return jsonify(result)

@app.route("/")
def server_index():
    return send_from_directory('www', 'index.html')

@app.route("/static/<path:filename>")
def serve_static(filename):
    print(filename)
    return send_from_directory('www', filename)
