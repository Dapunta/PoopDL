import re, json, requests, cloudscraper

max_redirects  = 50

class Dood():

    #--> konstruktor
    def __init__(self) -> None:

        self.r       = cloudscraper.create_scraper()
        self.url     = None
        self.host    = None
        self.referer = None
        self.redirect_count = 0

    #--> redirect karena domain berubah-ubah
    def redirect(self, url:str) -> None:

        while self.redirect_count < max_redirects:
            response = self.r.get(url, allow_redirects=False)
            if response.status_code in (301, 302, 303, 307, 308):
                try:
                    url = response.headers['Location']
                    self.url = url
                    self.host = 'https://{}/'.format(self.url.split('/')[2])
                    self.redirect_count += 1
                except Exception: pass
            else: break

    #--> main method
    def get_file(self, url:str):

        #--> cek apakah url valid
        self.redirect(url)
        if not self.host: return

        id_file = self.url.split('/')[4]
        self.get_embeded_url(id_file)
    
    #--> dapetin embed url
    def get_embeded_url(self, id_file:str):
        
        url = '{}d/{}'.format(self.host, id_file)
        headers = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding':'gzip, deflate',
            'accept-language':'en-US,en;q=0.9',
            'cache-control':'no-cache',
            # 'cookie':'_ym_uid=1745609992734705383; _ym_d=1745609992; _ym_isad=2; _ym_visorc=w',
            'pragma':'no-cache',
            'priority':'u=0, i',
            'referer':'https://doodsearch.com/',
            'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile':'?1',
            'sec-ch-ua-platform':'"Android"',
            'sec-fetch-dest':'document',
            'sec-fetch-mode':'navigate',
            'sec-fetch-site':'same-origin',
            'sec-fetch-user':'?1',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
        }
        print(url)

        response = cloudscraper.create_scraper().get(url)
        response_text = response.text.replace('\\','')
        print(response_text)


if __name__ == '__main__':

    url = 'https://doodsearch.com/d/0t8xhkr5fpiv'
    # headers = {
    #         'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #         'accept-encoding':'gzip, deflate',
    #         'accept-language':'en-US,en;q=0.9',
    #         'cache-control':'no-cache',
    #         'cookie':'_ym_uid=1745609992734705383; _ym_d=1745609992; _ym_isad=2; _ym_visorc=w',
    #         'pragma':'no-cache',
    #         'priority':'u=0, i',
    #         'referer':'https://doodsearch.com/',
    #         'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    #         'sec-ch-ua-mobile':'?1',
    #         'sec-ch-ua-platform':'"Android"',
    #         'sec-fetch-dest':'document',
    #         'sec-fetch-mode':'navigate',
    #         'sec-fetch-site':'same-origin',
    #         'sec-fetch-user':'?1',
    #         'upgrade-insecure-requests':'1',
    #         'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
    #     }
    
    # response = requests.get(url, headers=headers, allow_redirects=False)
    # print(response.headers)
    # print(response.text)

    dood = Dood()
    dood.get_file(url)