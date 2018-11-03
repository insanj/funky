# funky

🎷 simple call &amp; response python to google cloud function

# example

🔥 test out the live deployment of the gcloud flask python app!

- run `python funky.py <PARAM>` to get a response via python
- go to https://funky-221323.appspot.com/ to get a response via web browser

> put in a custom param to see a custom result based on the endpoint tree (such as [🍗](https://funky-221323.appspot.com/🍗))

# usage

- modify `main.py` to change flask endpoints
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

# authors

julian weiss (insanj). (c) 2018. reach out on [github](https://github.com/insanj)!

# license

funky is licensed under gpl-3.0. [see license file](LICENSE).
