from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

app.secret_key =" config.SECRET_KEY"

from .route import *