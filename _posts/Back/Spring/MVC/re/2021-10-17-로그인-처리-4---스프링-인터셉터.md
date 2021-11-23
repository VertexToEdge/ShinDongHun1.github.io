---
title:  "스프링 인터셉터"
excerpt: "스프링 인터셉터, 인터셉터를 사용한 로그인 처리"
date:   2021-10-17 20:01:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-17T20:01:00

---

<br/>

## 💡 스프링 인터셉터

필터가 서블릿이 제공하는 기술이라면, 스프링 인터셉터는 스프링MVC가 제공하는 기술이다. 둘다 웹과 관련된 공통 사항을 처리하지만, 적용되는 순서와 범위, 그리고 사용방법이 다르다.

<br/>

#### 🔎스프링 인터셉터 흐름

> ##### HTTP 요청 -> WAS -> 필터 -> 서블릿 -> 스프링 인터셉터 -> 컨트롤러

- ##### 스프링 인터셉터는 디스패처 서블릿과 컨트롤러 사이에서 컨트롤러 호출 직전에 호출된다.

<br/>

### 스프링 인터셉터 제한

> ##### HTTP 요청 -> WAS -> 필터 -> 서블릿 -> 스프링 인터셉터 -> 컨트롤러 //로그인 사용자
>
> ##### HTTP 요청 -> WAS -> 필터 -> 서블릿 -> 스프링 인터셉터 (적절하지 않은 요청이라 판단, <span style="color:red">컨트롤러 호출 X</span>)

<br/>

<br/>

####  🔎 HandlerInterceptor - 스프링 인터셉터 인터페이스

<script src="https://gist.github.com/ShinDongHun1/90870c1566c7344928d5f8b15cb42007.js"></script>

#### ☀️ 스프링의 인터셉터를 사용하려면 HandlerInterceptor 인터페이스를 구현하면 된다.

- ##### 인터셉터는 컨트롤러 호출 전( preHandle ),호출 후( postHandle ), 요청 완료 이후( afterCompletion )에 호출할 수 있다.


<br/>

![image-20211017184956816](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211017184956816.png)

#### 🔎 정상 흐름

- ##### preHandle : 컨트롤러 호출 전에 호출된다. (더 정확히는 핸들러 어댑터 호출 전에 호출된다.)
  
  - ##### **preHandle 의 응답값이 true 이면 다음으로 진행**하고, **false 이면 더는 진행하지 않는다.** false인 경우 나머지 인터셉터는 물론이고, **핸들러 어댑터도 호출되지 않는다.** 
- ##### postHandle : 컨트롤러 호출 후에 호출된다. (더 정확히는 핸들러 어댑터 호출 후에 호출된다.)
- ##### afterCompletion : 뷰가 렌더링 된 이후에 호출된다.

<br/>

#### 🔎 스프링 인터셉터 예외 상황

![image-20211017185108455](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211017185108455.png)

#### 예외가 발생시

- ##### **preHandle** : 컨트롤러 호출 전에 호출된다.

- ##### **postHandle** : 컨트롤러에서 예외가 발생하면 postHandle 은 호출되지 않는다.

- ##### **afterCompletion** : afterCompletion 은 항상 호출된다. 이 경우 예외( ex )를 파라미터로 받아서 어떤 예외가 발생했는지 로그로 출력할 수 있다.

  - ##### 그러나 preHandle의 응답값이 false이면, 나머지 인터셉터들과, 어댑터 모두 호출되지 않으므로, afterCompletion 도 호출되지 않는다

  - ##### 예외가 발생하면 postHandle() 는 호출되지 않으므로 예외와 무관하게 공통 처리를 하려면afterCompletion() 을 사용해야 한다.

<br/>

<br/>

#### 🔎 사용해보기

<script src="https://gist.github.com/ShinDongHun1/ab157020bef1b51c5efd5d796650ac1b.js"></script>

##### request.setAttribute(LOG_ID, uuid)

##### 서블릿 필터의 경우 지역변수로 해결이 가능하지만, 스프링 인터셉터는 호출 시점이 완전히 분리되어 있다. 

##### 따라서 preHandle 에서 지정한 값을 postHandle , afterCompletion 에서 함께 사용하려면 어딘가에 담아두어야 한다.

#####  LogInterceptor 도 싱글톤 처럼 사용되기 때문에 맴버변수를 사용하면 위험하다. 

##### 따라서 request 에 담아두었다. 

##### 이 값은 afterCompletion 에서 request.getAttribute(LOG_ID) 로 찾아서 사용한다.

<br/>

```java
if (handler instanceof HandlerMethod) {
    HandlerMethod hm = (HandlerMethod) handler; //호출할 컨트롤러 메서드의 모든 정보가 포함되어 있다.
}
```

<br/>

#### HandlerMethod

- 핸들러 정보는 어떤 핸들러 매핑을 사용하는가에 따라 달라진다. 

  스프링을 사용하면 일반적으로 @Controller , @RequestMapping 을 활용한 핸들러 매핑을 사용하는데, 이 경우 핸들러 정보로 HandlerMethod 가 넘어온다.

<br/>

#### ResourceHttpRequestHandler

- @Controller 가 아니라 /resources/static 와 같은 정적 리소스가 호출 되는 경우
  ResourceHttpRequestHandler 가 핸들러 정보로 넘어오기 때문에 타입에 따라서 처리가 필요하다.

<br/>

#### postHandle, afterCompletion

- 종료 로그를 postHandle 이 아니라 afterCompletion 에서 실행한 이유는, 예외가 발생한 경우
  postHandle 가 호출되지 않기 때문이다. afterCompletion 은 예외가 발생해도 호출 되는 것을 보장한다.

<br/>

<br/>

#### 🔎 WebConfig - 인터셉터 등록

<script src="https://gist.github.com/ShinDongHun1/f9745839f5d4764e994f7205820d8754.js"></script>

#### ☀️ WebMvcConfigurer 가 제공하는 addInterceptors() 를 사용해서 인터셉터를 등록할 수 있다.

- ##### registry.addInterceptor(new LogInterceptor()) : 인터셉터를 등록한다.
- ##### order(1) : 인터셉터의 호출 순서를 지정한다. 낮을 수록 먼저 호출된다.
- ##### addPathPatterns("/**") : 인터셉터를 적용할 URL 패턴을 지정한다.
- ##### excludePathPatterns("/css/\*\*", "/*.ico", "/error") : 인터셉터에서 제외할 패턴을 지정한다.

<br/>

#### 🔎 스프링의 URL 경로

##### 스프링이 제공하는 URL 경로는 서블릿 기술이 제공하는 URL 경로와 완전히 다르다. 

##### 더욱 자세하고, 세밀하게 설정할 수 있다.

#### PathPattern 공식 문서

![image-20211017191915473](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211017191915473.png)

##### 공식문서 - [https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/util/pattern/PathPattern.html](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/util/pattern/PathPattern.html)

##### 참고 블로그 - [https://velog.io/@roeniss/Path-Pattern](https://velog.io/@roeniss/Path-Pattern)

<br/>

<br/>

## 💡 스프링 인터셉터를 사용한 인증 체크

<script src="https://gist.github.com/ShinDongHun1/cdeca24a2ea9a7de0bb1dcfa54729fc6.js"></script>

<br/>

<script src="https://gist.github.com/ShinDongHun1/048074af79996ec4f5e7e6ac9de7aaea.js"></script>

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

<br/>
