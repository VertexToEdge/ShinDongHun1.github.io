---
title:  "HttpServletRequest"
excerpt: "스프링 MVC 공부하기[3]"
date:   2021-09-20 06:18:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-12T06:18:00-05:00
---

<br/>

## 💡 HttpServletRequest 역할

##### 서블릿은 개발자가 HTTP 요청 메세지를 편리하게 사용할 수 있도록 개발자 대신에 <span style="color:orange">**HTTP 요청 메시지를 파싱**</span> 

##### 결과를 **<span style="color:orange">HttpServletRequest</span>** 객체에 담아서 제공

<br/>

#### 🔎 HTTP 요청 메세지 정보

> ##### POST /save HTTP/1.1      //START LINE<br/>Host: localhost:8080       //HEADER<br/>Content-Type: application/x-www-form-urlencoded      //HEADER
>
> 
>
> ##### username=kim&age=20      //BODY

- **START LINE**
  - **HTTP 메소드 (GET, POST)**
  - **URL**
  - **쿼리 스트링**
  - **스키마, 프로토콜**
- **헤더**
- **바디**

##### 위 요청 메세지 정보들을 조회할 수 있다.

<br/>

### 💡 HttpServletRequest가 제공하는 추가 기능

#### ☀️ 임시 저장소 기능

##### 해당 HTTP 요청이 시작부터 끝날 때 까지 유지되는 임시 저장소 기능

- ##### 저장: request.setAttribute(name, value)

- ##### 조회: request.getAttribute(name)

#### ☀️ 세션 관리 기능

- ##### request.getSession(true) 

  - ##### false 이면 세션이 존재하지 않을 경우 새로 생성 x

  - ##### true 이면 세션이 존재하지 않을 경우 새로운 세션 생성

<br/>

<br/>

## 💡 HTTP 요청 데이터

#### HTTP 요청 데이터를 통해서 클라이언트가 서버에게 메세지를 전달하는 방법

#### 1. GET - 쿼리 파라미터

- ##### /url?username=shindonghun&age=22

- ##### 메세지 바디 없이, <span style="color:orange">URL의 쿼리 파라미터에 데이터를 포함</span>해서 전달

- ##### 검색 , 필터, 페이징 등에서 많이 사용하는 방식

<br/>

#### 2. POST - HTML Form

- ##### content-type: application/x-www.form.urlencoded

- ##### <span style="color:orange">메세지 바디</span>에 쿼리 파라미터 형식으로 전달 username=hello&age=20

- ##### 회원 가입, 상품 주문, HTML Form 사용

<br/>

#### 3. HTTP message body에 데이터를 직접 담아서 요청

- ##### **HTTP** API(Rest API)에서 주로 사용, JSON, XML, TEXT

- ##### 데이터 **형식은** 주로 **JSON** 사용

- ##### POST, PUT, PATCH

<br/>

#### 🔎참고 (content-type)

##### <span style="color:orange">content-type</span>은 <span style="color:orange">HTTP 메시지 바디의 데이터 형식</span>을 지칭하며

##### GET URL 쿼리 파라미터 형식으로 클라이언트에서 서버로 데이터를 전달할 때는 <span style="color:orange">HTTP 메시지 바디를 사용하지 않기 때문</span>에 <span style="color:orange">content-type이 없다</span>.

##### POST HTML Form 형식으로 데이터를 전달하면, HTTP 메시지 바디에 해당 데이터를 포함해서 보내기 때문에, 바디에 포함된 데이터가 어떤 형식인지 <span style="color:orange">content-type을 꼭 지정</span>해야 한다. 이렇게 <span style="color:orange">폼으로 데이터를 전송</span>하는 형식을 <span style="color:orange">application/x-www-form-urlencoded</span> 라 한다.

##### request.getParameter()는 <span style="color:orange">GET URL 쿼리 파라미터 형식</span>과, <span style="color:orange">POST HTML Form 형식</span> 둘 다 지원한다.

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 1편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-1/dashboard)
