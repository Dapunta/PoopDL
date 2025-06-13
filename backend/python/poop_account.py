import re, requests, json, random, string

def create_account():

    username : str = "".join(random.choices(string.ascii_letters + string.digits, k=8)).lower()
    domain   : str = "".join(random.choices(string.ascii_letters + string.digits, k=6)).lower()
    email    : str = f"{username}@{domain}.com".lower()

    r = requests.Session()
    signup_url = "https://app.poophd.com/signup"
    data : dict[str,str] = {
        "username"       : username,
        "email"          : email,
        "password"       : username,
        "match_password" : username,
    }
    response = r.post(url=signup_url, data=data, allow_redirects=True)

    result = {
        **{k:v for k,v in data.items() if k != "match_password"},
        "cookie" : " ".join([f"{k}={v};" for k,v in r.cookies.get_dict().items()])
    }

    print(result)

def search(cookie:str):

    text = "dildo"
    page = 4

    r = requests.Session()
    search_url : str = f"https://app.poophd.com/search?q={text}&p={page}"
    response = r.get(url=search_url, cookies={'cookie':cookie})
    response_json = response.json()

    list_video = response_json["contents"]["videos"]
    for video in list_video:
        video_url = f"https://poophd.pro/e/{video["poop_id"]}"
        print(video_url)

if __name__ == "__main__":

    #--> buat akun
    create_account()

    #--> search
    # cookie = "_ga=helloworld; ci_session=uc0n04574mjuua4pv5v69svungh02k81;"
    # search(cookie)