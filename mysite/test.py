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


html = requests.get("http://hm.seoil.ac.kr/65/76?page=1")
soup = BeautifulSoup(html.text, 'html.parser')
semi_title = soup.select('table > tbody > tr > td.al > a > p')
date = soup.select('table > tbody > tr > td.al > a > time')
links = soup.find_all('td', {"class": "al"})

'''for link in links:
    print("http://hm.seoil.ac.kr" + link.find("a").get('href'))'''
