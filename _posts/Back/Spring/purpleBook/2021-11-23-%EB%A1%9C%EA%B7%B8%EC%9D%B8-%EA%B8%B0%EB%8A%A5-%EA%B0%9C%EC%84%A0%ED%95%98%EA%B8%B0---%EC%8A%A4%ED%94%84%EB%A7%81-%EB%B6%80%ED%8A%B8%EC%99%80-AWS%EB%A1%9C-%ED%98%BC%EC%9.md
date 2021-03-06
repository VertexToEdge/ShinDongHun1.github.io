---
title:  "로그인 기능 개선하기 - 스프링 부트와 AWS로 혼자 구현하는 웹 서비스"
excerpt: "스프링 부트와 AWS로 혼자 구현하는 웹 서비스 4-2"
date:   2021-11-23 15:16:00 
header:
  teaser: /assets/images/spring.png

categories: purpleBook
tags:
  - Java
  - Spring
last_modified_at: 2021-11-23T15:16:00



---

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124204433310.png" alt="image-20211124204433310" style="zoom:30%;" />



<br/>

사실 한 챕터에 포함된 내용인데, 글이 너무 길어져서 이렇게 나눈다!

## 어노테이션 기반으로 개선하기

이전 글에서 만들었던 구글을 통한 로그인 방법에서 개선할 부분이 무엇이 있을까?

IndexController에서 세션값을 가져오는 부분이다.

```java
SessionUser user = (SessionUser) httpSession.getAttribute("user");
```

##### index메소드 외에도 다른 컨트롤러와 세션값이 필요하면 그때마다 직접 세션에서 값을 가져와야 한다.

##### 이 부분을 어노테이션을 활용하여 바꿔보자.

<br/>

#### LoginUser 생성

```java
package web.purplebook.config.auth;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.PARAMETER)
@Retention(RetentionPolicy.RUNTIME)
public @interface LoginUser {
}
```

##### @Target(ElementType.PARAMETER)

- 이 어노테이션이 생성(적용)될 수 있는 위치를 지정한다.
- PARAMETER로 지정했으니 메소드의 파라미터로 선언된 객체에서만 사용할 수 있다.

<br/>

<br/>

#### LogInUserArgumentResolver

```java
package web.purplebook.config.auth;

import lombok.RequiredArgsConstructor;
import org.springframework.core.MethodParameter;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.support.WebDataBinderFactory;
import org.springframework.web.context.request.NativeWebRequest;
import org.springframework.web.method.support.HandlerMethodArgumentResolver;
import org.springframework.web.method.support.ModelAndViewContainer;
import web.purplebook.config.auth.dto.SessionUser;

import javax.servlet.http.HttpSession;

@RequiredArgsConstructor
@Component
public class LogInUserArgumentResolver implements HandlerMethodArgumentResolver {
    
    private final HttpSession httpSession;

    @Override
    public boolean supportsParameter(MethodParameter parameter) {
        boolean isLoginUserAnnotation = parameter.hasParameterAnnotation(LoginUser.class);
        boolean isUserClass = SessionUser.class.isAssignableFrom(parameter.getParameterType());

        return isLoginUserAnnotation && isUserClass;
    }

    @Override
    public Object resolveArgument(MethodParameter parameter, ModelAndViewContainer mavContainer, NativeWebRequest webRequest, WebDataBinderFactory binderFactory) throws Exception {

        return httpSession.getAttribute("user");
    }
}
```

<br/>

<br/>

#### WebConfig

```java
package web.purplebook.config;

import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.method.support.HandlerMethodArgumentResolver;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import web.purplebook.config.auth.LogInUserArgumentResolver;

import java.util.List;

@RequiredArgsConstructor
@Configuration
public class WebConfig implements WebMvcConfigurer {
    private final LogInUserArgumentResolver logInUserArgumentResolver;

    @Override
    public void addArgumentResolvers(List<HandlerMethodArgumentResolver> resolvers) {
        resolvers.add(logInUserArgumentResolver);
    }
}
```

<br/>

