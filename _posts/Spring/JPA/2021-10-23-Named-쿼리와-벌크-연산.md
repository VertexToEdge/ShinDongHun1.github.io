---
title:  "Named 쿼리와 벌크 연산"
excerpt: "네임드 쿼리와 벌크 연산"
date:   2021-10-23 18:00:00
header:
  teaser: /assets/images/spring.png

categories: JPA
tags:
  - Java
  - Spring
  - JPA
  - JPQL
last_modified_at: 2021-10-23T18:00:00


---

<br/>

# 💡 Named 쿼리

##### 미리 정의해서 이름을 부여해두고 사용하는 JPQL

##### 정적 쿼리

##### 어노테이션, XML에 정의

##### 애플리케이션 로딩 시점에 초기화 후 재사용

##### 애플리케이션 로딩 시점에 쿼리를 검증

<br/>

#### 어노테이션으로 사용

```java
@Entity
@NamedQuery{
	name = "Member.findByUsername",  //Member.는 관례로 사용
	query = "select m from Member m where m.username = :username"
}
```

#### em.createNamedQuery("Member.findByUsername", Member.class)로 사용

#### (스프링 데이터 JPA에서는 @Query를 통해 사용할 수 있음)

<br/>

##### XML이 어노테이션보다 항상 우선권을 가진다

<br/>

<br/>

## 💡 벌크 연산

##### 모든 직원의 연봉을 10% 인상시켜주는 쿼리를 실행하려면?

##### JPA의 변경 감지 기능으로 변경하기엔 쿼리가 너무 많이 나간다.

##### 벌크 연산이 이를 해결해준다.

- ##### UPDATE, DELETE 지원

- ##### executeUpdate()의 결과는 영향받은 엔티티 수 반환

```java
public int bulkAgePlus(){//영향을 받은 엔티티 수 반환
	return em.createQuery("update Member m set m.age = m.age + 1")
        .executeUpdate();
}
```

<br/>

### 👿 주의

##### 벌크 연산은 영속성 컨텍스트를 무시하고 데이터베이스에 직접 쿼리를 날린다

- ##### 따라서 벌크 연산을 먼저 실행 후

- ##### 벌크 연산 수행 후에 영속성 컨텍스트를 초기화 해야한다

<br/>

<br/>

### 📔 Reference

[인프런 - 자바 ORM 표준 JPA 프로그래밍](https://www.inflearn.com/course/ORM-JPA-Basic/dashboard)

