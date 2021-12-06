---
title:  "[Security] REST API 통신에서 OAuth2 회원가입 이후, 추가 정보를 입력받는 방법"
excerpt: "소셜 회원으로 가입 시, 추가 정보를 입력받는 방법에 대해"
date:   2021-12-07 02:58:00
header:
  teaser: /assets/images/spring.png

categories: Security
tags:
  - Security
last_modified_at: 2021-12-07T02:58:00

---

<br/>

## REST API 통신에서 OAuth2가입 이후, 추가 정보를 입력받는 방법

요즘은 OAuth2를 이용한 소셜 로그인 방식을 많이 사용한다.

그런데 각각의 소셜 로그인 API마다 필수로 제공해야 하는 항목도 다르고, 추가적으로 필요한 정보가 더 필요한 경우에는 어떻게 처리를 해야할까?

이것에 대한 자료가 너무 없었기에, 처음에는 정말 힘들었다. 이게 좋은 방법인지는 확실하지 않으나 필자의 방법을 공유해보고자 한다.

<br/>

## userInfoEndpoint 설정

```java
package com.cnuboard.cnuboard.global.config;

import com.cnuboard.cnuboard.domain.member.Role;
import com.cnuboard.cnuboard.domain.member.service.oauth.CustomOAuth2UserService;
import com.cnuboard.cnuboard.global.config.handler.CustomLogInFailureHandler;
import com.cnuboard.cnuboard.global.config.handler.CustomLogInSuccessHandler;
import com.cnuboard.cnuboard.global.config.handler.CustomLogoutSuccessHandler;
import com.cnuboard.cnuboard.global.config.handler.OAuth2LoginSuccessHandler;
import com.cnuboard.cnuboard.global.jwt.TokenProvider;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.factory.PasswordEncoderFactories;
import org.springframework.security.crypto.password.PasswordEncoder;

@RequiredArgsConstructor
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    private final CustomOAuth2UserService customOAuth2UserService;
    private final OAuth2LoginSuccessHandler oAuth2LoginSuccessHandler;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
        		.csrf().disable()
        		
       			 // 세션을 사용하지 않기 때문에 STATELESS로 설정
                .and()
                .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
                
                
                .oauth2Login()
                .successHandler(oAuth2LoginSuccessHandler)
                .userInfoEndpoint()
                .userService(customOAuth2UserService)
                ;

}

```

- **userInfoEndpoint()** : oauth2Login 성공 이후, user정보를 받아오는 설정 시작
- **userService(customOAuth2UserService)** : customOAuth2UserService에서 처리하겠다고 설정.
- **successHandler(oAuth2LoginSuccessHandler)**: oauth2Login 성공 이후, **user정보를 받아오고 나서 실행.**(**userInfoEndpoint().userService(customOAuth2UserService)가 먼저 실행된다는 것을 알아두자**)

<br/>

우선 User의 정보를 받아오는 코드부터 살펴보도록 하자.

## OAuth2UserService 구현

userService에 등록하기 위해서는 **OAuth2UserService<OAuth2UserRequest, OAuth2User>**를 구현해야 한다.