<br/>

이러면 어노테이션 적용이 끝났다.

##### 이제 적용해보자

<br/>

#### IndexController 수정

```java
package web.purplebook.web;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import web.purplebook.config.auth.LoginUser;
import web.purplebook.config.auth.dto.SessionUser;
import web.purplebook.service.posts.PostsService;
import web.purplebook.web.dto.PostsResponseDto;

@Controller
@RequiredArgsConstructor
public class IndexController {

    private final PostsService postsService;

    @GetMapping("/")
    public String index(Model model, @LoginUser SessionUser user){//추가
        model.addAttribute("posts", postsService.findAllDesc());
        
        if(user != null && user.getUsername() != null){
            model.addAttribute("username", user.getName());
        }

        return "index";
    }

    @GetMapping("/posts/save")
    public String postsSave(){
        return "posts-save";
    }


    @GetMapping("/posts/update/{id}")
    public String postsUpdate(@PathVariable("id")Long id, Model model) {
        PostsResponseDto dto = postsService.findById(id);
        model.addAttribute("post",dto);
        return "posts-update";
    }

}
```

<br/>

<br/>

#### CustomOAuth2SignUpController 수정

```java
package web.purplebook.web;

import lombok.RequiredArgsConstructor;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import web.purplebook.config.auth.LoginUser;
import web.purplebook.config.auth.dto.OAuth2SignUpDto;
import web.purplebook.config.auth.dto.SessionUser;
import web.purplebook.domain.user.User;
import web.purplebook.repository.UserRepository;

import javax.servlet.http.HttpSession;
import java.util.ArrayList;
import java.util.List;

@Controller
@RequiredArgsConstructor
public class CustomOAuth2SignUpController {

    private final HttpSession httpSession;
    private final UserRepository userRepository;

    @GetMapping("/addform")
    public String addForm(Model model, @LoginUser SessionUser user){
        if(user.getUsername() != null){
            model.addAttribute("username", user.getName());
            return "index";//이미 회원가입 한 사람이라면 메인 페이지로
        }
        else {
            return "/add-form";
        }
    }



    //추가 입력
    @PostMapping("/signUp")
    @ResponseBody
    @Transactional
    public Long signUp(@RequestBody OAuth2SignUpDto oAuth2SignUpDto, @LoginUser SessionUser user){
        Long id = user.getId();

        User user1 = userRepository.findById(id).orElse(null);
        user1.googleSignUp(oAuth2SignUpDto.getUsername());//username 등록


        updateRole(user1);

        httpSession.setAttribute("user", new SessionUser(user1));
        return 0L;
    }

    private void updateRole(User user) {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        List<GrantedAuthority> updatedAuthorities = new ArrayList<>();
        updatedAuthorities.add(new SimpleGrantedAuthority(user.getRoleKey()));
        Authentication newAuth = new UsernamePasswordAuthenticationToken(auth.getPrincipal(), auth.getCredentials(), updatedAuthorities);
        SecurityContextHolder.getContext().setAuthentication(newAuth);
    }
}
```

<br/>

<br/>

<br/>

## 세션 저장소로 데이터베이스 사용하기

사실 필자는 프론트와 백을 나누어서 Rest API 방식으로 통신하는 웹 애플리케이션을 만들고 싶었다.

그래서 사실 아까 로그인부터 세션을 사용하는 부분을 없애고 JWT를 사용하여 Stateless하게 정보를 주고받고 싶었으나, 아직 내가 프론트를 다룰 줄 모른다 ㅠㅠ

여기서 잠시 멈추고 프론트를 공부한 후 다시 와서 마무리 하기에는 시간도 너무 오래걸리고 여러모로 별로라는 생각이 들었다.

그래서 일단은 이 책에 나온 방식대로 세션을 사용할 것이다.

그러나 이후 이 책을 끝까지 다 따라 한 다음에는 토큰을 사용해서 REST API 방식으로 웹 애플리케이션을 배포하도록 코드를 바꿔볼 것이다.

우선을 세션을 사용하면서 코드를 작성해보자.

