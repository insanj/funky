#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Try using 🍗 or 🍝!"

@app.route('/<thing>')
def funkyTime(thing):
	if thing == u'🍗':
		return "🍝"
	elif thing == u'🍝':
		return "🍗"
	else:
		return "👎"

@app.errorhandler(500)
def error(e):
	return 500