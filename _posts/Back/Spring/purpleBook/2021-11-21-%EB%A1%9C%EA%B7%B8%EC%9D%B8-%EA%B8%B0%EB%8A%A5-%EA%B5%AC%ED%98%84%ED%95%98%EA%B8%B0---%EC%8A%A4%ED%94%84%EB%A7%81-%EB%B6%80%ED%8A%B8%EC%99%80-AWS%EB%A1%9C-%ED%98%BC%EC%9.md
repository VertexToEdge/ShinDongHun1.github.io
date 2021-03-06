---
title:  "구글 로그인 기능 구현하기 - 스프링 부트와 AWS로 혼자 구현하는 웹 서비스"
excerpt: "스프링 부트와 AWS로 혼자 구현하는 웹 서비스 4"
date:   2021-11-23 01:16:00 
header:
  teaser: /assets/images/spring.png

categories: purpleBook
tags:
  - Java
  - Spring
last_modified_at: 2021-11-23T01:16:00


---

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124204433310.png" alt="image-20211124204433310" style="zoom:30%;" />

<br/>

## 스프링 시큐리티

스프링 시큐리티는 막강한 인증과 인가(권한 부여) 기능을 가진 프레임워크이다.

사실상 스프링 기반의 애플리케이션에서는 보안을 위한 표준이라고 보면 된다.

인터셉터, 필터 기반의 보안 기능을 구현하는 것보다 스프링 시큐리티를 통해 구현하는 것을 적극 권장하고 있다.

여기서는 스프링 시큐리티와 OAuth2을 구현한 구글 로그인을 연동하여 로그인 기능을 만들어보겠다.

<br/>

## 스프링 부트 1.5 VS 스프링 부트 2.0

스프링 부트 1.5에서의 OAuth2 연동 방법이 2.0에서는 크게 변경되었다.

그러나 인터넷 자료들을 보면 설정 방법이 크게 달라진 것이 없는데 이는 

##### spring-security-oauth2-autoconfigure 

덕분이다.

이 라이브러리를 사용할 경우 스프링 부트 2에서도 1.5에서의 설정을 그대로 가져갈 수 있다.

그러나 이 책의 필자는 Spring Security Oauth2 Client 라이브러리를 사용해서 진행한다 밝혔다. 이유는 다음과 같다.

- 스프링 팀에서 기존 1.5에서 사용되던 spring-security-oauth 프로젝트는 유지 상태로 결정했으며 더는 신규 기능은 추가하지 않고 버그 수정 정도의 기능만 추가될 예정, 신규 기능은 새 oauth2 라이브러리에서만 지원하겠다고 선언.
- 스프링 부트용 라이브러리(starter)출시
- ...

그리고 한 가지 더 이야기하지면, 이 책(이 글)이외에 스프링 부트 2 방식의 자료를 찾고 싶은 경우 인터넷 자료들 사이에서 다음 두 가지만 확인하면 된다.

먼저 spring-security-oauth2-autoconfigure 라이브러리를 썼는지

application.properties 혹은 application.yml 정보가 다음과 같이 차이가 있는지.

##### 스프링 부트 1.5

![image-20211122155751761](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122155751761.png)

<br/>

##### 스프링 부트 2.0

![image-20211122155843903](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122155843903.png)

<br/>

스프링 부트 1.5 방식에서는 url 주소를 모두 명시해야 했지만 2.0 방식에서는 client 인증 정보만 입력하면 된다. 1.5 방식에서 직접 입력했던 값들은 2.0 버전으로 오면서 모두 enum으로 대체되었다.

**CommonOAuth2Provider**라는 enum이 새롭게 추가되어 **구글, 깃허브, 페이스북, 옥타**의 기본 설정값은 모두 여기서 제공한다.

