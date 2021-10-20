---
title:  "Referential integrity constraint violation"
excerpt: "JPA에서 연관관계로 맺어진 엔티티의 삭제 시 주의점"
date:   2021-10-26 22:03:00 
header:
  teaser: /assets/images/spring.png

categories: error
tags:
  - Java
  - Spring
  - 오류
  - error
last_modified_at: 2021-10-26T22:03:00
---

<br/><br/>

#### <span style="color:red">org.h2.jdbc.JdbcSQLIntegrityConstraintViolationException: Referential integrity constraint violation: "FKES2P3MEP278N5EXB8IBFU1PAH: PUBLIC.RECOMMEND FOREIGN KEY(POST_ID) REFERENCES PUBLIC.POST(POST_ID) (3)"; SQL statement: delete from post where post_id=? [23503-200]</span>

<br/>

#### 연관관계의 주인인 테이블에 속한 엔티티를 삭제하려 할 때, 발생하는 오류

무슨 말이냐 하면..

나는 현재 Post와, Recommend, 그리고 Member를 테이블로 가지고 있다.

Post에 좋아요를 누르게 되면, Recommend에 

![image-20211020222236436](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211020222236436.png)

다음과 같이, 좋아요를 누른 사람과, POST_ID를 FK로 가지고 있다.

이러한 상황에서 id가 3번인 POST를 지우려고 하였을 때 저 오류가 발생하였다.

<br/>

<br/>

#### 해결

POST에

```java
@OneToMany(mappedBy = "post", cascade = CascadeType.ALL, orphanRemoval = true)
private List<Recommend> recommends = new ArrayList<>();
```

다음과 같이 cascade = CascadeType.ALL, orphanRemoval = true속성을 추가하여,  POST가 삭제될 때 Recommned도 같이 삭제되게 만들었다.

