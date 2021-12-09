---
title:  "[Security] JSON으로 로그인처리 하기"
excerpt: "JSON으로 로그인을 어떻게 처리할 수 있을까?"
date:   2021-12-09 16:57:00
header:
  teaser: /assets/images/spring.png

categories: Security
tags:
  - Security
last_modified_at: 2021-12-09T16:57:00

---

<br/>

## [Security] - JSON으로 로그인처리 하기

##### 스프링 시큐리티의 formLogin()을 사용하면 오로지 x-www-form-urlencoded의 Content-Type으로만 데이터를 받을 수 있다.

##### 오늘은 formLogin을 사용하지 않고, JSON으로 username과 password를 받아서 로그인 처리를 진행하는 방법을 소개하겠다.

<br/>

## formLogin()의 작동방식

##### 시큐리티의 formLogin()을 활성화 시키면 다음 사진과 같이 FormLoginConfigurer가 활성화 되는것을 알 수 있다.

![image-20211209164717441](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211209164717441.png)이때 FormLoginConfigurer 에서는 **UsernamePasswordAuthenticationFilter**란 것을 사용하는데 이것이 어떻게 작동하는지 공부할 필요가 있다.

<br/>

## UsernamePasswordAuthenticationFilter

코드로 확인하자.

```java
public class UsernamePasswordAuthenticationFilter extends AbstractAuthenticationProcessingFilter {

   public static final String SPRING_SECURITY_FORM_USERNAME_KEY = "username";

   public static final String SPRING_SECURITY_FORM_PASSWORD_KEY = "password";

   private static final AntPathRequestMatcher DEFAULT_ANT_PATH_REQUEST_MATCHER = new AntPathRequestMatcher("/login",
         "POST");

   private String usernameParameter = SPRING_SECURITY_FORM_USERNAME_KEY;

   private String passwordParameter = SPRING_SECURITY_FORM_PASSWORD_KEY;

   private boolean postOnly = true;

   public UsernamePasswordAuthenticationFilter() {
      super(DEFAULT_ANT_PATH_REQUEST_MATCHER);
   }

   public UsernamePasswordAuthenticationFilter(AuthenticationManager authenticationManager) {
      super(DEFAULT_ANT_PATH_REQUEST_MATCHER, authenticationManager);
   }

   @Override
   public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response)
         throws AuthenticationException {
      if (this.postOnly && !request.getMethod().equals("POST")) {
         throw new AuthenticationServiceException("Authentication method not supported: " + request.getMethod());
      }
      String username = obtainUsername(request);
      username = (username != null) ? username : "";
      username = username.trim();
      String password = obtainPassword(request);
      password = (password != null) ? password : "";
      UsernamePasswordAuthenticationToken authRequest = new UsernamePasswordAuthenticationToken(username, password);
      // Allow subclasses to set the "details" property
      setDetails(request, authRequest);
      return this.getAuthenticationManager().authenticate(authRequest);
   }


   @Nullable
   protected String obtainPassword(HttpServletRequest request) {
      return request.getParameter(this.passwordParameter);
   }


   @Nullable
   protected String obtainUsername(HttpServletRequest request) {
      return request.getParameter(this.usernameParameter);
   }


   protected void setDetails(HttpServletRequest request, UsernamePasswordAuthenticationToken authRequest) {
      authRequest.setDetails(this.authenticationDetailsSource.buildDetails(request));
   }


   public void setPasswordParameter(String passwordParameter) {
      Assert.hasText(passwordParameter, "Password parameter must not be empty or null");
      this.passwordParameter = passwordParameter;
   }


   public void setPostOnly(boolean postOnly) {
      this.postOnly = postOnly;
   }

   public final String getUsernameParameter() {
      return this.usernameParameter;
   }

   public final String getPasswordParameter() {
      return this.passwordParameter;
   }

}
```

모두 볼 필요 없이, 왜 POST 요청의  x-www-form-urlencoded 방식으로만 로그인이 가능한지에 대해서만 알아보겠다.

