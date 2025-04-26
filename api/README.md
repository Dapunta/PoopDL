# API Documentation

**`Domain`** : [`poopdl-api.dapuntaratya.com`](https://poopdl-api.dapuntaratya.com)  
**`Endpoint`** : [`/get_file`](https://poopdl-api.dapuntaratya.com/get_file)

### Get All File

URL
  - ```py
    https://poopdl-api.dapuntaratya.com/get_file
    ```

Params
  - ```json
    {"url":url}
    ```
    `url` dapat berupa string maupun array/list

Response
  - ```json
    {"status":status, "message":message, "data":[]}
    ```

### Contoh Kode

**`python`**
```py
import requests

response = requests.post(
    url     = "https://poopdl-api.dapuntaratya.com/get_file",
    headers = {"Content-Type":"application/json"},
    json    = {"url":[
        "url_1...",
        "url_2...",
        "url_3...",
    ]}
).json()
```

**`javascript`**
```js
const fetchData = async () => {
    const response = await fetch(
        "https://poopdl-api.dapuntaratya.com/get_file",
        {
            method  : "POST",
            headers : {"Content-Type":"application/json"},
            body    : JSON.stringify({"url":[
                "url_1...",
                "url_2...",
                "url_3...",
            ]})
        }
    );
    const data = await response.json();
};

fetchData();
```