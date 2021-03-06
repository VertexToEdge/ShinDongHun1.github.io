---
title:  "기존 테스트에 시큐리티 적용하기"
excerpt: "스프링 부트와 AWS로 혼자 구현하는 웹 서비스 4-5"
date:   2021-11-24 18:36:00 
header:
  teaser: /assets/images/spring.png

categories: purpleBook
tags:
  - Java
  - Spring
last_modified_at: 2021-11-24T18:36:00



---

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124204433310.png" alt="image-20211124204433310" style="zoom:30%;" />

<br/>

## 기존 테스트에 시큐리티 적용하기

지금까지 우리는 시큐리티를 이용하여 로그인을 진행하였다. 로그인을 구현하기 전에는 API를 바로 호출할 수 있어서 테스트 코드 역시 바로 API를 호출하도록 구성하였다.

그러나 이제는 시큐리티의 옵션을 활성화하였기 때문에 인증을 해야만 API를 호출할 수 있다.

기존의 테스트에 인증한 사용자가 API를 호출한 것 처럼 코드를 수정해보자.

<br/>

#### 기존 테스트 전부 실행

![image-20211124181202262](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124181202262.png)

하나씩 확인해 보자.

<br/>

<br/>

### hello가_리턴된다()

![image-20211124181326233](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124181326233.png)

##### 문제 : CustomOAuth2UserService를 생성하는데 피요한 소셜 로그인 관련 설정값들이 없기 때문에 발생한다.

우리는 소셜 로그인 관련 설정을 application-oauth.properties에 추가했었다. 그런데 왜 없다고 뜨는 것일까?

##### 이는 src/main 환경과 src/test 환경의 차이 때문이다.

둘을 각자만의 환경 구성을 가진다. 다만 src/main/resources/application.properties가 테스트 코드를 수행할 때에도 적용되는 이유는 **<span style="color:orange">test에  application.properties속성이 없으면 main의 설정을 그대로 가져오기 때문</span>이다.**

다만 자동으로 가져오는 옵션의 범위는 application.properties 까지이기 때문에 application-oauth.properties는 test 파일에 없다고 해서 가져오지 않는다.

이 문제를 해결하기 위해 test 환경을 위한 application.properties를 만들겠다.

실제로 구글 연동을 진행할 것은 아니므로 가짜 설정값을 등록한다.

<br/>

##### test/resources/application.properties

```properties
spring.jpa.show_sql=true
spring.h2.console.enabled=true
spring.session.store-type=jdbc


#Test OAuth

spring.security.oauth2.client.registration.google.client-id=test;
spring.security.oauth2.client.registration.google.client-secret=test;
spring.security.oauth2.client.registration.google.scope=profile,email
```

<br/>

<br/>

### 302 Status Code 

두 번째로 [Posts_등록된다] 테스트 로그를 확인하자

![image-20211124183025325](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124183025325.png)

응답의 결과로 200을 원했는데 302가 와서 실패했다. 이는 시프링 시큐리티 설정 때문에 인증되지 않는 사용자의 요청은 이동시키기 때문이다. 그래서 이런 api 요청은 임의로 인증된 사용자를 추가하여 API만 테스트해 볼 수 있게 하겠다.

##### 스프링 시큐리티 테스트를 위한 spring-security-test를 build.gradle 에 추가하자.

```properties
implementation 'org.springframework.security:spring-security-test'
```

그리고 PostsApiControllerTest의 2개 테스트 메소드에 다음과 같이 임의 사용자 인증을 추가하자.

![image-20211124183400780](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124183400780.png)

##### 다음은 전체 코드이다.

