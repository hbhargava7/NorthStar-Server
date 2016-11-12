from flask import Flask, render_template, jsonify, request
from model import connect_to_db


app = Flask(__name__)

@app.route('/')
def hello(): 
	return "hello world"

