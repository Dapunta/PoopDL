from playwright.sync_api import sync_playwright

def fetch_url(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Kunjungi homepage dulu untuk inisialisasi cookies/session
        page.goto("https://doodsearch.com", wait_until="load")
        page.wait_for_timeout(3000)  # Tunggu 3 detik biar JS jalan dan cookie kebentuk

        # 2. Sekarang baru ke halaman tujuan
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(2000)  # Tambahan delay kecil kalau mau aman

        html = page.content()
        print(html[:1000])

        browser.close()

if __name__ == "__main__":
    fetch_url("https://doodsearch.com/d/0t8xhkr5fpiv")