```java
package com.cnuboard.cnuboard.domain.member.service.oauth;

import com.cnuboard.cnuboard.domain.member.Member;
import com.cnuboard.cnuboard.domain.member.SocialType;
import com.cnuboard.cnuboard.domain.member.repository.MemberRepository;
import com.cnuboard.cnuboard.domain.member.service.oauth.dto.OAuthAttributes;
import com.cnuboard.cnuboard.domain.member.service.oauth.store.MemberThreadLocal;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.oauth2.client.userinfo.DefaultOAuth2UserService;
import org.springframework.security.oauth2.client.userinfo.OAuth2UserRequest;
import org.springframework.security.oauth2.client.userinfo.OAuth2UserService;
import org.springframework.security.oauth2.core.OAuth2AuthenticationException;
import org.springframework.security.oauth2.core.user.DefaultOAuth2User;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Service;

import java.util.Collections;

@Service
@RequiredArgsConstructor
public class CustomOAuth2UserService implements OAuth2UserService<OAuth2UserRequest, OAuth2User> {

    private final MemberRepository memberRepository;

    private static final String NAVER="naver";
    private static final String KAKAO="kakao";
    private static final String GOOGLE="google";


    @Override
    public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException {
        OAuth2UserService<OAuth2UserRequest, OAuth2User> delegate = new DefaultOAuth2UserService();
        OAuth2User oAuth2User = delegate.loadUser(userRequest);
        //정보를 받아옴


        String registrationId = userRequest.getClientRegistration().getRegistrationId();/
        String userNameAttributeName = userRequest.getClientRegistration().getProviderDetails().getUserInfoEndpoint().getUserNameAttributeName();

        OAuthAttributes attributes = OAuthAttributes.of(registrationId, userNameAttributeName, oAuth2User.getAttributes());


        Member member = getMember(attributes, registrationId);
        MemberThreadLocal.memberThreadLocal.set(member);


        return new DefaultOAuth2User(
                Collections.singleton(new SimpleGrantedAuthority(member.getRole().getKey())),
                attributes.getAttributes(),
                attributes.getNameAttributeKey()
        );
    }





    private Member getMember(OAuthAttributes attributes, String registrationId ) {
        if (NAVER.equals(registrationId)) {
            return memberRepository.findBySocialTypeAndId(SocialType.NAVER, attributes.getId())
                    .orElse(memberRepository.save(attributes.toEntity(SocialType.NAVER)));

        }
        if (KAKAO.equals(registrationId)){
            return memberRepository.findBySocialTypeAndId(SocialType.KAKAO,attributes.getId())
                    .orElse(memberRepository.save(attributes.toEntity(SocialType.KAKAO)));
        }

        return memberRepository.findBySocialTypeAndId(SocialType.GOOGLE,attributes.getId())
                .orElse(memberRepository.save(attributes.toEntity(SocialType.GOOGLE)));

    }


}

```

