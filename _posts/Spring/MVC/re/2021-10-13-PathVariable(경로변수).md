---
title:  "PathVariable(경로변수)"
excerpt: "스프링 MVC 공부하기[9]"
date:   2021-10-13 19:33:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-13T17:33:00

---

<br/>

### 💡PathVariable(경로 변수) 사용

<script src="https://gist.github.com/ShinDongHun1/49f6477afc7af5fa0d5691a874620467.js"></script>

##### 최근 HTTP API는 다음과 같이 리소스 경로에 식별자를 넣는 스타일을 선호한다.

- ##### /mapping/<span style="color:orange">userA</span>
- ##### /users/<span style="color:orange">1</span>

- ##### @RequestMapping 은 <span style="color:orange">URL 경로를 템플릿화</span> 할 수 있는데, @PathVariable을 사용하면 매칭되는 부분을 편리하게 조회할 수 있다.

- ##### @PathVariable의 이름과 파라미터 이름이 같으면 생략할 수 있다.

  - 위의 예시에서는 data 대신 userId를 사용하면, ("userId") 생략이 가능하다

<br/>

#### ☀️ 다중 사용

<script src="https://gist.github.com/ShinDongHun1/3b7dac34a3768f0c134c0512276c1182.js"></script>

<br/>

#### ☀️ 특정 파라미터가 있거나 없는 조건을 추가 가능

파라미터로 추가 매핑 

- params="mode", 
- params="!mode" 
- params="mode=debug" 
- params="mode!=debug"
- params = {"mode=debug","data=good"} 

<script src="https://gist.github.com/ShinDongHun1/508e648e54c0727a1411c78739e8ed9f.js"></script>

<br/>

#### ☀️ 미디어 타입 조건 매핑 - HTTP 요청 Content-Type, consume

<script src="https://gist.github.com/ShinDongHun1/073f5ddeff78879fb61ce05a5a4219da.js"></script>

##### application/json 의 데이터만 받을 수 있음. 다른 형식이 오면 오류

<br/>

#### ☀️미디어 타입 조건 매핑 - HTTP 요청 Accept, produce

<script src="https://gist.github.com/ShinDongHun1/460a77ef67459bf7120aa596717bd85d.js"></script>

##### 요청의 Accept가 text/html 데이터를 받을 수 있어야 함. 그렇지 않으면 오류

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 1편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-1/dashboard)
