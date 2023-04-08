# README
Requirements:
    - python3.8 and python3.8-devel installed


## Usage
```sh
usage:  python3 server.py [-h] [-p PORT_NUMBER]

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  PORT NUMBER (Must be integer between 1025-65536). Default 8080
```

Running without argument will serve this service in port 8080
```sh
python3 server.py
```

## Testing
On a new terminal run this Curl Command:
```sh
curl --location --request GET 'http://0.0.0.0:8080/api/payload'
```

For PUT endpoint:
```sh
curl --location --request PUT 'http://0.0.0.0:8080/api/payload' \
--header 'Content-Type: application/json' \
--data-raw '{
  "Assessment": {
    "Origin": "ERX233",
    "Designator": "AP101",
    "Toaster": [
      {
        "Query": {
          "question": "What great debilitation opponent hertz cartesian duelism insipid agreement",
          "response": "We appear along have rain late temporal today. Yes but I do not think it will rain tomorrow",
          "R1": "0.4",
          "R2": "0.1",
          "R3": "0.3",
          "R4": "0.2"
        }
      }
    ]
  }
}'
```



## Custom Port
```sh
python3 server.py -p 8485
```
Will run this REST Service in PORT 8485