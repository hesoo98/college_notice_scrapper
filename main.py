from seoil_scrap import seoil_notice


seoil_url = "http://hm.seoil.ac.kr/65/76?page="
seoil_scholar_url = "http://hm.seoil.ac.kr/65/78?page="
seoil_lastPage = 10

a = seoil_notice(seoil_scholar_url, seoil_lastPage)
b = seoil_notice(seoil_url, seoil_lastPage)
