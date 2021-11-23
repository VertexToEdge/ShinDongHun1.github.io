---
title:  "일대 다 관계에서의 조인 사용시 주의사항"
excerpt: "컬렉션 조인 & 패치 조인 시 결과의 증가 발생"
date:   2021-10-18 05:20:00
header:
  teaser: /assets/images/spring.png

categories: JPA
tags:
  - Java
  - Spring
  - JPA
last_modified_at: 2021-10-18T05:20:00


---

<br/>

### 컬렉션 패치 조인

일대다 관계에서도 패치 조인을 사용할 수 있다.

```
SELECT t
FROM Team t INNER JOIN FETCH t.members
```

<br/>

SELECT 절에 t 만 명시했음에도 불구하고, `T.*, M.*`의 형태로 연관된 회원까지 함께 조회된다.
근데 여기서 주의할 점이 있는데, 쿼리의 결과가 증가해서 그런지 위 jpql의 결과를 리스트로 받아보면 Team의 개수가 Member의 개수와 동일함을 볼 수 있다.

```java
List<Team> list = em.createQuery(jpql, Team.class).getResultList(); // 위에서 작성한 쿼리

for(Team t : list){
    System.out.println(t);

    for(Member m : t.getMembers()){
        System.out.println("-> " + m);
    }
}
```

> Team@0x100
> -> Member@0x200
> -> Member@0x300
> Team@0x100
> -> Member@0x200
> -> Member@0x300

이렇듯 일대다 조인은 결과가 증가할 수 있음에 주의해야 한다.

<br/>

<br/>

## DISTINCT

JPQL의 DISTINCT는 SQL에 DISTINCT를 추가하는 것은 물론이고, 어플리케이션에서 한번 더 중복을 제거한다.
이 특징을 이용해서 위의 컬렉션 패치 조인에서 리스트가 중복되서 나오는 문제를 해결할 수 있다.

```
SELECT DISTINCT t
FROM Team t INNER JOIN FETCH t.members
```

<br/>

<br/>

##### 출처 - [https://joont92.github.io/jpa/JPQL/](https://joont92.github.io/jpa/JPQL/)