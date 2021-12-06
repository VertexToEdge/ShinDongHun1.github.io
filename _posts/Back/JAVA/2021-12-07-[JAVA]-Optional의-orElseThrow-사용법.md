---
title:  "[JAVA] Optional의 orElseThrow 사용법"
excerpt: "Optional의 orElseThrow 사용"
date:   2021-12-07 03:52:00 
header:
  teaser: /assets/images/java.png

categories: java
tags:
  - Java
last_modified_at: 2021-12-07T03:52:00




---

<br/>

## Optional - orElseThrow

Optinal에 대해서는 설명하지 않고 orElseThrow를 사용하는 방법을 소개하겠다.

##### Supplier 클래스를 작성해주면 되는데, 이는 익명 클래스를 사용할 수 있으며, 따라서 람다식으로 사용 가능하다.

```java
Member member = memberRepository.findByUsername(username).orElseThrow(() -> new UsernameNotFoundException("찾는 정보 없음"));
```

<br/>

<br/>

### 📔 Reference

##### [Optional .orElseThrow(Function) 사용법](https://krksap.tistory.com/1515)