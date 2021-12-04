---
title:  "@Configuration"
excerpt: "@Configuration과 싱글톤"
date:   2021-09-19 00:19:00 
header:
  teaser: /assets/images/spring.png

categories: javaSpring
tags:
  - Java
  - Spring
last_modified_at: 2021-10-09T00:18:00

---

<br/>

## @Configuration

@Configuration은 스프링 설정 클래스를 선언하는 애노테이션이다.

@Configuration 어노테이션을 사용하면, 가시적으로 이 클래스는 스프링 빈 관련 설정 클래스임을 알 수 있다.

그러나 @Configuration에는 특별한 기능이 하나 있다

<br/>

<br/>

## @Configuration과 싱글톤

##### 다음 코드를 보자.

<script src="https://gist.github.com/ShinDongHun1/094daf07381198b26aa0eb0915fb5715.js"></script>

**memberService** 빈을 만드는 코드를 보면, memberRepository를 생성한다.<br/>memberRepository는 **new MemoryMemberRepository();를 실행**한다.

**orderService** 빈을 만드는 코드를 보면, memberRepository를 생성한다.<br/>memberRepository는 **new MemoryMemberRepository();**를 실행한다.

결과적으로는 각각 다른 2개의 MemoryMemberRepository가 생성되면서 싱글톤이 깨지는 것 처럼 보인다.

그러나 확인해보면 그렇지 않다는것을 알 수 있다.

<br/>

##### @Configuration은 스프링 빈을 싱글톤으로 유지시켜준다!

<br/>

<br/>

## @Configuration과 바이트코드 조작

앞서 배웠듯이 스프링 컨테이너는 싱글톤 컨테이너이다. 즉 스프링 빈을 싱글톤으로 관리해 주는 것이다.

스프링은 스프링 빈을 싱글톤으로 관리하기 위해 클래스의 **바이트코드를 조작하는 라이브러리를 사용**한다. 

<br/>

##### 다음과 코드를 실행 시켜 보자.

<script src="https://gist.github.com/ShinDongHun1/4bf8f77f78856e343a25a436511cd39b.js"></script>

##### 결과

> **bean = class hello.core.AppConfig$$EnhancerBySpringCGLIB$$bd479d70**

##### 순수한 클래스라면 다음과 같이 출력될 것이다.

`class hello.core.AppConfig `

<br/>

#### 이유

스프링이 **<span style="color:orange">CGLIB라는 바이트코드 조작 라이브러리를 사용</span>**해서 AppConfig 클래스를 **상속받은 임의의 다른 클래스**를 만들고, 그 다른 클래스를 **스프링 빈으로 등록**하였기 때문에 다음과 같이 출력되는 것이다.

![image-20211009232607416](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211009232607416.png)

<br/>

##### AppConfig@CGLIB 에서는 아마 다음과 같은 방식으로 코드가 작동할것이다

```java
...
@Bean
public MemberRepository memberRepository() {
	if(memoryMemberRepository가 이미 스프링 컨테이너에 등록되어 있다면){
 		return 스프링 컨테이너에서 찾아서 반환
	}
	else{
		기존 로직을 호출해서 MemoryMemberRepository를 생성하고 스프링 컨테이너에 등록
		return 반환
	}
}
...
```

<br/>

<br/>

### @Configuration을 적용하지 않고, @Bean만 적용한다면?

##### @Bean만 사용해도 스프링 빈으로 등록되지만, 싱글톤을 보장하지 않는다.

<br/>

<br/>

### 📔 Reference

##### [인프런 - 스프링 핵심 원리 -기본편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B8%B0%EB%B3%B8%ED%8E%B8/dashboard)