<br/>

<br/>

우리가 현재까지 만든 서비스는 애플리케이션을 재실행하면 로그인이 풀린다.

이는 세션이 내장 톰켓의 메모리에 저장되기 때문이다.

기본적으로 세션은 실행되는 WAS의 메모리에서 저장되고 호출된다.

메모리에 저장되다 보니 내장 톰캣처럼 애플리케이션 실행 시 실행되는 구조에선 항상 초기화가 된다.

##### 즉 배포할 때마다 톰캣이 재시작되는 것이다.

이 외에도 한 가지 문제가 더 있는데, 2대 이상의 서버에서 서비스하고 있다면 톰캣마다 세션 동기화 설정을 해주어야 한다.

그래서 실제 현업에서는 세션 저장소에 대해 다음의 3가지중 한 가지를 선택한다.

(1) 톰캣 세션을 사용한다

- 일반적으로 별다른 설정을 하지 않을 때 기본적으로 선택되는 방식이다.
- 이렇게 될 경우 톰캣(WAS)에 세션이 저장되기 때문에 2대 이상의 WAS가 구동되는 환경에서는 톰캣들 간의 세션 공유를 위한 추가 설정이 필요하다.

(2) MySQL과 같은 데이터베이스를 세션 저장소로 사용한다

- 여러 WAS간의 공용 세션을 사용할 수 있는 가장 쉬운 방법이다.
- 많은 설정이 필요 없지만 결국 로그인 요청마다 DB IO가 방생하여 성능상 이슈가 발생할 수 있다.
- 보통 로그인 요청이 많이 없는 백오피스, 사내 시스템 용도에서 사용한다.

(3) Redis, Memcached와 같은 메모리 DB를 세션 저장소로 사용한다.

- B2C 서비스에서 가장 많이 사용하는 방식이다.
- 실제 서비스로 사용하기 위해서는 Embedded Redis와 같은 방식이 아닌 외부 메모리 서버가 필요하다.

여기서는 두 번째 방식인 데이터베이스를 세션 저장소로 사용하는 방식을 선택하여 진행하겠다.

이유는 설정이 간단하고, 이후 서비스를 배포하는 경우를 생각해 보면, 레디스와 같은 서비스를 사용하려면 별도로 사용료를 지불해야 하기 때문이다.

일단은 데이버테이스로 처리한 후 이후 서비스가 커진다면 메모리DB를 고려해보자.

<br/>

<br/>

### Spring-session-jdbc 등록

##### build.gradle에 다음과 같이 의존성을 등록한다.

```properties
implementation 'org.springframework.session:spring-session-jdbc'
```

<br/>

##### application.properties에 다음 코드를 추가한다.

```properties
spring.session.store-type=jdbc
```

<br/>

이후 애플리케이션을 다시 실행하여 로그인 진행 후, h2-console로 접속해보자.

<br/>

![image-20211123181534494](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123181534494.png)

다음과 같이 세션을 위한 테이블 2개가 자동으로 생성되었다.

현재는 H2의 메모리 DB를 사용하고 있기 때문에 애플리케이션을 재시작 하면 로그인이 풀린다.

그러나 이후 AWS로 배포하게 되면 AWS의 데이터베이스인 RDS를 사용할 것이기 때문에 세션이 풀리지 않는다.

<br/>

<br/>

##### 다음 글 부터는 나머지 소셜 로그인 등을 진행하는 방법에 대해서도 알아보자.

책에서는 네이버를 통한 로그인이 마지막이다. 그러나 나는 이후 진행할 어떤 프로젝트던지 소셜 로그인을 사용할 것 같기 때문에, 미리 모든 소셜 로그인을 만들어두고 싶다.

지금 생각하는 소셜 로그인은 다음과 같다.

- 구글 (완료)
- 네이버
- 카카오
- 페이스북
- 깃허브
- 애플
- 라인

<br/>

### 📔 Reference

##### 스프링 부트와 AWS로 혼자 구현하는 웹 서비스 124~161P