```java
package web.purplebook.web;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.web.server.LocalServerPort;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.test.context.support.WithMockUser;
import web.purplebook.domain.posts.Posts;
import web.purplebook.repository.PostsRepository;
import web.purplebook.web.dto.PostsSaveRequestDto;
import web.purplebook.web.dto.PostsUpdateRequestDto;

import java.util.List;

import static org.assertj.core.api.Assertions.*;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class PostsApiControllerTest {

    @LocalServerPort private int port;
    @Autowired private TestRestTemplate restTemplate;
    @Autowired private PostsRepository postsRepository;

    @AfterEach
    public void tearDown() throws Exception{
        postsRepository.deleteAll();
    }

    @Test
    @WithMockUser(roles = "USER")
    public void Posts_등록된다() throws Exception {
        //given
        String title = "title";
        String content = "content";
        PostsSaveRequestDto requestDto = PostsSaveRequestDto.builder()
                .title(title)
                .content(content)
                .author("author")
                .build();

        String url = "http://localhost:"+port+"/api/v1/posts";

        //when
        ResponseEntity<Long> responseEntity = restTemplate.postForEntity(url, requestDto, Long.class);

        //then
        assertThat(responseEntity.getStatusCode()).isEqualTo(HttpStatus.OK);
        assertThat(responseEntity.getBody()).isGreaterThan(0L);

        List<Posts> all = postsRepository.findAll();
        assertThat(all.get(0).getTitle()).isEqualTo(title);
        assertThat(all.get(0).getContent()).isEqualTo(content);

    }
    @Test
    @WithMockUser(roles = "USER")
    public void Posts_수정된다() throws Exception {
        //given
        Posts savePosts = postsRepository.save(Posts.builder()
                .title("title")
                .content("content")
                .author("author")
                .build());

        Long updateId = savePosts.getId();
        String expectedTitle = "title2";
        String expectedContent = "content2";

        PostsUpdateRequestDto requestDto = PostsUpdateRequestDto.builder()
                .title(expectedTitle)
                .content(expectedContent)
                .build();

        String url = "http://localhost:"+port+"/api/v1/posts/"+updateId;
        HttpEntity<PostsUpdateRequestDto> requestEntity = new HttpEntity<>(requestDto);

        //when
        ResponseEntity<Long> responseEntity = restTemplate.exchange(url, HttpMethod.PUT, requestEntity, Long.class);

        //then
        assertThat(responseEntity.getStatusCode()).isEqualTo(HttpStatus.OK);
        assertThat(responseEntity.getBody()).isGreaterThan(0L);

        List<Posts> all = postsRepository.findAll();
        assertThat(all.get(0).getTitle()).isEqualTo(expectedTitle);
        assertThat(all.get(0).getContent()).isEqualTo(expectedContent);

    }

}
```

그런데 실행해 봐도 작동하지 않는다. 

##### @WithMockUser가 MockMvc에서만 작동하기 때문이다. 

현재 PostApiControllerTest 는 @SpringBootTest로만 되어있으며 MockMVC를 전혀 사용하지 않습니다. 그래서 @SpringBootTest에서 MockMvc를 사용하는 방법을 소개하겠다. 코드를 다음과 같이 변경한다.

<br/>

```java
package web.purplebook.web;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.web.server.LocalServerPort;
import org.springframework.http.*;
import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.security.test.web.servlet.setup.SecurityMockMvcConfigurers;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;
import web.purplebook.domain.posts.Posts;
import web.purplebook.repository.PostsRepository;
import web.purplebook.web.dto.PostsSaveRequestDto;
import web.purplebook.web.dto.PostsUpdateRequestDto;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;


@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class PostsApiControllerTest {

    @LocalServerPort private int port;
    @Autowired private TestRestTemplate restTemplate;
    @Autowired private PostsRepository postsRepository;

    @Autowired
    private WebApplicationContext context;//[추가]
    private MockMvc mvc;//[추가]
    @BeforeEach//[추가]
    public void setup(){
        mvc = MockMvcBuilders
                .webAppContextSetup(context)
                .apply(SecurityMockMvcConfigurers.springSecurity())
                .build();
    }


    @AfterEach
    public void tearDown() throws Exception{
        postsRepository.deleteAll();
    }


    @Test
    @WithMockUser(roles = "USER")
    public void Posts_등록된다() throws Exception {
        //given
        String title = "title";
        String content = "content";
        PostsSaveRequestDto requestDto = PostsSaveRequestDto.builder()
                .title(title)
                .content(content)
                .author("author")
                .build();

        String url = "http://localhost:"+port+"/api/v1/posts";

        //when -> [수정]
        mvc.perform(post(url)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(new ObjectMapper().writeValueAsString(requestDto)))
                        .andExpect(status().isOk());


        //then
        List<Posts> all = postsRepository.findAll();
        assertThat(all.get(0).getTitle()).isEqualTo(title);
        assertThat(all.get(0).getContent()).isEqualTo(content);

    }

    @Test
    @WithMockUser(roles = "USER")
    public void Posts_수정된다() throws Exception {
        //given
        Posts savePosts = postsRepository.save(Posts.builder()
                .title("title")
                .content("content")
                .author("author")
                .build());

        Long updateId = savePosts.getId();
        String expectedTitle = "title2";
        String expectedContent = "content2";

        PostsUpdateRequestDto requestDto = PostsUpdateRequestDto.builder()
                .title(expectedTitle)
                .content(expectedContent)
                .build();

        String url = "http://localhost:"+port+"/api/v1/posts/"+updateId;
        HttpEntity<PostsUpdateRequestDto> requestEntity = new HttpEntity<>(requestDto);

        //when -> [수정]
        mvc.perform(put(url)
                .contentType(MediaType.APPLICATION_JSON)
                .content(new ObjectMapper().writeValueAsString(requestDto)))
                .andExpect(status().isOk());

        //then


        List<Posts> all = postsRepository.findAll();
        assertThat(all.get(0).getTitle()).isEqualTo(expectedTitle);
        assertThat(all.get(0).getContent()).isEqualTo(expectedContent);

    }

}
```

