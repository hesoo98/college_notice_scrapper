# college_notice_scrapper

이 프로젝트는 Django와 파이썬, 간단한 크롤링을 공부하기 위해 만들고 있는 프로젝트입니다.

프로젝트를 로컬에서 실행시키는 법
파일을 다운받고, 콘솔창에서 파이썬 가상환경으로 진입합니다.

윈도우 기준 가상환경 진입법
venv 폴더 안에 Scripts폴더 안으로 들어가서 .\activate 입력

진입이 되면 콘솔 명령어 입력줄 가장 왼쪽이 (venv)로 바뀝니다.
이 상태에서 mysite 폴더로 이동 후
python .\manage.py runserver를 실행하면 완료.

만약 django.db.migrations.exceptions.NodeNotFoundError: Migration seoilNotice.0005_academicnotice dependencies reference nonexistent parent node ('seoilNotice', '0004_eventinfo')
이러한 오류가 뜬다면 적혀있는데로 seoilNotice 폴더안의 0005~ 하는 파일에 문제가 있다는것이니 지워주고
저 오류가 안뜰때까지 문제가있는 파일을 지워주고 다시 시도합니다.


실행화면
메인 화면
![image](https://user-images.githubusercontent.com/8851063/216335192-5596cea7-1656-4e5e-a457-365b8db7d1cd.png)
<br><br>

서일공지 ->행사 안내
![image](https://user-images.githubusercontent.com/8851063/216335431-607a9c83-12e8-4a53-bfb6-d00ea371d330.png)
<br><br>
검색창 -> 서일공지
![image](https://user-images.githubusercontent.com/8851063/216335544-b355ec3e-8717-4e8d-a145-eaeb3997fde6.png)

