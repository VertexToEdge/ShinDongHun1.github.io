---
title:  "AOP"
excerpt: "스프링 AOP"
date:   2021-12-03 19:40:00 
header:
  teaser: /assets/images/spring.png

categories: javaSpring
tags:
  - Java
last_modified_at: 2021-12-03T19:40:00

---

 <br/>

## AOP

애플리케이션을 개발할 때 부가 기능을 각각의 기능마다 직접 추가하여 적용하려면 다음과 같은 문제점들이 발생한다.

- 부가 기능을 적용할 때 아주 많은 반복이 필요하다.
- 부가 기능이 여러 곳에 퍼져서 중복 코드를 만들어낸다.
- 부가 기능을 변경할 때 중복 때문에 많은 수정이 필요하다.
- 부가 기능의 적용 대상을 변경할 때 많은 수정이 필요하다.

이러한 문제점들을 해결하기 위해 개발자들은 부가 기능의 로직을 핵심 기능에서 분리하고 한 곳에서 관리하려고 많은 노력을 하였고, 그 결과 부가 기능과 부가 기능을 어디에 적용할지 선택하는 기능을 합해서 하나의 모듈로 만들었다. 이것이 애스펙트(aspect)이다.

 <br/>

#### 애스펙트?

애스펙트는 우리말로 해석하자면 관점이라는 뜻이다. 이름 그대로 애플리케이션을 바라보는 관점을 하나하나의 기능에서 횡단 관심사(cross-cutting concerns)관점으로 달리 보는것이다.

##### 이렇게 애스펙트를 사용한 프로그래밍 방식을 관점 지향 프로그래밍 AOP(Aspect-Oriented Programming)이라 한다.

참고로 AOP는 OOP(Object-Oriented Programming)를 대체하기 위한 것이 아니라 횡단 관심사를 깔끔하게 처리하기 어려운 OOP의 부족한 부분을 보조하는 목적으로 개발되었다.

 <br/>

#### AspectJ 프레임워크

AOP의 대표적인 구현으로 [AspectJ 프레임워크](https://www.eclipse.org/aspectj/)가 있다. 물론 스프링도 AOP를 지원하지만 대부분 AspectJ의 문법을 차용하고, AspectJ가 제공하는 기능의 일부만 제공한다.

 <br/>

 <br/>

## 용어

### 조인 포인트 - Join Point

- 어드바이스가 적용될 수 있는 위치. (메소드 실행, 생성자 호출, 필드 값 접근, static 메서드 접근 등)

- 조인 포인트는 추상적인 개념으로, AOP를 적용할 수 있는 모든 지점이라 생각하면 된다.
- **스프링 AOP는 프록시 방식을 사용하므로 조인 포인트는 항상 <span style="color:orange">메소드 실행 지점</span>으로 제한된다.**

### 포인트컷 - Pointcut

- 조인 포인트 중에서 **<span style="color:orange">어드바이스가 적용될 위치를 선별</span>**하는 기능
- 주로 AspectJ표현식을 사용해서 지정

### 타겟 - Target

- 어드바이스를 받는 객체, 포인트컷으로 지정

### 어드바이스 - Advice

- 부가 기능

### 애스펙트 - Aspect

- 어드바이스 + 포인트컷을 모듈화 한 것
- @Aspect 
- 여러 어드바이스와 포인트컷이 함께 존재

### 어드바이저 - Advisor

- 하나의 어드바이스와 하나의 포인트컷으로 구성
- 스프링 AOP에서만 사용되는 특별한 용어

### 위빙 - Weaving

- 포인트컷으로 결정한 타겟의 조인 포인트에 어드바이스를 적용하는 것
- 위빙을 통해 핵심 기능 코드에 영향을 주지 않고 부가 기능을 추가할 수 있음

### AOP 프록시

- AOP 기능을 구현하기 위해 만든 프록시 객체, 스프링에서는 JDK 동적 프록시 또는 CGLIB 프록시이다.

 <br/>

 <br/>

## @Aspect AOP

스프링 애플리케이션에 프록시를 적용하려면 포인트컷과 어드바이스로 구성된 어드바이저를 만들어서 스프링 빈으로 등록해야 했다. 그러면 프록시 자동 생성기인 AnnotationAwareAspectJAutoProxyCreator가 모두 자동으로 처리해 주었다.

<br/>

##### 스프링은 @Aspect 애노테이션으로 매우 편리하게 포인트컷과 어드바이스로 구성되어 있는 어드바이저 생성 기능을 지원한다.

<br/>

```java
@Slf4j
@Aspect
public class CustomAspect {
	
	@Around("execution(* hello.proxy.app..*(..))")//포인트컷
	public Object execute(ProceedingJoinPoint joinPoint) throws Throwable{
		//어드바이스 로직
	}
}
```

<br/>

<br/>

### 자동 프록시 생성기의 역할 

##### AnnotationAwareAspectJAutoProxyCreator은 두 가지 역할을 한다.

1. @Aspect를 보고 어드바이저로 변환해서 저장한다(@Aspect 어드바이저 빌더를 통해 생성한다.)
2. 어드바이저를 기반으로 프록시를 생성한다

<br/>

#### @Aspect 어드바이저 빌더

##### BeanFactoryAspectJAdvisorBuilder 클래스이다. @Aspect의 정보를 기반으로 포인트컷, 어드바이스, 어드바이저를 생성하고 보관하는 것을 담당한다.

<br/>

<br/>

### 📔 Reference

##### [인프런 - 스프링 핵원 원리 - 고급편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B3%A0%EA%B8%89%ED%8E%B8/dashboard)