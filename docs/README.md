# [🎷 funky](https://github.com/insanj/funky)

---

simple call &amp; response python to google cloud function

![](funky.gif)


# 🔥 try it out!

---


test the live deployment of the gcloud flask python app 🖇

1. run `python funky.py <PARAM>` [to get a response via python](https://github.com/insanj/funky/archive/master.zip)
2. go to [https://funky-221323.appspot.com/](https://funky-221323.appspot.com/) to get a response via web browser

> try putting in a custom param to see a custom result based on the endpoint tree (such as [🍗](https://funky-221323.appspot.com/🍗))!

# 🚙 usage

---

- modify `main.py` to change flask endpoints

```python
from flask import Flask
app = Flask(__name__)

@app.route('/<thing>')
def mirrorThing(thing):
	return thing
```

- run `gcloud app deploy` to sync your changes with the google app engine you've set up

```
$ gcloud app deploy
Services to deploy:

descriptor:      [/funky/app.yaml]
source:          [/funky]
target project:  [funky-221323]
target service:  [default]
target version:  [20181102t210815]
target url:      [https://funky-221323.appspot.com]


Do you want to continue (Y/n)?  Y

Beginning deployment of service [default]...
╔════════════════════════════════════════════════════════════╗
╠═ Uploading 15 files to Google Cloud Storage               ═╣
╚════════════════════════════════════════════════════════════╝
File upload done.
Updating service [default]...done.
Setting traffic split for service [default]...done.
Deployed service [default] to [https://funky-221323.appspot.com]

You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

To view your application in the web browser run:
  $ gcloud app browse
```

- check [app engine dashboard](https://console.cloud.google.com/appengine) to see how the project is faring

![](screenie.jpg)

# 🥡 setup

---

1. (mostly optional) setup local [Google Cloud Platform Python Development Environment](https://cloud.google.com/python/setup)
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

# 🎨 authors

---

julian weiss (insanj), (c) 2018. reach out on [github](https://github.com/insanj)!

# 🔐 license

---

funky is licensed under gpl-3.0. [see license file](https://github.com/insanj/funky/blob/master/LICENSE).
