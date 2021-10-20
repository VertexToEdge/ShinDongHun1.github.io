---
title:  "Pattern Matching"
excerpt: "패턴 매칭 사용법"
date:   2021-10-20 16:50:00 
header:
  teaser: /assets/images/spring.png

categories: java
tags:
  - Java
  - Spring
last_modified_at: 2021-10-20T16:50:00

---

<br/>

<br/>

## 💡 Pattern Matching 사용법

<script src="https://gist.github.com/ShinDongHun1/b79a823abc51a3ece512aeaff81371ed.js"></script>

해당 코드에서 instanceof를 사용한 부분을 보면

Post, Comment, Reply로의 형변환 가능 여부를 확인한 후, 

(Post) object 를 통해 직접 형변환을 해주는 것을 알 수 있다.

이 코드를 바꿔보자.

<br/>

#### 🔍 변경 후

<script src="https://gist.github.com/ShinDongHun1/9afd91061cf77e5a5b940af150d76440.js"></script>

<br/>

<br/>

##### 추가로 JAVA 17버전의 프리뷰에서는 Switch 문에서도 사용할 수 있게끔 만들었다!

<br/>

<br/>

#### 📔 Reference

[https://velog.io/@sinyoung3016/%EC%B0%A8%EA%B7%BC%EC%B0%A8%EA%B7%BC-%EA%B8%B0%EC%B4%88-%EB%8B%A4%EC%A7%80%EA%B8%B0-04-BackEnd-H2-Exception](https://velog.io/@sinyoung3016/%EC%B0%A8%EA%B7%BC%EC%B0%A8%EA%B7%BC-%EA%B8%B0%EC%B4%88-%EB%8B%A4%EC%A7%80%EA%B8%B0-04-BackEnd-H2-Exception)

[https://openjdk.java.net/jeps/305](https://openjdk.java.net/jeps/305)

[https://openjdk.java.net/jeps/406](https://openjdk.java.net/jeps/406)

