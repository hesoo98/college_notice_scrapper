import requests
from bs4 import BeautifulSoup


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from seoilNotice.models import SeoilNotice, EventInfo, BachelorNotice


req = requests.get('http://hm.seoil.ac.kr/65/69?page=1')
req.encoding = 'utf-8'

html = req.text
soup = BeautifulSoup(html, 'html.parser')
#contents > div > div.clearfix.con_wrap > div > table > tbody > tr:nth-child(1) > td.al > a > p
posts = soup.select('table > tbody > tr > td.al > a > p')
latest = posts[0].get_text(strip=True)


latest_event_list = EventInfo.objects.all().order_by('id')[:1]

print(latest_event_list[0])
print(latest)
