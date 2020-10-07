import requests
from bs4 import BeautifulSoup
#find_next_sibiling()
#https://stackoverflow.com/questions/31731217/extracting-text-outside-of-a-div-tag-beautifulsoup 외부 텍스트 추춟법
# https://sodocumentation.net/ko/beautifulsoup/topic/1940/%EC%9C%84%EC%B9%98-%EC%9A%94%EC%86%8C  요소뒤 텍스트 찾기
#soup.select("dl:nth-child(2) > dd > span:nth-child(6)") date 경로
#이 함수는 도서관 공지사항의 제목과 날짜를 리스트로 반환합니다.

def seoil_libraryNotice(url, lastPage):
    for p in range(lastPage):
        html = requests.get(f"{url}{p+1}")
        #html = requests.get("http://lib.seoil.ac.kr/Board?n=notice&p=1")
        soup = BeautifulSoup(html.text, 'html.parser')
        title = soup.find_all("dl", {"class": "onroad-board"})
        dates = title               #soup.find("span", text=" / 게시일")
        links = title

        title_list = []
        for i in zip(title, dates, links):
            title_list.append(
                 {
                    "title": i[0].find("a").get_text().strip(),
                    "date": i[1].find("dd").find("span", text=" / 게시일").next_sibling.strip(),
                    "link": "http://lib.seoil.ac.kr/" + i[2].find("dd").find("a").get('href'),
                 }
            )

        for a in range(0, lastPage):
            print(title_list[a]['title'], title_list[a]['date'], title_list[a]['link'])


    return title_list

# #mainWrap > div.sponge-page-guide > dl:nth-child(2n) > dd > span:nth-child(6)
# #mainWrap > div.sponge-page-guide > dl:nth-child(4) > dd > span:nth-child(6)
url="http://lib.seoil.ac.kr/Board?n=notice&p="
seoil_libraryNotice(url, 10)
