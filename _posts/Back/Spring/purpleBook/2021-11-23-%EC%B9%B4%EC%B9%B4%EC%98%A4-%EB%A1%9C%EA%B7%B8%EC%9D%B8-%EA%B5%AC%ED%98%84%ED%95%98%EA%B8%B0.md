---
title:  "카카오 로그인 구현하기"
excerpt: "스프링 부트와 AWS로 혼자 구현하는 웹 서비스 4-4"
date:   2021-11-23 18:36:00 
header:
  teaser: /assets/images/spring.png

categories: purpleBook
tags:
  - Java
  - Spring
last_modified_at: 2021-11-23T18:36:00


---

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124204433310.png" alt="image-20211124204433310" style="zoom:30%;" />



<br/>

## 카카오 구현하기

[카카오 개발자 페이지](https://developers.kakao.com/console/app)로 이동하자.

![image-20211123193815385](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123193815385.png)

[애플리케이션 추가하기] 버튼을 누르자

<br/>

![image-20211123194043571](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123194043571.png)



##### 먼가 허용되지 않는 이름이 참 많았다 :(

<br/>

![image-20211123194153896](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123194153896.png)

##### 클릭

<br/>

![image-20211123194216705](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123194216705.png)

##### 좌측 사이드바의 [카카오 로그인]을 클릭하자.

<br/>

![image-20211123194258080](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123194258080.png)

![image-20211123194308594](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123194308594.png)

![image-20211123194321203](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123194321203.png)

<br/>

![image-20211123194404160](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123194404160.png)

##### http://localhost:8080/login/oauth2/code/kakao 로 리다이렉트 URI를 등록하자.

<br/>

### 동의항목 설정

![image-20211123194517691](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123194517691.png)

![image-20211123194459468](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123194459468.png)

##### 닉네임과 프로필 사진만 필수 동의를 하고 진행하겠다.

<br/>

### API 확인

앱설정 -> 요약 정보로 이동하자

![image-20211123194739762](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123194739762.png)

REST API키가 이전에 했던 ClientId이다.

<br/>

#### [선택] 시크릿 키 발급

제품 설정 -> 보안으로 이동

![image-20211123194909993](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123194909993.png)

<br/>

<br/>

### 시큐리티 설정하기

[카카오톡 로그인 API](https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api) 를 보고 참고하자.

#### application-oauth.propertuies

```properties

spring.security.oauth2.client.registration.kakao.client-id=REST API 키
spring.security.oauth2.client.registration.kakao.client-secret=시크릿 키
spring.security.oauth2.client.registration.kakao.redirect-uri=http://localhost:8080/login/oauth2/code/kakao

#중요!!
spring.security.oauth2.client.registration.kakao.client-authentication-method=POST 

spring.security.oauth2.client.registration.kakao.authorization-grant-type=authorization_code
spring.security.oauth2.client.registration.kakao.scope=profile_nickname,profile_image
spring.security.oauth2.client.registration.kakao.client-name=Kakao

spring.security.oauth2.client.provider.kakao.authorization-uri=https://kauth.kakao.com/oauth/authorize
spring.security.oauth2.client.provider.kakao.token-uri=https://kauth.kakao.com/oauth/token
spring.security.oauth2.client.provider.kakao.user-info-uri=https://kapi.kakao.com/v2/user/me
spring.security.oauth2.client.provider.kakao.user-name-attribute=id

```

##### spring.security.oauth2.client.registration.kakao.client-authentication-method=POST 

- 카카오는 다른 api와 다르게 위 코드가 필요하다.
- ![image-20211123200636180](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123200636180.png)



<br/>

#### OAuthAttributes 추가

```java
package web.purplebook.config.auth.dto;

import lombok.Builder;
import lombok.Getter;
import web.purplebook.domain.user.Role;
import web.purplebook.domain.user.User;

import java.util.Map;

@Getter
public class OAuthAttributes {

    private Map<String, Object> attributes;
    private String nameAttributeKey;//OAuth2 로그인 진행 시 키가 되는 필드값, Primary Key와 같은 의미.
    private String name;
    private String username;
    private String email;
    private String picture;

    private static final String NAVER="naver";
    private static final String NAVER_NAME_ATTRIBUTE_KEY="id";
    private static final String KAKAO="kakao";


    @Builder
    public OAuthAttributes(Map<String, Object> attributes, String nameAttributeKey, String name, String username, String email, String picture) {
        this.attributes = attributes;
        this.nameAttributeKey = nameAttributeKey;
        this.name = name;
        this.username = username;
        this.email = email;
        this.picture = picture;
    }

    public static OAuthAttributes of(String registrationId, String userNameAttributeName, Map<String, Object> attributes) {
        if (NAVER.equals(registrationId)) {
            return ofNaver(NAVER_NAME_ATTRIBUTE_KEY, attributes);
        }
        if (KAKAO.equals(registrationId)){
            return ofKakao(userNameAttributeName,attributes);
        }

        return ofGoogle(userNameAttributeName, attributes);
    }

    private static OAuthAttributes ofKakao(String userNameAttributeName, Map<String, Object> attributes) {
        // kakao는 kakao_account에 유저정보가 있다. (email)
        Map<String, Object> kakaoAccount = (Map<String, Object>)attributes.get("kakao_account");
        // kakao_account안에 또 profile이라는 JSON객체가 있다. (nickname, profile_image)
        Map<String, Object> kakaoProfile = (Map<String, Object>)kakaoAccount.get("profile");

        return OAuthAttributes.builder()
                .name((String) kakaoProfile.get("nickname"))
                .picture((String) kakaoProfile.get("profile_image_url"))
                .attributes(attributes)
                .nameAttributeKey(userNameAttributeName)
                .build();
    }


    public static OAuthAttributes ofGoogle(String userNameAttributeName, Map<String, Object> attributes) {
        return OAuthAttributes.builder()
                .name((String) attributes.get("name"))
                .email((String) attributes.get("email"))
                .picture((String) attributes.get("picture"))
                .attributes(attributes)
                .nameAttributeKey(userNameAttributeName)
                .build();
    }

    public static OAuthAttributes ofNaver(String userNameAttributeName, Map<String, Object> attributes) {
        Map<String, Object> response = (Map<String, Object>) attributes.get("response");

        return OAuthAttributes.builder()
                .name((String) response.get("name"))
                .email((String) response.get("email"))
                .picture((String) response.get("profile_image"))
                .attributes(response)
                .nameAttributeKey(userNameAttributeName)
                .build();
    }



    public User toEntity(){//domain의 USER, 아직 회원가입은 안 하고 소셜 로그인 동의만 한 상태
        return User.builder()
                .name(name)
                .email(email)
                .picture(picture)
                .role(Role.GUEST)
                .build();
    }


}
```

<br/>

#### index.html에 추가

```html
<a href="/oauth2/authorization/kakao"class="btn btn-light active" role="button" th:unless="${not #strings.isEmpty(username)}">Kakao Login</a>
```

<br/>

<br/>

<br/>

### 확인해보자

![image-20211123201231007](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123201231007.png)

![image-20211123201239952](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123201239952.png)

![image-20211123201248952](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123201248952.png)

![image-20211123201258962](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123201258962.png)

<br/>

#### 성공이다!!!

<br/>

<br/>

### 📔 Reference

[[Spring] 스프링으로 OAuth2 로그인 구현하기3 - 카카오](https://loosie.tistory.com/302)

[카카오톡 로그인 API, REST API사용법](https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#req-user-info)