from flask import Flask, Response, request
app = Flask(__name__)
import os
import socket


@app.route("/")
def hello():
  return "hello"

if __name__ == "__main__":
    try:
        port = int(os.getenv("PORT"))
    except TypeError:
        port = None
    app.run(debug=True, port=port)
