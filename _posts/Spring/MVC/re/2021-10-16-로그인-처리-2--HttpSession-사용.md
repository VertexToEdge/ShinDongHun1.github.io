---
title:  "로그인 처리 2 -HttpSession 사용"
excerpt: "스프링 MVC 공부하기[20]"
date:   2021-10-16 21:02:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-16T21:02:00



---

<br/>

## 💡 서블릿이 지원하는 세션

### 🌌 HttpSession 

##### 🔎 세션 생성과 조회

- ##### 세션을 생성하려면 request.getSession(true) 를 사용하면 된다.

  - public HttpSession getSession(boolean create);

##### 🔎 세션의 create 옵션에 대해 알아보자.

- ##### request.getSession(true)

  - 세션이 있으면 기존 세션을 반환한다.
  - 세션이 없으면 새로운 세션을 생성해서 반환한다.

- ##### request.getSession(false)

  - 세션이 있으면 기존 세션을 반환한다.
  - 세션이 없으면 새로운 세션을 생성하지 않는다. null 을 반환한다.

- request.getSession() : 신규 세션을 생성하는 request.getSession(true) 와 동일하다.

<br/>

<br/>

## 💡 서블릿이 지원하는 세션을 사용하기

#### 🔎 로그인과 로그아웃

<script src="https://gist.github.com/ShinDongHun1/f93286d25a68434ef9ff030e7ef59539.js"></script>

##### (참고로 SessionConst.LOGIN_MEMBER 는 "loginMember" 이다.)

- ##### 로그인 시: session.setAttribute(SessionConst.LOGIN_MEMBER, member);를 통해 쿠키를 세션에 저장.

- ##### 로그아웃 시 : session.invalidate(); 를 통해 세션 삭제

<br/>

#### 🔎 로그인한 사용자만 접근 가능한 화면 만들기

<script src="https://gist.github.com/ShinDongHun1/4bf7e495b82207e20e6b333932a90895.js"></script>

##### 🔎 세션을 통해 로그인한 사용자만 접근할 수 있는 화면을 만들기 위해서는 다음과 같은 코드가 필요하다.

```java
HttpSession session = request.getSession(false);

if(session == null){
	return new ResponseEntity<>("쿠키에 해당하는 정보가 없습니다", HttpStatus.BAD_REQUEST);
}
Member member =(Member)session.getAttribute(SessionConst.LOGIN_MEMBER);
```

<br/>

<br/>

## 💡 @SessionAttribute

##### 스프링은 세션을 더 편리하게 사용할 수 있도록 @SessionAttribute를 지원한다.

##### (참고로 이 기능은 세션을 생성하지 않는다)

##### 🔎이 기능을 사용하면 바로 위의 코드들을 모두 생략하고 member 객체를 가져올 수 있다.

<script src="https://gist.github.com/ShinDongHun1/8660fc9d85c6a206db9971803d83a23c.js"></script>

<br/>

### 🌌 TrackingModes

API방식이 아닌 방법으로, 로그인을 처음 시도하면 URL이 다음과 같이 jsessionid를 포함하고 있는 것을 확인할 수 있다.

http://localhost:8080/;jsessionid=F59911518B921DF62D09F0DF8F83F872

이것은 웹 브라우저가 쿠키를 지원하지 않을 때 쿠키 대신 URL을 통해서 세션을 유지하는 방법이다. 이

URL 전달 방식을 끄고 항상 쿠키를 통해서만 세션을 유지하고 싶으면 다음 옵션을 넣어주면 된다. 

##### 🔎 application.properties

```properties
server.servlet.session.tracking-modes=cookie
```

<br/>

<br/>

## 💡 세션 정보와 타임아웃 설정

#### 🔎 세션 정보 확인

<script src="https://gist.github.com/ShinDongHun1/3a8f24d90985acbeaf971603cd2611cf.js"></script>

<br/>

- sessionId : 세션Id, JSESSIONID 의 값이다. 예) 34B14F008AA3527C9F8ED620EFD7A4E1
- maxInactiveInterval : 세션의 유효 시간, 예) 1800초, (30분)
- creationTime : 세션 생성일시
- lastAccessedTime : 세션과 연결된 사용자가 최근에 서버에 접근한 시간, 클라이언트에서 서버로
  sessionId ( JSESSIONID )를 요청한 경우에 갱신된다.
- isNew : 새로 생성된 세션인지, 아니면 이미 과거에 만들어졌고, 클라이언트에서 서버로
  sessionId ( JSESSIONID )를 요청해서 조회된 세션인지 여부

<br/>

<br/>

### 🌌 세션 타임아웃 설정

- #### 스프링 부트로 글로벌 설정

  - #####  🔎 application.properties 에 다음과 같이 설정

  - ```properties
    server.servlet.session.timeout=1800
    ```

  - ##### (글로벌 설정은 초 단위로 설정해야 한다. 60(1분), 120(2분), ...)

- #### 특정 세션 단위로 시간 설정

  - ##### session.setMaxInactiveInterval(1800); //1800초

<br/>

<br/>

#### 🔎 자료 - [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

<br/>