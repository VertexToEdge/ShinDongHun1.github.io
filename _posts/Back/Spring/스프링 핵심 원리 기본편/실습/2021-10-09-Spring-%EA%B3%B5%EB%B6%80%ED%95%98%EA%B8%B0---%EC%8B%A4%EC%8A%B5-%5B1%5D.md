---
title:  "IoC, DI 이해를 위한 예제 코드 만들기"
excerpt: "예제 만들기"
date:   2021-10-09 20:33:00 +0900
header:
  teaser: /assets/images/spring.png

categories: javaSpring
tags:
  - Java
  - Spring
last_modified_at: 2021-12-04T00:33:00-05:00


---

<br/>

## 프로젝트 생성

https://start.spring.io 로 이동

- 프로젝트 선택 

  Project: Gradle Project 

  Spring Boot: (영어)가 붙어있지 않은 가장 최신 버전

  Language: Java 

  Packaging: Jar 

  Java: 11 

- Project Metadata 

  group: hello 

  artifact: core 

  Dependencies: 선택하지 않는다.

<br/>

<br/>

## 요구사항 설계하기

- 회원 
  - 기능- 가입, 조회
  - 등급 - BASIC, VIP
  - 회원 데이터를 저장하는 방식을 아직 결정하지 못하였다.
- 주문
  - 회원은 상품 주문 가능
  - 회원 등급에 따라 할인을 적용할 수 있다.
  - 할인 정책은 변경 가능성이 높다.

##### <br/>

<br/>

## 개발하기

### 회원 기능 개발

#### - Grade

<script src="https://gist.github.com/ShinDongHun1/a25f68d36d4f5caa2fbb137129105d4b.js"></script>

#### <br/> - Member

<script src="https://gist.github.com/ShinDongHun1/0357fc587bf16f91a36facbdbadf3eb8.js"></script>

#### <br/>

#### <br/> - MemberRepository 

<script src="https://gist.github.com/ShinDongHun1/54f4022431e2ebbb5e95874c4e55915b.js"></script>

####  <br/>- MemoryMemberRepository

<script src="https://gist.github.com/ShinDongHun1/b0c4879d6e9ad7cb9e0662c2fefff0a5.js"></script>

#### <br/>

#### <br/>- MemberService 

<script src="https://gist.github.com/ShinDongHun1/b76bae6226a2d1bebe1977221d45c5d0.js"></script>

#### <br/>- MemberServiceImpl

<script src="https://gist.github.com/ShinDongHun1/604a41ee71b1fadb40cd823019cdbd8e.js"></script>

<br/>

#### 회원 기능 설계의 문제점

- 저장소를 다른 저장소로 변경할 때, 아래 코드를 변경해 주어야 한다.

  ```java
  private final MemberRepository memberRepository =
          new MemoryMemberRepository();
  ```

- **즉 OCP와 DIP 모두를 위반하였다.**

<br/>

<br/>

## 주문과 할인 기능 개발

#### - DiscountPolicy

<script src="https://gist.github.com/ShinDongHun1/233969ee261259c220ca4489328cffd5.js"></script>

#### <br/>- FixDiscountPolicy

<script src="https://gist.github.com/ShinDongHun1/2f796ed4d0f350ba68673f1964ac2ed2.js"></script>
#### <br/>- Order 

<script src="https://gist.github.com/ShinDongHun1/0eafb1f6c399ff74a6895546d45edf15.js"></script>

#### <br/>- OrderService 

<script src="https://gist.github.com/ShinDongHun1/cd12dedba09e4f54e46cc807b95aa8ac.js"></script>

#### <br/>- OrderServiceImpl

<script src="https://gist.github.com/ShinDongHun1/6d7b9c7d1ca0a5a610ba6bf80ca8c118.js"></script>

<br/>

<br/>

#### 주문 기능 설계의 문제점

- 회원 저장소를 변경할 때는 물론, 할인 정책을 변경할 때 아래 코드를 변경해 주어야 한다.

  ```java
  private final DiscountPolicy discountPolicy 
  						= new FixDiscountPolicy();
  ```

- **즉 OCP와 DIP 모두를 위반하였다.**

<br/>

<br/>

