from flask import Flask, jsonify, send_file
from datetime import datetime
import pytz
import os

app = Flask(__name__)


@app.route("/")
def get_time():
    jst = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"jst": jst})

@app.route("/soul")
def get_soul():
    return send_file("core/chappie_core.md", mimetype="text/markdown")

@app.route("/memory")
def get_memory():
    return send_file("memory/chatgpt.md", mimetype="text/markdown")

@app.route("/log")
def get_log():
    return send_file("log/log.txt", mimetype="text/plain")

@app.route("/flag")
def get_flag():
    return send_file("flags/rotate.flag", mimetype="text/plain")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
