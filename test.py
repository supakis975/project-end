import requests
from bs4 import BeautifulSoup
import json

cookies = {
    'cf_clearance': 'fMxWFilxb4Ac93lzrT83eABYBFVVERX6mTOxUJjH9DA-1735908449-1.2.1.1-Na.3eXKedlfLHeVwjn8I2.bUfIRoG34_vvQG7FYisCjcArrKUmzkQuHzwghW0pPgurnDuoFbPzlZv8sQWt_Cq_sIhFymI_TRG3kL7buEMst5LYAxPmLQZcOUkpuNDF8lmBffOrjEFKzCWgdfjus_l9T7pbW5Rj5MGJ3NW37EcJ6MWy9DjRr2inev_fepG2kF_70D2p4GzWnB2NyN0cRhkPa6aEISjmVnARdYn_y5cZnntrY2ApI9Kka506wsjg_Y9Ypnmu9BN0C0tXcu41TUbS6Qdam1V4IP33urB1LJomuvm92LuZyFfU6WIp2Yh4RUC1Y3GVc3iNSw3KVXtamskYzm4Qr.lk4i31vOHflvHY7OvIQ88uQj8f4v2ZRpNgy234UZiJm7y1ALWDgPYp_o9OdMDeDL_YWZCWaoG8eSnvMGOXbCal9o.KcH2LcRrkSu',
    '__Host-steamdb': '7335786-c5c4ea4fc43c4cbf98e3919f4f7136c4dad875e1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,th;q=0.8,ku;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'cf_clearance=fMxWFilxb4Ac93lzrT83eABYBFVVERX6mTOxUJjH9DA-1735908449-1.2.1.1-Na.3eXKedlfLHeVwjn8I2.bUfIRoG34_vvQG7FYisCjcArrKUmzkQuHzwghW0pPgurnDuoFbPzlZv8sQWt_Cq_sIhFymI_TRG3kL7buEMst5LYAxPmLQZcOUkpuNDF8lmBffOrjEFKzCWgdfjus_l9T7pbW5Rj5MGJ3NW37EcJ6MWy9DjRr2inev_fepG2kF_70D2p4GzWnB2NyN0cRhkPa6aEISjmVnARdYn_y5cZnntrY2ApI9Kka506wsjg_Y9Ypnmu9BN0C0tXcu41TUbS6Qdam1V4IP33urB1LJomuvm92LuZyFfU6WIp2Yh4RUC1Y3GVc3iNSw3KVXtamskYzm4Qr.lk4i31vOHflvHY7OvIQ88uQj8f4v2ZRpNgy234UZiJm7y1ALWDgPYp_o9OdMDeDL_YWZCWaoG8eSnvMGOXbCal9o.KcH2LcRrkSu; __Host-steamdb=7335786-c5c4ea4fc43c4cbf98e3919f4f7136c4dad875e1',
    'priority': 'u=0, i',
    'referer': 'https://steamcommunity.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"131.0.6778.205"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.205", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

response = requests.get('https://steamdb.info/stats/gameratings/', cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
titles = []
for title in soup.find_all("a"):
    titles.append(title.get_text().strip())

scraped_data = {"titles": titles}

with open('game3.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(scraped_data, jsonfile, indent=4)

print("Scraped data saved")