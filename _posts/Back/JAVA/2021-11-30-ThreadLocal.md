---
title:  "ThreadLocal"
excerpt: "쓰레드 로컬 사용법"
date:   2021-11-30 16:50:00 
header:
  teaser: /assets/images/spring.png

categories: java
tags:
  - Java
  - Spring
last_modified_at: 2021-11-30T16:50:00


---

<br/>

<br/>

## 💡 ThreadLocal

해당 쓰레드만 접근할 수 있는 특별한 저장소이다. 여러 쓰레드에서 같은 쓰레드 로컬 저장소를 사용하더라도, 쓰레드에 따라 다른 정보를 저장할 수 있다.

<br/>

#### 일반적인 변수 필드

여러 쓰레드가 같은 인스턴스의 필드의 접근하면 처음 쓰레드가 보관한 데이터가, 이후에 접근한 쓰레드에 의해 사라질 수 있다.

<br/>

#### 쓰레드 로컬

쓰레드 로컬을 사용하면 각 쓰레드마다 별도의 내부 저장소를 제공한다. 따라서 같은 인스턴스의 쓰레드 로컬 필드에 접근해도 문제가 없다.

<br/>

<br/>

### 사용법

```java
ThreadLocal<String> nameStore = new ThreadLocal<>();


//저장
nameStore.set("신동훈");

//조회
nameStore.get();

//삭제
namteStore.remove();
```

##### ThreadLocal<타입> 

- 위와 같이 선언해주면 된다.
- 값을 저장할때는 set을 사용한다.
- 값을 조회할때는 get을 사용한다.
- 값을 제거할때는 remove를 사용한다.

<br/>

<br/>

### 주의 

해당 쓰레드가 쓰레드 로컬을 모두 사용하고 나면 ThreadLocal.remove()를 호출해서 쓰레드 로컬에 저장된 값을 제거해주어야 한다. 

##### 쓰레드 로컬의 값을 사용 후 제거하지 않고 그냥 두면 WAS(톰캣)처럼 쓰레드 풀을 사용하는 경우에 심각한 문제가 발생할 수 있다.

<br/>![image-20211130184808579](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211130184808579.png)

1. ##### 사용자A가 저장 HTTP를 요청한다

2. ##### WAS는 쓰레드 풀에서 쓰레드를 하나 조회한다.

3. ##### 쓰레드 A가 할당되었다

4. ##### 쓰레드 A는 사용자A의 데이터를 쓰레드 로컬에 저장한다.

5. ##### 쓰레드 로컬의 쓰레드A 전용 보관소요 사용자A의 데이터를 보관한다

<br/>

![image-20211130185133450](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211130185133450.png)

1. 사용자 A의 HTTP 응답이 끝난다.
2. WAS는 사용이 끝난 쓰레드A를 쓰레드 풀에 반환한다. 쓰레드를 생성하는 비용은 비싸기 때문에 쓰레드를 제거하지 않고 재사용한다.
3. 쓰레드A는 쓰레드풀에 아직 살아있으므로, 쓰레드 로컬의 쓰레드A 전용 보관소에 저장된 사용자 A의 데이터도 남아있다.

<br/>

![image-20211130185712253](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211130185712253.png)

1. 사용자B 가 조회를 위한 새로운 HTTP요청을 한다.
2. WAS는 쓰레드 풀에서 쓰레드를 하나 조회한다.
3. 쓰레드A가 할당되었다.
4. 조회하는 요청이므로 쓰레드A는 쓰레드 로컬에서 데이터를 조회한다.
5. 쓰레드 로컬은 쓰레드A 전용 보관소에 있는 사용자A 의 데이터를 반환한다.
6. 사용자B는 사용자A의 정보를 조회하게 된다.

<br/>

##### 이런 문제를 예방하기 위해 ThreadLocal.remove()를 통해서 꼭 제거해야 한다.

<br/>

<br/>

### 📔 Reference

##### [ThreadLocal 사용법과 활용](https://javacan.tistory.com/entry/ThreadLocalUsage)

##### [인프런 - 스프링 핵원 원리 - 고급편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B3%A0%EA%B8%89%ED%8E%B8/dashboard)