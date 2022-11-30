
from flask import Flask, render_template

from api_files.api_html_page import app as html_page
from api_files.api_json_page import app as json_page
from api_files.api_config_page import app as config_page
from oop.car import Car

# Init app

app = Flask(__name__)

app.register_blueprint(json_page)
app.register_blueprint(html_page)
app.register_blueprint(config_page)


# Flask maps HTTP requests to Python functions.
@app.route('/', methods=['GET'])
def home():
    return "<h1>Used Cars Database System</h1><p>Vehicle Data Query</p>"


# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
