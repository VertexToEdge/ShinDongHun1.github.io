---
title:  "HTTP 요청 조회-기본,헤더 ,MultiValueMap"
excerpt: "스프링 MVC 공부하기[10]"
date:   2021-10-13 19:35:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-13T17:35:00


---

<br/>

### 💡 HTTP 요청 - 기본, 헤더 조회

<script src="https://gist.github.com/ShinDongHun1/3c9be30f16e5bdfe948bfc83946a10c1.js"></script>

- ##### HttpMethod : HTTP 메서드를 조회한다.(GET, POST 등)

- ##### Locale : Locale 정보를 조회한다.

- ##### @RequestHeader MultiValueMap<String, String> headerMap : 모든 HTTP 헤더를 MultiValueMap 형식으로 조회한다.

- ##### @RequestHeader("host") : String host 특정 HTTP 헤더를 조회한다. 

- ##### @CookieValue(value = "myCookie", required = false) String cookie :  특정 쿠키를 조회한다.

#### 🔎참고 MultiValueMap

- MAP과 유사한데, 하나의 키에 여러 값을 받을 수 있다.
- HTTP header, HTTP 쿼리 파라미터와 같이 하나의 키에 여러 값을 받을 때 사용한다.

<br/>

##### 🔎참고 

##### @Conroller 의 사용 가능한 파라미터 목록은 다음 공식 메뉴얼에서 확인할 수 있다.

> [https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annarguments](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annarguments) 

##### @Conroller 의 사용 가능한 응답 값 목록은 다음 공식 메뉴얼에서 확인할 수 있다. 

> [https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annreturn-types](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annreturn-types)

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 1편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-1/dashboard)

##### [https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annarguments](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annarguments) 

##### [https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annreturn-types](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annreturn-types)
