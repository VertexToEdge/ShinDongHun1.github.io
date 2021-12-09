---
title:  "JPA 사용하기 - 스프링 부트와 AWS로 혼자 구현하는 웹 서비스"
excerpt: "스프링 부트와 AWS로 혼자 구현하는 웹 서비스 2"
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

## JPA로 데이터베이스 다루기

### JPA 소개

현대의 웹 애플리케이션에서 관계형 데이터베이스(RDB)는 빠질 수 없는 요소이다. Oracle, MySQL 등을 쓰지 않는 웹 애플리케이션은 거의 없다.

그러다 보니 객체를 **관계형 데이터베이스에서 관리**하는 것이 무엇보다 중요하다.

그러나 RDB와 객체지향 프로그래밍 언어사이에는 **패러다임의 불일치**가 존재한다. (예를 들면 객체 사이의 관계 등..)

JPA는 둘 사이의 패러다임의 불일치를 해소하기 위해 등장했다.

즉 JPA덕분에 개발자는 객체지향적으로 프로그래밍을 하고, 관계형 데이터베이스에 매핑하는 것은 JPA가 대신 해준다.

<br/>

<br/>

### 요구사항 분석

##### 게시판 기능

- 게시글 조회, 등록, 수정, 삭제

##### 회원 기능

- 구글 / 네이버 로그인
- 로그인 한 사용자 글 작성 권한
- 본인 작성 글에 대한 관리

<br/>

<br/>

## 프로젝트에 Spring Data JPA 적용하기

##### build.gradle에 추가

```properties
//Spring Data JPA 추가
implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
//h2 데이터베이스 추가
runtimeOnly 'com.h2database:h2'

```

![image-20211120141811350](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211120141811350.png)



의존성을 등록했다면 이제 시작해보자.

<br/>

<br/>

#### DOMAIN

다음 위치에 domain 패키지를 만들자.

![image-20211120141938980](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211120141938980.png)

##### domain 아래에 posts 패키지를 만들고, Posts 클래스를 만들자.

<br/>

##### Posts 클래스 작성

```java
package web.purplebook.domain.posts;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Getter//롬복
@NoArgsConstructor//롬복
@Entity//JPA 어노테이션,테이블과 링크될 클래스임을 나타낸다.,클래스에 가장 가깝게 두었는데, 그 이유는 이후에 코틀린 등의 새 언어 전환으로 롬복이 더이상 필요 없을 경우 쉽게 삭제할 수 있다.
public class Posts {

    @Id //PK로 지정
    @GeneratedValue(strategy = GenerationType.IDENTITY)//ex) mysql의 auto_increment
    @Column(name = "POSTS_ID")
    private Long id;

    @Column(length = 500, nullable = false)//varchar(500), NOT_NULL 제약조건 추가
    private String title;

    @Column(columnDefinition = "TEXT", nullable = false)//content = TEXT로 지정, NOT_NULL 제약조건 추가
    private String content;

    private String author;

    @Builder //
    public Posts(String title, String content, String author) {
        this.title = title;
        this.content = content;
        this.author = author;
    }
}
```

#### <span style="color:red">Setter 메소드 생성 금지!</span>

자바빈 규약을 생각하면서 Setter, Getter를 무작정 생성하는 경우가 있는데, 이렇게 되면 해당 클래스의 인스턴스 값들이 언제 어디서 변해야 하는지 코드상으로 명확하게 구분할 수가 없어, 차후 기능 변경 시 정말 복잡해진다.

그래서 Entity 클래스에는 절대 Setter 메소드를 만들지 않는다. 

##### 대신 해당 필드의 값 변경이 필요하면 명확히 그 목적과 의도를 나타낼 수 있는 메소드를 추가해야만 한다.

#### 예시

```java
public class Order {
	private boolean status;
	
    //잘못된 사용
	public void setStatus(boolean status){
		this.status = status;
	}
	
	//올바른 사용
	public void cancelOrder(){
		this.status = fasle;
	}
}

//잘못된 사용
public void cancleOrder(){
	order.setStatus(false);
}

//올바른 사용
public void cancleOrder(){
	order.cancelOrder();
}

```

<br/>

<br/>

#### 그럼 어떻게 값을 채워서 DB에 삽입하지?

setter가 없는 이 상황에서 어떻게 값을 채워서 DB에 삽입할 수 있을까?

기본적인 구조는 생성자를 통해 최종값을 채운 후 DB에 삽입하는 것 이며, 값 변경이 필요한 경우 해당 이벤트에 맞는 pulbic 메소드를 호출(ex: cancleOrder)하여 변경하는 것을 전재로 한다.

여기서는 생성자 대신 @Builder를 통해 제공되는 빌더 클래스를 사용한다.

빌더나 생성자나 생성시에 값을 채워주는 역할은 똑같으며, 빌더 패턴에 대해 궁금하다면 구글링을 해보자!

