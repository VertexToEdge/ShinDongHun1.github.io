---
title:  "@ControllerAdvice - @ExceptionHandler를 더욱 편리하게 사용"
excerpt: "스프링 MVC 공부하기[32]"
date:   2021-10-18 14:33:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-18T14:33:00


---

<br/>

## 💡 @ControllerAdvice 

##### @ExceptionHandler 를 사용해서 예외를 깔끔하게 처리할 수 있게 되었지만, 정상 코드와 예외 처리 코드가 하나의 컨트롤러에서 섞여있다. 

####  @ControllerAdvice  또는 @RestControllerAdvice 를 사용하면 둘을 분리할 수 있다.

<br/>

#### 🔎사용

<script src="https://gist.github.com/ShinDongHun1/9dcdac5673c2e271fb2d9622e224f38d.js"></script>

<br/>

### ☀️ @ControllerAdvice

- ##### @ControllerAdvice 는 대상으로 지정한 여러 컨트롤러에 @ExceptionHandler , @InitBinder 기능을 부여해주는 역할을 한다.

- ##### <span style="color:red">@ControllerAdvice 에 대상을 지정하지 않으면 모든 컨트롤러에 적용</span>된다. (글로벌 적용)

- ##### @RestControllerAdvice 는 @ControllerAdvice 와 같고, @ResponseBody 가 추가되어 있다.

- ##### @Controller , @RestController 의 차이와 같다.



<br/>

### 대상 컨트롤러 지정 방법

```java
// Target all Controllers annotated with @RestController
@ControllerAdvice(annotations = RestController.class)
public class ExampleAdvice1 {}

// Target all Controllers within specific packages
@ControllerAdvice("org.example.controllers")
public class ExampleAdvice2 {}

// Target all Controllers assignable to specific classes
@ControllerAdvice(assignableTypes = {ControllerInterface.class, AbstractController.class})
public class ExampleAdvice3 {}
```

#### 참고

#### [스프링 공식 문서](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-anncontroller-advice) 

##### 스프링 공식 문서 예제에서 보는 것 처럼 특정 애노테이션이 있는 컨트롤러를 지정할 수 있고, 특정 패키지를 직접 지정할 수도 있다. 

##### 패키지 지정의 경우 해당 패키지와 그 하위에 있는 컨트롤러가 대상이 된다. 

##### 그리고 특정 클래스를 지정할 수도 있다.

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

##### [스프링 공식 문서](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-anncontroller-advice) 

<br/>

