---
title:  "Spring 관련 용어 정리"
excerpt: "내가 공부하며 헷갈렸고 어려웠었던 용어 정리"
date:   2021-09-18 01:16:00 +0900
header:
  teaser: /assets/images/spring.png

categories: javaSpring
tags:
  - Java
  - Spring
  - 용어
last_modified_at: 2021-09-18T01:16:00-05:00



---

<br/>



### **AOP**

**Aspect Oriented Programming**의 약자로 **관점 지향 프로그래밍**이라고 불린다.<br/>**관점 지향**은 어떤 로직을 기준으로 **핵심적인 관점**, **부가적인 관점**으로 나누어 보고 그 관점을 기준으로 각각 **모듈화**하겠다는 것이다. <br/>여기서 모듈화란 어떤 **공통된 로직이나 기능을 하나의 단위로 묶는 것**이다.

<br/><br/>

### **트랜잭션** 

**데이터베이스의 상태를 변환**시키는 하나의 논리적 기능을 수행하기 위한 **작업의 단위** 또는 한꺼번에 모두 수행되어야 할 **일련의 연산**들을 의미한다.

<br/>

<br/>

### **JDBC** 

**Java DataBase Connectivity**의 약자로 해석 그대로 자바에서 데이터베이스에 연결 및 작업을 하기 위한 자바 API이다

<br/>

<br/>

### **ORM** 

**Object Relational Mapping**의 약자로 관계형 데이터베이스의 데이터와 객체를 매핑해주는것을 말한다.

<br/><br/>

### **JPA** 

**Java Persistent API**의 약자로 자바 ORM 기술에 대한 API표준 명세를 의미한다. **ORM을 사용하기 위한 인터페이스들을 모아둔 것**이며, JPA를 사용하기 위해서는 **JPA를 구현한** **Hibernate,** EclipseLink, DataNucleus 같은 **ORM 프레임워크**를 사용해야 합니다.(대부분 Hibernate를 사용한다)

<br/><br/>

### **Java EE** 

**엔터프라이즈 에디션**의 자바 플렛폼.

**Java Platform Enterprise Edition**의 약자로 서버측 자바 애플리케이션을 위한 산업 표쥰이다. EJB는 이에 포함되며, 분산 애플리케이션을 지원하는 컴포넌트 기반의 객체이다.