#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template
import socketio, eventlet, eventlet.wsgi

# Flask setup
app = Flask(__name__)

# Socket setup
sio = socketio.Server(async_mode='eventlet')
app.wsgi_app = socketio.Middleware(sio, app.wsgi_app)

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
	sio.enter_room(sid, "room")
	sio.emit("text_response", {"text" : str(sid) + " connected", "flag" : True}, room="room")

@sio.on('disconnect')
def disconnect(sid):
	print str(sid) + " disconnected"
	#sio.emit("text_response", {"text" : str(sid) + " disconnected", "flag" : True}, room="room")
	#sio.leave_room(sid, "room")

@sio.on("prompt_input")
def prompt_input(sid, data):
	sio.emit("text_response", {"text" : str(sid) + ":" + data["text"], "flag" : False}, room="room")