---
title:  "Spring 개념&용어 정리"
excerpt: "Spring 개념&용어 정리"
date:   2021-09-19 01:16:00 +0900
header:
  teaser: /assets/images/spring.png

categories: javaSpring
tags:
  - Java
  - Spring
  - 용어
last_modified_at: 2021-09-19T01:16:00-05:00



---

<br/>

<br/>

#### 목차

- **스프링**
- **Spring Boot**
- **의존관계**
- **DI (Dependency Injection) - 의존관계 주입**
- **IoC (Inversion of Control) - 제어의 역전**
- **IoC 컨테이너, DI 컨테이너**
- **스프링 컨테이너**
- **빈(Bean)**
- **싱글톤**
- **싱글톤 레지스트리**

<br/>

## <br/>💡 스프링

#### <span style="color:Orange">좋은 객체 지향 애플리케이션을 개발</span>할 수 있게 도와주는 <span style="color:Orange">프레임워크</span>.

백엔드를 개발하고 뭐 하고, 그런게 중요한게 아니다. 핵심을 객체 지향을 도와준다!<br/>좋은 객체 지향의 5가지 원칙 -SOLID

단 하나의 기술이 아닌 여러 기술들의 집합이다.

<br/>

<br/>

## 💡 Spring Boot

#### <span style="color:Orange">스프링의 여러 기술</span>들을 <span style="color:Orange">편하게 쓸 수 있게</span> 도와주는 <span style="color:Orange">프레임워크</span>.

<br/>

<br/>

## 💡 의존관계

#### <span style="color:Orange">한쪽의 변화가 다른 쪽에 영향</span>을 주는 것

#### A가 B를 의존한다 => B가 변하면 A에 영향을 미친다.

<br/>

<br/>

## 💡 DI (Dependency Injection) - 의존관계 주입

#### <span style="color:Orange">의존하는 객체</span>를 직접 생성하는 것이 아니라, <span style="color:Orange">외부에서 생성한 후 주입</span>하는 것.

#### 3가지 조건이 필요

- ##### 클래스 모델이나 코드에는 <span style="color:Orange">런타임(실행) 시점의 의존관계가 드러나지 않는다</span>. (= 정적인 클래스 의존관계가 아니다)(= 동적인 객체 인스턴스 의존관계이다) => <span style="color:Orange">인터페이스에만 의존</span>하고 있어야 한다

- ##### <span style="color:Orange">런타임 시점</span>의 의존관계는 <span style="color:Orange">외부에서 결정</span>한다

- ##### <span style="color:Orange">외부</span>에서 <span style="color:Orange">실제 구현 객체(사용할 오브젝트에 대한 레퍼런스)</span>를 생성하고 클라이언트(사용할 오브젝트)에 <span style="color:Orange">전달(주입)</span>함으로써 의존관계가 연결되는 것이다

<br/>예를 들어 

- ##### private Car myCar = new 벤츠();   
  - => Car가 인터페이스고 벤츠가 구현 객체라면, 런타임 이전에, 즉 코드상으로 벤츠 클래스를 의존하는 것을 알 수 있다

- ##### private Car myCar; 
  - ##### => Car에 대해 무슨 차가 들어올지 알 수 없다.(런타임 시점의 의존관계가 드러나지 않으므로) 

  - ##### 이렇게 인터페이스에만 의존해야 의존관계 주입이 발생할 수 있다.

<br/>

<br/>

## 💡 IoC (Inversion of Control) - 제어의 역전

<br/>

#### <span style="color:Orange">프로그램의 제어 흐름</span>(ex:메소드나 객체의 호출작업)을 개발자가 결정하는 것이 아니라, <span style="color:Orange">외부에서 결정(관리)</span>하는 것.

<br/>

##### 즉 객체를 개발자가 Member member = new Member(); 이런식으로 만드는 것이 아니라, <span style="color:Orange">스프링이 스스로 객체를 생성</span>해서, 필요한 곳에 사용할 수 있게 해줌!

