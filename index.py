from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('q-vercel-python.json', 'r') as f:
    marks_data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [marks_data.get(name, None) for name in names]
    return jsonify({"marks": marks})

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    return response
