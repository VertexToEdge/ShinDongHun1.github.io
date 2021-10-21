---
title:  "즉시 로딩과 지연 로딩"
excerpt: "즉시로딩, 지연로딩 ,프록시"
date:   2021-10-21 18:07:00
header:
  teaser: /assets/images/spring.png

categories: JPA
tags:
  - Java
  - Spring
  - JPA
  - 영속성 컨텍스트
last_modified_at: 2021-10-21T18:07:00



---

<br/>

## 💡 프록시

#####  Member를 조회할 때 Team도 함께 조회해야 할까?

<br/>

### em.find() vs em.getReference()

- ##### em.find() : 데이터베이스를 통해서 실제 엔티티 객체 조회

- ##### em.getReference() : 데이터베이스 조회를 미루는 가짜(프록시) 엔티티 객체 조회

<br/>

### 프록시의 특징

- ##### 실제 클래스를 상속 받아서 만들어짐

- ##### 실제 클래스와 겉모양이 같다.

- ##### 사용하는 입장에서는 진짜 객체인지 프록시 객체인지 구분하지 않고 사용하면 됨

- ##### 프록시 객체는 실제 객체의 참조를 보관한다.

- ##### 프록시 객체를 호출하면 프록시 객체는 실제 객체의 메소드를 호출한다.

<br/>

### 프록시 객체의 초기화

```java
Member member = em.getReference(Member.class, "id1");
member.getName();
```

##### member.getName()을 호출하면 맨 객체의 참조에 값이 있는지 확인한다.

##### 값이 없으므로 JPA가 <span style="color:orange">영속성 컨텍스트</span>에 진짜 객체를 가져오라고 요청한다.(초기화 요청)

##### 영속성 컨텍스트는DB를 조회해서 실제 Entity 객체를 가져와 프록시 객체의 참조(target)에 연결시켜준다.

<br/>

### 중요

- ##### 프록시 객체는 처음 사용할 때 한 번만 초기화

- ##### 프록시 객체를 초기화 할 때, 프록시 객체가 실제 엔티티로 바뀌는 것은 아니다, 초기화되면 프록시 객체를 통해서 실제 엔티티에 접근이 가능해짐

- ##### 프록시 객체는 원본 엔티티를 상속받는다, 따라서 타입 체크시 == 대신 instance of 를 사용해야 함

- ##### 영속성 컨텍스트에 찾은 엔티티가 이미 존재하면 em.getReference()를 호출해도 실제 엔티티 반환.

- ##### 영속성 컨텍스트의 도움을 받을 수 없는 준영속 상태일 때, 프록시를 초기화하면 문제 발생

  - ##### org.hibernate.LazyInitializationException 예외 발생

<br/>

<br/>

### 프록시 확인

- ##### 프록시 인스턴스의 초기화 여부 확인

  - ##### PersistenceUnitUtil.isLoaded(Object entity)

- ##### 프록시 클래스 확인 방법

  - ##### entity.getClass().getName()

- ##### 프록시 강제 초기화

  - ##### org.hibernate.Hibernate.initialize(entity);

<br/>

<br/>

## 💡 즉시 로딩과 지연 로딩

#####  Member를 조회할 때 Team도 함께 조회해야 할까?

<br/>

<br/>

### 지연 로딩을 사용해서 프록시로 조회

- #### 지연로딩 적용

```java
@ManyToOne(fetch = FetchType.LAZY)
```

<br/>

```java
Member member = em.fine(Member.class, 1L);

Team team = member.getTeam();
System.out.println(team.getClass()); //프록시 출력

team.getName(); //실제 team을 사용하는 시점에 초기화
```

<br/>

<br/>

### 즉시 로딩

Member랑 Team을 함께 사용한다면? =>  FetchType.EAGER를 사용하여 즉시 로딩을 적용할 수 있음.

#### <span style="color:red">그러나 즉시 로딩은 사용하지 말자</span>

<br/>

<br/>

### 프록시와 즉시로딩 주의

- ##### 가급적 지연 로딩만 사용하자

- ##### <span style="color:red">즉시 로딩을 적용하면 예상하지 못한 SQL이 발생한다.</span>

- ##### <span style="color:red">즉시 로딩은 JPQL에서 N+1 문제를 일으킨다.</span>

- ##### @XToOne은 기본이 즉시 로딩 => LAZY로 설정

<br/>

<br/>

### 📔 Reference

[인프런 - 자바 ORM 표준 JPA 프로그래밍](https://www.inflearn.com/course/ORM-JPA-Basic/dashboard)