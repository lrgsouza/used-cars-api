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


def errorStr(e):
    err = "Error " + str(e) + ": " + http_error[e]
    return err


def regexStr(text):
    r = '.*' + text + '.*'
    return {'$regex': r, '$options': 'i'}
