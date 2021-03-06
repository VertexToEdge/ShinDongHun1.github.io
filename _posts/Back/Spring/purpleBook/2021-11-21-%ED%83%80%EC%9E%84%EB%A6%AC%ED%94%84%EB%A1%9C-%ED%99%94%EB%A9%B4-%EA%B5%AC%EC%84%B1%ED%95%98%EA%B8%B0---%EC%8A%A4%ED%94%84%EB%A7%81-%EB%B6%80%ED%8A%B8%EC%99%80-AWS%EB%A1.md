---
title:  "타임리프로 화면 구성하기 - 스프링 부트와 AWS로 혼자 구현하는 웹 서비스"
excerpt: "스프링 부트와 AWS로 혼자 구현하는 웹 서비스 3"
date:   2021-11-21 01:16:00 
header:
  teaser: /assets/images/spring.png

categories: purpleBook
tags:
  - Java
  - Spring
last_modified_at: 2021-11-21T01:16:00






---

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124204433310.png" alt="image-20211124204433310" style="zoom:30%;" />

<br/>

## 시작에 앞서

책에서는 타임리프가 아닌 머스테치로 화면을 구성하였다. 이 책은 정말 스프링을 갓 시작한 사람들을 위해서 쓴 책인 것 같고, 또한 타임리프 대신 머스테치를 사용하는 이유로 타임리프가 어렵기에 머스테치를 사용한다 하였다. 

그러나 나는 그냥 미래를 본다면 타임리프를 사용하는 것이 맞다고 생각했다. 어차피 공부를 하는 목적인데 조금 어려우면 어떤가. 게다가 사놓은 강의도 있기에 하다가 막히면 강의를 참고하면서 공부할 예정이다.

<br/>

<br/>

### 기본 페이지 만들기

우선 타임리프 의존성을 등록하자. 이제는 익숙해졌을 테지만 build.gradle에 들어가서 의존성을 추가하자.

```properties
implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
```

<br/>

##### src/main/resources/templates/index.html

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org"> 
<head>
    <meta charset="UTF-8">
    <title>스프링 부트 웹 서비스</title>
</head>
<body>
    <h1>스프링 부트로 시작하는 웹 서비스</h1>
</body>
</html>
```

타임리프를 사용하기 위해서는 \<html xmlns:th="http://www.thymeleaf.org"> 해당 코드를 꼭 넣어주어야 한다.

##### IndexController

```java
package web.purplebook.web;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class IndexController {

    @GetMapping("/")
    public String index(){
        return "index";
    }
}
```

<br/>

### 테스트코드 작성

```java
package web.purplebook.web;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class IndexControllerTest {
    
    @Autowired
    private TestRestTemplate restTemplate;

    @Test
    public void 메인페이지() throws Exception {
        //when
        String body = this.restTemplate.getForObject("/",String.class);

        //then
        assertThat(body).contains("스프링 부트로 시작하는 웹 서비스"); // org.assertj.core.api.Assertions 를 static import
    }
}
```

테스트 코드만 작성하기 아쉬우니 직접 들어가보자.

localhost:8080 으로 들어가면 화면이 잘 출력될 것이다.

<br/>

## 게시글 등록 화면 만들기

이전 포스팅에서 PostApiController를 통해 API는 구현해 놓았으니 이제 화면만 개발하면 된다.

[https://getbootstrap.kr/docs/5.1/getting-started/download/](https://getbootstrap.kr/docs/5.1/getting-started/download/) 해당 사이트로 이동해서 부트스트랩을 다운받자.

![image-20211121165407282](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121165407282.png)



<br/>

다운받은 파일 속 css 와 js를 복사하자.

![image-20211121165456939](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121165456939.png)

<br/>

##### src/main/resources/static 아래에 붙여넣기를 하자.

![image-20211121165620659](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121165620659.png)

<br/>

<br/>

##### src/main/resources/templates/fragments/header.html

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:fragment="header">
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!-- Custom styles for this template -->
    <link href="/css/jumbotron-narrow.css" rel="stylesheet">

    <title>Hello, world!</title>
</head>

```

<br/>

##### index.html 수정

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="fragments/header :: header">
    <title>Hello</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>

