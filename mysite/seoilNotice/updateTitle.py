import requests
from bs4 import BeautifulSoup
from seoilNotice.models import SeoilNotice

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

html = requests.get("http://hm.seoil.ac.kr/65/76?page=1")
soup = BeautifulSoup(html.text, 'html.parser')
semi_title = soup.select('table > tbody > tr > td.al > a > p')

a = SeoilNotice.objects.all()
print(a)

#print(semi_title[0].get_text(strip=True))
