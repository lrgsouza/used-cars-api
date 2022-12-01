
from flask import Flask, request, redirect, url_for, render_template

from api_files.api_html_page import app as html_page
from api_files.api_json_page import app as json_page

# Init app

app = Flask(__name__)

app.register_blueprint(json_page)
app.register_blueprint(html_page)


# Flask maps HTTP requests to Python functions.
@app.errorhandler(404)
def page_not_found(e):
    return render_template("errorTemplate.html", error="Error 404: Not Found"), 404


@app.errorhandler(405)
def page_not_found(e):
    return render_template("errorTemplate.html", error="Error 405: Method Not Allowed"), 404


@app.errorhandler(400)
def page_not_found(e):
    return render_template("errorTemplate.html", error="Error 400: Bad Request"), 400


@app.errorhandler(500)
def page_not_found(e):
    return render_template("errorTemplate.html", error="Error 500: Internal Server Error"), 500


# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
