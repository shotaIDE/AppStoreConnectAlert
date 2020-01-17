# AppStoreConnectAlert
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
