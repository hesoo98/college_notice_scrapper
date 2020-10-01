import requests
from bs4 import BeautifulSoup


#   title경로 #contents > div > div.clearfix.con_wrap > div > table > tbody > tr:nth-child(1) > td.al > a > p
#   date경로 #contents > div > div.clearfix.con_wrap > div > table > tbody > tr:nth-child(1) > td.al > a > time
#title = soup.find("td", {"class":"al"}).find("p").text

#title = soup.find_all("td", {"class": "al"})
#s = title[1]
# a.get_text(strip=True),

#semi_title1 = soup.find("td",{'class':'al'}).find('a').find('p').get_text(strip=True)
#semi_title2 = semi_title.find('a')
#html = requests.get("http://hm.seoil.ac.kr/65/76?page=1")

def seoil_notice(url ,lastPage):
    for page in range(lastPage):
        html = requests.get(f"{url}{page+1}")         #f-string
        soup = BeautifulSoup(html.text, 'html.parser')
        semi_title = soup.select('table > tbody > tr > td.al > a > p')
        date = soup.select('table > tbody > tr > td.al > a > time')
        links = soup.find_all('td', {"class": "al"})

        title_list = []
        for a in zip(semi_title, date, links):
            title_list.append(
                {
                    'title': a[0].get_text(strip=True),
                    'date': a[1].get_text(strip=True),
                    'link': "http://hm.seoil.ac.kr"+a[2].find("a").get('href'),
                }
            )

        for i in range(0, 20):
            print(title_list[i]['title'], title_list[i]['date'], title_list[i]['link'])

    return title_list
