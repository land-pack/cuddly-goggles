from flask import Flask
from flask import send_from_directory
from flask import render_template
from flask import url_for
from flask import request
from flask import jsonify
# from core import *

app = Flask(__name__, static_url_path="/static_file")

@app.context_processor
def inject_stage_and_region():
    return dict(email_addr="abc@gmail.com", region="NA",
    phone="123-123")



@app.route("/")
def index():
    return render_template("index.html")


@app.route('/<path:path>')
def static_file(path):
    return send_from_directory('static_file', path)



if __name__ == '__main__':
    app.run(debug=True, port=23333)
