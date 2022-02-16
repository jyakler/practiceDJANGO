# practiceDJANGO
## 장고 연습

    activate 해서 가상환경 활성화
    terminal에 (djangovenv)가 생김
    
    프로젝트 생성: django-admin startproject 프로잭트이름
    앱 생성     : python manage.py startapp 앱이름
    서버실행    : python manage.py runserver
    서버닫기    : ctrl + c
    
***
## 뷰, 템플릿, 모델
    뷰: 웹클라이언트에서 요청이 전달되면 요청에 맞는 서비스로직 수행, 결과 응답하거나 템플릿을 통해 응담
        파이썬함수, 클래스로 구현하는데 함수로 구현
    
    템플릿: 브라우저에 렌더링(출력)하는 웹페이지 내용 - HTML로 만듬
    
    모델: DB에 대한 CRUD(create, read, update, delete)작업 구현 -파이썬 클래스로 구현
 
 템플릿,모델 사용시 settings.py에 등록해주어야함
 ***
 
