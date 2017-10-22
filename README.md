# Twitter Tools

## Install
* `virtualenv -ppython3.6 venv venv`
* `pip install -r requirements.txt`
* `touch ttools/local_settings.py`
* Make your own apps and get access token
* Put them in `local_settings.py` (refer `ttools/settings.py`)
* If you want to receive email alerts, also put your email address

## With Cron
* ex: `00 10-23 * * * cd /path/to/ttools/ && ./run bnu > /dev/null 2>&1`

## Warnings
* Use at your own risk
* You need to install any mail servers to receive email alerts
