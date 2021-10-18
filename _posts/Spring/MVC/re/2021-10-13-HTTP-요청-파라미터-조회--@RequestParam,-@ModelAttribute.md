---
title:  "HTTP 요청 파라미터 조회 -@RequestParam, @ModelAttribute"
excerpt: "스프링 MVC 공부하기[11]"
date:   2021-10-13 19:38:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-13T17:38:00
---

<br/>

## 💡 HTTP 요청 파라미터 조회

#### **🔎 **쿼리 파라미터와 HTML Form 조회

##### 1. GET , 쿼리 파라미터 전송

##### 예시 : http://localhost:8080/request-param?username=hello&age=20

<br/>

##### 2. POST, HTML Form 전송

##### 예시

> ##### POST /request-param ...
>
> ##### content-type: application/x-www-form-urlencoded 
>
> 
>
> ##### username=hello&age=20

<br/>

##### GET 쿼리 파리미터 전송 방식이든, POST HTML Form 전송 방식이든 둘다 형식이 같으므로 구분없이 조회할 수 있다. 

##### 이것을 간단히 <span style="color:orange">요청 파라미터(request parameter) 조회</span>라 한다

<br/>

### 🌌 HTTP 요청 파라미터 조회 - @RequestParam

<script src="https://gist.github.com/ShinDongHun1/442526edb45d5ce92c80c891b2b7953a.js"></script>

- ##### @RequestParam의 name(value) 속성이 파라미터 이름으로 사용

- ##### HTTP 파라미터 이름이 변수 이름과 같으면 @RequestParam(name="xx") 생략 가능

- ##### String , int , Integer 등의 단순 타입이면 @RequestParam 도 생략 가능

<br/>

##### 🔎@RequestParam 생략 

<script src="https://gist.github.com/ShinDongHun1/b69c85af9c338a7793173064b3195ef7.js"></script>

#####  주의  

- ##### @RequestParam 애노테이션을 생략하면 스프링 MVC는 내부에서 @RequestParam의  required속성을 false로 적용한다. 

- ##### username=   :이렇게 쓴다면 null이 아니라 빈문자("")로 인식한다.

- ##### required 속성을 true로 설정한 후 defaultValue를 설정하면, 파라미터 값이 없어도 오류가 발생하지 않고 defaultValue값이 들어간다.

- ##### defaultValue 를 설정하면, 빈문자의 경우(username= )의 경우에도 defaultValue값이 설정된다.

<br/>

##### 🔎파라미터를 Map으로 조회하기 - requestParamMap

<script src="https://gist.github.com/ShinDongHun1/6e7b99071cf3482ade361a3219d3730f.js"></script>

##### 파라미터를 Map , MultiValueMap으로 조회할 수 있다.

- ##### 파라미터의 값이 1개가 확실하다면 Map을 사용해도 되지만 그렇지 않다면 MultiValueMap을 사용하자.

<br/>

<br/>

### 🌌 HTTP 요청 파라미터 조회 - @ModelAttribute

보통 개발을 하면 요청 파라미터를 받아서 필요한 객체를 만들고, 그 객체에 값을 넣어주는데

##### 스프링은 이 과정을 자동화해주는 @ModelAttribute란 기능을 제공한다.

<br/>

##### 우선 요청 파라미터를 바인딩 받을 객체를 만들자.

<script src="https://gist.github.com/ShinDongHun1/fe55ad3446b8729a0eaa458a27d2d4ba.js"></script>

- @Data는 롬복을 사용한 것이다.

<br/>

<script src="https://gist.github.com/ShinDongHun1/442bbf368a5a9fce16e19a7506ae1628.js"></script>

##### 스프링MVC는 @ModelAttribute 가 있으면 다음을 실행한다

- ##### HelloData 객체를 생성한다. 

- ##### 요청 파라미터의 이름으로 HelloData 객체의 프로퍼티를 찾는다. 그리고 해당 프로퍼티의 setter를 호출해서 파라미터의 값을 입력(바인딩) 한다. 

  - ##### 예) 파라미터 이름이 username 이면 setUsername() 메서드를 찾아서 호출하면서 값을 입력한다

  - ##### setter가 없으면 null값이 들어온다.

<br/>

#### 🔎 @ModelAttribute 는 생략할 수 있다. 

##### 그런데 @RequestParam 도 생략할 수 있으니 혼란이 발생할 수 있다.

##### 스프링은 해당 생략시 다음과 같은 규칙을 적용한다. 

- ##### String , int , Integer 같은 단순 타입 = @RequestParam 

- ##### 나머지 = @ModelAttribute (argument resolver 로 지정해둔 타입 외)

<br/>

#### 🔎 프로퍼티

- ##### 객체에 getUsername() , setUsername() 메서드가 있으면, 이 객체는 username 이라는 프로퍼티를 가지고 있다고 한다. 

- ##### username 프로퍼티의 값을 변경하면 setUsername() 이 호출되고, 조회하면 getUsername() 이 호출된다

<br/>

##### 🔎 바인딩 오류

-  age=abc 처럼 숫자가 들어가야 할 곳에 문자를 넣으면 BindException 이 발생한다. 이런 바인딩 오류를 처리하는 방법은 검증 부분에서 다룬다

<br/>

<br/>

## 🧾 정리

#### 🌌  쿼리 파라미터, HTML Form 조회

- #####  @RequestParam : 요청 파라미터의 값을 가져온다.

- ##### @ModelAttribute : 요청 파라미터의 값을 객체에 바인딩.

<br/>

<br/>

#### 🔎 자료 - [스프링 MVC 1편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-1/dashboard)

<br/>