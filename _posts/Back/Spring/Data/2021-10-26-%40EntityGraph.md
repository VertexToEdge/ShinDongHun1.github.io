---
title:  "@EntityGraph"
excerpt: "EntityGraph ์ฌ์ฉ๋ฒ"
date:   2021-10-26 06:50:00
header:
  teaser: /assets/images/spring.png

categories: DATA
tags:
  - Java
  - Spring
  - JPA
  - DATA JPA
  - EntityGraph
last_modified_at: 2021-10-26T06:50:00


---

<br/>

## ๐ก @EntityGraph

##### ํ์น ์กฐ์ธ์ ํธ๋ฆฌํ๊ฒ ์ฌ์ฉํ  ์ ์๊ฒ ํด์ค๋ค.

<br/>

##### ์ฌ์ฉ๋ฒ

```java
@Override //JpaRepository์ ์ ์๋ ๋ฉ์๋๋ฏ๋ก Override๋ฅผ ํด์ค
@EntityGraph(attributePath = {"team"})
List<Member> findAll();

//์ด๋ฆ ์๋ ๋ค์๋ ์ฟผ๋ฆฌ์ ์ ์ฉ
@EntityGraph(attributePath = {"team"})
@Query("select m from Member m")
List<Member> findMemberEntityGraph();


//๋ฉ์๋ ์ด๋ฆ์ผ๋ก ์ฌ์ฉ
@EntityGraph(attributePath = {"team"})
List<Member> findByUsername(String username)
```

##### ์ฌ์ค์ ํ์น ์กฐ์ธ์ ๊ฐํธ ๋ฒ์ ์ด๋ฉฐ

##### <span style="color:orange">LEFT OUTER JOIN์ ์ฌ์ฉ</span>ํ๋ค

##### ์ฌ๋ฌ๊ฐ๋ ์ ์ฉ ๊ฐ๋ฅํ๋ค!

<br/>

<br/>

### ๐ Reference

[์ธํ๋ฐ - ์ค์ ! ์คํ๋ง ๋ฐ์ดํฐ JPA](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EB%8D%B0%EC%9D%B4%ED%84%B0-JPA-%EC%8B%A4%EC%A0%84/dashboard)

