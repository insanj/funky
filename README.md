# funky
🎷 simple call &amp; response python to google cloud function

# use

- modify `main.py` to change flask endpoints
- run `gcloud app deploy` to sync your changes with the google app engine you've set up

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

# authors

julian weiss (insanj). (c) 2018. reach out on [github](https://github.com/insanj)!

# license

funky is licensed under gpl-3.0. [see license file](LICENSE).
