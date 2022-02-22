# practiceDJANGO
## 장고 연습

    activate 해서 가상환경 활성화
    terminal에 (djangovenv)가 생김
    
    프로젝트 생성: django-admin startproject 프로잭트이름
    앱 생성     : python manage.py startapp 앱이름
    서버실행    : python manage.py runserver
                 python manage.py runserver 포트번호
    서버닫기    : ctrl + c
    
***
## 뷰, 템플릿, 모델
    뷰: 웹클라이언트에서 요청이 전달되면 요청에 맞는 서비스로직 수행, 결과 응답하거나 템플릿을 통해 응담
        파이썬함수, 클래스로 구현하는데 함수로 구현
    
    템플릿: 브라우저에 렌더링(출력)하는 웹페이지 내용 - HTML로 만듬
    
    모델: DB에 대한 CRUD(create, read, update, delete)작업 구현 -파이썬 클래스로 구현
 
 템플릿,모델 사용시 settings.py에 등록해주어야함
 ***
 ## path (프로젝트 urls.py에서)
 1. import 앱이름.views
 
    path('',앱이름.views.함수)
 2. from django.urls import include
 
    path('',include('앱이름.urls')
    
    -> urls.py(앱)에서 추가로 pathing해줌
 ***
## 뷰함수
    -Query 문자열 추출
     요청방법에 따라 2가지 방법이 있음
     GET 방식 요청: request.GET, 변수=request.GET['name'],//get 못받으면 에러남
                                변수=request.GET.get('name')//get못받으면 None으로 받아짐
                                변수=request.GET.get('name','기본값')
     POST 방식 요청: 변수=request.POST
                    변수=requst.POST['name']
                    변수=request.POST.get('name')
                    변수=request.POST.get('name','기본값')
    -요청 방식을 체크: request.method
    -이런저런 서비스 로직(처리로직)을 구현
    -템플릿을 통해서 응답페이지 구성되도록 처리
    -응답 페이지에 전달할 데이터가 존재하면 dictionary 객체에 담아서 보냄
***
템플릿 불러오는 방법

    django.template
    template=loader.get_template("템플릿.html")
    HttpResponse(template.render(전달할내용,request))    //전달할 내용 생략시 None사용가능
    or
    django.shortcut
    render(request,"템플릿.html",전달할내용)
    
### [템플릿]

   - HTML로 작성(CSS, Javascript)
   - 장고에서 제공하는 구문을 이용해서 동적처리 구현가능
     동적 처리가 수행되는 위치에 따라서
        - 서버: 장고의 템플릿 변수, 장고의 템플릿 태그
        - 클라이언트: 자바스크립트
        
    ex. 웹페이지상 시간을 출력
    
    서버 기반의 시간: 장고 템플릿 태그(python)
    
    클라이언트 기반의 시간: 자바스크립트
      
#### 템플릿 태그
    {% tag %}
    {% tag %} ... {% endtag %}
    
    example)
    {% csrf_token %}
    {% if 조건 %}
    ...
    {% else %}
    ...
    {% endif %}
    
## GET,POST 전달하는 방법(템플릿)
#### GET
**\<a>, \<form>, url** 등으로 

#### POST -query안보이게 하고싶을때, 사이즈가 
\<form>태그를 이용해서만 전달가능, {% csrf_token %} 사용해야함


example:

    <form method="POST" action="요청이 될 path사이트"></form>

***    
## 다양한 요청방식
1. \<input type='타입' name='카테고리' value='이름'>

        타입: checkbox: 체크박스(여러개가능)
              radio: 선택 (1개가능)
              date: 날짜
              submit:전송
              reset: 리셋
              text: 
          
2. \<select name='카테고리'> \</select> : 목록 선택이 생김
    
        <option value='저장될이름'>보이는이름</option>
        
3. \<textarea name='변수' rows='' cols=''>
    텍스트 적는 칸 생김
      
***

# DB-SQL

data CRUD - DB 연동

   Create - INSERT명령
     
   Read - SELECT 명령
     
   Update - UPDATE 명령
     
   Delete - DELETE 명령
     
***
몇개를 찾을지 모름- filter(), exclude()사용
정확히 하나 뭐꺼낼지 알음- get()사용
 
    필드이름__룩업타입=조건값
 
 
모델클래스----------------------->DB테이블 생성
             migrate명령         앱이름_모델클래스명(대소문자구분x)
             
 DB테이블 생성------------------------>모델클래스 생성   Model API로 CRUD작업
 앱이름_모델클래스명

***
# 파일 업로드

업로드하게 되는 파일을 모델에 저장하는 path인 models.FileField, 서브폴더 사용하고싶을때는 upload_to 사용

file upload 시 form 으로 post로 넘겨주고 enctype="multipart/form-data" 넣어주어야함

파일 타입의 input 태그도 사용해야함

당연히 csrf_token도 필요(post이기 떄문)

파일을 추출할때는 request.FILES 속성 사용