<body>
    <h1>스프링 부트로 시작하는 웹 서비스</h1>
    <div class="row">
        <div class="col-md-6">
            <a href="/posts/save" role="button" class="btn btn-primary">글등록</a>
        </div>
    </div>

    <div th:replace="fragments/footer :: footer" />
</body>
</html>
```

<br/>

##### posts-save.html 등록

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="fragments/header :: header">
  <title>Hello</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>

  <h1>게시글 등록</h1>

  <div class="col-md-12">
    <div class="col-md-4">
      <form>
        <div class="form-group">
          <label for="title">제목</label>
          <input type="text" class="form-control" id="title" placeholder="제목을 입력하세요">
        </div>

        <div class="form-group">
          <label for="author">작성자</label>
          <input type="text" class="form-control" id="author" placeholder="작성자를 입력하세요">
        </div>

        <div class="form-group">
          <label for="content"> 내용</label>
          <textarea class="form-control" id="content" placeholder="내용을 입력하세요"></textarea>
        </div>
      </form>
      <a href="/" role="button" class="btn btn-secondary">취소</a>

      <button type="button" class="btn btn-primary" id="btn-save">등록</button>


    </div>
  </div>


  <div th:replace="fragments/footer :: footer" />
</body>
</html>
```

<br/>

##### index.js 등록 (경로 : resources/static/js/app/index.js)

![image-20211121174631587](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121174631587.png)

```javascript
var main = {
    init : function () {
        var _this = this;
        $('#btn-save').on('click', function (){
        _this.save();
        });
    },
    save : function () {
        var data = {
            title: $('#title').val(),
            author: $('#author').val(),
            content: $('#content').val()
        };

        $.ajax({
            type: 'POST',
            url: '/api/v1/posts',
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function (){
            alert('글이 등록되었습니다.');
            window.location.href = '/';
        }).fail(function (error){
            alert(JSON.stringify(error));
        })

    }

};

main.init();
```

<br/>

##### src/main/resources/templates/fragments/footer.html 등록

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<div class="footer" th:fragment="footer">
    <script type="text/javascript" th:src="@{/js/app/index.js}"></script>
</div>
```

<br/>

#### 참고

코드를 보면 css는 header.html에, js는  footer에 두었는데, 이는 페이지 로딩속도를 높이기 위함이다.

HTML은 위에서부터 코드가 실행되기 때문에 js는 body 하단에 두어 화면이 다 그려진 뒤에 호출하는 것이 좋다.

<br/>

### 이제 직접 한번 확인해보자

#### 메인 화면

![image-20211121174757812](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121174757812.png)

#### 글 등록 화면

![image-20211121174820457](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121174820457.png)

<br/>

#### 등록 버튼 눌렀을 때

![image-20211121174848431](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121174848431.png)

<br/>

##### http://localhost:8080/h2-console 로 이동 -> 확인

![image-20211121174920402](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121174920402.png)

<br/>

<br/>

<br/>

## 전체 조회 화면 만들기

##### index.html 수정

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="fragments/header :: header">
    <title>Hello</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>

<body>
    <h1>스프링 부트로 시작하는 웹 서비스</h1>
    <div class="col-md-12">
        <div class="row">
            <div class="col-md-6">
                <a href="/posts/save" role="button" class="btn btn-primary">글등록</a>
            </div>
        </div>
        <br/>
        <!-- 목록 출력 영역 -->
        <table class="table table-horizontal table-bordered">
            <thead class="thead-strong">
            <tr>
                <th>게시글번호</th>
                <th>제목</th>
                <th>작성자</th>
                <th>최종수정일</th>
            </tr>
            </thead>
            
            <tbody id="tbody">
                <tr th:each="post : ${posts}">
                    <td th:text="${post.id}"></td>
                    <td th:text="${post.title}"></td>
                    <td th:text="${post.author}"></td>
                    <td th:text="${post.modifiedDate}"></td>
                </tr>
            </tbody>
        </table>
    </div>

    <div th:replace="fragments/footer :: footer" />
</body>
</html>
```

##### th:each="post : ${posts}" 는 타임리프의 반복문이다. 자바의 for-each문과 비슷하지 않은가? 그럼 저 posts는 어디서 넣어주나??? 아래 IndexController에서 설명하겠다.

