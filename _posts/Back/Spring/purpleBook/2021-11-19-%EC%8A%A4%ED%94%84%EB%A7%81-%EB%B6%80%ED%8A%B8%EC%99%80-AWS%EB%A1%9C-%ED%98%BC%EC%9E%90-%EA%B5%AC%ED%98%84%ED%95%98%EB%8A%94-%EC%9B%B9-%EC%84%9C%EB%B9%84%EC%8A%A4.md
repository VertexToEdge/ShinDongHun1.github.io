---
title:  "스프링 부트와 AWS로 혼자 구현하는 웹 서비스"
excerpt: "스프링 부트와 AWS로 혼자 구현하는 웹 서비스 1"
date:   2021-11-19 01:16:00 
header:
  teaser: /assets/images/spring.png

categories: purpleBook
tags:
  - Java
  - Spring
last_modified_at: 2021-11-19T01:16:00




---

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124204433310.png" alt="image-20211124204433310" style="zoom:30%;" />

<br/>

## 스프링 부트와 AWS로 혼자 구현하는 웹 서비스 따라하기

최근 웹 프로그래밍 대회에 나가면서, 기능을 구현하는 것 까지는 어느정도 할 수 있었으나, AWS를 사용하서 서버를 배포하는 부분이라던지, OAuth를 사용하여 로그인을 하는 부분(이부분은 어찌어찌 구현을 하긴 했지만 거의 코드를 복붙하는 수준..)에서 막혀서 너무 힘들었었고, 그럴 때마다 이 책을 사용해서 구현된 코드를 보고 베껴왔었다. 그럼에도 정확히 모든 내용이 담겨있는 것이 아니라 나의 코드에 적절히 녹여내지 못하였고, 시간이 너무 촉박해서 결국 서버를 배포하지 못하고 집에서 컴퓨터를 끄지 않고 평가가 끝날때까지 돌려두었다는..... ㅎㅎ...

아무튼 그래서 대회도 끝났겠다, 이번 기회에 서버 배포와 더불어, 무중단 배포 환경도 구축해보고 싶었기에 평소 눈에 자주 띄었던 이 책을 사서 공부해 보려고 한다. 

서론은 여기까지 하고, 이제 시작해보자.

<br/>

<br/>

## 프로젝트 생성하기