<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">AnnotationConfigApplicationContext&nbsp;ac&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#ff3399">new</span>&nbsp;AnnotationConfigApplicationContext(TestConfig.<span style="color:#ff3399">class</span>);</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

##### 위 코드 단 하나만 실행했을 뿐인데, 우리는 ac.getBean을 통해, 원하는 객체를 사용할 수 있음!!!!!

##### 참고로 <span style="color:Orange">DI도 제어의 역전에 포함</span>되는 기술이며, IoC는 좀더 광범위하게 쓰인다!

<br/>

<br/>

## 🧾 부분 정리

##### 자바만으로는 <span style="color:Orange">DIP</span>(의존관계 역전 원칙)와 <span style="color:Orange">OCP</span>(계방-폐쇠 원칙)을 지켜가며 객체지향적으로 설계하는데 어려움이 있었는데, 이를 스프링은 <span style="color:Orange">IoC, DI</span>와 같은 기술을 사용함으로써 해결.

##### 스프링이 좋은 객체 지향 애플리케이션을 개발하는데 도움을 주는 프레임워크인 것 처럼, <span style="color:Orange">스프링 부트</span>는 <span style="color:Orange">스프링의 기술</span>들을 좀 더 <span style="color:Orange">편리하게 사용</span>하는데 도움을 주는 프레임워크.

<br/>

<br/>

## 💡 IoC 컨테이너, DI 컨테이너

##### 객체(오브젝트)의 생성과 관계설정, 사용, 제거 등의 작업(쉽게 말해 <span style="color:Orange">프로그램에 대한 제어</span>)을 애플리케이션 코드(개발자의 영역) 대신 독립된 <span style="color:Orange">컨테이너가 담당</span>할 때, 이 컨테이너를 <span style="color:Orange">IoC컨테이너</span>라고 부른다.

##### 즉 IoC(제어의 역전)를 해주는 컨테이너라고 볼 수 있다.

##### 같은 맥락으로 DI(의존관계 주입)를 해주는 컨테이너를 DI컨테이너라 부른다

<br/>

<br/>

## 💡 스프링 컨테이너 (ApplicationContext)

##### <span style="color:Orange">스프링 빈을 생성하고 관리</span>하는 컨테이너

##### ApplicationContext 와 BeanFactory 두 가지 종류가 있으나 BeanFactory는 거의 사용하는 일이 없으므로 일반적으로 <span style="color:Orange">ApplicationContext </span>를 <span style="color:Orange">스프링 컨테이너</span>라 한다.

##### 내부에는 스프링 빈 저장소를 가지고 있으며, 이곳에 <span style="color:Orange">스프링 빈의 이름과, 그 객체를 저장</span>한다. 

- ##### 스프링 빈의 이름은 @Bean을 사용하면  <span style="color:Orange">메소드명</span>을 사용한다. 빈의 이름을 직접 등록할 경우 @Bean(name = "이름")으로 등록할 수 있다.

- ##### <span style="color:Orange">@Component</span>를 사용할 경우, 이름은 <span style="color:Orange">클래스명</span>을 사용하되, <span style="color:Orange">맨 앞글자를 소문자</span>로 지정한다. @Component(name = "이름")으로 이름을 부여할 수 있다.

  - ##### EX ) Member 클래스는 member로 저장한다

##### <span style="color:Orange">스프링 컨테이너</span>(ApplicationContext)는 <span style="color:Orange">IoC컨테이너</span>이자, <span style="color:Orange">DI컨테이너</span>이며, 후에 나올 <span style="color:Orange">싱글톤 컨테이너</span>의 역할을 한다.

<br/>

<br/>

## 💡 빈(Bean)

#### 스프링 컨테이너가 관리하는 <span style="color:Orange">자바 객체</span>

<br/>

<br/>

## 💡 싱글톤(Singleton)

#### 클래스의 <span style="color:Orange">객체(인스턴스)</span>가 <span style="color:Orange">딱 1개만 생성</span>되는 것을 보장하는 디자인 패턴

<br/>

<br/>

## 💡 싱글톤 레지스트리

#### 싱글톤 객체를 생성하고 관리하는 기능

<br/>

<br/>

