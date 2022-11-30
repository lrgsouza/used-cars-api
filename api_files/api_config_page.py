from flask import render_template, Blueprint

from oop.car import Car

app = Blueprint('config_page', __name__)


# Flask maps HTTP requests to Python functions.
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error="Error 404: Not Found"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("error.html", error="Error 500: Internal Server Error"), 500


@app.route('/help', methods=['GET'])
def help():
    return "<h1>Used Cars Database System</h1>" \
           "<p>Try use <b>/api/help</b> for getting api help</p>" \
           "<p>Try use <b>/filter</b> for filtering</p>" \
           "<p>Try use <b>/home</b> for go to start</p>"