<br/>

### JpaRepository 생성하기

책에서와는 조금 다른 경로로 생성하겠다.

domain 패키지와 같은 위치에서 repository 패키지를 생성한 후 PostsRepository 인터페이스를 생성하자.

![image-20211120145122757](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211120145122757.png)

<br/>

```java
package web.purplebook.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import web.purplebook.domain.posts.Posts;

public interface PostsRepository extends JpaRepository<Posts, Long> {
}
```

- JpaRepository<Entity 클래스, PK 타입>를 상속하면 기본적인 CRUD 메소드가 자동으로 생성된다.

##### 즉 저렇게만 해두면, save, find, update, delete등의 메소드가 자동으로 생성된다!!!

<br/>

<br/>

## Spring data JPA 테스트코드 작성하기

##### 똑같이 PostsRepository 클래스에 들어가 Ctrl + Shift + T 를 눌러서 테스트를 만들자.

```java
package web.purplebook.repository;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import web.purplebook.domain.posts.Posts;

import java.util.List;

@SpringBootTest
class PostsRepositoryTest {

    @Autowired PostsRepository postsRepository;

    @Test
    public void 게시글저장_불러오기() throws Exception {
        //given
        String title = "테스트 게시글 제목";
        String content = "테스트 게시글 본문";
        postsRepository.save(Posts.builder()
                        .title(title)
                        .content(content)
                        .author("ShinDongHun")
                        .build());

        //when
        List<Posts> postsList = postsRepository.findAll();


        //then
        Posts posts = postsList.get(0);
        Assertions.assertThat(posts.getTitle()).isEqualTo(title);
        Assertions.assertThat(posts.getContent()).isEqualTo(content);

    }

}
```

<br/>

##### 테스트는 통과하였지만, 실제 쿼리가 어떻게 나가는지 보고싶다. 

![image-20211120152215443](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211120152215443.png)

```java
spring.jpa.show_sql=true
```

다음 설정을 application.properties 속성에 추가하고 실행시켜 보자.

<br/>

<br/>

### 등록, 수정, 조회 API 만들기

API를 만들기 위해 총 3개의 클래스가 필요하다.

- Request 데이터를 받을 Dto
- API 요청을 받을 Controller
- 트랜잭션, 도메인 기능 간의 순서를 보장하는 Service

<br/>

#### 비지니스 로직은 어디서 처리하나?

많은 사람들이 Service에서 비지니스 로직을 처리해야 한다고 오해하고 있다.(나도 그랬다.. 이번 대회에서도 Service 단에서 모든 비지니스 로직을 처리했었다.)

하지만 전혀 그렇지 않다. **Service는 트랜잭션, 도메인 간 순서 보장**의 역할만 한다.

비지니스 로직은 누가 처리하나? 잠깐 다음 그림을 보자.

![image-20211120153416709](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211120153416709.png)

##### Web Layer :

- ##### 흔히 사용하는 컨트롤러와 JSP등의 뷰 템플릿 영역이다.

- ##### 이외에도 필터, 인터셉터, 컨트롤러 어드바이스등 외부 요청과 응답에 대한 전반적인 영역을 이야기한다.

##### Service Layer 

- @Service에 사용되는 서비스 영역이다
- 일반적으로 Controller와 Dao의 중간 영역에서 사용된다
- @Transational이 사용되어야 하는 영역이기도 하다.

##### Repository Layer

- Database와 같이 데이터 저장소에 접근하는 영역이다.
- 기존에 개발하셨던 분들이라면 Dao 영역으로 이해하시면 쉬울 것이다.

##### Dtos

- Dto는 계층 간에 데이터 교환을 위한 객체를 이야기하며, Dtos는 이들의 영역을 이야기한다.
- 예를 들어 뷰 템플릿 엔진에서 사용될 객체나 Repository Layer에서 결과로 넘겨준 객체 등이 이들을 이야기한다.

##### Domain model

- 도메인이라 불리는 개발 대상을 모든 사람이 동일한 관점에서 이해할 수 있고 공유할 수 있도록 단순화시킨 것을 도메인 모델이라고 한다.
- 택시 앱이라고 한다면 배차, 탑승, 요금 등이 모두 도메인이 될 수 있다.

#### 위 5가지 영역 중 비지니스 처리를 담당해야 할 부분은 <span style="color:orange">Domain</span>이다.

이를 기억하고 코드를 작성해 보도록 하자.

<br/>

![image-20211120155526051](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211120155526051.png)

위치는 다음과 같다. 하나하나 생성해보자.

##### PostsApiController 

```java
package web.purplebook.web;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import web.purplebook.service.posts.PostsService;
import web.purplebook.web.dto.PostsSaveRequestDto;

@RequiredArgsConstructor
@RestController
public class PostsApiController {

    private final PostsService postsService;

    @PostMapping("/api/v1/posts")
    public Long save(@RequestBody PostsSaveRequestDto requestDto){
        return postsService.save(requestDto);
    }
}
```

