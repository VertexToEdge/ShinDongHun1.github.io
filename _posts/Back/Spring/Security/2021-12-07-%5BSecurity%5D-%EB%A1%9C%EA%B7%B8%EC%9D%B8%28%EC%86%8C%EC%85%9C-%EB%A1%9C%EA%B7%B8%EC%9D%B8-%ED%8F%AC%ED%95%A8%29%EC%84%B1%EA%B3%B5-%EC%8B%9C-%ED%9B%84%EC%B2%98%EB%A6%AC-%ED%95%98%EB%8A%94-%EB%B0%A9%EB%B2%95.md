---
title:  "[Security] 로그인(소셜 로그인 포함)성공 시 후처리 하는 방법"
excerpt: "로그인 성공 시 후처리를 어떻게 할 수 있을까?"
date:   2021-12-07 02:57:00
header:
  teaser: /assets/images/spring.png

categories: Security
tags:
  - Security
last_modified_at: 2021-12-07T02:57:00
---

<br/>

## [Security] - Login이 성공했을 때 후처리 하는 방법

Spring Security를 사용한다면 login을 손쉽게 구현할 수 있다.

그러나 로그인 이후, 토큰을 발급한다던가 하는 추가적인 상황이 필요한 경우 어떻게 해결할 수 있는지 알아보겠다.

<br/>

## AuthenticationSuccessHandler 구현

##### 후처리 방법은 매우 간단한데, Spring Security에 존재하는 **AuthenticationSuccessHandler** 인터페이스를 구현하기만 하면 된다.

##### AuthenticationSuccessHandler 은 총 2개의 메소드로 이루어져 있고 그 중 하나는 default 메소드이다.

![image-20211207024943419](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211207024943419.png)

<br/>

이 인터페이스를 구현하는 Handler 클래스를 새롭게 작성하자.

```java
@Slf4j
@Component
public class CustomLogInSuccessHandler implements AuthenticationSuccessHandler {

    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
        
        log.info("로그인에 성공했습니다. 토큰을 발급합니다.");
    }
}
```

<br/>

##### 이후 Security Config를 설정해주는 곳(WebSecurityConfigurerAdapter)를 상속받은 곳에서successHandler를 등록해주자.

```java
@RequiredArgsConstructor
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    
    private final CustomLogInSuccessHandler customLogInSuccessHandler;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
                .formLogin()
                .successHandler(customLogInSuccessHandler);
             
    }
}
```

<br/>

## OAuth2를 사용하는 경우

마찬가지다.

```java
@RequiredArgsConstructor
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    
    private final CustomLogInSuccessHandler customLogInSuccessHandler;
 	private final CustomOAuth2UserService customOAuth2UserService;
 	
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
                .formLogin()
                .successHandler(customLogInSuccessHandler)
                
                .and()
                .oauth2Login()
                .successHandler(oAuth2LoginSuccessHandler)
                .userInfoEndpoint()
                .userService(customOAuth2UserService);
    }
}
```

##### oauth2Login 이후에 successHandler를 등록시켜 주자.

##### 이때 userInfoEndpoint().userService()가 먼저 실행되고, 그 이후에 successHandler()가 실행된다는 것도 알아두자!



<br/>

### 📔 Reference

##### [https://csy7792.tistory.com/332](https://csy7792.tistory.com/332)