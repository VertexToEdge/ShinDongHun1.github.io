---
title:  "Aggregate Root"
excerpt: "DDD와 Aggregate Root"
date:   2021-10-22 20:07:00
header:
  teaser: /assets/images/spring.png

categories: JPA
tags:
  - 도메인
  - DDD
  - Aggregate Root

last_modified_at: 2021-10-22T20:07:00

---

<br/>

## 💡 Domain

##### 도메인의 사전적 의미는 "영역", "집합"이다.

##### 비즈니스에서는 해결하고자 하는 문제 영역 혹은 유사한 업무의 집합을 도메인이라 부른다.

##### 예를 들어 게시판 서비스를 구현하고자 하는 경우에는 게시판이 도메인이 된다.

##### 도메인은 하위 도메인으로 나뉠 수 있는데, 게시판 도메인은 게시글, 댓글 등의 하위 도메인으로 나뉜다.

<br/>

<br/>

## 💡 도메인 모델

##### 도메인을 개념적으로 표현한 것.

##### 도메인을 개념적으로 표현하는 방법은 다양하다. 예를 들어  UML(클래스/상태 다이어그램), 그래프, 수학 공식 등이 도메인 모델이 될 수 있다.

<br/>

<br/>

## 💡 도메인 모델 패턴

##### 도메인 계층(Domain Layer)의 유형 중 하나.

##### 간단하게 말하자면, 데이터와 데이터의 행위가 함께 객체를 이루는 형태이다.

##### 도메인 모델 패턴은 객체지향 요소들을 더 적극적으로 활용하여, 다음과 같은 이점들을 제공한다.

- ##### 설계의 이해가 쉬워진다

- ##### 설계를 관리하기 쉬워진다

- ##### 테스트하기 쉬워진다

- ##### Design Pattern 등의 도움을 받을 수 있다.

<br/>

##### 도메인 모델 패턴은 결국 아키텍처상의 도메인 계층(Domain Layer)을 객체 지향 기법으로 구현하는 패턴이다.

<br/>

<br/>

## 💡 아키텍쳐 패턴 - 계층화 패턴(Layered pattern)

##### 이 패턴은 **n-티어 아키텍쳐 패턴**이라고도 불린다. 

##### 이는 하위 모듈들의 그룹으로 나눌 수 있는 구조화된 프로그램에서 사용할 수 있다. 

##### 각 하위 모듈들은 특정한 수준의 추상화를 제공한다. 

##### 각 계층은 다음 상위 계층에 서비스를 제공한다.

<br/>

##### 일반적인 정보 시스템에서 공통적으로 볼 수 있는 계층 4가지는 다음과 같다.

- ##### **프레젠테이션 계층** (Presentation layer) - **UI 계층** (UI layer) 이라고도 함

  - ##### 사용자의 요청을 받아 애플리케이션 계층에 전달하고, 그 결과를 사용자에게 보여준다.

- ##### **애플리케이션 계층** (Application layer) - **서비스 계층** (Service layer) 이라고도 함

  - ##### 사용자가 요청한 기능을 실행한다. 로직을 직접 구현하는 것이 아니라, 도메인 계층을 조합해서 기능을 실행한다.

- ##### **비즈니스 논리 계층** (Business logic layer) - **도메인 계층** (Domain layer) 이라고도 함

  - ##### 시스템이 제공할 도메인의 규칙, 핵심 로직을 구현한다.

- ##### **데이터 접근 계층** (Data access layer) - **영속 계층** (Persistence layer) 이라고도 함

  - ##### DB나 메시징 시스템과 같은 외부 시스템과의 연동을 처리한다.