<br/>

<br/>

##### PostsRepository 수정

```java
package web.purplebook.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import web.purplebook.domain.posts.Posts;

import java.util.List;

public interface PostsRepository extends JpaRepository<Posts, Long> {

    @Query("select p from Posts p order by p.id desc")
    List<Posts> findAllDesc();
}
```

<br/>

##### PostsListResponseDto 생성

```java
package web.purplebook.web.dto;

import lombok.Getter;
import web.purplebook.domain.posts.Posts;

import java.time.LocalDateTime;

@Getter
public class PostsListResponseDto {
    private Long id;
    private String title;
    private String author;
    private LocalDateTime modifiedDate;

    public PostsListResponseDto(Posts entity) {
        this.id = entity.getId();
        this.title = entity.getTitle();
        this.author = entity.getAuthor();
        this.modifiedDate = entity.getModifiedDate();
    }
}
```

<br/>

##### PostService에 추가

```java
@Transactional(readOnly = true)
public List<PostsListResponseDto> findAllDesc(){
    return postsRepository.findAllDesc().stream()
            .map(PostsListResponseDto::new)//posts -> new PostsListResponseDto(posts)
            .toList();
}
```

##### 조회한 Posts 의 List를 PostsListResponseDto의 List로 변환

<br/>

##### IndexController 수정(메인 화면에서 게시글 리스트 볼 수 있도록)

```java
package web.purplebook.web;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import web.purplebook.service.posts.PostsService;

@Controller
@RequiredArgsConstructor
public class IndexController {

    private final PostsService postsService;
    
    @GetMapping("/")
    public String index(Model model){
        model.addAttribute("posts", postsService.findAllDesc());
        return "index";
    }

    @GetMapping("/posts/save")
    public String postsSave(){
        return "posts-save";
    }
}
```

##### 아까 설명하기로 한 posts를 넣어주는 코드이다. model.addAttribute를 통해 html의 posts에 postsService.findAllDesc()를 통해 나온 PostsListResponseDto의 List를 넣어준다는 의미이다.

<br/>

<br/>

#### 이제 확인해보자

![image-20211121180801614](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121180801614.png)

잘 나온다 굳!!!!!!

<br/>

<br/>

<br/>

### 게시글 수정 

##### posts-update-html 등록

![image-20211121183926994](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121183926994.png)

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="fragments/header :: header">
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>

  <div class="col-md-12">
    <div class="col-md-4">
    <form th:object="${post}" method="post">
      <div class="form-group">
        <label th:for="id">글 번호</label>
        <input type="text" th:field="*{id}" class="form-control" placeholder="이름을 입력하세요" readonly />
      </div>

      <div class="form-group">
        <label th:for="title">제목</label>
        <input type="text" th:field="*{title}" class="form-control" placeholder="이름을 입력하세요" />
      </div>
      <div class="form-group">
        <label th:for="author">작성자</label>
        <input type="text" th:field="*{author}" class="form-control" placeholder="가격을 입력하세요" readonly/>
      </div>
      <div class="form-group">
        <label th:for="content">내용</label>
        <textarea class="form-control" id="content" th:field="*{content}"></textarea>
      </div>
    </form>

    <a href="/" role="button" class="btn btn-secondary">취소</a>

    <button type="button" class="btn btn-primary" id="btn-update">수정 완료</button>


    </div>

  </div>

  <div th:replace="fragments/footer :: footer" />
</body>
</html>

