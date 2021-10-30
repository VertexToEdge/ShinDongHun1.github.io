---
title:  "연관된 컬렉션과, 컬렉션의 컬렉션 조회, DISTINCT에 대하여"
excerpt: "정리 안하면 까먹고 고통받을까봐 정리해두는 글"
date:   2021-10-30 12:30:00
header:
  teaser: /assets/images/spring.png

categories: JPA
tags:
  - Java
  - Spring
  - JPA
  - QueryDSL
  - N+1 문제
  - JPA
last_modified_at: 2021-10-30T12:30:00



---

<br/>

## 여러 단계로 연관된 컬렉션을 조회하는 것에 대하여

##### 어떤 식으로 말을 전해야 할 지 몰라서, 너무 없어보이지만 이렇게라도 적어놓는다.

##### 여러 단계로 연관된 컬렉션이라 함은... 예를 들어보자.

### 예시

##### Post는 Comment의 목록을 컬렉션으로 가진다.(게시물에는 여러 댓글이 달릴 수 있음)

##### 하나의 Comment는 Re-Comment의 목록을 컬렉션으로 가진다(댓글에는 여러 대댓글들이 달릴 수 있음)

<br/>

##### 결론적으로 1개의 포스터를 조회하는 경우, Comment 컬렉션과, 각각의 Comment가 가진 Re-Comment의 컬렉션을 모두 조회해야 한다.

<br/>

<br/>

### 구하려는 것

##### Post의 달려있는 댓글과, 대댓글의 총 개수를 구하고 싶었다. (내용 X, 오직 개수만)

##### 그냥 뭐 정말 아무 생각 없이 구현하자면

```java
int total=0;
total = commentList.size();
for (Comment comment : commentList) {
	total+=comment.getReCommentList().size();
}
```

##### 이런식으로 구현할 수 있겠다.

##### 그러나 이건 comment를 구할 때  쿼리가 1번(batchSize에 따라서 더 늘어날 수 있음), 각각의 comment에 대해 getRecCommentList를 구할 때 1번씩, 

##### 총 comment의 개수(N) + 1만큼 쿼리가 발생한다

<br/>

<br/>

### 그래서 뭐... 또 결국 쿼리를 줄이는 방법을 고민했다...

<script src="https://gist.github.com/ShinDongHun1/69e6bb617bcf7b69c5510d86aed73b89.js"></script>

##### 결론적으로 이 코드를 만들었다.

##### 당연히 이것보다 더 좋은 코드가 있을테지만 나는 개멍청이 초보이기 때문에 이정도로 만족한다 일단은..

##### 코드를 작성하면서 고민을 한 포인트는 두개였다.

##### 1. post.comments 는 연관관계가 있으니 그렇다 쳐도, reComment는 어떻게 가져오지?

##### 2. distinct로 결국 해결했는데, 그럼 이전에 올렸던, 컬렉션 프로젝션  최적화에서도 distinct를 쓰면 굳이 groupingBy에 mapping 뭐 이것저것 안 해도 되는거 아니었나?

<br/>

<br/>

### 결론

##### 1. reComment는 left, 혹은 innerJoin을 사용하여 해결할 수 있었다. 

##### <span style="color:red">2. 컬렉션 프로젝션 최적화에서는 사용이 안되었다. 아직 잘 모르겠다...ㅠㅠ</span>

<br/>

<br/>

## 추가

##### <span style="color:red">지금 이 방법에서 페이징 하는게 굉장히 위험해보인다!!!!! 공부하고 수정할것!</span>

<br/>

<br/>

### 📔 Reference

##### 내 엄청난 두뇌