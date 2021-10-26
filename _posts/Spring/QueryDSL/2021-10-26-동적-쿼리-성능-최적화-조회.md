---
title:  "동적 쿼리 성능 최적화 조회"
excerpt: "builder와 where 다중 파라미터 사용"
date:   2021-10-26 22:30:00
header:
  teaser: /assets/images/spring.png

categories: QueryDSL
tags:
  - Java
  - Spring
  - JPA
  - QueryDSL
last_modified_at: 2021-10-26T22:30:00


---

<br/>

## 💡 동적 쿼리 사용 -Builder

<script src="https://gist.github.com/ShinDongHun1/18c57bbffa5c356c50a71b644cc74e80.js"></script>

<br/>

<script src="https://gist.github.com/ShinDongHun1/432c688c5b9a5c69193b6f69c5fe8da6.js"></script>

##### member.id.as("memberId") 라고 적었는데, QMemberTeamDto 는 생성자를 사용하기 때문에 필드 이름을 맞추지 않아도 된다. 따라서 member.id 만 적으면 된다

<br/>

<br/>

## 💡 Where 다중 파라미터 사용

<script src="https://gist.github.com/ShinDongHun1/931030f243d6065cb58af6add8e3f3c3.js"></script>

<br/>

### 📔 Reference

[실전! Querydsl](https://www.inflearn.com/course/Querydsl-%EC%8B%A4%EC%A0%84/dashboard)

