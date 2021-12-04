---
title:  "@ComponentScan"
excerpt: "컴포넌트 스캔"
date:   2021-09-19 08:58:00 +0900
header:
  teaser: /assets/images/spring.png

categories: javaSpring
tags:
  - Java
  - Spring
last_modified_at: 2021-10-10T00:08:00-05:00

---

<br/>

## @ComponentScan

`@ComponentScan` 은 `@Component`  및 `@Service`, `@Repository`, `@Controller`, `@Configuration`등과 같이 `@Component`가 붙어있는 Class들을 **자동으로 Scan하여 스프링 Bean으로 등록**해주는 역할을 한다.

<br/>

<br/>

## @ComponentScan의 작동원리

##### <span style="color:orange">@ComponentScan</span>은 <span style="color:orange">@Component</span>가 붙은 모든 클래스를 <span style="color:orange">스프링 빈</span>으로 등록한다.

![image-20211010000312169](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211010000312169.png)

메소드를 사용하는 @Bean과 달리 클래스에 사용되는 @Component는 빈의 이름을 지정할 때 **<span style="color:orange">클래스명을 사용</span>한다. 단 <span style="color:orange">맨 앞글자만 소문자</span>로 바꿔서 저장한다.**

EX) Member 클래스를 빈으로 등록하면 member가 된다.

<br/>

## @Autowired의 작동원리

@Autowired를 지정하면, 스프링 컨테이너가 자동으로 필요한 의존관계에 해당하는 스프링 빈을 찾아서 등록해준다.

![image-20211010000336427](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211010000336427.png)

주입할 때는 타입이 같은 빈을 찾아서 주입하는데 **같은 타입의 빈이 여러개면 기본적으로는 오류가 발생**한다.

<br/>

<br/>

## 탐색 위치

##### default값, 즉 기본적으로는 <span style="color:orange">@ComponentScan</span>이 붙은 클래스의 페키지를 시작 위치로 해서 하위 디렉토리를 탐색한다.

내가 범위를 지정해주고 싶다면 **@ComponentScan의  <span style="color:orange">basePackages</span> 속성**에 시작 위치를 지정하면 된다.

```java
@ComponentScan( basePackages = "hello.core" }
```

이러면 hello.core 패키지를 포함해서 하위에 있는 모든 패키지를 탐색한다.

참고로 **basePackageClasses**속성을 통해 클래스를 지정하면, 지정한 클래스의 패키지를 탐색 시작 위치로 지정할 수 있다.

#### 참고

스프링 부트를 사용하면 스프링 부트의 대표 시작 정보인 `@SpringBootApplication`를 프로젝트 시작 루트 위치에 두는 것이 관례이다. (`@SpringBootApplication`에도 `@ComponentScan`이 붙어있다.)

 <br/>

<br/>

## 스캔 기본 대상

- ##### @Componet - 기본

- ##### @Controller - 스프링 MVC 컨트롤러에서 사용

- ##### @Service - 스프링 비즈니스 로직에서 사용, 특별한 기능은 없으나 개발자들이 핵심 비즈니스 로직이 여기에 있겠구나 하고 인식하는 용도

- ##### @Repository - 스프링 데이터 접근 계층에서 사용, 데이터 계층의 예외를 스프링 예외로 변환

- ##### @Configuraton - 스프링 설정 정보에서 사용. 스프링 빈이 싱글톤을 유지하도록 추가 처리를 한다.

 <br/>

<br/>

## 필터

- **includeFilters : 컴포넌트 스캔 대상을 추가로 지정**
- **excludeFilters : 컴포넌트 스캔에서 제외할 대상을 지정**

#### 예시

##### 컴포넌트 스캔 대상에 추가하는 경우

```java
import java.lang.annotation.*;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface CustomIncludeComponent {
}
```
```java
@CustomIncludeComponent
public class IncludeClass {
}
```


##### 컴포넌트 스캔 대상에서 제외하는 경우

```java
import java.lang.annotation.*;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface CustomExcludeComponent {
}
```

```java
@CustomExcludeComponent
public class ExcludeClass {
}
```

##### 적용


```
@ComponentScan(
	includeFilters = {
		@ComponentScan.Filter(type=FilterType.ANNOTATION, classes=CustomIncludeComponent.class)
	},
	excludeFilters = {
		@ComponentScan.Filter(type=FilterType.ANNOTATION, classes=CustomExcludeComponent.class)
	}
	)
@Configuration
public class CustomConfig {
}
```

<br/>

#### FilterType의 옵션

- **ANNOTATION**: 기본값, 애노테이션을 인식해서 동작한다. 
- **ASSIGNABLE_TYPE**: 지정한 타입과 자식 타입을 인식해서 동작한다. 
- **ASPECTJ**: AspectJ 패턴 사용 
- **REGEX**: 정규 표현식 
- **CUSTOM**: `TypeFilter` 라는 인터페이스를 구현해서 처리 

<br/>

<br/>

## 빈 중복 등록과 충돌

빈 이름이 중복되는 경우에는 두 가지 상황이 있다.

- **자동 빈 등록 vs 자동 빈 등록** : 오류가 발생한다! 
  -  <span style="color:red">**ConflictingBeanDefinitionException**</span>
- **수동 빈 등록 vs 자동 빈 등록** : 수동 빈 등록이 우선권을 가진다(수동 빈이 자동 빈을 오버라이딩)
  - ##### 그러나 최근 스프링 부트에서는 오류가 발생하도록 기본 값을 바꾸었다.(원하면 설정 변경 가능)

<br/>

<br/>

### 📔 Reference

##### [인프런 - 스프링 핵심 원리 -기본편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B8%B0%EB%B3%B8%ED%8E%B8/dashboard)
