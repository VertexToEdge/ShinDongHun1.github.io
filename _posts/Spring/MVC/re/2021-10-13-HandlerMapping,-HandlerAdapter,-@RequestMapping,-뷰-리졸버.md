---
title:  "HandlerMapping, HandlerAdapter, 뷰 리졸버"
excerpt: "스프링 MVC 공부하기[7]"
date:   2021-10-13 17:31:00 
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-13T17:31:00
---

<br/>

### 💡 HandlerMapping과 HandlerAdapter

##### 스프링 부트가 자동으로 등록하는 핸들러 매핑과 핸들러 어댑터

#### 🌌HandlerMapping(인터페이스)

> ##### 0 = RequestMappingHandlerMapping : 애노테이션 기반의 컨트롤러인 @RequestMapping에서 사용 
>
> ##### 1 = BeanNameUrlHandlerMapping : 스프링 빈의 이름으로 핸들러를 찾는다.

<br/>

#### 🌌HandlerAdapter(인터페이스)

> ##### 0 = RequestMappingHandlerAdapter : 애노테이션 기반의 컨트롤러인 @RequestMapping에서 사용 
>
> ##### 1 = HttpRequestHandlerAdapter : HttpRequestHandler 처리 
>
> 2 = SimpleControllerHandlerAdapter : Controller 인터페이스(애노테이션X, 과거에 사용) 처리

<br/>

<br/>

### 💡 뷰 리졸버

##### 스프링 부트는 InternalResourceViewResolver 라는 뷰 리졸버를 자동으로 등록하는데, 이때 application.properties 에 등록한 spring.mvc.view.prefix , spring.mvc.view.suffix 설정 정보를 사용해서 등록한다.

##### 🔎application.properties

```properties
spring.mvc.view.prefix=/WEB-INF/views/
spring.mvc.view.suffix=.jsp
```

<br/>

#### 스프링 부트가 자동 등록하는 뷰 리졸버

> 1 = BeanNameViewResolver : 빈 이름으로 뷰를 찾아서 반환한다. (예: 엑셀 파일 생성 기능에 사용) 
>
> 2 = InternalResourceViewResolver : JSP를 처리할 수 있는 뷰를 반환한다.

<br/>

<br/>

#### 🔎자료 - [스프링 MVC 1편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-1/dashboard)

<br/>