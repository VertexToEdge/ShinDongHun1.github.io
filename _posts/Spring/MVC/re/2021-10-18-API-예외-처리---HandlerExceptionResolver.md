---
title:  "API 예외 처리 - HandlerExceptionResolver"
excerpt: "스프링 MVC 공부하기[28]"
date:   2021-10-18 15:00:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-18T15:00:00

---

<br/>

##### 🔎 참고

##### 예외가 발생해서 서블릿을 넘어 WAS까지 전달되면 HTTP 상태코드가 500으로 처리된다.

<br/>

## 💡 HandlerExceptionResolver

##### 컨트롤러 밖으로 던져진 예외를 해결하고, 동작 방식을 변경하고 싶으면 HandlerExceptionResolver 를 사용하면 된다. 줄여서 ExceptionResolver 라 한다.

<br/>

##### 🔎 ExceptionResolver  적용 전

![image-20211018141944749](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211018141944749.png)

<br/>

##### 🔎 ExceptionResolver  적용 후

![image-20211018142039955](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211018142039955.png)

<br/>

<br/>

## 🌌 HandlerExceptionResolver 구현

<script src="https://gist.github.com/ShinDongHun1/27f3767732197b39ef23032c878eb927.js"></script>

<br/>

#### 🔎 WebConfig 수정

```java
@Override
public void extendHandlerExceptionResolvers(List<HandlerExceptionResolver>resolvers) {
	resolvers.add(new MyHandlerExceptionResolver());
}
```

##### WebMvcConfigurer 를 구현하여 extendHandlerExceptionResolvers를 오버라이드 해서 사용할 수 있다.

<br/>

<br/>

## 🌌 HandlerExceptionResolver 활용

#### 🔎 UserException 정의

<script src="https://gist.github.com/ShinDongHun1/b79192d984cf0d640f2ba25ac8c22cc7.js"></script>

<br/>

#### 🔎 UserException을 발생시키는 컨트롤러 추가

<script src="https://gist.github.com/ShinDongHun1/c0e5f4d9e479a9ecc65afedc7cc1a640.js"></script>

<br/>

#### 🔎 HandlerExceptionResolver 구현

<script src="https://gist.github.com/ShinDongHun1/b660c4e429f86f17680766056d4870d4.js"></script>

<br/>

#### 🔎 WebConfig 에 등록

<script src="https://gist.github.com/ShinDongHun1/67c5794b92b74a6f733da750dc19d741.js"></script>

<br/>

### 🔎정리

ExceptionResolver 를 사용하면 컨트롤러에서 예외가 발생해도, ExceptionResolver에서 예외를 처리한다. 따라서 예외가 발생해도 서블릿 컨테이너까지 예외가 전달되지 않고, 스프링 MVC에서 예외 처리는 끝이 난다. 

##### 핵심은 예외를 이곳에서 모두 처리할 수 있다는 것이다.

<br/>

<br/>

#### 🔎 자료 - [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

<br/>

