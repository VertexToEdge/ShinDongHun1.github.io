---
title:  "사용자 정의 리포지토리 구현하기"
excerpt: "데이터 JPA 커스텀 리포지토리 만들기"
date:   2021-10-26 08:00:00
header:
  teaser: /assets/images/spring.png

categories: DATA
tags:
  - Java
  - Spring
  - JPA
  - DATA JPA
last_modified_at: 2021-10-26T08:00:00


---

<br/>

## 💡 사용자 정의 리포지토리 구현하기

##### 스프링 데이터 JPA의 문제점은, 다 interface로 되어있었기 때문에, 해당 인터페이스를 상속받으면 모든 기능을 구현해야하는 문제점이 있었다.

<br/>

##### 다양한 이유들로 인해 인터페이스의 메서드를 직접 구현하고 싶다면 어떻게 해야할까?

- ##### JPA 직접 사용(EntityManager)

- ##### <span style="color:orange">Querydsl 사용</span>

- ##### 스프링 JDBC Template 사용

- ##### 마이바티스 사용

- ##### 데이터베이스 커넥션 직접 사용 등등..

##### 이번에는 이를 해결할 수 있는 방법에 대해 알아보자.

<br/>

##### 🐹사용자 정의 인터페이스

```java
public interface MemberRepositoryCustom {
	List<Member> findMemberCustom();
}
```

<br/>

##### 🐹 사용자 정의 인터페이스 구현체

```java
@RequiredArgsConstructor
public class MemberRepositoryImpl implements MemberRepositoryCustom {
	
    private final EntituManager em;
    
	@Override
	List<Member> findMemberCustom(){
		return em.createQuery("select m from Member m").getResultList();
	}
}
```

<br/>

##### 🐹 JpaRepository 상속받은 interface에 추가로 상속

```java
public interface MemberRepository extends JpaRepository<Member, Long>, MemberRepositoryCustom{
}
```

<br/>

##### 🐹 사용은 MemberRepository를 사용

```java
@Autowired
private MemberRepository memberRepository;

@Test
public void callCustom(){
    List<Member> result = memberRepository.findMemberCustom();
}
```

<br/>

### 👿규칙

##### MemberRepositoryImpl에서 MemberRepository + Impl을 반드시 맞춰주어야 한다.(두개의 인터페이스 중 아무 인터페이스나 상관없으나, 꼭 인터페이스의 이름 + Impl을 붙여주어야 한다)

<br/>

<br/>

#### Impl 대신 다른 이름으로 변경하고 싶으면?

##### 🐹JavaConfig 설정

```java
@EnableJpaRepositories(basePackages = "study.datajpa.repository", repositoryImplementationPostfix = "Impl")
```

<br/>

<br/>

#### 추가로 항상 사용자 정의 리포지토리가 필요한 것은 아니다.

##### 예를들어 화면에 맞춘 DTO를 바로 조회하는 등의 기능을 가진 리포지토리는 임의의 리포지토리를 만들고, 스프링 빈으로 등록해서 사용하는 것이 유지보수의 관점에서 훨씬 좋다. 물론 이 경우 스프링 데이터 JPA와는 아무런 관계 없이 별도로 동작한다.

<br/>

<br/>

### 📔 Reference

[인프런 - 실전! 스프링 데이터 JPA](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EB%8D%B0%EC%9D%B4%ED%84%B0-JPA-%EC%8B%A4%EC%A0%84/dashboard)

