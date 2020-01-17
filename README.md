# AppStoreConnectAlert
## What is this?
An automation tools to check if there is some updates on Apple Developer Program License Agreement.
Apple will not notify you that the agreement have been updated, so you may have to agree without a carefully confirmation.
If you run this tool on a cron or other platform, you can receive the notification in real time!

## How to start?
Open folder in VSCode.

Prepare Python environment by using virtualenv.

```shell
pip install virtualenv
virtualenv env
```

Activate Python environment.

```shell
source env/bin/activate
```

Install required packages.

```shell
pip install -r requirements.txt
```

Copy settings json file and write chrome driver path and credentials in it.

```shell
cp settings_sample.json settings.json
```

Run the script using the "Launch" configuration.
