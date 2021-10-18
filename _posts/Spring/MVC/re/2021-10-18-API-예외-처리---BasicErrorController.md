---
title:  "API 예외 처리 - BasicErrorController"
excerpt: "스프링 MVC 공부하기[28]"
date:   2021-10-18 14:01:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-18T14:01:00
---

<br/>

## 💡 API 예외 처리

##### 🔎 WebServerCustomizer - API응답 추가

<script src="https://gist.github.com/ShinDongHun1/db25247b3e84474272d06294b0159a14.js"></script>

<br/>

##### 🔎 ErrorPageController - API응답 추가

<script src="https://gist.github.com/ShinDongHun1/649f9180916d8d8d04e8a3dd39406a4f.js"></script>

다음과 같이 에러 페이지에 등록한 URI에 해당하는 요청을 처리하는 Controller를 만들어서 처리하면 된다.

<br/>

<br/>

## 🌌 스프링 부트 기본 오류 처리

##### 스프링 부트가 제공하는 BasicErrorController 코드를 보자.

##### 🔎 BasicErrorController 코드

```java
@RequestMapping(produces = MediaType.TEXT_HTML_VALUE)
public ModelAndView errorHtml(HttpServletRequest request, HttpServletResponse
response) {}
@RequestMapping
public ResponseEntity<Map<String, Object>> error(HttpServletRequest request) {}
```

##### 클래스에는 @RequestMapping으로 "/error" 경로가 등록되어 있고, 

##### /error 경로를 처리하는 두 개의 메소드 errorHtml(), error() 이 있다.

- ##### errorHtml() : produces = MediaType.TEXT_HTML_VALUE : 요청의 Accept 해더 값이 text/html 인 경우에 호출해서 view를 제공한다.

- ##### error() : 그외 경우에 호출되고 ResponseEntity 로 HTTP Body에 JSON 데이터를 반환한다.

<br/>

##### BasicErrorController를 확장하면 JSON 메시지도 변경할 수 있다. 그러나 이 다음에 설명할 @ExceptionHandler가 제공하는 기능을 대부분 사용하므로, 그냥 확장할 수 있다 정도로만 이해하자

<br/>

<br/>

#### 🔎 자료 - [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

<br/>