아직 PostService를 만들지 않았기 때문에 오류가 날것이다. 이제 PostsService를 만들어보자.

##### PostService

```java
package web.purplebook.service.posts;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import web.purplebook.repository.PostsRepository;
import web.purplebook.web.dto.PostsSaveRequestDto;

@Service
@RequiredArgsConstructor
public class PostsService {
    private final PostsRepository postsRepository;

    @Transactional
    public Long save(PostsSaveRequestDto requestDto){
        return postsRepository.save(requestDto.toEntity()).getId();
    }
}
```

<br/>

마지막으로 PostSaveRequestDto를 만들자.

##### PostSaveRequestDto

```java
package web.purplebook.web.dto;

import lombok.Builder;
import web.purplebook.domain.posts.Posts;

public record PostsSaveRequestDto(String title, String content, String author) {

    @Builder
    public PostsSaveRequestDto(String title, String content, String author) {
        this.title = title;
        this.content = content;
        this.author = author;
    }

    public Posts toEntity(){
        return Posts.builder()
                .title(title)
                .content(content)
                .author(author)
                .build();
    }

}
```

책에서는 이렇게 만들지 않았지만, record 클래스를 써보고 싶은 마음에..,, 이렇게 하고 싶지 않다면 코드는 다음과 같다.

```java
package web.purplebook.web.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import web.purplebook.domain.posts.Posts;

@Getter
@NoArgsConstructor
public class PostsSaveRequestDto {
    private String title;
    private String content;
    private String author;

    @Builder
    public PostsSaveRequestDto(String title, String content, String author) {
        this.title = title;
        this.content = content;
        this.author = author;
    }

    public Posts toEntity() {
        return Posts.builder()
                .title(title)
                .content(content)
                .author(author)
                .build();
    }
}
```

##### 무엇이 됐던 중요한 것은 <span style="color:red">절대로 Entity 클래스를 Request/Response 클래스로 사용해서는 안된다</span>

Entity 클래스는 데이터베이스와 맞닿은 핵심 클래스이다.

Entity 클래스를 기준으로 테이블이 생성되고, 스키마가 변경된다.

Entity를 변경하는 것은 여러 클래스에 영향을 미치지만, Dto는 그렇지 않다.

따라서 DB Layer와 View Layer의 역할 분리를 철저하게 하자.

<br/>

### 테스트코드 작성하기

##### 똑같이 PostApiControllerTest클래스에 들어가 Ctrl + Shift + T 를 눌러서 테스트를 만들자.

```java
package web.purplebook.web;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.web.server.LocalServerPort;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import web.purplebook.domain.posts.Posts;
import web.purplebook.repository.PostsRepository;
import web.purplebook.web.dto.PostsSaveRequestDto;

import java.util.List;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.*;

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

}
```

ApiController 를 테스트하는데 HelloController와 달리 @WebMvcTest를 사용하지 않았다.

@WebMvcTest의 경우 JPA의 기능이 작동하지 않기 때문인데, Controller와 ControllerAdvice등 외부 연동과 관련된 부분만 활성화되니 

#### 지금과 같이 JPA기능까지 한번에 테스트할 때는 @SpringBootTest와 TestRestTemplate를 사용하면 된다.

<br/>

### 수정/ 조회 기능 추가

##### PostsApiController

```java
package web.purplebook.web;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import web.purplebook.service.posts.PostsService;
import web.purplebook.web.dto.PostsSaveRequestDto;

@RequiredArgsConstructor
@RestController
public class PostsApiController {

    private final PostsService postsService;

    @PostMapping("/api/v1/posts")
    public Long save(@RequestBody PostsSaveRequestDto requestDto){
        return postsService.save(requestDto);
    }
    
    @PutMapping("/api/v1/posts/{id}")
    public Long update(@PathVariable("id") Long id, @RequestBody PostsUpdateDto requestDto){
        return postsService.update(id,requestDto);
    }

    @GetMapping("/api/v1/posts/{id}")
    public PostsResponseDto findById(@PathVariable("id") Long id){
        return postsService.findById(id);
    }
}
```

<br/>

##### PostResponseDto

```java
package web.purplebook.web.dto;

import lombok.Getter;
import web.purplebook.domain.posts.Posts;

@Getter
public class PostsResponseDto {

    private Long id;
    private String title;
    private String content;
    private String author;

    public PostsResponseDto(Posts entity) {
        this.id = entity.getId();
        this.title = entity.getTitle();
        this.content = entity.getContent();
        this.author = entity.getAuthor();
    }
}
```

<br/>

##### PostsUpdateRequestDto

