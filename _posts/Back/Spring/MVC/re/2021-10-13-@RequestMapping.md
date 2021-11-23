---
title:  "@RequestMapping"
excerpt: "스프링 MVC 공부하기[8]"
date:   2021-10-13 17:32:00 
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-13T17:32:00

---

<br/>

## 💡 @RequestMapping

##### 스프링은 @RequestMapping 애노테이션을 사용하는 컨트롤러를 제공한다.

##### 앞서 보았듯이 가장 스프링에서 우선순위가 가장 높은 핸들러 매핑과 핸들러 어댑터는 RequestMappingHandlerMapping , RequestMappingHandlerAdapter 이다. 

<br/>

<br/>

### 🔎 예시

```java
 @RequestMapping("/hello-basic")
```

- ##### /hello-baisc : URL 호출이 오면 이 메서드가 실행되도록 매핑한다.

- ##### 대부분의 속성을 배열로 제공하므로 다중 설정이 가능하다. {"/hello", "/member"} 

- ##### @RequestMapping 에 method 속성으로 HTTP 메서드를 지정할 수 있다.

  - 축약 가능
  - @GetMapping , @PostMapping , @PutMapping , @DeleteMapping , @PatchMapping

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 1편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-1/dashboard)
