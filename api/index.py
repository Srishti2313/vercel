from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open("q-vercel-python.json") as f:
    data = json.load(f)

@app.route("/api")
def get_marks():
    names = request.args.getlist("name")
    lookup = {d["name"]: d["marks"] for d in data}
    result = [lookup.get(name, None) for name in names]
    return jsonify({"marks": result})
