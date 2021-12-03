---
title:  "Inner Class를 스프링 빈으로 등록하는 경우 주의점"
excerpt: "Inner Class를 스프링 빈으로 등록하는 경우 주의점"
date:   2021-12-04 07:33:00 
header:
  teaser: /assets/images/spring.png

categories: javaSpring
tags:
  - Java
  - Spring
last_modified_at: 2021-12-04T07:33:00
---

<br/>

##### Inner Class를 스프링 빈으로 등록하는 경우 static 키워드를 붙여주지 않으면 오류가 발생한다.

코드를 통해 확인하자.

```java
@SpringBootTest
class InnerClassTests {

	@Test
	void AutowiredOption() {
		ApplicationContext ac = new AnnotationConfigApplicationContext(InnerClass.class);
	}

	class InnerClass {
		@Autowired
		public void setNoBean1(){

		}
	}

}

```

##### <span style="color:red">org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'InnerClassTests.InnerClass': Unsatisfied dependency expressed through constructor parameter 0; nested exception is org.springframework.beans.factory.NoSuchBeanDefinitionException: No qualifying bean of type 'com.cnupost.cnupost.InnerClassTests' available: expected at least 1 bean which qualifies as autowire candidate. Dependency annotations: {}</span>

뭐 이런 오류가 뜰것인데 InnerClass를 static 클래스로 바꾸어주면 해결된다.

##### 이유는 아래 Reference를 참고하자

<br/>

<br/>

### 📔 Reference

##### [https://www.inflearn.com/questions/257297](https://www.inflearn.com/questions/257297)

##### [https://www.inflearn.com/questions/110694](https://www.inflearn.com/questions/110694)