# coding: utf-8
from flask import Flask, request
import env_switcher
import logging

app = Flask(__name__)

@app.route("/")
def index():
    return "hello"

@app.route("/api/switch_env/")
def switch_env():

    env = request.values.get('env')
    platform = request.values.get('platform')
    return env_switcher.switch(env, platform)


if __name__ == '__main__':
    app.run("0.0.0.0")
