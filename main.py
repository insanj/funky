#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template
import socketio, eventlet, eventlet.wsgi

# Flask setup
app = Flask(__name__)

# Socket setup
sio = socketio.Server(async_mode='eventlet')
app.wsgi_app = socketio.Middleware(sio, app.wsgi_app)
people = []

# Flask endpoints
@app.route('/')
def home():
	return render_template("funky.html")

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

# Socket endpoints
@sio.on('connect')
def connect(sid, data):
	global people
	if sid not in people:
		people.append(sid)
		sio.enter_room(sid, "room")
		sio.emit("text_response", {"text" : str(sid) + " connected", "flag" : True}, room="room")

@sio.on('disconnect')
def disconnect(sid):
	global people
	if sid in people:
		people.remove(sid)

@sio.on("prompt_input")
def prompt_input(sid, data):
	sio.emit("text_response", {"text" : str(sid) + ":" + data["text"], "flag" : False}, room="room")
