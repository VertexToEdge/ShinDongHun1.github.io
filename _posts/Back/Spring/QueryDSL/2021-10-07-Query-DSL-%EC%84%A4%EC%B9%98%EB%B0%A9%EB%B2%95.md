---
title:  "Query DSL 설치방법"
excerpt: "Query DSL 설치방법"
date:   2021-10-07 09:09:00 +0900
header:
  teaser: /assets/images/spring.png

categories: QueryDSL
tags:
  - Java
  - Spring
  - QueryDSL
last_modified_at: 2021-10-07T09:09:00-05:00

---



<br/>

## <br/>💡 설치방법

### build.gradle 파일에 추가

#### 🐬 plugins에 추가

```java
//querydsl 추가
id "com.ewerk.gradle.plugins.querydsl" version "1.0.10"
```

<br/>

#### 🐬 dependencies에 추가

```java
//querydsl 추가
implementation 'com.querydsl:querydsl-jpa'
annotationProcessor group: 'com.querydsl', name: 'querydsl-apt', version: '4.3.1'
```

<br/>

#### 🐬 맨 아래 부분에 새로 생성

```java
//querydsl 추가 시작
def querydslDir = "$buildDir/generated/querydsl"
querydsl {
   jpa = true
   querydslSourcesDir = querydslDir
}
sourceSets {
   main.java.srcDir querydslDir
}
configurations {
   querydsl.extendsFrom compileClasspath
}
compileQuerydsl {
   options.annotationProcessorPath = configurations.querydsl
}
//querydsl 추가 끝
```

##### 무슨 소린지 잘 모르겠다면

![image-20211007094348613](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211007094348613.png)

이런 식으로 설정해주면 된다!

<br/>

이렇게 설정했다면 reflesh 후 잘 설정되었는지 테스트를 해보자

<br/>

<br/>

### Hello.java

![image-20211007094721348](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211007094721348.png)

<br/>

다음과 같은 Hello 클래스를 만든 후.

![image-20211007094820420](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211007094820420.png)

인텔리제이 우측 상단에 Gradle을 누르고, other, compileQuerydsl을 클릭해주자

<br/>![image-20211007094943695](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211007094943695.png)

이렇게 초록 체크표시가 뜨면 성공!

<br/>

![image-20211007095114621](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211007095114621.png)

build -> generated -> querydsl -> 그 후 main 파일의 Hello가 있는 경로와 동일하게 QHello가 생긴것을 볼 수 있다.

![image-20211007095232447](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211007095232447.png)

우리가 아까 build.gradle에 설정할 때 이렇게 위치를 잡아주었기 때문에 이 위치에 생성된 것이며, 

##### Query DSL은 깃허브에 올려서 관리하면 안된다!

build 파일은 기본적으로 gitIgnore 되기 때문에, 다음과 같이 설정했다면 굳이 신경 쓸 필요는 없다! 

<br/>

<br/>

#### 추가로 cmd로 컴파일도 가능하다

- ##### gradlew compileQuerydsl 

- ##### gradlew compilejava 