```java
public enum CommonOAuth2Provider {

   GOOGLE {

      @Override
      public Builder getBuilder(String registrationId) {
         ClientRegistration.Builder builder = getBuilder(registrationId,
               ClientAuthenticationMethod.CLIENT_SECRET_BASIC, DEFAULT_REDIRECT_URL);
         builder.scope("openid", "profile", "email");
         builder.authorizationUri("https://accounts.google.com/o/oauth2/v2/auth");
         builder.tokenUri("https://www.googleapis.com/oauth2/v4/token");
         builder.jwkSetUri("https://www.googleapis.com/oauth2/v3/certs");
         builder.issuerUri("https://accounts.google.com");
         builder.userInfoUri("https://www.googleapis.com/oauth2/v3/userinfo");
         builder.userNameAttributeName(IdTokenClaimNames.SUB);
         builder.clientName("Google");
         return builder;
      }

   },

   GITHUB {

      @Override
      public Builder getBuilder(String registrationId) {
         ClientRegistration.Builder builder = getBuilder(registrationId,
               ClientAuthenticationMethod.CLIENT_SECRET_BASIC, DEFAULT_REDIRECT_URL);
         builder.scope("read:user");
         builder.authorizationUri("https://github.com/login/oauth/authorize");
         builder.tokenUri("https://github.com/login/oauth/access_token");
         builder.userInfoUri("https://api.github.com/user");
         builder.userNameAttributeName("id");
         builder.clientName("GitHub");
         return builder;
      }

   },

   FACEBOOK {

      @Override
      public Builder getBuilder(String registrationId) {
         ClientRegistration.Builder builder = getBuilder(registrationId,
               ClientAuthenticationMethod.CLIENT_SECRET_POST, DEFAULT_REDIRECT_URL);
         builder.scope("public_profile", "email");
         builder.authorizationUri("https://www.facebook.com/v2.8/dialog/oauth");
         builder.tokenUri("https://graph.facebook.com/v2.8/oauth/access_token");
         builder.userInfoUri("https://graph.facebook.com/me?fields=id,name,email");
         builder.userNameAttributeName("id");
         builder.clientName("Facebook");
         return builder;
      }

   },

   OKTA {

      @Override
      public Builder getBuilder(String registrationId) {
         ClientRegistration.Builder builder = getBuilder(registrationId,
               ClientAuthenticationMethod.CLIENT_SECRET_BASIC, DEFAULT_REDIRECT_URL);
         builder.scope("openid", "profile", "email");
         builder.userNameAttributeName(IdTokenClaimNames.SUB);
         builder.clientName("Okta");
         return builder;
      }

   };

   private static final String DEFAULT_REDIRECT_URL = "{baseUrl}/{action}/oauth2/code/{registrationId}";

   protected final ClientRegistration.Builder getBuilder(String registrationId, ClientAuthenticationMethod method,
         String redirectUri) {
      ClientRegistration.Builder builder = ClientRegistration.withRegistrationId(registrationId);
      builder.clientAuthenticationMethod(method);
      builder.authorizationGrantType(AuthorizationGrantType.AUTHORIZATION_CODE);
      builder.redirectUri(redirectUri);
      return builder;
   }

   /**
    * Create a new
    * {@link org.springframework.security.oauth2.client.registration.ClientRegistration.Builder
    * ClientRegistration.Builder} pre-configured with provider defaults.
    * @param registrationId the registration-id used with the new builder
    * @return a builder instance
    */
   public abstract ClientRegistration.Builder getBuilder(String registrationId);

}
```

이곳에 명시된 소셜 로그인이 아닌 다른 방식(네이버, 카카오 등)을 추가한다면 직접 다 추가해 주어야 한다. 이점을 기억해 해당 블로그에서 어떤 방식을 사용하는지 확인 후 참고하도록 하자.

<br/>

<br/>

## 구글 서비스 등록

