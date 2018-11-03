# funky

🎷 simple call &amp; response python to google cloud function

## Table of Contents
- [Cloud Function](#cloud-function)
- [App Engine](#app-engine)

# Cloud Function

## example

🔥 test out the live deployment of the REST gcloud cloud function!

- go to [https://us-central1-funky-221323.cloudfunctions.net/chicken-or-pasta](https://us-central1-funky-221323.cloudfunctions.net/chicken-or-pasta) to get a response via web browser

> put in a custom param to see a custom result based on the endpoint tree (such as [🍗](https://us-central1-funky-221323.cloudfunctions.net/chicken-or-pasta?message=%F0%9F%8D%97))


## usage

- [edit or create a new cloud function](https://console.cloud.google.com/functions) using Python 3.7 using this template:
```python
# -*- coding: utf8 -*-
def funkyTime(request):
	"""Responds to any HTTP request.
	Args:
	request (flask.Request): HTTP request object.
	Returns:
	The response text or any set of values that can be turned into a
	Response object using
	`make_response <http://flask.pocoo.org/docs/0.12/api/#flask.Flask.make_response>`.
	"""
	request_json = request.get_json()
	message = None
	if request.args and 'message' in request.args:
		message = request.args.get('message')
	elif request_json and 'message' in request_json:
		message = request_json['message']

	if message == u'🍗':
		return "🍝"
	elif message == u'🍝':
		return "🍗"
	else:
		return "👎"
```

- your google cloud platform console should look like this once completed:

![](docs/cloudie.jpg)

# App Engine

# example

🔥 test out the live deployment of the gcloud flask python app!

- run `python funky.py <PARAM>` to get a response via python
- go to [https://funky.host/](https://funky.host/) to get a response via web browser

> put in a custom param to see a custom result based on the endpoint tree (such as [🍗](https://funky.host/🍗))

# usage

- modify `main.py` to change flask endpoints
- locally run `gunicorn -k eventlet -w 1 --bind 0.0.0.0:$(PORT) wsgi` to test the flask/socket server
- run `gcloud app deploy` to sync your changes with the google app engine you've set up
- check [app engine dashboard](https://console.cloud.google.com/appengine) to see how the project is faring

# setup

1. setup local [Google Cloud Platform Python Development Environment](https://cloud.google.com/python/setup)
- `sudo apt install python python-dev python3 python3-dev`
- `wget https://bootstrap.pypa.io/get-pip.py`
- `sudo python get-pip.py`
- `pip install --upgrade virtualenv`
- `virtualenv --python python3 env`
-  `pip install google-cloud-storage`

2. create new app engine using a [Python App Engine Standard Environment](https://cloud.google.com/appengine/docs/standard/python/quickstart)
- new app engine
- python standard environment

3. download the [Google Cloud SDK](https://cloud.google.com/sdk/?hl=en_US) and setup the `gcloud` command
- `wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-223.0.0-linux-x86_64.tar.gz`
- `tar zxvf google-cloud-sdk-223.0.0-linux-x86_64.tar.gz ~/google-cloud-sdk`
- `cd ~ && ./google-cloud-sdk/install.sh`

4. initialize using `gcloud init`
- requires logging into google account and setting up `PATH`

5. deploy using `gcloud app deploy`

6. enable websocket use by running the following command:
```
gcloud compute firewall-rules create default-allow-websockets --allow tcp:65080 --target-tags websocket --description "allow websocket traffic on port 65080"
```

> using websockets requires a configured billing account linked to your app engine project. using the basic flask endpoints, however, does not.

# authors

julian weiss (insanj). (c) 2018. reach out on [github](https://github.com/insanj)!

# license

funky is licensed under gpl-3.0. [see license file](LICENSE).