![image-20211209165012823](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211209165012823.png)

우선 POST가 아닌 요청인 경우에 예외를 발생하는 부분은 쉽게 찾을 수 있을 것이다.

이후 username과 password를 받아오는 obtain~~~ 코드를 보면 다음과 같다.

![image-20211209165122817](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211209165122817.png)

보이는 바와 같이 getParameter로 데이터를 가져오기 때문에 parameter 형식이 아닌 JSON 데이터는 가져올 수 없는 것이다.

<br/>

### 그럼 어떻게 JSON으로 로그인 하지?

##### AbstractAuthenticationProcessingFilter나 UsernamePasswordAuthenticationFilter을 상속하여 처리할 수 있다. 여기서는 AbstractAuthenticationProcessingFilter를 상속받아 처리해보겠다.

우선 시작 전에 formlogin()의 전체적인 인증의 흐름을 살펴보자.

<br/>

## formlogin() 인증 절차

1. /login 으로 요청이 들어오면 UsernamePasswordAuthenticationFilter가 작동한다

   ![image-20211209170040547](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211209170040547.png)

   (username과 password를 사용하여 인증을 처리하며, 기본 url은 /login이고, POST의 요청을 처리하는 것을 알 수 있다.)

2. ##### attemptAuthentication 메소드가 작동하여 인증을 처리한다. 이때 username과 password로 UsernamePasswordAuthenticationToken을 만든 후, 이를 사용하여 AuthenticationManager의 authenticate()를 호출한다.![image-20211209170228898](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211209170228898.png)![image-20211209170419987](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211209170419987.png)

3. AuthenticationManager의 authenticate()에서는 UsernamePasswordAuthenticationToken의 정보를 이용하여 username과 password가 유효한지 검증한다.

<br/>

이제 직접 구현해보자.

<br/>

## 로그인 JSON으로 처리하기

#### AbstractAuthenticationProcessingFilter 상속

```java
package com.cnuboard.cnuboard.global.jsonlogin;

import com.cnuboard.cnuboard.global.handler.CustomLogInSuccessHandler;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.nimbusds.jose.util.StandardCharset;
import lombok.Data;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.lang.Nullable;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.AuthenticationServiceException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.web.authentication.AbstractAuthenticationProcessingFilter;
import org.springframework.security.web.authentication.AuthenticationFailureHandler;
import org.springframework.security.web.authentication.AuthenticationSuccessHandler;
import org.springframework.security.web.util.matcher.AntPathRequestMatcher;
import org.springframework.stereotype.Component;
import org.springframework.util.Assert;
import org.springframework.util.StreamUtils;
import org.springframework.util.StringUtils;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Slf4j
@Component
public class JsonUsernamePasswordAuthenticationFilter extends AbstractAuthenticationProcessingFilter {

    private final ObjectMapper objectMapper;

    public static final String SPRING_SECURITY_FORM_USERNAME_KEY = "username";

    public static final String SPRING_SECURITY_FORM_PASSWORD_KEY = "password";

    public static final String HTTP_METHOD = "POST";

    private static final AntPathRequestMatcher DEFAULT_ANT_PATH_REQUEST_MATCHER = new AntPathRequestMatcher("/login",
            HTTP_METHOD);
    
    
    @Autowired
    public JsonUsernamePasswordAuthenticationFilter(ObjectMapper objectMapper,
                                                    AuthenticationManager authenticationManager,
                                                    CustomLogInSuccessHandler customLogInSuccessHandler,//TODO : 이거 좀 더 이쁘게 수정
                                                    AuthenticationFailureHandler authenticationFailureHandler
    ) {
        super(DEFAULT_ANT_PATH_REQUEST_MATCHER, authenticationManager);
        this.objectMapper =objectMapper;
        setAuthenticationSuccessHandler(customLogInSuccessHandler);
        setAuthenticationFailureHandler(authenticationFailureHandler);

    }
    

    @Override
    public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response)
            throws AuthenticationException, IOException {
        log.info("JsonUsernamePasswordAuthenticationFilter 이 동작합니다!!!");

        if (!request.getMethod().equals(HTTP_METHOD) || !request.getContentType().equals("application/json")) {//POST가 아니거나 JSON이 아닌 경우
            log.error("POST 요청이 아니거나 JSON이 아닙니다!");
            throw new AuthenticationServiceException("Authentication method not supported: " + request.getMethod());
        }
        LoginDto loginDto = objectMapper.readValue(StreamUtils.copyToString(request.getInputStream(), StandardCharset.UTF_8), LoginDto.class);


        String username = loginDto.getUsername();
        String password = loginDto.getPassword();

        if(username ==null || password == null){
            throw new AuthenticationServiceException("DATA IS MISS");
        }

        UsernamePasswordAuthenticationToken authRequest = new UsernamePasswordAuthenticationToken(username, password);
        // Allow subclasses to set the "details" property
        setDetails(request, authRequest);
        return this.getAuthenticationManager().authenticate(authRequest);//getAuthenticationManager를 커스텀해줌
    }



    protected void setDetails(HttpServletRequest request, UsernamePasswordAuthenticationToken authRequest) {
        authRequest.setDetails(this.authenticationDetailsSource.buildDetails(request));
    }




    @Data
    private static class LoginDto{
        String username;
        String password;
    }

}

```