[구글 클라우드 플랫폼](https://console.cloud.google.com)으로 이동한다

![image-20211122160459855](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122160459855.png)

##### 프로젝트 선택을 클릭한다.

<br/>

![image-20211122160655837](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122160655837.png)

##### [새 프로젝트] 버튼을 클릭한다.

<br/>

![image-20211122160912398](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122160912398.png)

##### 등록될 서비스의 이름을 입력한다. 원하는 이름으로 지으면 되고, 나는 social-login-google-test로 지었다. 위치는 조직 없음으로 해주었다.

<br/>

![image-20211122161028672](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122161028672.png)

##### 생성이 완료되면 다음과 같은 창이 뜰 것이다.(진짜 똑같이 보여주려고 전체 화면을 캡쳐했다..) API 및 서비스를 클릭하자. 

<br/>

![image-20211122161418097](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122161418097.png)

##### [사용자 인증 정보]를 클릭 후 [사용자 인증 정보 만들기] 버튼을 클릭한다.

##### 이후 [OAuth 클라이언트 ID]를 클릭하자.

<br/>

![image-20211122161507958](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122161507958.png)

##### [동의 화면 구성]을 클릭하자

<br/>

![image-20211122161620565](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122161620565.png)

##### 여기서부터 책과 조금 달랐다. 우선 우리는 조직 내 사용자만 사용하는 것이 아닌, 아무 사람이나 구글 계정을 가지고 있으면 로그인을 할 수 있도록 만들 것이기 때문에 외부로 하는 것이 맞다고 판단하여 외부를 선택했다. 이 글을 보는 여러분들도 외부를 클릭하고 만들기를 눌러주자.

<br/>

![image-20211122162610523](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122162610523.png)

##### 먼저 앱 정보이다.

- 앱 이름 : 구글 로그인 시 사용자에게 노출될 애플리케이션 이름을 이야기한다.
- 사용자 지원 이메일: 사용자 동의 화면에서 노출될 이메일 주소이다. 보통은 서비스의 help 이메일 주소를 사용하지만 여기서는 그냥 우리들의 이메일 주소를 사용하면 된다.

<br/>

![image-20211122163319434](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122163319434.png)

##### 이것들은 아직 잘 모르겠다... 우선 우리는 테스트만 할거니까 공백으로 두고 넘어가자

##### 개발자 연락처 정보에는 자신이 주로 사용하는 이메일을 적어주도록 하자.

##### 작성했다면 [저장 후 계속]버튼을 눌러주자.

<br/>

![image-20211122163854202](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122163854202.png)

##### 모르겠다. 빈칸으로 두고 [저장 후 계속]버튼을 눌러주자.

<br/>

![image-20211122163935257](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122163935257.png)

##### 모르겠다. 빈칸으로 두고 [저장 후 계속]버튼을 눌러주자.

<br/>

![image-20211122164232363](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122164232363.png)

##### 완료되면 다음과 같이 요약이 뜰것인데 맨 아래 [대시보드로 돌아가기]를 눌러주자.

<br/>

##### 이제 OAuth2 클라이언트 ID를 발급받을 차례이다. 다시 처음과 같이 [사용자 인증 정보]로 들어가서 [사용자 인증 정보 만들기]를 클릭 후 [OAuth 클라이언트 ID]를 클릭하자.

![image-20211122164455068](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122164455068.png)

<br/>

![image-20211122164711612](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122164711612.png)

- ##### 애플리케이션 유형 : 웹 애플리케이션

- ##### 이름 : 맘대로 지어주자.

#### 승인된 리디렉션 URI

- 서비스에서 파라미터로 인증 정보를 주었을 때 인증이 성공하면 구글에서 리다이렉트할  URL이다.

- 스프링 부트 2 버전의 시큐리티에서는 기본적으로 

  ##### [도메인]/login/oauth2/code/{소셜서비스코드}

  로 리다이렉트 URL을 지원하고 있다.

- 사용자가 별도록 리다이렉트 URL을 지원하는 Controller를 만들 필요가 없다. 시큐리티에서 이미 구현해 놓은 상태이다.

- 현재는 개발 단계이므로 http://localhost:8080/login/oauth2/code/google로만 등록한다.

- 이후 AWS 서버에 배포하게 되면 localhost외에 추가로 주소를 추가해야 하며, 이건 이후 단계에서 진행한다.

##### 다 작성하였다면  맨 아래 [만들기] 버튼을 클릭해주자.

<br/>

![image-20211122165323025](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122165323025.png)

완료됐다. 위 창에서 클라이언트 ID와 보안 비밀번호를 가지고 있자.

##### 이는 절대 외부로 유출되어서는 안된다.

이 화면에서 실수로 복사를 못했어도 상관없다. 다시 확인할 수 있다!

<br/>

<br/>

### application-oauth.properties 등록

application.properties와 동일한 경로에 application-oauth.properties 파일을 생성해주자.

![image-20211122165923483](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122165923483.png)

<br/>

![image-20211122170311160](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122170311160.png)

```properties
spring.security.oauth2.client.registration.google.client-id=클라이언트 ID
spring.security.oauth2.client.registration.google.client-secret=클라이언트 보안 비밀번호
spring.security.oauth2.client.registration.google.scope=profile,email
```

- ##### 많은 예제에서는 이 scope를 별도로 등록하지 않고 있다.

- ##### 기본값이 openid, profile, email이기 때문이다.

- ##### profile, email를 강제로 등록한 이유는 openid라는 scope가 있으면 Open Id Provider로 인식하기 때문이다.

- ##### 이렇게 되면 OpenId Provider인 서비스(구글)와 그렇지 않은 서비스(네이버/카카오 등)로 나눠서 각각 OAuth2Service를 만들어야 한다.

- ##### 하나의 OAuth2Service로 사용하기 위해 일부러 openid scope를 빼고 등록한다.

<br/>

##### 스프링 부트에서는 properties의 이름을 application-xxx.properties로 만들면 xxx라는 이름의 profile이 생성되어 이를 통해 관리할 수 있다.

##### 즉 profile=xxx라는 식으로 호출하면 해당 properties의 설정들을 가져올 수 있다.

호출하는 방식에는 여러 방식이 있지만 이 책에서는(이 글에서는)스프링 부트의 기본 설정 파일인 application.properties에서 application-oauth.properties를 포함하도록 구성한다.

<br/>

##### application.properties에 다음과 같은 코드 추가.

```properties
spring.profiles.include=oauth
```

<br/>

### .gitignore 등록

구글 로그인을 위한 클라이언트ID와 클라이언트 보안 비밀번호는 보안이 중요한 정보들이다.

이들이 외부에 노출될 경우 언제든 개인정보를 가져갈 수 있는 취약점이 될 수 있다.

깃허브와 연동해서 applicaiton-oauth.properties 파일을 올릴 경우 문제가 될 수 있기 때문에 이를 방지하기 위해 .gitignore파일에 다음 코드를 추가한다.

```properties
applicaion-oauth.properties
```

![image-20211122172008640](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122172008640.png)

##### 설정했다면 커밋 후 푸쉬해보자.

[gitignore가 작동하지 않는다면](https://jojoldu.tistory.com/307)

<br/>

<br/>

## 구글 로그인 연동하기

사용자 정보를 담당할 User 클래스를 생성하자.

domain 패키지 아래에 user패키지를 생성해서 만들자.

![image-20211122174608340](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122174608340.png)

<br/>

```java
package web.purplebook.domain.user;

import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import web.purplebook.domain.BaseTimeEntity;

import javax.persistence.*;

@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Entity
public class User extends BaseTimeEntity {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "USER_ID")
    private Long id;

    @Column(unique = true)
    private String username;

    @Column(nullable = false)
    private String name;

    @Column(unique = true)
    private String email;

    private String picture;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private Role role;

    @Builder
    public User( String name, String username,String email, String picture, Role role) {
        this.name = name;
        this.username = username;
        this.email = email;
        this.picture = picture;
        this.role = role;
    }
    public User update(String name, String picture){
        this.name = name;
        this.picture = picture;
        return this;
    }

    public String getRoleKey() {
        return this.role.getKey();
    }


    public void googleSignUp(String username){
        this.username = username;
        this.role = Role.USER;
    }
}


```

##### googleSignUp

- 책에는 없고 나 혼자 추가한 코드이다.
- 조금 이따가 구글을 통한 정보 제공 동의 후, 추가 정보를 입력받아 회원가입을 진행할 때 사용된다.

<br/>

<br/>

##### Role 클래스 생성

```java
package web.purplebook.domain.user;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum Role {

    GUEST("ROLE_GUEST","손님"),
    USER("ROLE_USER","일반 사용자"),
    ADMIN("ROLE_ADMIN", "관리자");

    private final String key;
    private final String title;

}
```

##### 책에서는 ADMIN 역할은 부여하지 않았으나 임의로 생성하였다.

##### 스프링 시큐리티에서는 권한 코드에 항사 ROLE_이 앞에 있어야만 한다.(근데 필자가 며칠 전 대회에서 권한을 부여할 때는 ROLE\_을 사용하지 않고 하였는데도, 권한이 잘 작동했었는데 나중에 알아봐야겠다.)

<br/>

##### UserRepository 생성

```java
package web.purplebook.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import web.purplebook.domain.user.User;

import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByUsername(String username);
    Optional<User> findByEmail(String email);
}

```

<br/>

<br/>

### 스프링 시큐리티 의존성 추가

```properties
implementation 'org.springframework.boot:spring-boot-starter-security'
implementation 'org.springframework.boot:spring-boot-starter-oauth2-client'
```

```properties
plugins {
   id 'org.springframework.boot' version '2.6.0'
   id 'io.spring.dependency-management' version '1.0.11.RELEASE'
   id 'java'
}

group = 'web'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '17'

repositories {
   mavenCentral()
}

dependencies {
   implementation 'org.springframework.boot:spring-boot-starter'
   testImplementation 'org.springframework.boot:spring-boot-starter-test'

   //Spring Data JPA 추가
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
    //h2 데이터베이스 추가
    runtimeOnly 'com.h2database:h2'


   //타임리프 추가
   implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'

   implementation 'org.springframework.boot:spring-boot-starter-web'

   //시큐리티 추가
   implementation 'org.springframework.boot:spring-boot-starter-security'
   implementation 'org.springframework.boot:spring-boot-starter-oauth2-client'

   compileOnly 'org.projectlombok:lombok'
   annotationProcessor 'org.projectlombok:lombok'

   //테스트에서 lombok 사용
   testCompileOnly 'org.projectlombok:lombok'
   testAnnotationProcessor 'org.projectlombok:lombok'
}

test {
   useJUnitPlatform()
}
```

##### 전체 gradle은 다음과 같다.

##### 책에서는 oauth2-client없이도 잘 작동하였지만 버전이 업데이트 되면서 바뀐 것 같다.

<br/>

#### config.auth패키지 생성

앞으로 시큐리티 관련 클래스는 모두 이곳에 담아서 관리할 것이다.

![image-20211122180213367](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122180213367.png)

<br/>

### SecurityConfig 클래스 작성

CustomOAuth2UserService 클래스를 만들지 않아 컴파일 에러가 발생하지만, 우선 작성하고 이후에 추가하겠다.

##### 참고

- 작성 중 팁을 주자면 ctrl + o를 눌러서 Override할 메소드를 선택할 수 있다

![image-20211122180800369](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122180800369.png)

<br/>

#### SecurityConfig 생성

<script src="https://gist.github.com/ShinDongHun1/5de105c91becdc363bbca9b2a7cdef31.js"></script>

<br/>

#### CustomOAuth2UserService 생성

<script src="https://gist.github.com/ShinDongHun1/cf7734c660b7e4384060f9a013c1a34a.js"></script>

##### registrationId 

- 현재 로그인 진행 중인 서비스를 구분하는 코드. 지금은 구글만 사용하여 필요가 없으나 이후 네이버, 카카오 등 연동 시에 구분을 위해 사용한다.

##### userNameAttributeName

- OAuth2 로그인 진행 시 키가 되는 필드값. Primary Key와 같은 의미.
- 구글의 경우 기본적으로는 코드를 지원하지만, 네이버, 카카오 등은 지원하지 않는다. 구글의 기본 코드는 **"sub"** 이다
- 이후 네이버 로그인과 구글 로그인을 동시 지원할 때 사용된다.

##### OAuthAttributes

- OAuth2UserService 를 통해 가져온 OAuth2User의 attribute를 담을 클래스이다.
- 이후 네이버 등 다른 소셜 로그인도 이 클래스를 사용한다.
- 이 다음에 이 클래스를 작성할 것이니 지금은 오류가 나도 넘어가자.

##### SessionUser

- 세션에 사용자 정보를 저장하기 위한 Dto 클래스이다. 
- 왜 User 클래스를 쓰지 않고 Dto를 새로 만들어서 사용하는지는 이후에 설명하겠다

> ##### 참고 
>
> 나는 Rest API 방식으로 이후 프로젝트들을 진행하고 싶다. 따라서 세션을 쓸 생각이 없지만, 아직은 세션을 안 쓰고 어떻게 구현해야 할 지 모르기 때문에 우선을 책을 따라 세션을 사용하여 구현할 생각이다. 이후 세션 없이 어떻게 구현하는 지에 대해서는 공부 후 따로 업로드 하겠다.

<br/>

#### <span style="color:red">참고</span>

##### 구글의 경우 email을 필수 제공 정보로 등록하며, 이는 겹치지 않는다 따라서 findByEmail을 통해 특정 회원을 식별할 수 있다. 그러나 카카오의 경우 email을 제공하지 않을수도 있다. 따라서 카카오의 경우 카카오에서 제공하는 kakaoId를 통해 따로 식별하도록 코드를 작성하여야 한다.

<br/>

#### OAuthAttributes 클래스 생성

OAuthAttributes 는 Dto기 때문에 config/auth/dto 패키지를 생성하여 추가해준다.

![image-20211122184214726](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122184214726.png)



<script src="https://gist.github.com/ShinDongHun1/ab56945bd9ecb0e241f9f21ea18d5990.js"></script>

##### of

- OAuth2User에서 반환하는 사용자 정보는 Map 이기 때문에 값 하나하나를 변환해야만 한다.

##### toEntity()

- User 엔티티를 생성한다
- OAuthAttributes에서 엔티티를 생성하는 시점은 처음 가입할 때이다.
- 가입할 때의 기본 권한을 GUEST로 주기 위해서 role 빌더값에는 Role.GUEST를 사용한다.
- OAuthAttributes 클래스 생성이 끝났으면 같은 패키지에 SessionUser 클래스를 생성한다.

<br/>

#### SessionUser 생성

```java
package web.purplebook.config.auth.dto;

import lombok.Getter;
import web.purplebook.domain.user.User;

import java.io.Serializable;

@Getter
public class SessionUser implements Serializable {

    private Long id;
    private String name;
    private String username;
    private String email;
    private String picture;


    public SessionUser(User user) {
        this.id = user.getId();
        this.name = user.getName();
        this.username = user.getUsername();
        this.email = user.getEmail();
        this.picture = user.getPicture();
    }
}

```

<br/>

<br/>

#### 왜 User 클래스를 그대로 사용하지 않나요?

User클래스를 세션에 저장하기 위해 사용한다면 **직렬화를 구현해야 한다.**

그러나 User 클래스는 엔티티이기 때문에 언제 다른 엔티티와 관계가 형성될지 모른다.

다른 엔티티와 관계가 형성된다면(예를 들어 @OneToMany, @ManyToOne) 직렬화 대상에 이들까지 포함되어 성능 이슈, 부수 효과가 발생할 확률이 높다.

따라서 직렬화 기능을 가진 세션 Dto를 하나 추가로 만드는 것이 이후 운영 및 유지보수 때 많은 도움이 된다.

<br/>

<br/>

### 화면 구성하기

##### index.html 추가

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
        <!-- 로그인 기능 -->
        <span id="user" th:if="${not #strings.isEmpty(username)}" th:text="${username}"></span>
        <a href="/logout"class="btn btn-info active" role="button" th:if="${not #strings.isEmpty(username)}">Logout</a>

        <a href="/oauth2/authorization/google"class="btn btn-success active" role="button" th:unless="${not #strings.isEmpty(username)}">Google Login</a>

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
import web.purplebook.config.auth.dto.SessionUser;
import web.purplebook.service.posts.PostsService;
import web.purplebook.web.dto.PostsResponseDto;

import javax.servlet.http.HttpSession;

@Controller
@RequiredArgsConstructor
public class IndexController {

    private final PostsService postsService;
    private final HttpSession httpSession;

    @GetMapping("/")
    public String index(Model model){
        model.addAttribute("posts", postsService.findAllDesc());

        SessionUser user = (SessionUser) httpSession.getAttribute("user");
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

책에서와 달리 user.getUsername() != null 조건을 넣어서 동의만 하고 가입은 안 한 상태일 경우에는 무시하도록 만들었다.

<br/>

![image-20211122200914743](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122200914743.png)

![image-20211122200924872](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211122200924872.png)

<br/>

<br/>

### 제공하는 정보 외에 추가 정보 입력

##### 위 내용은 책에 없으며 혼자서 열시미 이것저것 생각해보며 만들었다.

```java
package web.purplebook.web;

import lombok.RequiredArgsConstructor;
import org.apache.catalina.authenticator.SpnegoAuthenticator;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.context.SecurityContext;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import web.purplebook.config.auth.dto.OAuth2SignUpDto;
import web.purplebook.config.auth.dto.SessionUser;
import web.purplebook.domain.user.User;
import web.purplebook.repository.UserRepository;

import javax.servlet.http.HttpSession;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

@Controller
@RequiredArgsConstructor
public class CustomOAuth2SignUpController {

    private final HttpSession httpSession;
    private final UserRepository userRepository;

    @GetMapping("/addform")
    public String addForm(Model model){
        SessionUser user = (SessionUser)httpSession.getAttribute("user");
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
    public Long signUp(@RequestBody OAuth2SignUpDto oAuth2SignUpDto){
        SessionUser user = (SessionUser)httpSession.getAttribute("user");
        Long id = user.getId();

        User user1 = userRepository.findById(id).orElse(null);
        user1.googleSignUp(oAuth2SignUpDto.getUsername());//설명 참고
        

        updateRole(user1);//설명 참고
        
        httpSession.setAttribute("user", new SessionUser(user1));
        return 0L;
    }

    private void updateRole(User user ) {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        List<GrantedAuthority> updatedAuthorities = new ArrayList<>();
        updatedAuthorities.add(new SimpleGrantedAuthority(user.getRoleKey()));
        Authentication newAuth = new UsernamePasswordAuthenticationToken(auth.getPrincipal(), auth.getCredentials(), updatedAuthorities);
        SecurityContextHolder.getContext().setAuthentication(newAuth);
    }
}

```

#####  public String addForm 을 보면, SecurityConfig에서 

```
.oauth2Login()
.defaultSuccessUrl("/addform")//추가 정보 입력
```

##### 이러한 코드가 있었을 것이다. 이 때문에 이미 정보 제공에 동의를 한 사람이라면 /addform의 주소로 접속하게 되어있다.

##### 이때 접속하였을 때 그 사람이 이미 회원가입을 한 사람일 수도 있고, 정보 제공에 동의만 한 사람일 수도 있다. 이를 user.getUsername() != null 를 통해서 가려낸다.

##### 회원가입을 완료하려면 username을 추가로 입력해야 한다.  따라서 이미 회원가입을 한 사람이라면 username이 존재한다!

<br/>

googleSignUp

<br/>

##### updateRole

- CustomOAuth2UserService 에서 loadUser를 통해서 권한을 생성할 때, 회원가입을 하지 않은 상태라면 Guest로 만들어진다.(이미 가입을 한 사람이 로그인 버튼을 누른 경우에는 User로 만들어 짐)
- 만약 회원가입을 성공적으로 진행하였을 경우에는 권한을 GUEST에서 USER로 바꿔주어야 하는데, 위 메소드가 바로 그 역할을 한다.

<br/>

<br/>

#### add-form

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="fragments/header :: header">
    <title>소셜 로그인 추가 정보 입력창</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
<h1>회원가입 추가 정보 입력</h1>

<div class="col-md-12">
    <div class="col-md-4">
        <form>
            <div class="form-group">
                <label for="username">아이디</label>
                <input type="text" class="form-control" id="username" placeholder="아이디를 입력하세요">
            </div>

        <a href="/" role="button" class="btn btn-secondary">취소</a>

        <button type="button" class="btn btn-primary" id="btn-signUp">가입</button>


    </div>
</div>


<div th:replace="fragments/footer :: footer" />
</body>
</html>
```

<br/>

##### index.js 추가

```javascript
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

        $('#btn-signUp').on('click', function (){
            _this.signup();
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
    },




    signup : function () {

        var data = {
            username: $('#username').val(),
        };

        $.ajax({
            type: 'POST',
            url: '/signUp',
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function (){
            alert('회원가입이 완료되었습니다.');
            window.location.href = '/';

        }).fail(function (error){
            alert(JSON.stringify(error));
        });
    }


};

main.init();
```

<br/>

<br/>

### 이제 실행해보자

![image-20211123005517762](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123005517762.png)

##### 로그인 버튼을 누르면 동의를 하지 않았다면, 아까 저 위에서 보았던 동의하는 화면이 나올것이고, 이미 동의를 하였다면 다음과 같은 페이지로 이동된다.

![image-20211123005533841](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123005533841.png)

<br/>

##### 가입을 완료 시

![image-20211123005616208](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123005616208.png)

다음과 같이 나온다. 로그아웃 이후에 다시 메인 페이지로 접속해보자

그럼 다시 로그인 창이 뜰것인데, 여기서 로그인 버튼을 누르면

![image-20211123005659454](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123005659454.png)

##### 추가정보 입력 폼 없이 곧바로 로그인이 되는것을 알 수 있다.

![image-20211123005722486](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123005722486.png)

<br/>

<br/>

<br/>

이렇게 해서 대회때는 하지 못했던 시큐리티 + OAtuh2를 사용한 구글 로그인을 제대로 구현해 보았다. 책에서 나와있는 부분에서 혼자서 조금 발전도 시켜보았고, 굉장히 뿌듯했다.

정보 제공 동의 후 추가정보를 입력하여 로그인을 진행하는 방법에 대해서는 자료가 정말 없었다. 그래서 대회 준비 당시 너무 힘들었구, 결국 완료하지 못했다. 하지만 진짜 책을 보고 조금씩 공부하면서 어느정도 이해하고 사용하니 훨씬 수월했다. 

나와같이 회원가입을 구현하고 싶은 사람들에게 조금 도움이 됐으면 좋겠다.

<br/>

### 📔 Reference

##### 스프링 부트와 AWS로 혼자 구현하는 웹 서비스 124~161P

[SpringSecurity사용중 계정정보가 update되었을때 권한을 다시로드하는 방법.](https://taesan94.tistory.com/135)