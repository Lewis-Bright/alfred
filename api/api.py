import flask
from flask import request, jsonify
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Alfred</h1>"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/tasks/turn_on_pc/', methods=['POST'])
def api_all():
    os.system("sudo etherwake -i eth0 00:D8:61:C4:51:6A")
    return jsonify(success=True)

app.run(debug=True, port=80, host='0.0.0.0')