import requests
from bs4 import BeautifulSoup
from seoilLibraryNotice.models import LibNotice, NewsInfo

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()


#find_next_sibiling()
#https://stackoverflow.com/questions/31731217/extracting-text-outside-of-a-div-tag-beautifulsoup 외부 텍스트 추춟법
# https://sodocumentation.net/ko/beautifulsoup/topic/1940/%EC%9C%84%EC%B9%98-%EC%9A%94%EC%86%8C  요소뒤 텍스트 찾기
#soup.select("dl:nth-child(2) > dd > span:nth-child(6)") date 경로
#이 함수는 도서관 공지사항의 제목과 날짜를 리스트로 반환합니다.



def seoil_libraryNotice(url, lastPage):
    result = []
    for p in range(lastPage):
        html = requests.get(f"{url}{p+1}")
        soup = BeautifulSoup(html.text, 'html.parser')
        title = soup.find_all("dl", {"class": "onroad-board"})
        date = title               #soup.find("span", text=" / 게시일")
        links = title

        title_list = []
        for i in zip(title, date, links):
            title_list.append(
                 {
                    'title': i[0].find("a").get_text().strip(),
                    'date': i[1].find("dd").find("span", text=" / 게시일").next_sibling.strip(),
                    'link': "http://lib.seoil.ac.kr/" + i[2].find("dd").find("a").get('href'),
                 }
            )
        for a in title_list:
            result.append(a)


    return result

# #mainWrap > div.sponge-page-guide > dl:nth-child(2n) > dd > span:nth-child(6)
# #mainWrap > div.sponge-page-guide > dl:nth-child(4) > dd > span:nth-child(6)
#url=
seoil_libraryNotice("http://lib.seoil.ac.kr/Board?n=notice&p=", 2)

if __name__ == '__main__':
    lib_notice_list = seoil_libraryNotice("http://lib.seoil.ac.kr/Board?n=notice&p=", 2)
    lib_news_list = seoil_libraryNotice("http://lib.seoil.ac.kr/Board?n=news&p=", 2)

    for index1 in lib_notice_list:
        LibNotice(title=index1['title'], date=index1['date'], url=index1['link']).save()

    for index2 in lib_news_list:
        NewsInfo(title=index2['title'], date=index2['date'], url=index2['link']).save()
