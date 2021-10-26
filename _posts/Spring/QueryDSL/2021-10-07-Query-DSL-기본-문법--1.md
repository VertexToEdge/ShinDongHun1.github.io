---
title:  "Query DSL 기본문법"
excerpt: "검색 조건, 결과 조회, 정렬, 페이징, 집합, 조인"
date:   2021-10-26 19:00:00
header:
  teaser: /assets/images/spring.png

categories: QueryDSL
tags:
  - Java
  - Spring
  - Query DSL
last_modified_at: 2021-10-26T19:00:00
---



<br/>

## <br/>💡 기본 문법

### 💡 JPQL vs QueryDSL

<br/>

#### 하나의 member 찾기

#### 🐬 JPQL

<script src="https://gist.github.com/ShinDongHun1/2f0cc411b60ffdd45c61702fdc175af3.js"></script>

#### 🐬 QueryDSL

<script src="https://gist.github.com/ShinDongHun1/5a785453e3e8488308575c30a169c69d.js"></script>

<br/>

#### 참고

##### 실행되는 jpql이 궁금하다면? => spring.jpa.properties.hibernate.use_sql_comments=true

<br/>

### 💡 기본  Q-Type

##### Q클래스 인스턴스를 사용하는 2가지 방법

- ##### QMember m = new QMember("m"); : 별칭 직접 지정

- ##### QMember m = QMember.member; : 기본 인스턴스 사용

<br/>

<br/>

## 💡 검색 조건

<script src="https://gist.github.com/ShinDongHun1/2b54a976eea7ad793b4d75ac79b1f24a.js"></script>

#### 🐬 검색 조건

```java
member.username.eq("member1") // username = 'member1'
member.username.ne("member1") //username != 'member1'
member.username.eq("member1").not() // username != 'member1'
member.username.isNotNull() //이름이 is not null

member.age.in(10, 20) // age in (10,20)
member.age.notIn(10, 20) // age not in (10, 20)
member.age.between(10,30) //between 10, 30

member.age.goe(30) // age >= 30
member.age.gt(30) // age > 30
member.age.loe(30) // age <= 30
member.age.lt(30) // age < 30

member.username.like("member%") //like 검색
member.username.contains("member") // like ‘%member%’ 검색
member.username.startsWith("member") //like ‘member%’ 검색
```

<br/>

### 🐬 참고

- #### and 의 경우 , 으로 대체할 수 있다

```java
Member findMember = query
                      .select(member)//QMember.member
                      .from(member)
                      .where(
                     		 member.username.eq("member1")
               			     , member.age.eq(10)//중간에 null이 들어가면 무시
               			 )
                      .fetchOne();
```

<br/>

<br/>

<br/>

## 💡 결과 조회

- ##### fetch() : 리스트 조회, 데이터 없으면 빈 리스트 반환

- ##### fetchOne() : 단 건 조회

  - ##### 결과가 없으면 : null

  - ##### 결과가 둘 이상이면 : com.querydsl.core.NonUniqueResultException

- ##### fetchFirst() : limit(1).fetchOne()

- ##### fetchResults() : 페이징 정보 포함, total count 쿼리 추가 실행, QueryResults\<T> 반환

  - ##### getTotla(), getResults(), ... 제공

- ##### fetchCount() : count 쿼리로 변경해서 count 수 조회

<br/>

```java
//List
List<Member> fetch = queryFactory
 						.selectFrom(member)
 						.fetch();
 
//단 건
Member findMember1 = queryFactory
 						.selectFrom(member)
 						.fetchOne();
 
//처음 한 건 조회
Member findMember2 = queryFactory
 						.selectFrom(member)
 						.fetchFirst();
 
//페이징에서 사용
QueryResults<Member> results = queryFactory
 						.selectFrom(member)
 						.fetchResults();
 
//count 쿼리로 변경
long count = queryFactory
 						.selectFrom(member)
 						.fetchCount();
```

<br/>

<br/>

<br/>

## 💡 정렬

<script src="https://gist.github.com/ShinDongHun1/51891178a08b99b178cb751d96b62ced.js"></script>

<br/>

<br/>

## 💡 페이징

<script src="https://gist.github.com/ShinDongHun1/bdcbe97a91cf4e0656ce4e4fff0b01ac.js"></script>

<script src="https://gist.github.com/ShinDongHun1/723b51ab02c6c17d1d0520e3cb8debc4.js"></script>

<br/><br/>

## 💡 집합

<script src="https://gist.github.com/ShinDongHun1/173ab0a6e752d3c8191bca2b56db0f13.js"></script>

### +group by

##### 팀의 이름과 각 팀의 평균 연령 구하기

<script src="https://gist.github.com/ShinDongHun1/ba57156dd918322a41b4ccfa8b6ff9a7.js"></script>

<br/><br/>

## 💡 조인

### 🐬기본

- ####   join(조인 대상, 별칭으로 사용할 Q타입)