[구글 로그인 기능 구현하기](https://shindonghun1.github.io/purplebook/%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B8%B0%EB%8A%A5-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%EC%8A%A4%ED%94%84%EB%A7%81-%EB%B6%80%ED%8A%B8%EC%99%80-AWS%EB%A1%9C-%ED%98%BC%EC%9E%90-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EC%9B%B9-%EC%84%9C%EB%B9%84%EC%8A%A4/)에서 사용했던 코드를 바꾸어보았다. 위 코드가 이해가 되지 않는다면, 저 포스팅을 참고하자. 여기서는 달라진 부분에 대해서만 설명하겠다.

#### getMember() 

##### 데이터베이스에 Member를 저장할 때, SocialType과 attributes의 id(소셜 로그인 API에서 제공하는 식별값, 네이버-id, 카카오-id, 구글-email)를 저장한다. 

각각의 소셜 로그인에서 제공하는 식별값이 다르기에, 이를 하나로 공통지어 사용하기 위해 사용한 방식이다. 네이버와 카카오는 id를 제공하는데, 각각의 소셜 미디어의 식별값은 겹치지 않겠지만, 혹시나 네이버의 id와 카카오의 id가 같을수도 있을거란 생각에 SocialType을 지정해주어, 혹시나 발생할 예외에 대한 처리를 해주었다.

<br/>

#### MemberThreadLocal.memberThreadLocal.set(member);

이전에는 세션을 사용하여 진행하였는데, REST 방식이므로 세션을 사용하지 않을것이다.

세션을 사용하지 않고 정보를 어떻게 저장할 수 있을지 생각해 보았는데, 최근에 공부했던 **ThreadLoca**l이 생각나서 이를 사용해보기로 했다.

```java
public class MemberThreadLocal {
    public static ThreadLocal<Member> memberThreadLocal = new ThreadLocal<>();
}
```

<br/>

<br/>

## OAuthAttributes 생성

소셜 로그인 api로부터 사용자에 대한 정보를 받아와 저장하는 dto인 OAuthAttributes를 생성했다.

과거에는 여기에 name, email등 많은 값들이 필드로 있었지만, 우리는 id(식별값)만 사용할 것이기에 과감히 다 지워줬다.

```java
@Getter
public class OAuthAttributes {
    private Map<String, Object> attributes;

    private String nameAttributeKey;//OAuth2 로그인 진행 시 키가 되는 필드값, Primary Key와 같은 의미
    private String id;//식별값, 구글의 경우 email, 카카오의 경우 kakaoId, 네이버의 경우id

    private static final String NAVER="naver";
    private static final String NAVER_NAME_ATTRIBUTE_KEY="id";
    private static final String KAKAO="kakao";
    private static final String GOOGLE="google";


    @Builder
    public OAuthAttributes(Map<String, Object> attributes, String nameAttributeKey, String id) {
        this.attributes = attributes;
        this.nameAttributeKey = nameAttributeKey;
        this.id = id;
    }

    public static OAuthAttributes of(String registrationId, String userNameAttributeName, Map<String, Object> attributes) {

        System.out.println(registrationId);

        if (NAVER.equals(registrationId)) {
            return ofNaver(NAVER_NAME_ATTRIBUTE_KEY, attributes);
        }
        if (KAKAO.equals(registrationId)){
            return ofKakao(userNameAttributeName,attributes);
        }


        return ofGoogle(userNameAttributeName, attributes);
    }

    private static OAuthAttributes ofKakao(String userNameAttributeName, Map<String, Object> attributes) {
        Map<String, Object> kakaoAccount = (Map<String, Object>)attributes.get("kakao_account");
        Map<String, Object> kakaoProfile = (Map<String, Object>)kakaoAccount.get("profile");

        return OAuthAttributes.builder()
                .id((String) kakaoProfile.get("id"))
                .attributes(attributes)
                .nameAttributeKey(userNameAttributeName)
                .build();
    }


    public static OAuthAttributes ofGoogle(String userNameAttributeName, Map<String, Object> attributes) {
        return OAuthAttributes.builder()
                .id((String) attributes.get("email"))
                .attributes(attributes)
                .nameAttributeKey(userNameAttributeName)
                .build();
    }

    public static OAuthAttributes ofNaver(String userNameAttributeName, Map<String, Object> attributes) {
        Map<String, Object> response = (Map<String, Object>) attributes.get("response");

        return OAuthAttributes.builder()
                .id((String) response.get("id"))
                .attributes(response)
                .nameAttributeKey(userNameAttributeName)
                .build();
    }



    public Member toEntity(SocialType socialType){
        return Member.builder()
                .socialType(socialType)
                .socialId(id)
                .role(Role.GUEST)
                .build();
    }
}

```

#### .id((String) response.get("id"))

구글은 email을, 나머지는 id를 사용해서 식별값을 지정해주었다.

<br/>

#### toEntity(SocialType socialType)

이는 정보제공에 동의를 눌렀으나, 아직 회원가입이 완료되지 않은 상태(즉 추가정보를 입력하지 않은 상태)일 때 사용되며, 동의를 하였으나 아직 추가 정보를 더 입력해야 하기 때문에 GUEST의 권한을 주었다.

<br/>

<br/>

## 추가정보 입력

이제 추가정보를 입력하는 부분이다. 우리는 `SecurityConfig`에서 `successHandler`로 `oAuth2LoginSuccessHandler`를 등록했다

이부분에서 우리는 추가정보를 입력하는 처리를 해주면 된다.

```java
@Slf4j
@Component
public class OAuth2LoginSuccessHandler implements AuthenticationSuccessHandler {
    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
        try {
            Member member = MemberThreadLocal.memberThreadLocal.get();
            if(member.getRole() == Role.GUEST){
                log.info("아직 회원가입을 진행하지 않는 사용자입니다. 리다이렉션합니다.");
                response.sendRedirect("프론트엔드의 소셜 회원가입 정보입력 창 URL");
            }else {
                log.info("소셜 로그인에 성공했습니다. 토큰을 발급합니다.");
            }
        }catch (Exception e){
            throw e;
        }finally {
            MemberThreadLocal.memberThreadLocal.remove();
        }
    }
}

```

##### 과정

- 우선 MemberThreadLocal에 들어있는 member정보를 가져온다. 이는 CustomOAuth2UserService에서 저장해 주었기 때문에, 그 이후 실행되는 OAuth2LoginSuccessHandler에서 사용할 수 있는 것이다.
- 찾아온 멤버의 역할이 GUEST라면, 즉 아직 회원가입을 진행하지 않은 사용자라면, 리다이렉트를 시켜서 회원가입을 할 수 있도록 만든다. 이때 리다이렉션의 처리는 서버에서 하는것이 아니라, 요청을 보낸 프론트엔드의 주소로 redirect를 시킴으로써 추가적인 정보를 입력받아 서버에 회원가입 요청을 할 수 있게 만들었다

<br/>