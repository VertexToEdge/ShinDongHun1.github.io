---
title:  "로그인 처리 1 - 쿠키 사용"
excerpt: "스프링 MVC 공부하기[18]"
date:   2021-10-16 19:00:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-16T19:00:00

---

<br/>

## 💡 쿠키를 사용하여 로그인 처리

#### 쿠키를 통해 로그인의 상태 유지하기

![image-20211016182519324](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211016182519324.png)

![image-20211016182538867](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211016182538867.png)

![image-20211016182608424](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211016182608424.png)

##### 쿠키에는 영속 쿠키와 세션 쿠키가 있다

- ##### 영속 쿠키 : 만료 날짜를 입력하면 해당 날짜까지 쿠키 유지

- ##### 세션 쿠키 : 만료 날짜를 생략하면 브라우저 종료시까지만 유지

##### 브라우저 종료 시 로그아웃이 되길 기대하므로, 우리가 필요한 것은 세션 쿠키이다.

<br/>

#### 🔎 세션 쿠키 생성

##### 로그인 성공 시 세션 쿠키를 생성해보자.

<script src="https://gist.github.com/ShinDongHun1/0302d92137a8fe629576f3eedbec2da8.js"></script>

```java
Cookie isCookie = new Cookie("memberId",String.valueOf(member.getId()));
response.addCookie(isCookie);
```

위 코드를 통해 쿠키를 생성해 주었다.

<br/>

#### 🔎로그아웃

<script src="https://gist.github.com/ShinDongHun1/8742c6417f423eee8ecb5fa37e59e388.js"></script>

##### 다음처럼 쿠키의 MaxAge를 0으로 설정하면 쿠키를 없앨 수 있다.

<br/>

#### 🔎 로그인 한 사용자만 들어올 수 있는 페이지 만들기

<script src="https://gist.github.com/ShinDongHun1/19c2ae2be226386ad823c3e5d8bf9a29.js"></script>

다른 코드들은 볼 필요 없이, **@CookieValue(name = "memberId") Long memberId**를 통해 이름이 memberId인 쿠키가 있으면 해당 페이지를 보여주게 만든다.

사실 위에서는 쿠키를 임의로 생성해서 서버에 요청을 보낼 수 있기 때문에, 쿠키에 들어있는 memberId의 값이 실제 존재하는 것인지에 대한 검증하는 과정이 있어야 하지만, 일단은 공부용 예제이므로 단순하게 만들었다.

쿠키가 없으면 Bad Request가 발생하며, 접근할 수 없게 된다. (예외처리는 후에 배우도록 하겠다.)

<br/>

### 💡 쿠키를 사용한 로그인 방식의 보안 문제

#### ☀️ 쿠키 값은 임의로 변경할 수 있다

- 클라이언트가 쿠키를 강제로 변경하면 다른 사용자가 된다.
- 실제 웹브라우저 개발자모드 -> Application -> Cookie 변경으로 확인할 수 있다

#### ☀️ 쿠키에 보관된 정보는 훔쳐갈 수 있다

- 만약 쿠키에 개인정보나, 신용카드 정보가 들어있다면?
- 이 정보가 웹브라우저에도 보관되고, 네트워크 요청마다 계속 클라이언트에서 서버로 전달된다.
- 쿠키의 정보로 인해 나의 로컬 PC가 털릴수도 있고, 네트워크 전송 구간에서 쿠키가 털릴수도 있다.

#### ☀️ 해커가 쿠키를 한 번 훔쳐가면 평생 사용할 수 있다

- 해커가 쿠키를 훔쳐가서 그 쿠키로 악의적인 요청을 계속 시도할 수 있다.

<br/>

### 🔎 대안

- 쿠키에 중요한 값을 노출하지 않고, 사용자 별로 예측 불가능한 임의의 토큰을 노출하고, 서버에서 토큰과 사용자 id를 매핑해서 인식한다. 그리고 서버에서 토큰을 관리한다.
- 토큰은 해커가 임의의 값을 넣어도 찾을 수 없도록 예상 불가능 해야한다.
- 해커가 토큰을 털어가도 시간이 지나면 사용할 수 없도록 서버에서 해당 토큰의 만료시간을 짧게(예 30분) 유지한다. 또는 해킹의 의심되는 경우 서버에서 해당 토큰을 강제로 제거하면 된다.

#### => 세션을 도입하면 모두 해결 가능하다.

<br/>

<br/>

### 📔 Reference

#####  [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)