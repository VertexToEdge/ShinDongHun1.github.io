---
title:  "쿼리 메소드 - 메소드 이름으로 쿼리 생성"
excerpt: "메소드 이름만으로 기능 구현하기"
date:   2021-10-26 00:40:00
header:
  teaser: /assets/images/spring.png

categories: DATA
tags:
  - Java
  - Spring
  - JPA
  - DATA JPA
last_modified_at: 2021-10-26T00:40:00

---

<br/>

<br/>

## 💡 쿼리 메소드

##### findByUsername(String username) 과 같은 도메인에 특화된 기능을 어떻게 구현할 수 있을까?

##### JpaRepository를 상속받은 인터페이스를 구현하기에는 재정의할 메소드가 너무 많아 현실적으로 불가능하고..

<br/>

### 쿼리 메소드로 해결할 수 있다!

<br/>

<br/>

## 💡메소드 이름으로 쿼리 생성

- ##### username으로 엔티티를 찾고싶다? => findByUsername(String username) 이렇게 정의만 해주면 알아서 구현된다!

- ##### 이름 조건 -[스프링 데이터 JPA 공식 문서 참고](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#jpa.query-methods.query-creation)

- ##### 조회: find…By ,read…By ,query…By get…By 

  - ##### [https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#repositories.query-methods.query-creation](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#repositories.query-methods.query-creation)

  - #####  예:) findHelloBy 처럼 ...에 식별하기 위한 내용(설명)이 들어가도 된다.

- #####  COUNT: count…By, 반환타입 long 

- ##### EXISTS: exists…By, 반환타입 boolean 

- ##### 삭제: delete…By, remove…By, 반환타입 long 

- ##### DISTINCT: findDistinct, findMemberDistinctBy 

- ##### LIMIT: findFirst3, findFirst, findTop, findTop3 

  - ##### [https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#repositories.limit-query-result](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#repositories.limit-query-result)

<br/>

#### <span style="color:orange">참고로 이름으로 쿼리를 생성하는 경우 @Param은 사용하지 않아도 된다!</span>

<br/>

#### 이름 필터 조건

| Keyword                | Sample                                                       | JPQL snippet                                                 |
| :--------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| `Distinct`             | `findDistinctByLastnameAndFirstname`                         | `select distinct … where x.lastname = ?1 and x.firstname = ?2` |
| `And`                  | `findByLastnameAndFirstname`                                 | `… where x.lastname = ?1 and x.firstname = ?2`               |
| `Or`                   | `findByLastnameOrFirstname`                                  | `… where x.lastname = ?1 or x.firstname = ?2`                |
| `Is`, `Equals`         | `findByFirstname`,`findByFirstnameIs`,`findByFirstnameEquals` | `… where x.firstname = ?1`                                   |
| `Between`              | `findByStartDateBetween`                                     | `… where x.startDate between ?1 and ?2`                      |
| `LessThan`             | `findByAgeLessThan`                                          | `… where x.age < ?1`                                         |
| `LessThanEqual`        | `findByAgeLessThanEqual`                                     | `… where x.age <= ?1`                                        |
| `GreaterThan`          | `findByAgeGreaterThan`                                       | `… where x.age > ?1`                                         |
| `GreaterThanEqual`     | `findByAgeGreaterThanEqual`                                  | `… where x.age >= ?1`                                        |
| `After`                | `findByStartDateAfter`                                       | `… where x.startDate > ?1`                                   |
| `Before`               | `findByStartDateBefore`                                      | `… where x.startDate < ?1`                                   |
| `IsNull`, `Null`       | `findByAge(Is)Null`                                          | `… where x.age is null`                                      |
| `IsNotNull`, `NotNull` | `findByAge(Is)NotNull`                                       | `… where x.age not null`                                     |
| `Like`                 | `findByFirstnameLike`                                        | `… where x.firstname like ?1`                                |
| `NotLike`              | `findByFirstnameNotLike`                                     | `… where x.firstname not like ?1`                            |
| `StartingWith`         | `findByFirstnameStartingWith`                                | `… where x.firstname like ?1` (parameter bound with appended `%`) |
| `EndingWith`           | `findByFirstnameEndingWith`                                  | `… where x.firstname like ?1` (parameter bound with prepended `%`) |
| `Containing`           | `findByFirstnameContaining`                                  | `… where x.firstname like ?1` (parameter bound wrapped in `%`) |
| `OrderBy`              | `findByAgeOrderByLastnameDesc`                               | `… where x.age = ?1 order by x.lastname desc`                |
| `Not`                  | `findByLastnameNot`                                          | `… where x.lastname <> ?1`                                   |
| `In`                   | `findByAgeIn(Collection<Age> ages)`                          | `… where x.age in ?1`                                        |
| `NotIn`                | `findByAgeNotIn(Collection<Age> ages)`                       | `… where x.age not in ?1`                                    |
| `True`                 | `findByActiveTrue()`                                         | `… where x.active = true`                                    |
| `False`                | `findByActiveFalse()`                                        | `… where x.active = false`                                   |
| `IgnoreCase`           | `findByFirstnameIgnoreCase`                                  | `… where UPPER(x.firstname) = UPPER(?1)`                     |

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

### 📔 Reference

[인프런 - 실전! 스프링 데이터 JPA](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EB%8D%B0%EC%9D%B4%ED%84%B0-JPA-%EC%8B%A4%EC%A0%84/dashboard)