[https://start.spring.io/](https://start.spring.io/) 이곳으로 이동해서 다음과 같이 설정해주자. 

##### Artifact는 프로젝트의 이름이니 마음에 드는 이름으로 설정해주면 된다.



![image-20211119222419889](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211119222419889.png)

<br/>

GENERATE 버튼을 누르면 압축파일이 다운받아 질 것인데, 이것을 원하는 폴더에 압축해제를 시켜주자.

<br/>

![image-20211119222624048](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211119222624048.png)

##### build.gradle 파일을 우클릭하여 인텔리제이로 실행시켜주자

<br/>

아마 알아서 다 설정해주기 때문에, 여기까지 오류는 없었을 것이라 생각한다. 이제 깃허브와 연동해보자.

<br/>

<br/>

## 깃허브와 연동하기

윈도우에서느 Ctrl + Shift + A , 맥에서는 Command + Shift + A를 사용해서 Action 검색창을 열어 share project on github를 검색하자.

![image-20211119222937036](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211119222937036.png)

Add account 를 눌러 Log in via GitHub를 클릭 후 로그인해주자, 깃허브 아이디가 없다면 회원가입을 진행해주고, 모든 인증이 끝났다면 Share을 눌러주면 된다.

<br/>

![image-20211119223120487](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211119223120487.png)

책에는 설명이 없는데, 이러한 것들을 커밋할 것인지 묻는 것 같다. Add 해주자.

다음으로 자신의 깃허브 계정을 들어가 repositorues에 들어가보면

![image-20211119223253756](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211119223253756.png)

다음과 같이 푸시가 진행된 것을 볼 수 있다!

<br/>

<br/>

<br/>

## 스프링 부트에서 테스트 코드를 작성하자

### TDD 와 단위 테스트

TDD와 단위 테스트는 다른 이야기이다.

TDD는 테스트가 주도하는 개발이다. 테스트 코드를 먼저 작성하는 것부터 시작이다.

<br/>

##### 레드 그린 사이클 

- 항상 실패하는 테스트를 먼저 작성하고(Red)
- 테스트가 통과하는 프로덕션 코드를 작성하고(Green)
- 테스트가 통과하면 프로덕션 코드를 리팩토링한다.

<br/>

반면 단위 테스트는 TDD의 첫 번째 단계인 기능 단위의 테스트 코드를 작성하는 것을 이야기한다.

TDD와 달리 테스트 코드를 꼭 먼저 작성해야 하는것도 아니고, 리팩토링도 포함되지 않는다. 순수하게 테스트코드만 작성하는 것을 이야기한다.

여기서는 TDD가 아닌 단위 테스트 코드를 배운다. 

> TDD를 좀 더 알고 싶다면 다음 링크를 참고하자
>
> [채수원, TTD 실천법과 도구](https://repo.yona.io/doortts/blog/issue/1)
>
> [TDD(Test-Driven Development) 연습해보기 - 예제 1: Money (1) 1~8장](https://hororolol.tistory.com/518)
>
> 등등 구글 참고..

<br/>

## 컨트롤러 만들기

##### build.gradle에 추가.

다음과 같은 코드를 추가해주자. 

```properties
implementation 'org.springframework.boot:spring-boot-starter-web'
```

![image-20211119230601070](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211119230601070.png)



<br/>

web이란 패키지를 새로 생성한 후,HelloController라른 클래스를 생성해보자.

```java
package web.purplebook.web;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello(){
        return "hello";
    }
}
```

다음과 같이 코드를 작성하고 하나하나 살펴보자

- @RestController : @Controller + @ResponseBody 이며, JSON을 반환하는 컨트롤러로 만들어 준다.
- @GetMapping :HTTP Method인 Get의 요청을 받을 수 있는 API를 만들어준다. "/hello"로 들어오는 Get 요청에 대해서는 위 메서드가 작동한다.



이제 위 코드가 제대로 작동하는지 테스트를 해보자.

![image-20211119225704559](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211119225704559.png)

윈도우에서는 Ctrl + Shift + t 누르면 다음과 같이 TEST를 생성하는 알림이 나온다.



기본값을 따라 생성했다면 HelloControllerTest라는 클래스가 생성될 것인데, 일반적으로 테스트 클래스는 대상 클래스 이름에 Test를 붙인다.

```java
package web.purplebook.web;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;

@WebMvcTest(controllers = HelloController.class)
class HelloControllerTest {

    @Autowired
    private MockMvc mvc;

    @Test
    public void hello가_리턴된다() throws Exception {
        String hello = "hello";

        mvc.perform(MockMvcRequestBuilders.get("/hello"))
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andExpect(MockMvcResultMatchers.content().string(hello));

    }

}
```

다음과 같이 테스트 코드를 작성해보자.

- ##### WebMvcTest : 여러 스프링 어노테이션 중 Web(Spring MVC)에 집중할 수 있는 어노테이션이다. 선언할 경우 @Controller, @ControllerAdvice 등을 사용할 수 있다. 단 @Service, @Component, @Repository등은 사용할 수 없다. 여기서는 컨트롤러만 사용하기 때문에 선언한다.

- ##### Autowired : 스프링이 관리하는 빈(Bean)을 주입받는다.

- ##### MockMvc :  웹 API를 테스트할 때 사용한다. 이 클래스를 통해 HTTP GET , POST 등에 대한 API 테스트를 할 수 있다.

- ##### mvc.perform(MockMvcRequestBuilders.get("/hello")) : MockMvc를 통해 hello 주소로 get 요청을 한다.

- ##### andExpect : mvc.perform의 결과를 검증한다. HTTP header의 Status를 검증한다.

- ##### andExpect(MockMvcResultMatchers.content().string(hello)) : 응답 본문의 내용을 검증한다. 우리는 HelloController 클래스에서 "hello"를 리턴하게 했음으로,  이 값이 맞는지 검증한다.

<br/>

<br/>

## 롬복 설치하기

다음과 같은 코드를build.gradle 에 추가하자.

```properties
compileOnly 'org.projectlombok:lombok'
annotationProcessor 'org.projectlombok:lombok'

//테스트에서 lombok 사용
testCompileOnly 'org.projectlombok:lombok'
testAnnotationProcessor 'org.projectlombok:lombok'
```

![image-20211119231749564](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211119231749564.png)

##### 이후 Ctrl + Alt + S를 눌러서 다음과 같이 anno를 검색하여 Enable 어쩌고에 체크하자.

![image-20211119231841177](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211119231841177.png)

##### 이러면 롬복을 사용할 수 있다!

<br/>

<br/>

## Dto 개발하여 롬복 적용하기

web 패키지 아래에 dto 패키지를 만들어 dto들을 관리하자.

```java
@Getter
@RequiredArgsConstructor
public class HelloResponseDto {
    
    private final String name;
    private final int amount;
}
```

그런데 해당 코드를 작성하니까 다음과 같은 메세지가 떴다. Class can be a record.

record 클래스에 대해 언뜻 들어본 적은 있는 거 같은데 한번도 사용해 본 적이 없었다.

이번 기회에 한번 사용해 보겠다 하고 바꾸어보았다.

```java
public record HelloResponseDto(String name, int amount) {
}
```

다음과 같이 매우 간단하게 표현되었다. 

> 모든 record는 java.lang.Record 을 상속받은 클래스이다.
> record는 final class이고 선언할 때 적은 멤버들도 final이다.
> static 멤버를 만들 수도 있다.
> native 메소드는 만들 수 없다.
> 제네릭 된다.
> interface를 구현할 수 있다.
> annotation도 걸 수 있다.
> inner class는 좀 복잡하다. JDK 버전이 올라가면 바뀔 여지도 있는 듯하다.
>
> [참고 - Record](https://velog.io/@gilchris/Java-Record)

<br/>

### 컨트롤러에 DTO 추가하기.

```java
package web.purplebook.web;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import web.purplebook.web.dto.HelloResponseDto;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public HelloResponseDto hello(@RequestParam("name") String name,
                                  @RequestParam("amount") int amount){
        
        return new HelloResponseDto(name , amount);
    }
    
    
    //== 추가 ==//
    @GetMapping("/hello/dto")
    public HelloResponseDto hello(@RequestParam("name") String name,
                                  @RequestParam("amount") int amount){

        return new HelloResponseDto(name , amount);
    }
}
```

- ##### @RequestParam : 외부에서 API로 넘긴 파라미터를 가져오는 어노테이션이다.

- 여기서는 외부에서 name(@RequestParam("name"))이란 이름으로 넘긴 파라미터를 String name에 저장하게 된다.

이제 테스트 코드를 작성해보자.



```java
package web.purplebook.web;

import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;




@WebMvcTest(controllers = HelloController.class)
class HelloControllerTest {

    @Autowired
    private MockMvc mvc;

    @Test
    public void hello가_리턴된다() throws Exception {
        String hello = "hello";

        mvc.perform(MockMvcRequestBuilders.get("/hello"))
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andExpect(MockMvcResultMatchers.content().string(hello));
    }

    @Test
    public void helloDto가_리턴된다() throws Exception {
        String name = "hello";
        int amount = 1000;

        mvc.perform(
                MockMvcRequestBuilders.get("/hello/dto")
                        .param("name",name)
                        .param("amount",String.valueOf(amount)))

                        .andExpect(MockMvcResultMatchers.status().isOk())
                        .andExpect(MockMvcResultMatchers.jsonPath("$.name", Matchers.is(name)))
                        .andExpect(MockMvcResultMatchers.jsonPath("$.amount", Matchers.is(amount)));//import static org.hamcrest.Matchers.is;
    }
}
```

- ##### param : API 테스트할 때 사용될 요청 파라미터를 설정한다. 단 값은 String만 허용되며, 숫자/날짜 등의 데이터도 등록할 때는 문자열로 변경해야만 가능하다.

- ##### jsonPath : JSON 응답값을 필드별로 검증할 수 있는 메소드이다. $를 기준으로 필드명을 명시한다.

<br/>

<br/>

자 지금까지 Spring Web(MVC)와 테스트의 기본적인 기능들을 테스트 해 보았고, 다음에는 데이터 베이스를 다뤄보도록 하자.



<br/>

### 📔 Reference

[SpringBoot의 MockMvc를 사용하여 GET, POST 응답 테스트하기](https://shinsunyoung.tistory.com/52)

[Record 클래스](https://velog.io/@gilchris/Java-Record)

##### 스프링 부트와 AWS로 혼자 구현하는 웹 서비스 1~77P