<script src="https://gist.github.com/ShinDongHun1/7583673fff031d0155aebf7061ae47e5.js"></script>

<br/>

<br/>

### 🐬세타조인

<script src="https://gist.github.com/ShinDongHun1/5a1328410e9f14fc249091126d5aa9c5.js"></script>

- ##### from 절에 여러 엔티티를 선택해서 세타 조인

- ##### 외부 조인 불가능 -> 다음에 설명할 조인 on을 사용하면 외부 조인 가능

<br/>

<br/>

### 🐬조인 on

<script src="https://gist.github.com/ShinDongHun1/44945d70869b15c47ea301b9c8944c33.js"></script>

#### 결과

tuple = [Member(id=3, username=member1, age=10), Team(id=1, name=TeamA)]
tuple = [Member(id=4, username=member2, age=20), Team(id=1, name=TeamA)]
tuple = [Member(id=5, username=member3, age=30), null]
tuple = [Member(id=6, username=member4, age=40), null]

<br/>

#### 참고

##### on 절을 활용해 조인 대상을 필터링 할 때, 외부조인이 아니라 내부조인(inner join)을 사용하면, where 절에서 필터링 하는 것과 기능이 동일하다. 따라서 on 절을 활용한 조인 대상 필터링을 사용할 때, 내부조인 이면 익숙한 where 절로 해결하고, 정말 외부조인이 필요한 경우에만 이 기능을 사용하자.

<br/>

<br/>

### 🐬연관관계 없는 엔티티 외부 조인

<script src="https://gist.github.com/ShinDongHun1/c307d7df3f35fd615b97b868cf56b238.js"></script>

tuple = [Member(id=3, username=member1, age=10), null]
tuple = [Member(id=4, username=member2, age=20), null]
tuple = [Member(id=5, username=member3, age=30), null]
tuple = [Member(id=6, username=member4, age=40), null]
tuple = [Member(id=7, username=TeamA, age=0), Team(id=1, name=TeamA)]
tuple = [Member(id=8, username=TeamB, age=0), Team(id=2, name=TeamB)]
tuple = [Member(id=9, username=TeamC, age=0), null]

<br/>

<br/>

### 🐬페치 조인

<script src="https://gist.github.com/ShinDongHun1/cf847a35577bca958bbfe8513955581e.js"></script>

<br/>

<br/>

## 💡 서브쿼리

<script src="https://gist.github.com/ShinDongHun1/48795142855bff9c914de7227c557b22.js"></script>

##### JPAExpressions사용

##### 바깥과 안의 이름이 달라야 함으로 memberSub를 정의

<br/>

#### from 절의 서브쿼리 한계

#####  JPA JPQL 서브쿼리의 한계점으로 from 절의 서브쿼리(인라인 뷰)는 지원하지 않는다. 

##### 당연히 Querydsl 도 지원하지 않는다. 

##### 하이버네이트 구현체를 사용하면 select 절의 서브쿼리는 지원한다. 

##### Querydsl도 하이버네이트 구현체를 사용하면 select 절의 서브쿼리를 지원한다.

<br/>

#### from 절의 서브쿼리 해결방안 

##### 1. 서브쿼리를 join으로 변경한다. (가능한 상황도 있고, 불가능한 상황도 있다.) 

##### 2. 애플리케이션에서 쿼리를 2번 분리해서 실행한다. 

##### 3. nativeSQL을 사용한다.

<br/>

<br/>

<br/>

## 💡 Case 문

##### 단순한 조건

<script src="https://gist.github.com/ShinDongHun1/fa86dd1b9b19219414be0aa268e281c8.js"></script>

<br/>

##### 복잡한 조건

<script src="https://gist.github.com/ShinDongHun1/cadcb1be5a12d95500ea56ee2b33440e.js"></script>

<br/>

##### 예를 들어서 다음과 같은 임의의 순서로 회원을 출력하고 싶다면? 

##### 1. 0 ~ 30살이 아닌 회원을 가장 먼저 출력 

##### 2. 0 ~ 20살 회원 출력 

##### 3. 21 ~ 30살 회원 출력

<script src="https://gist.github.com/ShinDongHun1/2aaf765d2406286591ef702d6a4451fe.js"></script>

#### 결과 

username = member4 age = 40 rank = 3 

username = member1 age = 10 rank = 2 

username = member2 age = 20 rank = 2 

username = member3 age = 30 rank = 1

<br/>

<br/>

<br/>

## 💡 상수, 문자 더하기

##### 상수가 필요하다면 Expressions.constant(xxx) 사용

<script src="https://gist.github.com/ShinDongHun1/d334d594fd5a17692fde43ba419ff9d4.js"></script>

<br/>

##### 문자 더하기 concat

<script src="https://gist.github.com/ShinDongHun1/0cfbb71cfe3515332a6217fae842623c.js"></script>

<br/>

<br/>

### 📔 Reference

[실전! Querydsl](https://www.inflearn.com/course/Querydsl-%EC%8B%A4%EC%A0%84/dashboard)