```

#### th:object

##### form submit을 할 때, form의 데이터가 th:object에 설정해준 객체로 받아진다.

<br/>

##### index.js 수정 (업데이트 기능 추가)

```javascript
var main = {
    init : function () {
        var _this = this;
        $('#btn-save').on('click', function (){
        _this.save();
        });

        //업데이트 기능 추가
        $('#btn-update').on('click', function (){  
            _this.update();
        });
    },
    save : function () {
        var data = {
            title: $('#title').val(),
            author: $('#author').val(),
            content: $('#content').val()
        };

        $.ajax({
            type: 'POST',
            url: '/api/v1/posts',
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function (){
            alert('글이 등록되었습니다.');
            window.location.href = '/';
        }).fail(function (error){
            alert(JSON.stringify(error));
        });
    },

    
    //업데이트 기능 추가
    update : function () {
        var data = {
            title: $('#title').val(),
            content: $('#content').val()
        };

        var id = $('#id').val();

        $.ajax({
            type: 'PUT',
            url: '/api/v1/posts/'+id,
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function (){
            alert('글이 수정되었습니다.');
            window.location.href = '/';
        }).fail(function (error){
            alert(JSON.stringify(error));
        });
    }

};

main.init();
```

<br/>

##### index.html 수정 (수정 페이지로 이동할 수 있도록 수정)

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="fragments/header :: header">
    <title>Hello</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>

<body>
    <h1>스프링 부트로 시작하는 웹 서비스</h1>
    <div class="col-md-12">
        <div class="row">
            <div class="col-md-6">
                <a href="/posts/save" role="button" class="btn btn-primary">글등록</a>
            </div>
        </div>
        <br/>
        <!-- 목록 출력 영역 -->
        <table class="table table-horizontal table-bordered">
            <thead class="thead-strong">
            <tr>
                <th>게시글번호</th>
                <th>제목</th>
                <th>작성자</th>
                <th>최종수정일</th>
            </tr>
            </thead>

            <tbody id="tbody">
                <tr th:each="post : ${posts}">
                    <td th:text="${post.id}"></td>
                    <td>
                        <a href="#" th:href="@{/posts/update/{id} (id=${post.id})}" th:text="${post.title}">수정</a>
                    </td>
                    <td th:text="${post.author}"></td>
                    <td th:text="${post.modifiedDate}"></td>
                    <td>
                        <a href="#" th:href="@{/posts/update/{id} (id=${post.id})}" class="btn btn-primary" role="button">수정</a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <div th:replace="fragments/footer :: footer" />
</body>
</html>

```

<br/>

##### IndexController 수정

```java
package web.purplebook.web;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import web.purplebook.service.posts.PostsService;
import web.purplebook.web.dto.PostsResponseDto;

@Controller
@RequiredArgsConstructor
public class IndexController {

    private final PostsService postsService;

    @GetMapping("/")
    public String index(Model model){
        model.addAttribute("posts", postsService.findAllDesc());
        return "index";
    }

    @GetMapping("/posts/save")
    public String postsSave(){
        return "posts-save";
    }

    
    //== 업데이트 추가 ==//
    @GetMapping("/posts/update/{id}")
    public String postsUpdate(@PathVariable("id")Long id, Model model) {
        PostsResponseDto dto = postsService.findById(id);
        model.addAttribute("post",dto);
        return "posts-update";
    }
}
```

<br/>

### 확인해보자

![image-20211121190243489](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121190243489.png)

![image-20211121190255873](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121190255873.png)

![image-20211121190309155](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121190309155.png)

<br/>

<br/>

<br/>

### 게시물 삭제

진짜 마지막이다!!! 게시물을 삭제하는 기능을 추가하자.

##### posts-update.html 수정

```html
<button type="button" class="btn btn-danger" id="btn-delete">삭제</button>
```

이거 하나만 넣어주면 되지만... 혹시 모르니 전체 코드

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="fragments/header :: header">
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>

  <div class="col-md-12">
    <div class="col-md-4">
    <form th:object="${post}" method="post">
      <div class="form-group">
        <label th:for="id">글 번호</label>
        <input type="text" th:field="*{id}" class="form-control" placeholder="이름을 입력하세요" readonly />
      </div>

      <div class="form-group">
        <label th:for="title">제목</label>
        <input type="text" th:field="*{title}" class="form-control" placeholder="이름을 입력하세요" />
      </div>
      <div class="form-group">
        <label th:for="author">작성자</label>
        <input type="text" th:field="*{author}" class="form-control" placeholder="가격을 입력하세요" readonly/>
      </div>
      <div class="form-group">
        <label th:for="content">내용</label>
        <textarea class="form-control" id="content" th:field="*{content}"></textarea>
      </div>
    </form>

      <a href="/" role="button" class="btn btn-secondary">취소</a>

      <button type="button" class="btn btn-primary" id="btn-update">수정 완료</button>
        <!-- 삭제 -->
      <button type="button" class="btn btn-danger" id="btn-delete">삭제</button>


    </div>

  </div> 

  <div th:replace="fragments/footer :: footer" />
</body>
</html>
```

<br/>

##### index.js 수정

```html
var main = {
    init : function () {
        var _this = this;
        $('#btn-save').on('click', function (){
        _this.save();
        });

        $('#btn-update').on('click', function (){
            _this.update();
        });

        $('#btn-delete').on('click', function (){
            _this.delete();
        });
    },
    save : function () {
        var data = {
            title: $('#title').val(),
            author: $('#author').val(),
            content: $('#content').val()
        };

        $.ajax({
            type: 'POST',
            url: '/api/v1/posts',
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function (){
            alert('글이 등록되었습니다.');
            window.location.href = '/';
        }).fail(function (error){
            alert(JSON.stringify(error));
        });
    },

    update : function () {
        var data = {
            title: $('#title').val(),
            content: $('#content').val()
        };

        var id = $('#id').val();

        $.ajax({
            type: 'PUT',
            url: '/api/v1/posts/'+id,
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function (){
            alert('글이 수정되었습니다.');
            window.location.href = '/';
        }).fail(function (error){
            alert(JSON.stringify(error));
        });
    },
    
    
    delete : function () {

        var id = $('#id').val();

        $.ajax({
            type: 'DELETE',
            url: '/api/v1/posts/'+id,
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
        }).done(function (){
            alert('글이 삭제되었습니다.');
            window.location.href = '/';
        }).fail(function (error){
            alert(JSON.stringify(error));
        });
    }
    

};

main.init();
```

<br/>

##### PostsService 수정

```java
package web.purplebook.service.posts;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import web.purplebook.domain.posts.Posts;
import web.purplebook.repository.PostsRepository;
import web.purplebook.web.dto.PostsListResponseDto;
import web.purplebook.web.dto.PostsResponseDto;
import web.purplebook.web.dto.PostsSaveRequestDto;
import web.purplebook.web.dto.PostsUpdateRequestDto;

import java.util.List;

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

    @Transactional(readOnly = true)
    public List<PostsListResponseDto> findAllDesc(){
        return postsRepository.findAllDesc().stream()
                .map(PostsListResponseDto::new)//posts -> new PostsListResponseDto(posts)
                .toList();
    }
    
    
    // 삭제 추가
    @Transactional
    public void delete(Long id){
        Posts posts = postsRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("해당 게시글이 없습니다. id=" + id));
        postsRepository.delete(posts);
    }
}
```

<br/>

##### PostsApiController 수정

```java
package web.purplebook.web;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import web.purplebook.service.posts.PostsService;
import web.purplebook.web.dto.PostsResponseDto;
import web.purplebook.web.dto.PostsSaveRequestDto;
import web.purplebook.web.dto.PostsUpdateRequestDto;

@RequiredArgsConstructor
@RestController
public class PostsApiController {

    private final PostsService postsService;

    @PostMapping("/api/v1/posts")
    public Long save(@RequestBody PostsSaveRequestDto requestDto){
        return postsService.save(requestDto);
    }

    @PutMapping("/api/v1/posts/{id}")
    public Long update(@PathVariable("id") Long id, @RequestBody PostsUpdateRequestDto requestDto){
        return postsService.update(id,requestDto);
    }

    @GetMapping("/api/v1/posts/{id}")
    public PostsResponseDto findById(@PathVariable("id") Long id){
        return postsService.findById(id);
    }


    //추가
    @DeleteMapping("/api/v1/posts/{id}")
    public Long delete(@PathVariable("id") Long id){
        postsService.delete(id);
        return id;
    }
}
```

<br/>

### 테스트해보자

![image-20211121191942881](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211121191942881.png)

##### 굳 잘된다!!!!!

<br/>

<br/>

이렇게 해서 오늘은 타임리프를 사용해서 화면을 만들어 보았다! 

이제 회원가입과 로그인, 권한 기능만 추가한다면 간단한 게시판을 다 만들어 본 것이다!!!

다음 시간에는 소셜 로그인 기능과, 로그인을 하지 않으면 글을 쓸 수 없게끔 제한을 둬보겠다.

<br/>

<br/>

### 📔 Reference

##### 스프링 부트와 AWS로 혼자 구현하는 웹 서비스 124~161P