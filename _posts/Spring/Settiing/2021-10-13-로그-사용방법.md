---
title:  "로그 사용방법"
excerpt: "로그 사용방법"
date:   2021-10-13 17:43:00 +0900
header:
  teaser: /assets/images/spring.png

categories: setting
tags:
  - Java
last_modified_at: 2021-10-13T17:43:00-05:00



---

<br/>

<br/>

## 💡로깅 라이브러리

스프링 부트 라이브러리를 사용하면, 스프링 부트 로깅 라이브러리( spring-boot-starter-logging )가 함께 포함된다.

스프링 부트 로깅 라이브러리는 기본으로 다음 로깅 라이브러리를 사용한다.

- ##### SLF4J(인터페이스)

- Logback(구현체) - 실무에서는 스프링 부트가 기본으로 제공하는 Logback을 대부분 사용

<br/>

##### 로그 선언

- private Logger log = LoggerFactory.getLogger(getClass()); 

- private static final Logger log = LoggerFactory.getLogger(Xxx.class) 

- ##### @Slf4j : 롬복 사용 가능

<br/>

##### 로그 호출

- log.info("hello") 

<br/>

#### 로그 레벨 설정

##### application.properties에서 다음을 추가하자

```
#전체 로그 레벨 설정(기본 info)
logging.level.root=info

#hello.springmvc 패키지와 그 하위 로그 레벨 설정
logging.level.hello.springmvc=debug
```

<br/>

##### LEVEL: TRACE > DEBUG > INFO > WARN > ERROR 

- 개발 서버는 debug 출력 

- 운영 서버는 info 출력

<br/>

#### 로그 사용법

- ##### log.debug("data={}", data)

<br/>

<br/>

##### 참고 사이트

- SLF4J - http://www.slf4j.org 

- Logback - http://logback.qos.ch

- 스프링 부트 - https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.logging