##### 중요한 코드는 다음과 같다.

![image-20211209171653015](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211209171653015.png)

- 우선 POST가 아니거나, Content Type이 JSON이 아닌 경우 예외를 발생시킨다.
- LoginDto 클래스를 만들어서 request의 데이터를 파싱한다.
- 비어있는 값이 있으면 오류를 발생시키며, 이후 AuthenticationManager의 authenticate를 통해 검증하는데, AuthenticationManager는 아래 나올 **JsonAuthenticationManager**를 사용한다.

<br/>

#### AuthenticationManager 상속

```java
@Component
@RequiredArgsConstructor
@Slf4j
public class JsonAuthenticationManager implements AuthenticationManager {

    private final UserDetailsService userDetailsService;

    @Override
    public Authentication authenticate(Authentication authentication) throws AuthenticationException {
        log.info("JsonAuthenticationManager 이 동작합니다!!!");
        UserDetails userDetails = userDetailsService.loadUserByUsername((String) authentication.getPrincipal());//username

        return new UsernamePasswordAuthenticationToken(userDetails
                , userDetails.getPassword()
                , userDetails.getAuthorities());
    }
}
```

UserDetailsService를 주입받아서, 검증을 시도한다.

##### 나는 UserDetailsService를 상속받은 MemberService에서 username을 통해서 DB에서 회원을 찾아오고, 비밀번호를 검증하는 코드를 작성하였다.

##### 이후 올바르다면 UsernamePasswordAuthenticationToken을 만들어서 반환하는 것을 알 수 있다.

<br/>

<br/>

## 설정하기

```java
@RequiredArgsConstructor
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {


    private final JsonUsernamePasswordAuthenticationFilter jsonUsernamePasswordAuthenticationFilter;


    @Override
    protected void configure(HttpSecurity http) throws Exception {;


        http
             
                .formLogin().disable()
                //== JSON 로그인 처리 ==//
                .addFilterBefore(jsonUsernamePasswordAuthenticationFilter, UsernamePasswordAuthenticationFilter.class)

    }

}

```

<br/>

<br/>

### 📔 Reference

##### [Spring Security UsernamePasswordAuthenticationFilter의 특징+ JWT](https://tech.junhabaek.net/spring-security-usernamepasswordauthenticationfilter%EC%9D%98-%EB%8D%94-%EA%B9%8A%EC%9D%80-%EC%9D%B4%ED%95%B4-8b5927dbc037)

##### [Spring Security 스프링시큐리티 커스텀 필터의 구현(3)](https://kimchanjung.github.io/programming/2020/07/03/spring-security-03/)

##### [Spring Security with REST API Login AS JSON](https://johnmarc.tistory.com/74)

##### 