![img](https://miro.medium.com/max/700/1*9y2cUynZoq1KbarwlzEW9w.png)

<br/>

<br/>

## 💡 DDD (Domain Driven Design)

##### DDD(도메인 주도 설계)는 도메인 전문가와 개발자가 ‘도메인의 이해’를 목적으로 만들어낼 수 있는 유비쿼터스 언어, 도메인 모델(개념적인 그림/그래프)을 기반으로 하는 설계 방식을 의미한다.

> ##### 참고 : Domain Model은 이해를 위한 개념적 모델이며, Domain Model Pattern은 도메인 레이어의 ‘객체지향적 구현’을 의미합니다. 두 용어가 사용되는 맥락이 다릅니다.

##### 이 도메인 주도 설계는 도메인 레이어를 구현할 때 중요한 지침으로 활용될 수 있다.

<br/>

##### spring 개발을 했었다면, Entity/Repository/Service 등이 실제로는 DDD에서 비롯한 annotation들이기 때문에, 어느정도는 DDD를 해온 셈이다.

<br/>

<br/>

## 💡  Aggregate Root

##### Aggregate의 중심 객체

<br/>

### Aggregate란?

##### 데이터 변경의 단위로 다루는 연관 객체의 묶음

##### 이러한 연관 객체의 묶음을 Aggregate라고 한다,

##### 예를 들면, 주문이라는 Entity와 주문자라는 Value Object들이 결합하여 주문 Aggregate를 만들 수 있다.

<br/>

##### Aggregate에는 Aggregate Root라는 중심 객체가 존재하는데, 위의 예시에서는 주문 Entity가 Aggregate Root이다.

##### 여러 엔티티를 묶어서 가져오는 경우가 많을 땐 개발에서 Aggregate Root에 해당되는 Entity에 대해서만 Repository를 만드는 경우가 많다.

#### <br/>

### 영속성 전이와의 관계?

##### 스프링에서 공부했던 CascadeType.ALL + orphanRemoval = true  이 옵션들이 Aggregate Root를 구현할 때 유용한 것은, 부모와 자식 관계에서 부모가 Aggregate Root가 되고 부모 레포지토리만 만들어서 개발할 수 있도록 만들어 주기 때문이다.

<br/>

<br/>

<br/>

### 📔 Reference

[Layered Architecture](https://herbertograca.com/2017/08/03/layered-architecture/)

[10가지 아키텍처 패턴 요약](https://mingrammer.com/translation-10-common-software-architectural-patterns-in-a-nutshell/)

[도메인 주도 설계(DDD-Domain Driven Design) - 도메인 모델](https://gnidoc.tistory.com/entry/%EB%8F%84%EB%A9%94%EC%9D%B8-%EC%A3%BC%EB%8F%84-%EC%84%A4%EA%B3%84DDD-Domain-Driven-Design-%EB%8F%84%EB%A9%94%EC%9D%B8-%EB%AA%A8%EB%8D%B8)

[DDD 시작하기](https://sgc109.github.io/2020/08/09/ddd-basic/)

[Spring 코드와 함께 보는 백엔드 서버 아키텍처 — 시리즈 소개, 기본 구조](https://tech.junhabaek.net/spring-boot-%EC%BD%94%EB%93%9C%EC%99%80-%ED%95%A8%EA%BB%98-%EB%B3%B4%EB%8A%94-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%84%9C%EB%B2%84-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98-%EC%8B%9C%EB%A6%AC%EC%A6%88-%EC%86%8C%EA%B0%9C-%EA%B8%B0%EB%B3%B8-%EA%B5%AC%EC%A1%B0-bbf814e1b4e3)

[백엔드 서버 아키텍처 — Domain Layer1. Domain Layer와 DDD](https://tech.junhabaek.net/%EB%B0%B1%EC%97%94%EB%93%9C-%EC%84%9C%EB%B2%84-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98-domain-layer1-domain-layer%EC%99%80-ddd-e97a7587a7b0)

[백엔드 서버 아키텍처 — Application Layer 1. 개요와 기본 Variation](https://tech.junhabaek.net/%EB%B0%B1%EC%97%94%EB%93%9C-%EC%84%9C%EB%B2%84-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98-application-layer-1-%EA%B0%9C%EC%9A%94%EC%99%80-%EA%B8%B0%EB%B3%B8-variation-9fac801ddba8)

[DDD, Aggregate Root 란?](https://eocoding.tistory.com/36)

[DDD 핵심만 빠르게 이해하기](https://happycloud-lee.tistory.com/94)

[DDD Aggregate Pattern](https://www.secmem.org/blog/2020/02/19/ddd-aggregate-pattern/)