## 새로운 할인 정책 개발

#### <br/>- RateDiscountPolicy 

<script src="https://gist.github.com/ShinDongHun1/dbe87bb9c769473b05b776f6fa59d2a3.js"></script>

##### 위 새로운 할인 정책을 코드에 적용시켜보자.

#### - OrderServiceImpl  - 새로운 할인 정책 적용

<script src="https://gist.github.com/ShinDongHun1/54ff144bbdc839ef5d8e3fed7bdc2a33.js"></script>

<br/>

#### 문제점 발견 

- 다형성도 활용하고, 인터페이스와 구현 객체를 분리했다. OK 

- DIP : 주문서비스 클라이언트( OrderServiceImpl )는 추상(인터페이스) 뿐만 아니라 구체(구현) 클래스에도 의존하고 있다. 

  - 추상(인터페이스) 의존: DiscountPolicy 

  - 구체(구현) 클래스: FixDiscountPolicy , RateDiscountPolicy

- OCP : 지금 코드는 기능을 확장해서 변경하면, 클라이언트 코드에 영향을 준다! 따라서 OCP를 위반한다.

<br/>

#### 해결 방법

- ##### 인터페이스에만 의존하도록 설계를 변경하자

<script src="https://gist.github.com/ShinDongHun1/435021df5f8ff5aa1af2c31ae68331b4.js"></script>

그런데 구현체가 없는데 어떻게 코드를 실행해야 할까?

![image-20211009202005776](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211009202005776.png)

이렇게 오류가 발생한다.

#### 해결방법 

- 이 문제를 해결하려면 누군가가 클라이언트인 OrderServiceImpl 에 DiscountPolicy 의 구현 객체를 대신 생성하고 주입해주어야 한다.
- 후에 가서 배우겠지만, 이것이 스프링이 제공하는 기술인 의존성 주입(DI)이다. 
- 우선은 스프링을 사용하지 않고 해결해보자.

<br/>

<br/>

## AppConfig 생성

- ##### 애플리케이션의 전체 동작 방식을 구성(config)하기 위해, 구현 객체를 생성하고, 연결하는 책임을 가지는 별도의 설정 클래스인 AppConfig를 만들자

#### <br/>MemberServiceImpl 변경하기

<script src="https://gist.github.com/ShinDongHun1/65efcd5312276fe878e1c813b9909122.js"></script>

이렇게 생성자를 통해 만들어지도록 변경하였다.

#### <br/>OrderServiceImpl 변경하기

<script src="https://gist.github.com/ShinDongHun1/c22ca6d1bb9f9a4573423660a49c24ab.js"></script>

<br/>

<br/>

#### - AppConfig

<script src="https://gist.github.com/ShinDongHun1/804fc291de8ad88c5236403e54e3e6d7.js"></script>

이렇게 되면, AppConfig는 MemberServiceImpl과 OrderServiceImpl에  **의존성을 주입**해주며

##### MemberServiceImpl과 OrderServiceImpl 는 DIP와 OCP를 지킬 수 있어진다.

실제 사용은 

```java
AppConfig appConfig = new AppConfig();
//MemberService memberService = new MemberServiceImpl();
MemberService memberService = appConfig.memberService();
```

이렇게 사용해주면 된다.

#### - AppConfig 리펙터링

<script src="https://gist.github.com/ShinDongHun1/979c5db631b9e08fb929898084fee62e.js"></script>

<br/>

<br/>

## 스프링을 사용하여 변경하기

[IoC, DI](https://shindonghun1.github.io/javaspring/IoC,-DI/)를 보고 와주세여

<script src="https://gist.github.com/ShinDongHun1/094daf07381198b26aa0eb0915fb5715.js"></script>

- **@Configuration : 구성 정보라는것을 표시**

- **@Bean: 스프링 컨테이너에 등록됨**

<br/>

사용은 

```java
ApplicationContext ac  = new AnnotationConfigApplicationContext(AppConfig.class);

MemberService memberService = ac.getBean("memberService", MemberService.class);
```

<br/>

<br/>

### 📔 Reference

##### [인프런 - 스프링 핵심 원리 -기본편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B8%B0%EB%B3%B8%ED%8E%B8/dashboard)
