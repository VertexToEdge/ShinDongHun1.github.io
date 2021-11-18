---
title:  "템플릿 콜백 패턴"
excerpt: "템플릿 콜백 패턴"
date:   2021-11-18 15:00:00
header:
  teaser: /assets/images/spring.png

categories: GoF
tags:
  - GoF
last_modified_at: 2021-11-18T15:00:00


---

## 💡 템플릿 콜백 패턴

전략 패턴에서 Context는 변하지 않는 템플릿 역할을 하며, 변하는 부분은 파라미터로 넘어온 Strategy의 코드를 실행해서 처리했다. 

이렇게 다른 코드의 인수로서 넘겨주는 실행 가능한 코드를 콜백(callback)이라 한다.

<br/>

#### 정리

> 프로그램에서 콜백또는  콜에프터 한수는 다른 코드의 인수로서 넘겨주는 실행 가능한 코드를 말한다. 콜백을 넘겨받는 코드는 이 콜백을 필요에 따라 즉시 실행할 수도 있고, 아니면 나중에 실행할 수도 있다. (위키백과)

<br/>

#### 자바에서의 콜백

- 자바에서 실행 가능한 코드를 인수로 넘기려면 객체가 필요하다. 자바 8부터는 람다를 사용할 수 있다.

<br/>

#### 예제

[전략 패턴](https://shindonghun1.github.io/gof/%EC%A0%84%EB%9E%B5-%ED%8C%A8%ED%84%B4/)- > Context를 Template로, Strategy를 Callback으로 바꾸면 된다.

##### 즉 전략 패턴에서 Strategy를 필드가 아니라 매개변수로 주입받는 방법을 사용하는 방식을 템플릿 콜백 패턴이라 볼 수 있다.

<br/>

<br/>

#### 참고

템플릿 메서드 패던은 GoF 디자인 패턴은 아니지만 스프링에서 많이 사용하므로, 스프링에서만 따로 이렇게 부른다!

<br/>

## 📔 Reference

[인프런 - 스프링 핵심 원리 고급편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B3%A0%EA%B8%89%ED%8E%B8/dashboard)

