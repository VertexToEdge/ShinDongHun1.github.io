---
title:  "네이버 로그인 구현하기"
excerpt: "스프링 부트와 AWS로 혼자 구현하는 웹 서비스 4-3"
date:   2021-11-23 18:16:00 
header:
  teaser: /assets/images/spring.png

categories: purpleBook
tags:
  - Java
  - Spring
last_modified_at: 2021-11-23T18:16:00

---

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124204433310.png" alt="image-20211124204433310" style="zoom:30%;" />

<br/>

## 네이버 로그인 구현하기

[https://developers.naver.com/apps/#/wizard/register](https://developers.naver.com/apps/#/wizard/register)이곳으로 이동하자.

약관 동의를 해 주면 다음과 같은 화면이 뜰 텐데, 회사 이름은 체크만 하고 넘어가주자

![image-20211123183353100](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123183353100.png)

<br/>

### 애플리케이션 등록

![image-20211123183614353](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123183614353.png)

이름은 자신의 애플리케이션 이름을 등록해주자.

<br/>

![image-20211123183643231](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123183643231.png)

사용 API는 따로 설명이 필요 없을 거 같다.

<br/>

![image-20211123183724706](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123183724706.png)

환경을 PC웹, 서비스 URL은 localhost:8080,

Callback URL은 구글에서의 리디렉션 URL과 같은 역할을 한다. 여기서는 

> http://localhost:8080/login/oauth2/code/naver 

로 등록한다.

<br/>

![image-20211123183859857](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123183859857.png)

등록을 완료하면 다음과 같이 ClientID와 Client Secret이 생성되는데, 이를 application.oauth.properties에 등록한다.

##### 스프링 시큐리티는 네이버 API를 지원해주지 않기 때문에, 전부 수동으로 등록해야 한다.

등록할 때 참고하자

[네이버 로그인 API 가이드](https://developers.naver.com/docs/login/devguide/devguide.md#%EB%84%A4%EC%9D%B4%EB%B2%84%20%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B0%9C%EB%B0%9C%EA%B0%80%EC%9D%B4%EB%93%9C)

<br/>

#### application.oauth.properties

```properties
spring.security.oauth2.client.registration.naver.client-id=클라Id
spring.security.oauth2.client.registration.naver.client-secret=클라 Secret
spring.security.oauth2.client.registration.naver.redirect-uri=http://localhost:8080/login/oauth2/code/naver
spring.security.oauth2.client.registration.naver.authorization-grant-type=authorization_code
spring.security.oauth2.client.registration.naver.scope=name,email,profile_image
spring.security.oauth2.client.registration.naver.client-name=Naver

spring.security.oauth2.client.provider.naver.authorization-uri=https://nid.naver.com/oauth2.0/authorize
spring.security.oauth2.client.provider.naver.token-uri=https://nid.naver.com/oauth2.0/token
spring.security.oauth2.client.provider.naver.user-info-uri=https://openapi.naver.com/v1/nid/me
spring.security.oauth2.client.provider.naver.user-name-attribute=response
```

spring.security.oauth2.client.provider.naver.user-name-attribute=response

- 기준이 되는 user_name의 이름을 네이버에서는 response로 해야한다.
- 이유는 네이버 오픈 API의 로그인 회원 결과 때문인다.

![image-20211123185030154](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123185030154.png)

스프링 시큐리티에서는 하위 필드를 명시할 수 없다. 최상위 필드들만 user_name으로 지정 가능하다. 하지만 네이버의 응답값 최상위 필드는 resultcode, message, response이다. 이러한 이유로 response를 user_name으로 지정한 후, response의 id를 user_name으로 지정하겠다

<br/>

<br/>

#### OAuthAttributes에 추가

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

        return ofGoogle(userNameAttributeName, attributes);
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

##### index.html에 추가

```html
<a href="/oauth2/authorization/naver"class="btn btn-secondary active" role="button" th:unless="${not #strings.isEmpty(username)}">Naver Login</a>
```

전체 코드

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
        
        <!-- 네이버 추가 -->
        <a href="/oauth2/authorization/naver"class="btn btn-secondary active" role="button" th:unless="${not #strings.isEmpty(username)}">Naver Login</a>

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

##### /oauth2/authorization/naver

- 네이버 로그인 URL은 application-oauth.properties에 등록한 redirect-uri 값에 맞춰 자동으로 등록된다.

<br/>

<br/>

### 실행해보자

![image-20211123190522729](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123190522729.png)



![image-20211123192914150](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123192914150.png)

![image-20211123192922517](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123192922517.png)

![image-20211123192932722](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211123192932722.png)

다 잘 된다!!!!!

<br/>

#### 근데 문제점이 하나 있다.

필수 제공항목을 체크 안 하고 동의하는 경우에는, 따로 필요한 값들을 입력받아야 한다..!!

그건 추가 정보에서 알아서 할 수 있으니까 일단 넘어가고 다음은 카카오 로그인을 진행하겠다.

<br/>

<br/>

### 📔 Reference

##### 스프링 부트와 AWS로 혼자 구현하는 웹 서비스 124~161P
