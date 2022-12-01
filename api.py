from flask import Flask, request, redirect, url_for, render_template

from api_files.api_html_page import app as html_page
from api_files.api_json_page import app as json_page

# Init app

app = Flask(__name__)

app.register_blueprint(json_page)
app.register_blueprint(html_page)

http_error = {400: "Bad Request",
              401: "Unauthorized",
              403: "Forbidden",
              404: "Not Found",
              405: "Method Not Allowed",
              429: "Too Many Requests",
              500: "Internal Server Error",
              501: "Not Implemented",
              502: "Bad Gateway",
              503: "Service Unavailable",
              504: "Gateway Timed Out"}


def errorString(e):
    err = "Error " + e + ": " + http_error[e]
    return err


# Flask maps HTTP requests to Python functions.
@app.errorhandler(400)
def bad_request(e):
    return render_template("errorTemplate.html", error=errorString(400)), 400


@app.errorhandler(401)
def unauthorized(e):
    return render_template("errorTemplate.html", error=errorString(401)), 401


@app.errorhandler(403)
def forbidden(e):
    return render_template("errorTemplate.html", error=errorString(403)), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errorTemplate.html", error=errorString(404)), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template("errorTemplate.html", error=errorString(405)), 405


@app.errorhandler(429)
def too_many_requests(e):
    return render_template("errorTemplate.html", error=errorString(429)), 429


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("errorTemplate.html", error=errorString(500)), 500


@app.errorhandler(501)
def not_implemented(e):
    return render_template("errorTemplate.html", error=errorString(501)), 501


@app.errorhandler(502)
def bad_gateway(e):
    return render_template("errorTemplate.html", error=errorString(502)), 502


@app.errorhandler(503)
def service_unavailable(e):
    return render_template("errorTemplate.html", error=errorString(503)), 503


@app.errorhandler(504)
def gateway_timed_out(e):
    return render_template("errorTemplate.html", error=errorString(504)), 504


# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
