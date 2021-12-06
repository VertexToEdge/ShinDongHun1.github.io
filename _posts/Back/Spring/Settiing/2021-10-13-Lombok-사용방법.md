---
title:  "Lombok 사용방법"
excerpt: "Lombok 사용방법"
date:   2021-10-13 17:33:00 +0900
header:
  teaser: /assets/images/spring.png

categories: setting
tags:
  - Java
last_modified_at: 2021-10-13T17:33:00-05:00


---

<br/>

<br/>

## 💡Lombok 설치

<br/>

##### build.gradle로 이동하여 의존성 추가

```properties
compileOnly 'org.projectlombok:lombok'
annotationProcessor 'org.projectlombok:lombok'

testCompileOnly 'org.projectlombok:lombok:1.18.12'
testAnnotationProcessor 'org.projectlombok:lombok:1.18.12'
```

<br/>

<br/>

#### 사용방법

#### 💻Settings -> Build , Execution, Deployment -> Complier -> Annotation Processors 이동

##### Enable annotation processiong 체크하기

![image-20211013172817345](C:/Users/huipu/AppData/Roaming/Typora/typora-user-images/image-20211013172817345.png)

<br/>

<br/>

#### 제공하는 어노테이션 확인

https://projectlombok.org/features/all