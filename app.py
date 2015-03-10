import bottle
import os


@bottle.get("/FtoC/<farenheight>")
def FtoC(farenheight):
    # make sure the farenheight is a valid number
    try:
        farenheight = float(farenheight)
    except:
        # we have an error--return an error message
        return "'" + farenheight + "' is not a valid temperature"

    # convert the temperature to celsius
    celsius = (farenheight - 32.0) * 5.0 / 9.0

    # return the result statement
    return str(farenheight) + "&deg; F = " + str(celsius) + "&deg; C"


################################################################################


# utility routes/functions to run the web server
@bottle.route("/")
def index():
    return bottle.static_file("index.html", os.path.dirname(__file__))
@bottle.route("/js/app.js")
def js():
    return bottle.static_file("app.js", os.path.dirname(__file__))
@bottle.route("/css/app.css")
def css():
    return bottle.static_file("app.css", os.path.dirname(__file__))
bottle.run(host="localhost", port=8080)
