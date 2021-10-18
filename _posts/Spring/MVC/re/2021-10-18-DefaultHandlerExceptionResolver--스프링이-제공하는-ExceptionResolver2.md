---
title:  "DefaultHandlerExceptionResolver- 스프링이 제공하는 ExceptionResolver2"
excerpt: "스프링 MVC 공부하기[30]"
date:   2021-10-18 15:40:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-18T15:40:00


---

<br/>

### 💡 스프링 부트가 기본으로 제공하는 ExceptionResolver는 다음과 같다.

##### 🔎HandlerExceptionResolverComposite에 다음 순서로 등록

1. ##### ExceptionHandlerExceptionResolver

2. ##### ResponseStatusExceptionResolver -> HTTP 응답 코드 변경

3. ##### DefaultHandlerExceptionResolver -> 스프링 내부 예외 처리

<br/>

<br/>

### 🌌 DefaultHandlerExceptionResolver

##### 스프링 내부에서 발생하는 스프링 예외를 해결한다.

대표적으로 파라미터 바인딩 시점에 타입이 맞지 않으면 내부에서 TypeMismatchException이 발생하는데, 이 경우 예외가 발생했기 때문에 그냥 두면 서블릿 컨테이너까지 오류가 올라가고, 결과적으로 500 오류가 발생한다.

그러나 파라미터 바인딩은 대부분 클라이언트가 HTTP 요청 정보를  잘못 호출해서 발생하는 문제이다. 이런 경우 상태코드 400을 써야한다.

<br/>

##### DefaultHandlerExceptionResolver.handleTypeMismatch 를 보면 다음과 같은 코드를 확인할 수 있다.

##### response.sendError(HttpServletResponse.SC_BAD_REQUEST) 

##### 결국 response.sendError() 를 통해서 문제를 해결한다.

##### sendError(400) 를 호출했기 때문에 WAS에서 다시 오류 페이지( /error )를 내부 요청한다

<br/>

#### 🔎ApiExceptionController - 추가

```java
@GetMapping("/api/default-handler-ex")
public String defaultException(@RequestParam Integer data) {
	return "ok";
}
```

<br/>

<br/>

#### 🔎 자료 - [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

<br/>

