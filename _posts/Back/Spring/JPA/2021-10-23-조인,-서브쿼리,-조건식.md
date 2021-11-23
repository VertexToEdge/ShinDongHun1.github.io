---
title:  "조인, 서브쿼리, 조건식"
excerpt: "JPQL 조인 사용법, 조건식"
date:   2021-10-23 15:07:00
header:
  teaser: /assets/images/spring.png

categories: JPA
tags:
  - Java
  - Spring
  - JPA
  - JPQL
last_modified_at: 2021-10-23T15:07:00

---

<br/>

# 💡 조인

#### 내부 조인:

##### SELECT m FROM Member m [INNER] JOIN m.team t



#### 외부 조인:

##### SELECT m FROM Member m LEFT [OUTER] JOIN m.team t



#### 세타 조인:

##### SELECT count(m) form Member m , Team t where m.username = t.name

=> 전혀 연관 없는것들을 조인 => 카테시안 곱 발생

<br/>

<br/>

### 조인 - ON 절

##### ON절을 활용한 조인(JPA 2.1부터 지원)

1. ##### 조인 대상 필터링

2. ##### 연관관계 없는 엔티티 외부 조인

<br/>

#### 조인 대상 필터링

예) 회원과 팀을 조인하면서, 팀 이름이 A인 팀만 조인

```sql
SELECT m, t FROM Member m LEFT JOIN m.team t on t.name = 'A'
```

<br/>

#### 연관관계 없는 엔티티 외부 조인

예) 회원의 이름과 팀의 이름이 같은 대상 외부 조인

```sql
SELECT m, t FROM Member m LEFT JOIN Team t on m.username = t.name
```

##### 연관관계가 전혀 없은 엔티티를 조인하고 싶으면 on절에 위의 예시처럼 적어주면 된다.

<br/>

<br/>

## 💡 서브 쿼리

##### 예를 들어 나이가 평균보다 많은 회원을 주문한다고 생각해보자.

##### 회원을 찾아오는 쿼리와, 나이가 평균보다 많은것을 구하기 위해, 나이의 평균을 구하는 쿼리도 작성해야 할 것이다.

##### 이때 나이의 평균을 구하는 쿼리가 서브쿼리이다. 아래 예시로 확인해보자

```sql
select m from Member m where m.age > (select avg(m2.age) from Member m2)
```

<br/>

### 서브 쿼리 지원 함수

- [NOT] EXISTS(subquery) : 서브쿼리에 결과가 존재하면 참
  - {ALL | ANY | SOME} (subquery)
  - ALL 모두 만족하면 참
  - ANY, SOME : 같은 의미, 조건을 하나라도 만족하면 참
- [NOT] IN (subquery) : 서브쿼리의 결과 중 하나라도 같은 것이 있으면 참

##### 사용예시

```sql
//팀A 소속인 회원
select m from Membrer m where exist (select t from m.team t where t.name ='팀A')

//전체 상품 각각의 재고보다 주문량이 많은 주문들
select o from Order o where o.orderAmount > ALL(select p.stockAmount from Product p)

//어떤 팀이든 팀에 소속된 회원
select m from Member m where m.team = ANY(select t from Team t)
```

<br/>

<br/>

### JPA 서브 쿼리 한계

##### JAP는 WHERE, HAVING 절에서만 서브 쿼리 사용이 가능하다.(하이버네이트에서는 SELECT 까지 지원헤준다)

##### 그러나 FROM 절의 서브 쿼리는 현재 JPQL에서 불가능하다 => 조인으로 풀 수 있으면 풀어서 해결하자

<br/>

<br/>

## 💡 JPQL 타입 표현 

- ##### 문자 : 'HELLO', 'SHE"s'

- ##### 숫자 : 10L(Long), 10D(Double), 10F(Float)

- ##### Boolean : TRUE , FALSE

- ##### ENUM : jpabook.MemberType.Admin(패키지명 포함)

- ##### 엔티티 타입 : TYPE(m) = Member

<br/>

<br/>

## 💡 JPQL 기본 함수

- ##### CONCAT

- ##### SUBSTRING

- ##### TRIM

- ##### LOWER, UPPER

- ##### LENGTH

- ##### LOCATE

- ##### ABS,SQRT,MOD

- ##### SIZE, INDEX (JPA용도)

<br/>

### 사용자 정희 함수

하이버네이트는 사용전 방언에 추가해야 한다.

- 사용하는 방언을 상속받고, 사용자 정의 함수를 등록한다.
- 하이버네이트를 사용하면, 각각의 데이터베이스가 지원하는 함수들을 미리 등록해놓았다.

<br/>

<br/>

### 📔 Reference

[인프런 - 자바 ORM 표준 JPA 프로그래밍](https://www.inflearn.com/course/ORM-JPA-Basic/dashboard)

