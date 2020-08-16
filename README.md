# Get CO2ppm MHZ-14A

Get CO2 ppm value from MH-Z14A on Raspbbery Pi.

## Installation

If you don't install pipenv. Run this command.

```sh
pip install pipenv
```

Open `run.py` and update `DEV_PATH` (device path).

```python
DEV_PATH = "/dev/ttyAMA0"
```

Run `run.py` .

```sh
pipenv run python ./run.py
```

## Get CO2 ppm

GET request to localhost:5000

```sh
curl -s localhost:5000
```

Response(example)

```json
{"msg":"Get CO2 ppm","ppm":821,"time":"2020-08-16T15:18:57.519067"}
```

## Do zero calibration

If you want to zero calibration, GET request to localhost:5000/calibration

```sh
curl -s localhost:5000/calibration
```

## Reference

- [Raspberry Pi 3 Model B+ で二酸化炭素濃度を測る(MH-Z14A) -AWS IoT もあるよ-](https://qiita.com/watiko/items/5cfa2aedd5a67619add0)
- [CO2センサ MH-Z14Aの使い方](https://qiita.com/urib0/items/256973f68cc1fbcd1244)
