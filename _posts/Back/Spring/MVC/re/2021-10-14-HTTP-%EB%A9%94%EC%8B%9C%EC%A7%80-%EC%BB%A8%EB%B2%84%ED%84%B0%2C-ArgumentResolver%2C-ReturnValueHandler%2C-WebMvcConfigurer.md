---
title:  "HTTP 메시지 컨버터, ArgumentResolver, ReturnValueHandler, WebMvcConfigurer"
excerpt: "스프링 MVC 공부하기[15]"
date:   2021-10-14 15:51:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-14T15:51:00


---

<br/>

## 💡 HTTP 메시지 컨버터

##### 요청 본문에서 메시지를 읽어 들이거나(@RequestBody), 응답 본문에 메시지를 작성할 때(@ResponseBody) 사용한다.

#### @ResponseBody를 사용시

- ##### HTTP 의 BODY에 문자 내용을 직접 반환

- ##### viewResolver 대신에 <span style="color:orange">HttpMessageConverter</span> 가 동작한다.

  - ##### 기본 문자처리 : StringHttpMessageConverter

  - ##### 기본 객체처리 : MappingJackson2HttpMessageConverter

  - ##### byte 처리 등등 : 기타 여러 HttpMessageConverter가 기본으로 등록되어 있음

<br/>

#### 스프링 MVC는 다음의 경우에 HTTP 메시지 컨버터를 적용한다.

- ##### HTTP 요청 : @RequestBody, HttpEntity(RequestEntity)

- ##### HTTP 응답 : @ResponseBody, HttpEntity(ResponseEntity)

<br/>

<br/>

### ☀️주요한 메시지 컨버터

- #### ByteArrayHttpMessageConverter : byte[] 데이터를 처리한다. 

  - 클래스 타입: byte[] , 미디어타입: \*/\* , 
  - 요청 예) @RequestBody byte[] data 
  - 응답 예) @ResponseBody return byte[] 쓰기 미디어타입 application/octet-stream

- ####  StringHttpMessageConverter : String 문자로 데이터를 처리한다. 

  - 클래스 타입: String , 미디어타입: \*/\* 
  - 요청 예) @RequestBody String data 
  - 응답 예) @ResponseBody return "ok" 쓰기 미디어타입 text/plain 

- ####  MappingJackson2HttpMessageConverter : application/json 

  - 클래스 타입: 객체 또는 HashMap , 미디어타입 application/json 관련 
  - 요청 예) @RequestBody HelloData data 
  - 응답 예) @ResponseBody return helloData 쓰기 미디어타입 application/json 관련

<br/>

##### 그렇다면 이 메시지 컨버터는 어디서 사용되는 것일까?

<br/>

#### ☀️메시지 컨버터의 사용

![image-20211014153701251](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211014153701251.png)

<br/>

<br/>

## 💡 ArgumentResolver

##### Spring Argument Resolver는 <span style="color:orange">Controller에 들어오는 파라미터를 가공</span> 하거나 (ex. 암호화 된 내용 복호화), 파라미터를 추가하거나 수정해야 하는 경우에 사용한다

##### 애노테이션 기반 컨트롤러를 처리하는 RequestMappingHandlerAdaptor 는 ArgumnetResolver를 호출해서 컨트롤러(핸들러)가 필요로 하는 다양한 파라미터의 값(객체)을 생성한다. 

그 후 컨트롤러를 호출하면서 값을 넘겨준다

<br/>

참고로 원한다면 HandlerMethodArgumentResolver 인터페이스를 확장해서 원하는 ArgumentResolver를 만들 수도 있다. (이후 로그인 예제에서 확인)

<br/>

## 💡 ReturnValueHandler - 응답 값 처리

##### HandlerMethodReturnValueHandler 를 줄여서 ReturnValueHandle 라 부른다.

##### ArgumentResolver 와 비슷한데, 이것은 **응답 값을 변환하고 처리**한다

<br/>

##### 참고 

##### 스프링은 10여개가 넘는 ReturnValueHandler 를 지원한다.

> 가능한 응답 값 목록은 다음 공식 메뉴얼에서 확인할 수 있다. 
>
> [https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annreturn-types](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annreturn-types)

<br/>

<br/>

## 💡 WebMvcConfigurer 

#### ☀️ 확장 

##### 스프링은 다음을 모두 인터페이스로 제공한다. 따라서 필요하면 언제든지 기능을 확장할 수 있다. 

- ##### HandlerMethodArgumentResolver 

- ##### HandlerMethodReturnValueHandler 

- ##### HttpMessageConverter

스프링이 필요한 대부분의 기능을 제공하기 때문에 실제 기능을 확장할 일이 많지는 않다. 

##### 🔎 기능 확장은 WebMvcConfigurer 를 상속 받아서 스프링 빈으로 등록하면 된다. 

실제 자주 사용하지는 않으니 실제 기능 확장이 필요할 때 WebMvcConfigurer 를 검색해보자

<br/>

<br/>

## 🧾 정리

#### ☀️  HTTP 메시지 컨버터는 HTTP요청, HTTP 응답 둘 다 사용된다.

#### ☀️ ArgumentResolver : 요청의 경우에 사용

#### ☀️ ReturnValueHandler : 응답의 경우에 사용

#### ☀️기능 확장의 경우 WebMvcConfigurer 를 상속 받아서 스프링 빈으로 등록하면 된다. 

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 1편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-1/dashboard)

##### [https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annreturn-types](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annreturn-types)

##### [Spring Argument Resovler](https://jaehun2841.github.io/2018/08/10/2018-08-10-spring-argument-resolver/#spring-argument-resolver)