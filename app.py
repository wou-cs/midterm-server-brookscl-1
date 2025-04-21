from flask import Flask, abort, request


app = Flask(__name__)


@app.route("/api/calcs/<number>", methods=["GET"])
def calculate(number):
    try:
        number = int(number)
    except ValueError:
        abort(400, description="The provided value must be an integer.")
    
    dec = number - 1
    hexadecimal = hex(number)
    return {'dec': dec, 'hex': hexadecimal}
