### Step 1. Extracting
On home directory, extract the zip file on linux and move to the directory using this command.
```sh
tar -xvf rest-api-bare.tar.xz && cd ./rest-api-bare
```
### Step 2. Running the server
Run the server using
```sh
python3 server.py
```

### Step 3. Testing on Server
For testing the app, on a new terminal run these command:

On a new terminal on your server
**GET Payload**
```sh
curl --location --request GET 'http://0.0.0.0:8080/api/payload'
```

**PUT Payload (For updating JSON data)**
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


### Step 4. Testing from outside of server 
For testing the app, on a new terminal run these command:
Testing from another server.
First you need to have your target server IP Address and ensure that the port opened in firewal

**Opening port 8080**
```sh
sudo ufw allow from any to any port 8080 proto tcp
```

The rest is similar with the steps before except you should use your server public IP Address
For example if your IP Address is 103.80.0.43
**Get payload**
```sh
curl --location --request GET 'http://103.80.0.43:8080/api/payload'
```

***PUT Payload (For updating JSON data)***
```sh
curl --location --request PUT 'http://103.80.0.43:8080/api/payload' \
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

 For more detailed explanation, you can see the README.md