---
title:  "Validation - 검증"
excerpt: "스프링 MVC 공부하기[17]"
date:   2021-10-16 16:43:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-16T16:43:00



---

<br/>

## 💡 검증

#### 클라이언트 검증과 서버 검증

- 클라이언트 검증은 조작할 수 있으므로 보안에 취약하다.
- 서버만으로 검증하면, 즉각적인 고객 사용성이 부족해진다.
- 둘을 적절히 섞어서 사용하되, 최종적으로 서버 검증은 필수
- API 방식을 사용하면 API 스펙을 잘 정의해서 검증 오류를 API 응답 결과에 잘 남겨주어야 함

#### 참고

[유튜브 - [10분 테코톡] 👩🏻‍💻👨🏻‍💻해리&션의 MVC 패턴](https://www.youtube.com/watch?v=uoVNJkyXX0I&t=339s)

<br/>

<br/>

## 💡 MessageCodesResolver

검증 오류 코드로 메시지 코드들을 생성한다.

##### MessageCodesResolver는 인터페이스고 DefaultMessageCodesResolver는 기본 구현체이다

#### 객체 오류

객체 오류의 경우 다음 순서로 2가지의 오류 코드를 생성한다.

- ##### 1.: <span style="color:orange">code </span>+ "." + <span style="color:blue">object name</span>

- ##### 2.:<span style="color:orange"> code</span>

- ##### 예) 오류 코드: <span style="color:orange">required</span>, <span style="color:blue">object name: item</span>

- ##### 1.: <span style="color:orange">required</span>.<span style="color:blue">item</span>

- ##### 2.: <span style="color:orange">required</span>

#### 필드 오류

필드 오류의 경우 다음 순서로 4가지 메시지 코드 생성

- ##### 1.: <span style="color:orange">code</span> + "." + <span style="color:blue">object name</span> + "." + <span style="color:pink">field</span>

- ##### 2.: <span style="color:orange">code</span> + "." + <span style="color:pink">field</span>

- ##### 3.: <span style="color:orange">code</span> + "." + <span style="color:green">field type</span>

- ##### 4.: <span style="color:orange">code</span>

- ##### 예) 오류 코드: <span style="color:orange">typeMismatch</span>, <span style="color:blue">object name "user"</span>, <span style="color:pink">field "age"</span>,  <span style="color:green">field type: int</span>

  - ##### "<span style="color:orange">typeMismatch</span>.<span style="color:blue">user</span>.<span style="color:pink">age</span>"

  - ##### "<span style="color:orange">typeMismatch</span>.<span style="color:pink">age</span>"

  - ##### "<span style="color:orange">typeMismatch</span>. <span style="color:green">int</span>"

  - ##### "<span style="color:orange">typeMismatch</span>"

<br/>

<br/>

## 💡 @Valid , @Validated

Valid는 자바 표준으로 javax에 속해있으며, 사용하려면 build.gradle 에 의존관계를 추가해주어야 한다.

```properties
implementation 'org.springframework.boot:spring-boot-starter-validation'
```

<br/>

@Validated는 스프링 전용 검증 애노테이션이고, @Valid는 자바 표준 검증 애노테이션이다. 

작동은 동일하게 하지만 @Validated는 내부에 **groups**라는 기능을 포함하고 있다.

<br/>

#### 바인딩에 성공한 필드만 Valiation 적용

타입 변환에 성공하여야 검증이 의미있기에, 애당초 들어오는 타입 값이 잘못되었으면 TypeMismatch로 FieldError를 추가한다.

<br/>

<br/>

## 💡 @Validation

특정 필드에 대한 검증 로직은 대부분 빈 값인지 아닌지, 특정 키기를 넘는지 아닌지와 같이 매우 일반적인 로직이다.

##### 이런 검증 로직을 표준화 한 것이 바로 Bean Validation이다

<br/>

Bean Validation을 구현한 기술중, 일반적으로 사용하는 구현체는 하이버네이트 Validatior이다. 

하이버네이트 Validatior 관련 링크

- [공식 사이트](http://hibernate.org/validator/)
- [공식 메뉴얼](https://docs.jboss.org/hibernate/validator/6.2/reference/en-US/html_single/)
- [검증 애노테이션 모음](https://docs.jboss.org/hibernate/validator/6.2/reference/en-US/html_single/#validator-defineconstraints-spec)

<br/>

##### Bean Validation을 사용하려면 다음 의존관계를 추가해야 한다.

##### build.gradle

```properties
implementation 'org.springframework.boot:spring-boot-starter-validation'
```

<br/>

#### 스프링부트는 자동으로 글로벌 Validator를 등록한다.

참고로 다음과 같이 직접 글로벌 Validator를 직접 등록하면 스프링 부트는 Bean Validator를 글로벌
Validator 로 등록하지 않는다. 따라서 애노테이션 기반의 빈 검증기가 동작하지 않는다.

<script src="https://gist.github.com/ShinDongHun1/a566a9a805d0c5d2a1325f459c8f06ca.js"></script>

<br/>

### 검증 순서

1. ##### @ModelAttribute 각각의 필드에 타입 변환 시도

   - 성공하면 다음으로

   - ##### 실패하면 typeMismatch 로 FieldError 추가

2. ##### Validator 적용

<br/>

## 💡 Bean Validation - 에러 코드

Bean Validation이 기본으로 제공하는 오류 메시지를 좀 더 자세히 변경하고 싶으면 어떻게 하면 될까?

##### @NotBlank

`NotBlank.item.itemName`
`NotBlank.itemName`
`NotBlank.java.lang.String`
`NotBlank`

위와같이 생성되며,

<br/>

##### @Range

`Range.item.price`
`Range.price`
`Range.java.lang.Integer`
`Range`

위와같이 생성된다.

우리는 그저 해당 오류들에 대한 메시지만 적용해 놓으면 된다.

<br/>

#### 스프링 부트 메시지 설정 추가

##### application.properties

```properties
spring.messages.basename=messages,errors
```

<br/>

##### errors.properties

> ```properties
>NotBlank={0}:값을 반드시 입력하셔야 합니다.
> Size={0}:글자 수는 {2}글자 이상, {1}글자 이하이어야 합니다.
> ```

<br/>

#### Bean Validation 메시지 찾는 순서

1. 생성된 메시지 코드 순서대로 meesageSource에서 메시지 찾기
2. 애노테이션의 message 속성 사용
3. 라이브러리가 제공하는 기본 값 사용

<br/>

<br/>

## 💡 Bean Validation - 오브젝트 오류

#### @ScriptAssert() 사용

- ##### 그러나 실제 사용해보면 제약이 많고 복잡하다

##### 따라서 오브젝트 오류(글로벌 오류)의 경우 @ScriptAssert()를 억지로 사용하는 것 보다는 다음과 같이 오브젝트 오류 관련 부분만 직접 <span style="color:orange">자바 코드로 작성</span>하는 것을 권장한다.

<br/>

<script src="https://gist.github.com/ShinDongHun1/56f545138edcf419bba76fe2f799da19.js"></script>

<br/>

<br/>

## 💡 Bean Validation - 한계

예시로 데이터를 등록할 때와 수정할 때의 요구사항이 다른 경우를 생각해보자.

- 등록시 기존 요구사항
  - 타입 검증
    - 가격, 수량에 문자가 들어가면 검증 오류 처리
  - 필드 검증
    - 상품명: 필수, 공백X
    - 가격: 1000원 이상, 1백만원 이하
    - 수량: 최대 9999
  - 특정 필드의 범위를 넘어서는 검증
    - 가격 * 수량의 합은 10,000원 이상
- 수정시 요구사항
  - 등록시에는 quantity 수량을 최대 9999까지 등록할 수 있지만 수정시에는 수량을 무제한으로 변경할 수있다.
  - 등록시에는 id 에 값이 없어도 되지만, 수정시에는 id 값이 필수이다.

<br/>

##### 위와 같은 경우의 상황을 해결할 수 없다

<br/>

### ✏️  해결방법

##### 1. Bean Validation의 groups 기능 사용

##### 2. Item을 직접 사용하지 않고, ItemSaveForm, ItemUpdateForm같은 폼 전송을 위한 별도의 모델 객체를 만들어서 사용

<br/>

### 1. groups 사용

##### 저장용 groups 생성

<script src="https://gist.github.com/ShinDongHun1/5535b89c56e1f1dd61f6219018b56643.js"></script>

<br/>

##### 수정용 groups 생성

<script src="https://gist.github.com/ShinDongHun1/d463eed84594a634d54a1a060da26fa8.js"></script>

<br/>

##### Item - groups 적용 

<script src="https://gist.github.com/ShinDongHun1/574cca04e700dda189686f951b4fedf4.js"></script>

<br/>

##### ValidationItemControllerV3 - 저장 로직에 SaveCheck Groups 적용

<script src="https://gist.github.com/ShinDongHun1/1f4fcca5fabd2e2e1de2669a4427df8e.js"></script>

<br/>

##### 사실 groups 기능은 실제 잘 사용되지는 않는데, 그 이유는 실무에서는 주로 다음에 등장하는 등록용 폼 객체와 수정용 폼 객체를 분리해서 사용하기 때문이다.

<br/>

<br/>

## 2. 모델 객체를 만들어서 사용

##### @Valid , @Validated 는 HttpMessageConverter ( @RequestBody )에도 적용할 수 있다.

<br/>

#### API의 경우 3가지 경우를 나누어 생각할 수 있다

- 성공 요청 : 성공
- 실패 요청 : JSON 객체로 생성하는 것 자체가 실패함
- 검증 오류 요청 : JSON을 객체로 생성하는 것은 성공했고 검증에서 실패함

<br/>

#### 참고) 실패 요청 - JSON 객체로 생성하는 것 자체가 실패함

Interger 에 "q" 같이 문자열을 넣는 상황에는 해당 오류가 발생한다.

##### <span style="color:red">Resolved [org.springframework.http.converter.HttpMessageNotReadableException: JSON parse error: Cannot deserialize value of type `int` from String "dd": not a valid `int` value;</span>

##### 해당 오류의 처리는 이후 예외 처리에서 다루도록 하겠다.

<br/>

<br/>

#### 검증 오류 결과

```json
{

    "codes": [

      "NotBlank.signUpMemberDto.password",

      "NotBlank.password",

      "NotBlank.java.lang.String",

      "NotBlank"

    ],

    "arguments": [

      {

        "codes": [

          "signUpMemberDto.password",

          "password"

        ],

        "arguments": null,

        "defaultMessage": "password",

        "code": "password"

      }

    ],

    "defaultMessage": "must not be blank",

    "objectName": "signUpMemberDto",

    "field": "password",

    "rejectedValue": "",

    "bindingFailure": false,

    "code": "NotBlank"

  }
```

##### 실제 개발할 때는 이 객체들을 그대로 사용하지 말고, 필요한 데이터만 뽑아서, 별도의 API스펙을 정의하고 그에 맞는 객체로 만들어서 반환해야 한다

<br/>

<br/>

### 📔 Reference

#####  [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

##### [유튜브 - [10분 테코톡] 👩🏻‍💻👨🏻‍💻해리&션의 MVC 패턴](https://www.youtube.com/watch?v=uoVNJkyXX0I&t=339s)