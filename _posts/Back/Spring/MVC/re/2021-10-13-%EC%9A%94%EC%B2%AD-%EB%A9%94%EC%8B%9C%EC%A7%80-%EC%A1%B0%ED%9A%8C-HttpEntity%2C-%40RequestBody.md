---
title:  "요청 메시지 조회-HttpEntity, @RequestBody"
excerpt: "스프링 MVC 공부하기[12]"
date:   2021-10-13 19:50:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-13T17:50:00

---

<br/>

### 💡 HTTP 요청 메시지 조회 - 단순 텍스트

##### HTTP message body 에 데이터를 직접 담아서 요청

- ##### 데이터 형식은 주로 JSON
- ##### HTTP API에서 주로 사용

<br/>

##### 요청 파라미터와 다르게 HTTP 메시지 바디를 통해 데이터가 직접 넘어오는 경우는 @RequestParam, @ModelAttribute를 사용할 수 없다(HTML Form 형식 제외)

<br/>

#### 🌌 HttpEntity 사용

<script src="https://gist.github.com/ShinDongHun1/35bb65d9511276949e08f4206dce5b22.js"></script>

- ##### HttpEntity: HTTP header, body 정보를 편리하게 조회 

  - ##### 메시지 바디 정보를 직접 조회 
  - ##### 요청 파라미터를 조회하는 기능과 관계 없음 @RequestParam X, @ModelAttribute X 

- ##### HttpEntity는 응답에도 사용 가능 

  - ##### 메시지 바디 정보 직접 반환 헤더 정보 포함 가능 view 조회X

<br/>

##### 🔎 HttpEntity 를 상속받은 다음 객체들도 같은 기능을 제공한다. 

- ##### RequestEntity 

  - ##### HttpMethod, url 정보가 추가, 요청에서 사용 

- ##### ResponseEntity 

  - ##### HTTP 상태 코드 설정 가능, 응답에서 사용 

  - ##### return new ResponseEntity("Hello World", responseHeaders, HttpStatus.CREATED)

<br/>

<br/>

### 🌌 @RequestBody 

<script src="https://gist.github.com/ShinDongHun1/1493e492f0a3d80ab1b376b9171658f0.js"></script>

#### @RequestBody

- @RequestBody 를 사용하면 HTTP 메시지 바디 정보를 편리하게 조회할 수 있다. 참고로 헤더 정보가 필요하다면 HttpEntity 를 사용하거나 @RequestHeader 를 사용하면 된다

- ##### 이렇게 메시지 바디를 직접 조회하는 기능은 요청 파라미터를 조회하는 @RequestParam , @ModelAttribute 와는 전혀 관계가 없다.

<br/>

#### @ResponseBody

- @ResponseBody 를 사용하면 응답 결과를 HTTP 메시지 바디에 직접 담아서 전달할 수 있다. 물론 이 경우에도 view를 사용하지 않는다.

<br/>

<br/>

## 💡 HTTP 요청 메시지 조회 - JSON

ObjectMapper를 통해 조회할 수 있지만, 그렇게 조회하는 방법은 생략하겠다.

<br/>

#### 🌌 @RequestBody - 객체 변환 사용

<script src="https://gist.github.com/ShinDongHun1/bab8be1ba22cc53327349332ac0bb060.js"></script>

##### @RequestBody 에 직접 만든 객체를 지정할 수 있다

#### @RequestBody는 생략 불가능

- 위의 경우에 생략하면 String, int와 같은 단순 타입이 아니므로 @ModelAttribute가 적용되어버린다.

<br/>

#### 🌌 requestBodyJsonV4 - HttpEntity 사용

<script src="https://gist.github.com/ShinDongHun1/7ee0ac7283060e4db725452075c00d8a.js"></script>

 HttpEntity를 사용해도 된다.

<br/>

#### 🌌 객체를 응답으로 보내기

<script src="https://gist.github.com/ShinDongHun1/a282b91cd053d99404591215b0d8baea.js"></script>

##### @ResponseBody 

- 응답의 경우에도 @ResponseBody 를 사용하면 해당 객체를 HTTP 메시지 바디에 직접 넣어줄 수 있다. 물론 이 경우에도 HttpEntity 를 사용해도 된다.

<br/>

##### @RequestBody 요청 

- ##### JSON 요청 -> HTTP 메시지 컨버터 -> 객체 

##### @ResponseBody 응답 

- ##### 객체 -> HTTP 메시지 컨버터 -> JSON 응답

<br/>

<br/>

## 🧾 정리

#### 🌌 요청 파라미터 vs HTTP 메시지 바디 

- ##### 요청 파라미터를 조회하는 기능: 
  - ##### @RequestParam , @ModelAttribute HTTP 

- ##### 메시지 바디를 직접 조회하는 기능: 

  - ##### @RequestBody

<br/>

#### 🌌 HTTP 요청 메시지 조회 - 단순 텍스트

- ##### @RequestBody 사용

<br/>

#### 🌌 HTTP 요청 메시지 조회 - JSON

- ##### @RequestBody - 객체 변환 사용

- 응답으로도 객체를 보낼 수 있음.

<br/>

#### 🌌@RequestBody는 생략 불가능

<br/>

<br/>

#### 🔎 자료 - [스프링 MVC 1편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-1/dashboard)

<br/>