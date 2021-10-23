---
title:  "JPQL 기본 문법, 페이징"
excerpt: "JPQL의 기본 문법과 기능?"
date:   2021-10-23 14:07:00
header:
  teaser: /assets/images/spring.png

categories: JPA
tags:
  - Java
  - Spring
  - JPA
  - JPQL
last_modified_at: 2021-10-23T14:07:00



---

<br/>

# 💡 JPQL

```sql
select m from Member as m where m.age > 18 
```

-  엔티티와 속성은 대소문자를 구분한다.

- JPQL 키워드는 대소문자 구분을 하지 않는다(SELECT, from, ...)

- 테이블 이름이 아닌 엔티티 이름을 사용한다(@Table(name ="이거 아님"), @Entity(name = "이거 사용"))

- ##### 별칭은 필수(m), (as는 생략이 가능하다)

<br/>

```java
select 
	COUNT(m),   //회원 수
	Sum(m.age), //나이 합
	AVG(m),   //평균 나이
	MAX(m),   //최대 나이
	MIN(m),   //최소 나이
from Member m
```

<br/>

##### GROUP BY, HAVING, ORDER BY 모두 사용이 가능하다

<br/>

<br/>

### TypeQuery, Query

##### TypeQuery : 반환 타입이 명확할 때 사용한다.

##### Query : 반환 타입이 명확하지 않을 때 사용한다.

<br/>

<br/>

### 결과 조회 

##### getResultResult() : 결과가 하나 이상일 때 사용한다. 리스트를 반환한다.

- ##### 결과가 없으면 빈 리스트를 반환한다.

##### getSingleResult() : 결과가 정확히 하나, 단일 객체를 반환한다.

- ##### 결과가 없으면 NoResultResult,

- ##### 둘 이상이면 NonUniqueResultException

<br/>

<br/>

### 파라미터 바인딩

##### 이름을 기준으로 바인딩 할 수 있고, 위치를 기준으로 바인딩 할 수 있다.

![image-20211023130740554](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211023130740554.png)

<br/>

<br/>

<br/>

## 💡 프로젝션

SELECT 절에 조회할 대상을 지정하는 것.

프로젝션의 대상 : 엔티티, 임베디드 타입, 스칼라 타입(숫자, 문자 등 기본 데이터 타입)

```java
SELECT m FROM Member m 	//엔티티 프로젝션
SELECT m.team FROM Member m 	//엔티티 프로젝션(조인 쿼리 사용)
    
SELECT m.address FROM Member m 	
//임베디드 타입 프로젝션, 가져오는 타입은 (Address.class)

SELECT distinct m.username, m.age FROM Member m 	//스칼라 타입 프로젝션
```

#### DISTINCT로 중복을 제거할 수 있다.

<br/>

##### 위의 예시에서 스칼라 타입 프로젝션을 보자. 해당 쿼리의 결과를 어떻게 받아올 수 있을까?

1. #####  Query 타입으로 조회

2. #####  Object[] 타입으로 조회

3. #####  new 명령어로 조회

   - ##### 단순 값을 DTO로 바로 조회

     - ##### SELECT new jpabook.jpql.UserDTO(m.username, m.age) FROM Member m

   - ##### 패키지 명을 포함한 전체 클래스 이름을 입력해야 한다.

   - ##### 순서와 타입이 일치하는 생성자가 필요하다

<br/>

<br/>

## 💡 페이징

JPA는 페이징을 다음 두  API로 추상화했다.

- setFirstResult(int startPosition) : 조회 시작 위치(0부터 시작)
- setMaxResults(int maxResult) : 조회할 데이터 수

```java
em.createQuery("select p from Post p order by p.createdDate desc", Post.class)
        .setFirstResult(startIdx)
        .setMaxResults(count)
        .getResultList();
```

<br/>

<br/>

### 📔 Reference

[인프런 - 자바 ORM 표준 JPA 프로그래밍](https://www.inflearn.com/course/ORM-JPA-Basic/dashboard)

