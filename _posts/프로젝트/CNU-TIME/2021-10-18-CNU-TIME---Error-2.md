---
title:  "CNU TIME - Error 2"
excerpt: "컬렉션 패치조인 시 데이터가 늘어나는 문제"
date:   2021-10-18 05:28:00 +0900
header:
  teaser: /assets/images/spring.png

categories: CNUTime
tags:
  - project
last_modified_at: 2021-10-18T05:28:00-05:00



---
<br/>
<br/>

### 컬렉션 패치조인 시 데이터가 늘어나는 문제

<br/>
<br/>

<script src="https://gist.github.com/ShinDongHun1/180e8fdf36e6ef1b26a79e23d5d1ee30.js"></script>

해당 메소드를 사용하면, 만약 댓글이 3개 달린 게시물이 있으면, 3번 중복되어 보여졌다.

![image-20211018051846518](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211018051846518.png)

이런식으로 나왔었는데, 이는 일대 다 관계에서 페치 조인을 사용함으로써, 결과가 증가한 것이 이유인 것 같다.

[https://joont92.github.io/jpa/JPQL/](https://joont92.github.io/jpa/JPQL/)

```java
 @Query("select distinct p from Post p join fetch p.writer w left join fetch p.comments c order by p.createdDate desc")
```

를 사용하면 해결된다.