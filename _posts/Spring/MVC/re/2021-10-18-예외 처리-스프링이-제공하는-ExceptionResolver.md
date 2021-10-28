---
title:  "스프링이 제공하는 ExceptionResolver"
excerpt: "DefaultHandlerExceptionResolver ,ResponseStatusExceptionResolver에 대해서"
date:   2021-10-18 15:10:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-18T15:10:00

---

<br/>

## 💡 스프링 부트가 기본으로 제공하는 ExceptionResolver

#### ExceptionHandlerExceptionResolver (우선순위 1)

- ##### @ExceptionHandler를 처리한다. ([@ExceptionResolver](https://shindonghun1.github.io/mvc/@ExceptionResolver-%EC%8A%A4%ED%94%84%EB%A7%81%EC%9D%B4-%EC%A0%9C%EA%B3%B5%ED%95%98%EB%8A%94-ExceptionResolver3/))

#### ResponseStatusExceptionResolver  (우선순위 2)

- ##### HTTP 상태 코드를 지정해준다

#### DefaultHandlerExceptionResolver (우선순위 3)

- ##### 스프링 내부 기본 예외를 처리한다

<br/>

<br/>

## 💡 ResponseStatusExceptionResolver

##### 예외에 따라서 <span style="color:orange">HTTP 상태 코드를 지정해주는 역할</span>을 한다.

#### 🔎 다음 두 가지 경우를 처리한다

- ##### @ResponseStatus 가 달려있는 예외

- ##### ResponseStatusException 예외

<br/>

<br/>

### 1. @ResponseStatus 가 달려있는 예외

<script src="https://gist.github.com/ShinDongHun1/51d20137dd26a5ac7a2231c73bcb2f0d.js"></script>

<br/>

##### 🔎 메시지 기능

##### reason 을 MessageSource 에서 찾는 기능도 제공한다. reason = "error.bad"

```java
//@ResponseStatus(code = HttpStatus.BAD_REQUEST, reason = "잘못된 요청 오류")
@ResponseStatus(code = HttpStatus.BAD_REQUEST, reason = "error.bad")
public class BadRequestException extends RuntimeException {
}
```

##### 🔎messages.properties

```properties
error.bad=잘못된 요청 오류입니다. 메시지 사용
```

<br/>

<br/>

## 2. ResponseStatusException 예외

##### @ResponseStatus 는 개발자가 직접 변경할 수 없는 예외에는 적용할 수 없다. 

##### (애노테이션을 직접 넣어야 하는데, 내가 코드를 수정할 수 없는 라이브러리의 예외 코드 같은 곳에는 적용할 수 없다.)

##### 추가로 애노테이션을 사용하기 때문에 조건에 따라 동적으로 변경하는 것도 어렵다.

##### 이때 사용할 수 있는 것이 ResponseStatusException 예외이다.

<br/>

##### 🔎 ApiExceptionController에 추가

```java
@GetMapping("/api/response-status-ex2")
public String responseStatusEx2() {
    throw new ResponseStatusException(HttpStatus.NOT_FOUND, "error.bad", new IllegalArgumentException());
}
```

<br/>

<br/>

<br/>

## 💡 DefaultHandlerExceptionResolver

#### 스프링 내부에서 발생하는 스프링 예외를 해결한다.

#### 예시

##### 파라미터 바인딩 시점에 타입이 맞지 않으면 내부에서 TypeMismatchException이 발생한다.

##### 이 경우 예외가 발생했기 때문에 그냥 두면 서블릿 컨테이너까지 오류가 올라가고, 결과적으로 500 오류가 발생한다.

##### 그러나 파라미터 바인딩은 대부분 클라이언트가 HTTP 요청 정보를  잘못 호출해서 발생하는 문제이다. 이런 경우 상태코드 400을 써야한다.

<br/>

### ☀️ 코드로 확인해보자

##### DefaultHandlerExceptionResolver의 handleTypeMismatch 를 보면 다음과 같은 코드를 확인할 수 있다.

```java
response.sendError(HttpServletResponse.SC_BAD_REQUEST) 
```

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

> ##### /api/default-handler-ex?data=qqq

##### 이렇게 요청을 보내면 400 에러가 발생하는것을 볼 수 있다. 

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

<br/>