from flask import Flask, request, jsonify, redirect
from storage import store, generate_short_code, get_url_data
from utils import is_valid_url
from datetime import datetime

app = Flask(__name__)

@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")

    if not original_url or not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()
    store[short_code] = {
        "url": original_url,
        "clicks": 0,
        "created_at": datetime.utcnow().isoformat()
    }

    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 200

@app.route("/<short_code>", methods=["GET"])
def redirect_to_url(short_code):
    data = get_url_data(short_code)
    if not data:
        return jsonify({"error": "Short code not found"}), 404

    data["clicks"] += 1
    return redirect(data["url"])

@app.route("/api/stats/<short_code>", methods=["GET"])
def stats(short_code):
    data = get_url_data(short_code)
    if not data:
        return jsonify({"error": "Short code not found"}), 404

    return jsonify({
        "url": data["url"],
        "clicks": data["clicks"],
        "created_at": data["created_at"]
    }), 200
