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

You will also have to configure your own variables for...
```python
SLACK_WEB_HOOK = "your own webhook which you can generate through slack"
headers = {"User-Agent": 'you can just google search 'my user agent' in google and paste it here'}
server.login('your email', 'the key you generated through googles app passwords feature')
server.sendmail('email to send from', 'email to send to', msg)
```

Then just run
```bash
python3 bestbuyscraper.py
```