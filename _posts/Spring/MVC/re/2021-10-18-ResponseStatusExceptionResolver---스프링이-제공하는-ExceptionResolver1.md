---
title:  "ResponseStatusExceptionResolver - 스프링이 제공하는 ExceptionResolver1"
excerpt: "스프링 MVC 공부하기[29]"
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

### 💡 스프링 부트가 기본으로 제공하는 ExceptionResolver는 다음과 같다.

##### 🔎HandlerExceptionResolverComposite에 다음 순서로 등록

1. ##### ExceptionHandlerExceptionResolver

2. ##### ResponseStatusExceptionResolver

3. ##### DefaultHandlerExceptionResolver -> 우선순위 가장 낮다.

<br/>

<br/>

### 🌌 ResponseStatusExceptionResolver

##### 예외에 따라서 HTTP 상태 코드를 지정해주는 역할을 한다.

#### 🔎 다음 두 가지 경우를 처리한다

- ##### @ResponseStatus 가 달려있는 예외

- ##### ResponseStatusException 예외

<br/>

#### 1. @ResponseStatus 가 달려있는 예외

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

#### 2. ResponseStatusException

##### @ResponseStatus 는 개발자가 직접 변경할 수 없는 예외에는 적용할 수 없다. (애노테이션을 직접 넣어야 하는데, 내가 코드를 수정할 수 없는 라이브러리의 예외 코드 같은 곳에는 적용할 수 없다.)
추가로 애노테이션을 사용하기 때문에 조건에 따라 동적으로 변경하는 것도 어렵다.

##### 이때는 ResponseStatusException 예외를 사용하면 된다.

<br/>

##### 🔎 ApiExceptionController - 추가

```java
@GetMapping("/api/response-status-ex2")
public String responseStatusEx2() {
    throw new ResponseStatusException(HttpStatus.NOT_FOUND, "error.bad", new IllegalArgumentException());
}
```

<br/>

<br/>

#### 🔎 자료 - [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

<br/>