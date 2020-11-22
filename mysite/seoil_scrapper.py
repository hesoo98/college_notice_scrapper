import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from seoilNotice.models import SeoilNotice

# title경로 #contents > div > div.clearfix.con_wrap > div > table > tbody > tr:nth-child(1) > td.al > a > p
# date경로 #contents > div > div.clearfix.con_wrap > div > table > tbody > tr:nth-child(1) > td.al > a > time
# title = soup.find("td", {"class":"al"}).find("p").text

# title = soup.find_all("td", {"class": "al"})
# s = title[1]
# a.get_text(strip=True),

# semi_title1 = soup.find("td",{'class':'al'}).find('a').find('p').get_text(strip=True)
# semi_title2 = semi_title.find('a')
# html = requests.get("http://hm.seoil.ac.kr/65/76?page=1")


def seoil_notice(url, lastPage):
    result = []
    for page in range(lastPage):
        html = requests.get(f"{url}{page+1}")         #f-string
        soup = BeautifulSoup(html.text, 'html.parser')
        semi_title = soup.select('table > tbody > tr > td.al > a > p')
        date = soup.select('table > tbody > tr > td.al > a > time')
        links = soup.find_all('td', {"class": "al"})

        title_list = []

        '''title_dict = {}

        for t, d, l in semi_title, date, links:
            title_dict = {'title': t, 'date': d, 'links': l}'''


        for a in zip(semi_title, date, links):
            title_list.append(
                {
                    'title': a[0].get_text(strip=True),
                    'date': a[1].get_text(strip=True),
                    'link': "http://hm.seoil.ac.kr"+a[2].find("a").get('href'),
                }
            )

        for i in title_list:
            result.append(i)
    #title_dict = dict(title_list)

    #for i in title_list.items():
    #print(title_list[0]['title'], title_list[0]['date'], title_list[0]['link'])
    #print(title_list[9])
    return result


#seoil_notice("http://hm.seoil.ac.kr/65/76?page=", 10)

# https://armontad-1202.tistory.com/entry/%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-Django-DB%EC%97%90-%EB%84%A3%EA%B8%B0
# https://hashcode.co.kr/questions/4802/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%86%8D-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC-%ED%98%95%ED%83%9C%EC%97%90-%EC%9A%94%EC%86%8C%EC%97%90%EC%84%9C-%EC%9B%90%ED%95%98%EB%8A%94-%EB%B0%B8%EB%A5%98-%EA%B0%92-%EC%B0%BE%EA%B8%B0
# 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
#title_list len == 20
if __name__ == '__main__':
    seoil_notice_list = seoil_notice("http://hm.seoil.ac.kr/65/76?page=", 10)
    #for index in range(len(seoil_notice_list)):
    for i in seoil_notice_list:
        SeoilNotice(title=i['title'], date=i['date'], url=i['link']).save()


    #for item in seoil_notice_list:
        #for i in range(0, 10):
            #SeoilNotice(title=item[i]['title'], date=item[i]['date'], url=item[i]['link']).save()