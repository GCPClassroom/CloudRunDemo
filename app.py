from flask import Flask
from waitress import serve
import os
import logging
import random
from google.cloud import storage

app = Flask(__name__)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

@app.route("/")
def hello():
  randomnum = random.randint(1, 500000)/100
  return "Your Random Number between 1.00 and 5000.00 is " + str(randomnum) + "!\n"

@app.route("/listfiles")
def listfiles():
    bucket_name = "gc-demo-env-bucket"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs()

    file_list = "Files in bucket: " + bucket_name + "<br/>"
    for blob in blobs:
        file_list = file_list + blob.name + "<br/>"
    return file_list

@app.route("/version")
def version():
  return "GCPClassroom Demo 1.2\n"

if __name__ == "__main__":
  serve(app,host="0.0.0.0",port=int(os.environ.get("PORT", 8080)))
