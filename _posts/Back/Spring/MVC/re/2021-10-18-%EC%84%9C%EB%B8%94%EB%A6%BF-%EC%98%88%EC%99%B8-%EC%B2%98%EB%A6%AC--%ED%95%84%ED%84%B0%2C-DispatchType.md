---
title:  "예외 처리 - 필터, 인터셉터"
excerpt: "필터, 인터셉터의 중복 호출 방지"
date:   2021-10-18 01:01:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-18T01:01:00


---

<br/>

## 💡 서블릿 예외 처리 - 필터

##### 예외 발생과 오류 페이지 요청 흐름

> 1. ##### WAS(여기까지 전파) <- 필터 <- 서블릿 <- 인터셉터 <- 컨트롤러(예외발생)
>
> 2. ##### WAS `/error-page/500` 다시 요청 -> 필터 -> 서블릿 -> 인터셉터 -> 컨트롤러(/errorpage/500) -> View

<br/>

##### 오류가 발생하면 오류 페이지를 출력하기 위해 WAS 내부에서 다시 한 번 호출이 발생한다. 

##### <span style="color:orange">이때 필터, 서블릿, 인터셉터도 모두 다시 호출</span>된다. 

##### 그런데 로그인 인증 체크 같은 경우를 생각해보면, 이미 한 번 필터나, 인터셉터에서 로그인 체크를 완료했다. 

##### 따라서 서버 내부에서 오류 페이지를 호출한다고 해서 해당 필터나 인터셉트가 한번 더 호출되는 것은 매우 비효율적이다.

##### 결국 클라이언트로부터 발생한 정상 요청인지, 아니면 오류 페이지를 출력하기 위한 내부 요청인지 구분할 수 있어야 한다. 

##### 서블릿은 이런 문제를 해결하기 위해 **<span style="color:orange">DispatchType</span>**이라는 **추가 정보**를 제공한다.

<br/>

<br/>

### ☀️ DispatcherType

##### 필터는 이런 경우를 위해서 dispatcherType이라는 옵션을 준비했다.

##### 고객이 처음 요청하면 dispatcherType=REQUEST이다.

##### 이렇듯 서블릿 스펙은 실제 고객이 요청한 것인지, 서버가 내부에서 오류 페이지를 요청하는 것인지 DispatcherType으로 구분할 수 있는 방법을 제공한다.

<br/>

#### 🔎 javax.servlet.DispatcherType

```java
public enum DispatcherType {
	FORWARD,
	INCLUDE,
	REQUEST,
	ASYNC,
	ERROR
}
```

<br/>

##### ✍ DispatcherType

- ##### <span style="color:orange">REQUEST</span> : 클라이언트 요청

- ##### <span style="color:orange">ERROR </span>: 오류 요청

- ##### FORWARD : 서블릿에서 다른 서블릿이나 JSP를 호출할 때

- ##### INCLUDE : 서블릿에서 다른 서블릿이나 JSP의 결과를 포함할 때

- ##### ASYNC : 서블릿 비동기 호출

<br/>

<br/>

### 💡 오류 페이지 요청시에도 필터를 호출하는 방법

<script src="https://gist.github.com/ShinDongHun1/d5d97ffd6b4bf31664343df6c3c99cf7.js"></script>

```java
filterRegistrationBean.setDispatcherTypes(DispatcherType.REQUEST,DispatcherType.ERROR);
```

##### 이렇게 두 가지를 모두 넣으면 클라이언트 요청은 물론이고, 오류 페이지 요청시에도 필터가 호출된다.

##### 아무것도 넣지 않으면 기본값은 DispatcherType.REQUEST이다. 즉 클라이언트의 요청이 있는 경우에만 필터가 적용된다. 

<br/>

<br/>

## 💡 서블릿 예외 처리 - 인터셉터

##### 인터셉터는 서블릿이 제공하는 기능이 아니라 스프링이 제공하는 기능이다. 

##### 따라서 DispatcherType 과 무관하게 항상 호출된다.

##### 대신에 인터셉터는 다음과 같이 요청 경로에 따라서 추가하거나 제외하기 쉽게 되어 있기 때문에, 이러한 설정을 사용해서 오류 페이지 경로를 **<span style="color:orange">excludePathPatterns</span>** 를 사용해서 빼주면 된다.

<br/>

<br/>

### ☀️ 전체 흐름 정리

#### /hello 정상 요청

> ##### WAS(/hello, dispatchType=REQUEST) -> 필터 -> 서블릿 -> 인터셉터 -> 컨트롤러 -> View

<br/>

#### /error-ex 오류 요청

- ##### 필터는 setDispatcherTypes로 중복 호출 제거 (dispatchType=REQUEST)
- ##### 인터셉터는 경로 정보로 중복 호출 제거 (excludePathPatterns)

<br/>

1. ##### WAS(/error-ex, dispatchType=REQUEST) -> 필터 -> 서블릿 -> 인터셉터 -> 컨트롤러

2. ##### WAS(여기까지 전파) <- 필터 <- 서블릿 <- 인터셉터 <- 컨트롤러(예외발생)

3. ##### WAS 오류 페이지 확인

4. ##### WAS(/error-page/500, dispatchType=ERROR) -> 필터(x) -> 서블릿 -> 인터셉터(x) -> 컨트롤러(/error-page/500) -> View

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)