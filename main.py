from flask import Flask,redirect,url_for,render_template,request
import config
from application import app

if __name__ == '__main__':
    app.run(host=config.HOST ,port=config.PORT,debug=True)