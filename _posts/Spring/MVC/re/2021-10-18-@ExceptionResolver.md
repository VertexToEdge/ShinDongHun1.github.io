---
title:  "@ExceptionHandler"
excerpt: "API예외 처리- ExceptionResolver"
date:   2021-10-18 16:20:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-18T16:20:00

---

<br/>

## 💡 @ExceptionResolver

##### 스프링은 API 예외 처리 문제를 해결하기 위해 @ExceptionHandler 라는 애노테이션을 사용하는 매우 편리한 예외 처리 기능을 제공한다.

##### 이것을 처리하는것이 바로 ExceptionHandlerExceptionResolver 이다.

##### 스프링은 ExceptionHandlerExceptionResolver 를 기본으로 제공하고, 기본으로 제공하는 ExceptionResolver 중에 우선순위도 가장 높다. 

##### 실무에서 API 예외 처리는 대부분 이 기능을 사용한다.

<br/>

#### 🔎동작 원리

##### @ExceptionResolver 에노테이션을 선언하고, 해당 컨트롤러에서 처리하고 싶은 예외를 지정해주면 된다. 

##### 해당 컨트롤러에서 예외가 발생하면 이 메서드가 호출된다.

##### 참고로 지정한 예외 또는 그 예외의 자식 클래스를 모두 잡을 수 있다.



<br/>

### 🔎사용해보기

<script src="https://gist.github.com/ShinDongHun1/761d4e631e00afce4982a92ecc9928eb.js"></script>

##### 🔎 참고 - ErrorResult 는 직접 만들어준 클래스이다.

```java
@Data
@AllArgsConstructor
public class ErrorResult {
    private String code;
    private String message;
}
```

<br/>

#### 🔎 예외 생략

##### @ExceptionHandler에 예외를 생략할 수 있다. 생략하면 메서드 파라미터의 예외가 지정된다.

<br/>

#### 🔎 파리미터와 응답

##### @ExceptionHandler 에는 마치 스프링의 컨트롤러의 파라미터 응답처럼 다양한 파라미터와 응답을 지정할 수 있다.

##### 자세한 파라미터와 응답은 다음 공식 메뉴얼을 참고하자.

[https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annexceptionhandler-args](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annexceptionhandler-args)

<br/>

#### 🔎 실행 흐름

- ##### 컨트롤러를 호출한 결과 IllegalArgumentException 예외가 컨트롤러 밖으로 던져진다.

- ##### 예외가 발생했으로 ExceptionResolver 가 작동한다. 가장 우선순위가 높은ExceptionHandlerExceptionResolver 가 실행된다.

- ##### ExceptionHandlerExceptionResolver 는 해당 컨트롤러에 IllegalArgumentException 을 처리할 수 있는 @ExceptionHandler 가 있는지 확인한다.

- ##### illegalExHandle() 를 실행한다.

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

<br/>

