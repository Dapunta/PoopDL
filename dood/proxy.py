from flask import Flask, Response, request
import requests

app = Flask(__name__)

#--> masukin url tadi
SOURCE_URL = 'https://e587bdk.cloudatacdn.com/u5kj6r24mhblsdgge7iocmavlz3lu54cwyzhu2nzd67m2nuwdbdo4ofv7qbq/p48ldmlzmi~?token=ysi9a6skfr9lvrmtcs5buyu2'

HEADERS = {
    "Range": lambda: request.headers.get("Range", "bytes=0-"),
    "Referer": "https://all3do.com/", #--> ganti sesuai referer tadi
}

@app.route("/video")
def stream_video():
    headers = {k: v() if callable(v) else v for k, v in HEADERS.items()}
    r = requests.get(SOURCE_URL, headers=headers, stream=True)
    return Response(
        r.iter_content(chunk_size=8192),
        status = r.status_code,
        content_type = r.headers.get('Content-Type'),
        headers = {
            "Content-Range": r.headers.get("Content-Range", ""),
            "Accept-Ranges": "bytes"
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
