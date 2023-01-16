from flask import Flask, render_template, request
from pathlib import Path
from os import listdir
from werkzeug.utils import secure_filename
import boto3
import json

# --- old code for pushing submitted text to an S3 ---

# AWS_ACCESS_KEY_ID = ''
# AWS_SECRET_ACCESS_KEY = ''
# BUCKET_NAME='txt-to-polly'
# s3 = boto3.resource('s3')

# textFile = "polly.txt"

#--- old code for pushing submitted text to an S3 ---

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
        if request.method == 'POST':
            url = "https://ka1g5hkp7h.execute-api.eu-west-1.amazonaws.com/default/polly-demo?voice=Joanna"
            input_polly = request.form['text_box']
            url += "&text=" + input_polly

            print(input_polly)

            return render_template('home.html', variable=url)
        else:
            return render_template('home.html')

        #--- old code for pushing submitted text to an S3 ---

        # with open('polly.txt', 'w') as f:
        #     f.write(str(input_polly))

        # print ("Uploading {textFile} to Amazon S3 bucket {BUCKET_NAME}")
        # s3.Bucket(BUCKET_NAME).upload_file("polly.txt", "texts/polly")

        #--- old code for pushing submitted text to an S3 ---

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
