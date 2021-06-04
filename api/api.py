import flask
from flask import request, jsonify
from os import listdir
from os.path import isfile, join
from datetime import datetime
import os

log_folder = os.path.join(os.path.dirname(__file__), "logs")

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def latest_log_file():
  files = [f for f in listdir(log_folder) if isfile(join(log_folder, f))]
  return join(log_folder, sorted(files)[-1])

@app.route('/', methods=['GET'])
def home():
    log_file = latest_log_file()
    html = "<h1>Wake requests:</h1>\n"
    with open(log_file) as f:
        for line in f:
            html+=f"<h2>{line}</h2>\n"
    return html


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/tasks/turn_on_pc/', methods=['POST'])
def api_all():
    os.system("sudo etherwake -i eth0 00:D8:61:C4:51:6A")
    log_file = latest_log_file()
    with open(log_file, 'w') as f:
        f.write(f"Wake request submitted at {datetime.now()}\n")
    return jsonify(success=True)

app.run(debug=True, port=80, host='0.0.0.0')