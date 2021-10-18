---
title:  "@ControllerAdvice를 사용할 때 에러 메세지의 국제화"
excerpt: "해결법??? 뭐라하지 이거"
date:   2021-10-18 19:17:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-18T19:17:00

---

<br/>

### 🌌@ControllerAdvice를 사용할 때 에러 메세지의 국제화

##### 조금 찾아봤는데 찾기가 어려워서 일단 혼자서 만들어 보다가 성공하긴 했다.

<br/>

#### 우선 에러 코드부터 소개하겠다.

<br/>

#### 🔎 BaseException 

<script src="https://gist.github.com/ShinDongHun1/0d396580d374433538902aa78ca3b31d.js"></script>

##### 국제화를 적용할 에러들은 모두 BaseException을 구현하도록 만들었다.

<br/>

#### 🔎 BaseExceptionType 

<script src="https://gist.github.com/ShinDongHun1/0a6f309db930f9a4da50d6605b7340d1.js"></script>

##### BaseException을 구현한 객체들은, BaseExceptionType 을 가지고 있으며,  

##### BaseExceptionType 은 필드로 에러코드, HttpStatus, 에러 메세지를 가진다.

<br/>

#### 🔎 MemberException 

<script src="https://gist.github.com/ShinDongHun1/d14384da95a6b49411601c386276cdc1.js"></script>

##### MemberException 을 대표 예시로 들겠다. RuntimeException 을 상속받고, BaseException를 구현한다.

<br/>

#### 🔎 MemberExceptionType 

<script src="https://gist.github.com/ShinDongHun1/e0117c9fcc93b9eaf2305451e484a22a.js"></script>

##### MemberExceptionType 은 Enum 타입으로, 하나의 상수를 예시로 들자면

##### ALREADY_EXIST_USERNAME(1001, HttpStatus.CONFLICT,"ALREADY_EXIST_USERNAME")

- ##### 위와 같이 에러코드, HttpStatus, 에러 메세지를 지니고 있다.

<br/>

#### 🔎 ExControllerAdvice 

<script src="https://gist.github.com/ShinDongHun1/8b715d97cad93e182749ce61d0052999.js"></script>

##### ExControllerAdvice 는 @RestControllerAdvice가 붙어있으며, 이곳에서 예외를 처리한다.

```java
private final MessageSource messageSource;
```

##### 를 통해 MessageSource의 의존관계를 주입받아 사용한다.

##### 각각의 메소드들은 Locale을 매개변수로 전달받는데, 이는 에러 메세지의 국제화에 사용된다.

<br/>

##### makeResponseEntity를 보면 

```java
messageSource.getMessage(me.getExceptionType().getErrorMessage(), null, locale);
```



##### 를 통해 오류 메시지를 국제화 하는것을 볼 수 있다.

<br/>

#### 🔎 errors_kr.properties

<script src="https://gist.github.com/ShinDongHun1/44d546049eb7969f19737bc641f465c7.js"></script>

##### 위와 같이 Enum 의 에러 메세지(errorMessage)필드와 똑같은 값을 지정해주었다.(ALREADY_EXIST_USERNAME)

![image-20211018191542915](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211018191542915.png)

![image-20211018191550385](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211018191550385.png)



##### 잘 된다 :D