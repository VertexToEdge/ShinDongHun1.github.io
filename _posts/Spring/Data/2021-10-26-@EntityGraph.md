---
title:  "@EntityGraph"
excerpt: "@EntityGraph 사용법"
date:   2021-10-26 06:50:00
header:
  teaser: /assets/images/spring.png

categories: DATA
tags:
  - Java
  - Spring
  - JPA
  - DATA JPA
  - @EntityGraph
last_modified_at: 2021-10-26T06:50:00


---

<br/>

## 💡 @EntityGraph

##### 페치 조인을 편리하게 사용할 수 있게 해준다.

<br/>

##### 사용법

```java
@Override //JpaRepository에 정의된 메소드므로 Override를 해줌
@EntityGraph(attributePath = {"team"})
List<Member> findAll();

//이름 없는 네임드 쿼리에 적용
@EntityGraph(attributePath = {"team"})
@Query("select m from Member m")
List<Member> findMemberEntityGraph();


//메서드 이름으로 사용
@EntityGraph(attributePath = {"team"})
List<Member> findByUsername(String username)
```

##### 사실상 페치 조인의 간편 버전이며

##### <span style="color:orange">LEFT OUTER JOIN을 사용</span>한다

##### 여러개도 적용 가능하다!

<br/>

<br/>

### 📔 Reference

[인프런 - 실전! 스프링 데이터 JPA](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EB%8D%B0%EC%9D%B4%ED%84%B0-JPA-%EC%8B%A4%EC%A0%84/dashboard)