```java
package web.purplebook.web.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class PostsUpdateRequestDto {

    private String title;
    private String content;

    @Builder
    public PostsUpdateRequestDto(String title, String content) {
        this.title = title;
        this.content = content;
    }
}
```

<br/>

##### posts

```java
package web.purplebook.domain.posts;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Getter//롬복
@NoArgsConstructor//롬복
@Entity//JPA 어노테이션,테이블과 링크될 클래스임을 나타낸다.,클래스에 가장 가깝게 두었는데, 그 이유는 이후에 코틀린 등의 새 언어 전환으로 롬복이 더이상 필요 없을 경우 쉽게 삭제할 수 있다.
public class Posts {

    @Id //PK로 지정
    @GeneratedValue(strategy = GenerationType.IDENTITY)//ex) mysql의 auto_increment
    @Column(name = "POSTS_ID")
    private Long id;

    @Column(length = 500, nullable = false)//varchar(500), NOT_NULL 제약조건 추가
    private String title;

    @Column(columnDefinition = "TEXT", nullable = false)//content = TEXT로 지정, NOT_NULL 제약조건 추가
    private String content;

    private String author;

    @Builder //
    public Posts(String title, String content, String author) {
        this.title = title;
        this.content = content;
        this.author = author;
    }
    
    
    //==추가==//
    public void update(String title, String content){
        this.title = title;
        this.content = content;
    }
}
```

<br/>

##### PostService

```java
package web.purplebook.service.posts;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import web.purplebook.domain.posts.Posts;
import web.purplebook.repository.PostsRepository;
import web.purplebook.web.dto.PostsResponseDto;
import web.purplebook.web.dto.PostsSaveRequestDto;
import web.purplebook.web.dto.PostsUpdateRequestDto;

@Service
@RequiredArgsConstructor
public class PostsService {
    private final PostsRepository postsRepository;

    @Transactional
    public Long save(PostsSaveRequestDto requestDto){
        return postsRepository.save(requestDto.toEntity()).getId();
    }

    @Transactional
    public Long update(Long id, PostsUpdateRequestDto requestDto) {
        Posts posts = postsRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("해당 게시글이 없습니다. id=" + id));

        posts.update(requestDto.getTitle(), requestDto.getContent());
        return id;
    }


    @Transactional
    public PostsResponseDto findById(Long id) {
        Posts entity = postsRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("해당 게시글이 없습니다. id=" + id));
        return new PostsResponseDto(entity);
    }
}

```

<br/>

<br/>

### 테스트 코드 작성

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

<br/>

<br/>

### H2 데이터베이스에서 확인하기

##### application.properties에 추가

```properties
spring.h2.console.enabled=true
```

<br/>

##### 이후 Application클래스의 main 메소드, 나의 경우 아래 사진을 실행한다.

![image-20211120174622641](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211120174622641.png)

##### 이후 http://localhost:8080/h2-console로 접속하여

![image-20211120174735572](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211120174735572.png)

다음과 같이 URL 주소를 확인 후 접속해주자.

<br/>

<br/>

### JPA  Auditing으로 생성시간/수정시간 자동화하기

보통 엔티티에는 해당 데이터의 생성시간과 수정시간을 포함한다. 언제 만들어졌는지, 언제 수정되었는지 등은 차후 유지보수에 있어 굉장히 중요한 정보이기 때문이다.

그렇다 보니 매번DB에 삽입하기 전, 갱신하기 전에 날짜 데이터를 등록/수정하는 코드가 여기저기 들어가게 된다.

개발자들은 귀찮음을 싫어한다.. 이런 단순하고 반복적인 코드를 자동으로 생성해주는 JPA Auditing을 사용해보자.

<br/>

##### BasteTimeEntity 개발

```java
package web.purplebook.domain;

import lombok.Getter;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import javax.persistence.EntityListeners;
import javax.persistence.MappedSuperclass;
import java.time.LocalDateTime;

@Getter
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
public abstract class BaseTimeEntity {
    
    @CreatedDate
    private LocalDateTime createdDate;
    
    @LastModifiedDate
    private LocalDateTime modifiedDate;
    
}
```

<br/>

##### Posts 클래스가 BaseTimeEntity를 상속받도록 변경

```java
public class Posts extends BaseTimeEntity {
```

<br/>

##### Application 클래스 활성화

```
package web.purplebook;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@EnableJpaAuditing //Auditiong 활성화
@SpringBootApplication
public class PurplebookApplication {

   public static void main(String[] args) {
      SpringApplication.run(PurplebookApplication.class, args);
   }

}
```

<br/>

테스트 코드를 작성하여 확인해 볼 수 있지만.. 귀찮기에,, 궁금하면 직접 넣어보도록 하자!

<br/>

<br/>

### 📔 Reference

##### 스프링 부트와 AWS로 혼자 구현하는 웹 서비스 78~123P