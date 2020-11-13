# XboxBestBuyScraper

# Installations

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these packages.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install requests
pip install bs4
```

## Usage

If you'd like to use this scraper. You will have to configure your 2-step verification through Google. Look for "App Passwords" and add an app password for the device which will run the script.

You will also have to configure your own environment variables as well as a few other variables.

## Environment Variables

```bash
pip3 install python-dotenv
```


Create a `.env` file and add these to it
```python
SLACK_WEB_HOOK = "your own webhook which you can generate through slack, just follow" [this](https://api.slack.com/tutorials/slack-apps-hello-world)
GOOGLE_APP_PASSWORD = "your own google app password"
```

headers = {"User-Agent": 'you can just google search 'my user agent' in google and paste it here'}
server.login('your email', 'the key you generated through googles app passwords feature')
server.sendmail('email to send from', 'email to send to', msg)

Then just run
```bash
python3 bestbuyscraper.py
```