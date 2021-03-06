---
title:  "서블릿, SSR, CSR"
excerpt: "스프링 MVC 공부하기 [2]"
date:   2021-09-20 03:59:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-11T03:59:00-05:00
---

<br/>

## 💡 서블릿

##### HTML Form으로 데이터를 전송하는 경우를 생각해보자.

<br/>

![image-20211013232115838](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211013232115838.png)

##### 비즈니스 로직 전과 후로 해야 할 일이 너무 많다.

#### 이를 <span style="color:orange">서블릿</span>이 해결해준다.

<br/>

![image-20211013232129524](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211013232129524.png)

<br/>

<br/>

<br/>

### 🔎 서블릿

![image-20210921183856695](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20210921183856695.png)

- ##### urlPatterns에 들어있는 URL이 호출되면 서블릿 코드가 실행

- ##### HttpServletRequest => HTTP 요청 정보를 편리하게 사용

- ##### HttpServletResponse => HTTP 응답 정보를 편리하게 사용

<br/>

#### 🔎 서블릿의 전체 흐름

![image-20211013232145569](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211013232145569.png)

#### ☀️ HTTP 요청 시

- ##### WAS는 Request, Response 객체를 새로 만들어서 서블릿 객체 호출

- ##### 개발자는 Request 객체에서 HTTP 요청 정보를 편리하게 꺼내서 사용

- ##### 개발자는 Response 객체에 HTTP 응답 정보를 편리하게 입력

- ##### WAS는 Response 객체에 담겨있는 내용으로 HTTP 응답 정보를 생성

<br/>

<br/>

## 💡 서블릿 컨테이너

##### 서블릿 객체를 생성, 초기화, 호출, 종료하는 <span style="color:orange">생명주기를 담당</span>하는 컨테이너

##### 톰캣처럼 <span style="color:orange">서블릿을 지원하는 WAS</span>를 <span style="color:orange">서블릿 컨테이너</span>라고 한다.

<br/>

#### ☀️서블릿 컨테이너의 특징

- ##### 서블릿 객체는 <span style="color:orange">싱글톤</span>으로 관리 => 공유 변수 사용 주의(request, response는 들어올때마다 새로 생성)

- ##### JSP도 서블릿으로 변환 되어서 사용

- ##### 동시 요청을 위한 <span style="color:orange">멀티 쓰레드 처리 지원</span>

<br/>

<br/>

## 💡 멀티 쓰레드

##### WAS에서 멀티 쓰레드 처리를 지원

<br/>

### 💡 쓰레드

- ##### 에플리케이션 코드를 하나하나 순차적으로 실행시켜줌, (참고로 프로그램을 실행시키는 것은 프로세스!)

- ##### 자바 메인 메서드를 처음 실행하면 main이라는 이름의 쓰레드가 실행

- ##### 쓰레드가 없다면 자바 애플리케이션 실행이 불가능

- ##### 쓰레드는 한번에 하나의 코드 라인만 수행

- ##### 동시 처리가 필요하면 쓰레드를 추가로 생성

<br/>

<br/>

### 💡 멀티 쓰레드

다중 요청이 들어오는 경우

##### 요청마다 쓰레드를 생성해주는 방법

- ##### 장점

  - ##### 동시 요청을 처리할 수 있다

  - ##### 리소스(CPU, 메모리)가 허용될 때 까지 처리가능

  - ##### 하나의 쓰레드가 지연되어도, 나머지 쓰레드는 정상 동작

- ##### 단점

  - **고객의 요청이 올 때마다 쓰레드를 생성하면, 응답 속도가 늦어짐**
  - **컨텍스트 스위칭 비용이 발생**
  - **쓰레드 생성에 제한이 없기에, 고객이 요청이 너무 많다면, CPU, 메모리 임계점을 넘어서 서버가 죽을 수 있음**

  

#### 위의 단점들을 해결하기 위해 대부분의 WAS에서 <span style="color:orange">쓰레드 풀</span>을 사용

툼캣에서는 최대 200개가 기본 설정이고 변경 가능

##### 장점

- ##### 쓰레드를 생성하고 종료하는 비용(CPU)이 절약되고 응답 시간이 빨라짐.

- ##### 생성 가능한 쓰레드의 최대치가 있으므로 너무 많은 요청이 들어와도 기존 요청은 안전하게 처리할 수 있다.

<br/>

#### 성능 튜닝

- WAS의 주요 튜닝 포인트는 최대 쓰레드 수(max thread)
- 너무 낮으면?
  - 동시 요청이 많으면, 서버 리소스는 여유로우나, 클라이언트는 응답 지연
- 너무 높으면?
  - 동시 요청이 많으면, CPU, 메모리 임계정 초과로 서버 다운

<br/>

<br/>

### ☀️ WAS의 멀티 쓰레드 지원

- ##### 멀티 쓰레드에 대한 부분을 WAS가 처리

- #### 개발자가 <span style="color:orange">멀티 쓰레드 관련 코드를 신경쓰지 않아도 됨</span>

- ##### 개발차는 마치 싱글 쓰레드 프로그래밍을 하듯이 편리하게 소스 코드를 개발

- ##### 멀티 쓰레드 환경이므로 <span style="color:orange">싱글톤 객체(서블릿, 스프링 빈)는 주의해서 사용</span>

<br/>

<br/>

### 💡 리소스 제공 방법

#### 1. 정적 리소스 제공

- ##### 고정된 HTML파일, CSS, JS, 이미지, 영상 등을 제공

- ##### 주로 웹 브라우저에서 요청

<br/>

#### 2. 동적인 HTML 페이지 제공

- ##### 동적으로 필요한 HTML 파일을 생성해서 전달 (JSP, 타임리프 사용)

- ##### 웹 브라우저는 받은 HTML을 해석하면 된다.

<br/>

#### 3.  HTTP API(REST API)

- ##### HTML이 아니라 데이터를 전달

- ##### 주로 **JSON** 형식 사용

- ##### 다양한 시스템에서 호출

  - ##### 앱 클라리언트 to 서버

  - ##### 웹 클라이언트 to 서버

  - ##### 서버 to 서버

- ##### 데이터만 주고 받기에 UI 화면이 필요하면 클라이언트가 별도 처리

  - ##### UI 클라이언트 접점

    - ##### 앱 클라이언트(**아이폰, 안드로이드, PC앱**) 

    - ##### 웹 브라우저에서 자바스트립트를 통한 HTTP API 호출

    - ##### 웹 클라이언트(**React, Vue.js**) 

<br/>

<br/>

## 💡 SSR, CSR

#### ☀️ SSR - 서버 사이드 렌더링

- ##### HTML 최종 결과를 <span style="color:orange">서버</span>에서 만들어 웹 브라우저에 전달

- ##### 주로 정적인 화면에 사용

- ##### 관련기술 : JSP, 타임리프 -> 백엔드 개발자

<br/>

#### ☀️ CSR - 클라이언트 사이드 렌더링

- ##### HTML 결과를 자바스크립드를 사용해 <span style="color:orange">웹 브라우저에서</span>에서 동적으로 생성해서 적용

- ##### 주로 동적인 화면에 사용, 웹 환경을 마치 앱 처럼 필요한 부분부분 변경할 수 있음

- ##### 예)구글 지도, Gmail, 구글 캘린더

- ##### 관련기술 : React, Vue.js -> 웹 프론트엔드 개발자

<br/>

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 1편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-1/dashboard)

##### [스프링 공식사이트](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html)

