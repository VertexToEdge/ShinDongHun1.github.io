---
title:  "스프링 MVC 구조 - DispatcherServlet"
excerpt: "스프링 MVC 공부하기[6]"
date:   2021-10-13 17:30:00 
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-13T17:30:00
---

<br/>

## 💡 스프링 MVC 구조

<br/>

##### [스프링 MVC 실습 4- 프론트 컨트롤러 사용](https://shindonghun1.github.io/mvc/%EC%8A%A4%ED%94%84%EB%A7%81-MVC-%EC%8B%A4%EC%8A%B5-4/)에서 만들었던 구조

![image-20211013232457896](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211013232457896.png)

<br/>

##### 스프링 MVC 구조

![image-20211013232405510](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211013232405510.png)

##### DispatcherServlet : 프론트 컨트롤러

<br/>

## 💡 DispatcherServlet

##### 스프링 MVC도 프론트 컨트롤러 패턴으로 구현.

##### 스프링 MVC의 프론트 컨트롤러가 DispatcherServlet이다.

<br/>

#### 🔎등록

- ##### DispatcherServlet도 부모 클래스에서 HttpServlet을 상속 받아서 사용한다.
- ##### 스프링부트는 DispatcherServlet을 서블릿으로 자동 등록하면서, **모든 경로**에 대해서 매핑한다

<script src="https://gist.github.com/ShinDongHun1/e794ee8c48999af2e59b5da5dd5dea90.js"></script>

<br/>

<br/>

#### 🔎자료 - [스프링 MVC 1편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-1/dashboard)

<br/>

