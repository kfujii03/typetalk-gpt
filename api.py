from flask import Flask, render_template, request
import requests
import settings as env

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/webhook', methods=['POST'])
def webhook():
    msg = 'こんにちは'
    url = 'https://typetalk.com/api/v1/topics/' + env.TYPETALK_TOPIC_ID
    data = { 
        'message' : msg,
        'replyTo' : request.form.get('id')
    }
    headers = { 'X-TYPETALK-TOKEN': env.TYPETALK_TOKEN }
    requests.post(url, json = data, headers = headers)