##### 추가 또는 수정을 달아두었다. 테스트를 실행하면, 

![image-20211124184850450](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124184850450.png)

잘 된다.

<br/>

<br/>

### @WebMvcTest에서 CustomOAuth2UserService를 찾을 수 없음

제일 앞에서 발생한 [hello가_리턴된다] 테스트를 확인해 보자. 처음 문제와 동일하게 

> ##### No qualifying bean of type 'web.purplebook.config.auth.CustomOAuth2UserService' 

다음 에러가 발생한다

우리가 설정한 테스트 전용 시큐리티 설정은 잘 작동했지만 @WebMvcTest는 CustomOAuth2UserService 를 스캔하지 않는다.

<br/>

##### @WebMvcTest는 WebSecurityConfigurerAdapter, WebMvcCOnfigurer를 비롯한 @Controller와 @ControllerAdvice를 읽는다. 

##### 그러나 @Repository, @Service, @Component등은 스캔 대상이 아니다.

그러니 SecurityConfig는 읽지만, SecurityConfig를 생성하기 위한 CustomOAuth2UserService는 읽을 수 없어 에러가 발생한다.

##### 이 문제를 해결하기 위해 다음과 같이 스캔 대상에서 SecurityConfig를 제거한다.

```java
@WebMvcTest(controllers = HelloController.class,
            excludeFilters = {
        @ComponentScan.Filter(type = FilterType.ASSIGNABLE_TYPE,
        classes = SecurityConfig.class)
            })
```

<br/>

##### 그리고 여기서도 마찬가지로 @WithMockUser를 사용해서 가짜로 인증된 사용자를 생성한다.

```java
package web.purplebook.web;

import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.FilterType;
import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
import web.purplebook.config.auth.SecurityConfig;


@WebMvcTest(controllers = HelloController.class,
            excludeFilters = {
        @ComponentScan.Filter(type = FilterType.ASSIGNABLE_TYPE,
        classes = SecurityConfig.class)
            })
class HelloControllerTest {

    @Autowired
    private MockMvc mvc;

    @Test
    @WithMockUser(roles = "USER")
    public void hello가_리턴된다() throws Exception {
        String hello = "hello";

        mvc.perform(MockMvcRequestBuilders.get("/hello"))
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andExpect(MockMvcResultMatchers.content().string(hello));
    }

    @Test
    @WithMockUser(roles = "USER")
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

이제 테스트를 돌려보자.

그럼 다음과 같은 에러가 추가로 발생한다.

> ##### Caused by: java.lang.IllegalArgumentException: JPA metamodel must not be empty!

이 에러는 @EnableJpaAuditing으로 인해 발생한다. @EnableJpaAuditing을 사용하기 위해서는 최소 하나의 EntityClass가 필요하다. @WebMvcTest이다 보니 당연히 없다.

@EnableJpaAuditing가 @SpringBootApplication과 함께 있다보니 @WebMvcTest에서도 스캔하게 되었다.

그래서 @EnableJpaAuditing과 @SpringBootApplication 둘을 분리한다.

Application.java에서 @EnableJpaAuditing을 제거한다.

```java
package web.purplebook;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

//@EnableJpaAuditing [제거]
@SpringBootApplication
public class PurplebookApplication {

   public static void main(String[] args) {
      SpringApplication.run(PurplebookApplication.class, args);
   }

}
```

<br/>

##### 그리고 config 패키지에 JpaConfig를 생성하여 @EnableJpaAuditing을 추가한다.

```java
package web.purplebook.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@Configuration
@EnableJpaAuditing
public class JpaConfig {
}
```

##### 위치

![image-20211124190006437](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20211124190006437.png)

<br/>

##### 이제 다시 모든 테스트를 수행해보자!

![image-20211124190053938](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124190053938.png)

<br/>

성공이다.

<br/>

##### 이렇게 해서 지금까지 간단한 CRUD가 가능한 게시판 기능을 만들었고, 타임리프를 사용해 화면을 구성하였으며, 시큐리티와  OAuth로 인증과 권한을 배워보며 간단한 게시판을 모두 완성했다.

##### 이젠 드디어 AWS를 사용해서 서비스를 직접 배포하고 운영하는 과정을 진행해 보도록 하겠다.

<br/>

<br/>

### 📔 Reference

##### [스프링 부트와 AWS로 혼자 구현하는 웹 서비스] 211P~ 223P