---
title:  "ArgumentResolver 활용"
excerpt: "나만의 어노테이션 만들기"
date:   2021-10-17 20:51:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-17T20:51:00


---

<br/>

## 💡 ArgumentResolver 활용

<script src="https://gist.github.com/ShinDongHun1/26b68e43f3b5b99e35be393c9a05aa62.js"></script>

**@SessionAttribute(name = SessionConst.LOGIN_MEMBER , required = false)**를 바꿔보도록 하자.

<br/>

<br/>

#### 🔎 @Login 어노테이션 만들기

<script src="https://gist.github.com/ShinDongHun1/735005d1d0e72d55fb92700016a40ce0.js"></script>

##### @Target : 파라미터에 적용시킬 어노테이션이므로  ElementType.PARAMETER

##### @Retention: 리플렉션 등을 활용할 수 있도록 런타임까지 애노테이션 정보가 남아있음 (뭐라는지 모르겠다 일단 그냥 붙여주자)

<br/>

#### 🔎HandlerMethodArgumentResolver 구현

<script src="https://gist.github.com/ShinDongHun1/36ce546b3b2f132d77332ccf72fdf1d0.js"></script>

- ##### parameter.hasParameterAnnotation(Login.class) : 파라미터에 Login.class 의 어노테이션이 붙어있는가?

- ##### Member.class.isAssignableFrom(parameter.getParameterType()) : 해당 어노테이션이 붙어있는 파라미터가 Member가 지원 가능한 것인가?

##### 둘 다 만족하면 true 를 반환, true 가 반환되면 resolveArgument를 실행한다.

<br/>

#### 🔎addArgumentResolvers 오버라이드

<script src="https://gist.github.com/ShinDongHun1/aeda216dc1a368fad75b7ea37978e8ed.js"></script>

##### WebMvcConfigurer 를 구현한 후, addArgumentResolvers를 오버라이드 하여 해당 어노테이션을 추가하자.

<br/>

### 💡 어노테이션 적용하기

<script src="https://gist.github.com/ShinDongHun1/c8f1c57f4fa15ade30371adb6d525909.js"></script>

```java
 private ResponseEntity<?> showRecentPost(@Login Member member)  
```

다음과 같이 사용하면 된다.

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

<br/>
<br/>