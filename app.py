from flask import Flask
from waitress import serve
import os
import logging
import random

app = Flask(__name__)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

@app.route("/")
def hello():
  randomnum = random.randint(1, 100000)/100
  return "Your Random Number is " + str(randomnum) + "!\n"

@app.route("/listfiles")
def listfiles():
  return "Listing of files is not available right now!\n"


@app.route("/version")
def version():
  return "GCPClassroom Demo 1.1\n"

if __name__ == "__main__":
  serve(app,host="0.0.0.0",port=int(os.environ.get("PORT", 8080)))
