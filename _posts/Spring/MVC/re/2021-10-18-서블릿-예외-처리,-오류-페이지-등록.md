---
title:  "서블릿 예외 처리, 오류 페이지 등록"
excerpt: "스프링 MVC 공부하기[24]"
date:   2021-10-18 00:01:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-18T00:01:00






---

<br/>

## 💡 서블릿 예외 처리

스프링이 아닌 순수 서블릿 컨테이너는 예외를 어떻게 처리하는지 알아보겠다.

서블릿은 아래 두가지 방식으로 예외를 처리한다.

#### 🚫 서블릿의 예외 처리

- ##### Exception(예외) : NullPointException 등 우리가 흔하게 보는 그런 예외, 해당 예외가 WAS까지 전달되었을 경우.

- ##### response.sendError (HTTP 상태 코드, 오류 메시지)

<br/>

<br/>

### ☀️ Exception 

**웹 애플리케이션은 사용자 요청별로 별도의 쓰레드가 할당되고, 서블릿 컨테이너 안에서 실행된다.**

##### 애플리케이션에서 예외를 잡지 못하고,  서블릿 밖으로까지 예외가 전달되면 어떻게 동작할까?

> **WAS(여기까지 전파) <- 필터 <- 서블릿 <- 인터셉터 <- 컨트롤러 (예외발생)**

**결국 WAS까지 예외가 전달된다. WAS는 예외가 올라오면 어떻게 처리해야 할까?**

<br/>

🔎**먼저 스프링 부트가 제공하는 기본 예외 페이지가 있는데 이건 꺼두자.**

##### application.properties

`server.error.whitelable.enabled=false`

<br/>

<script src="https://gist.github.com/ShinDongHun1/737331a93d4322518599ae8ee1db16f5.js"></script>

다음 코드를 실행시켜보자.

![image-20211017222209796](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211017222209796.png)

##### WAS는 Exception의 경우 서버 내부에서 처리할 수 없는 오류가 발생한 것으로 생각해서 HTTP 상태 코드 500을 반환한다.

<br/>

<br/>

### ☀️ response.sendError(HTTP 상태 코드, 오류 메세지)

오류가 발생했을 때 HttpServletResponse가 제공하는 sendError 메서드를 사용해도 된다. 이것을 호출한다고 당장 예외가 발생하는 것은 아니지만, 서블릿 컨테이너에게 오류가 발생했다는 점을 전달할 수 있다.

- response.sendError(HTTP 상태 코드)
- response.sendError(HTTP 상태 코드, 오류 메시지)

<br/>

#### 🔎ServletExController 추가

<script src="https://gist.github.com/ShinDongHun1/e59d0e59200bb2656211701a21319869.js"></script>

<br/>

##### 🔎 sendError 흐름 

> ##### WAS (sendError  호출 기록 확인) <- 필터 <- 서블릿 <- 인터셉터 <- 컨트롤러(response.sendError())

##### response.sendError를 호출하면 response 내부에 오류가 발생되었다는 상태를 저장해둔다.

##### 그리고 서블릿 컨테이너는 고객에게 응답 전에 response에 sendError()가 호출되었는지 확인한다.

##### 그리고 호출되었다면 설정한 오류 코드에 맞추어 기본 오류 페이지를 보여준다.

<br/>

<br/>

## 💡 서블릿 예외 처리 - 오류 화면 제공

##### 서블릿은 Exception이 발생해서 서블릿 밖으로 전달되거나 또는 response.sendError()가 호출되었을 때 각각의 상황에 맞춘 오류 처리 기능을 제공한다.

##### 기본적으로 제공하는 오류 페이지는 너무 이쁘지 않기 때문에 새로운 오류 화면을 제공하는 법을 공부해보자

<br/>

### **☀️**서블릿 오류 페이지 등록

#### <span style="color:orange">WebServerFactoryCustomizer\<ConfigurableWebServerFactory> 구현</span>

<script src="https://gist.github.com/ShinDongHun1/61b2fdd385fbfc2c1a70e91ed21b97c3.js"></script>

```java
new ErrorPage(HttpStatus.NOT_FOUND, "/error-page/ 404") :
```

- #####  만약 HttpStatus가 NOT_FOUND인 에러가 발생하면,  /error-page/ 404경로로 에러 페이지를 다시 요청한다.

- #####  (다시 요청한다는것의 뜻은 'WAS 에서부터 필터 -> 서블릿 -> 인터셉터 -> 컨트롤러' 의 순서로 요청을 보낸다는 의미, 따라서 해당 오류 요청이 필터와 인터셉터에 걸리지 않게 하기 위해서는 필터는 setDispatcherTypes을 사용하여 제외해주고, 인터셉터는 excludePathPatterns로 해당 URI를 제거해 주면 된다.)

<br/>

#### 에러 페이지 컨트롤러

```java
@RequestMapping("/error-page/404")//WebServerCustomizer에서 적용한 에러페이지의 경로
public String errorPage404(HttpServletRequest request, HttpServletResponse response){
	log.info("errorPage 404")
	return "error-page/404";
}
```

##### 위와같이 error-page/404의 경로로 컨트롤러를 매핑시켜서 사용할 수 있고, 또한 ResponseBody를 사용하여 REST API 방식으로도 결과를 반환할 수 있다.

<br/>

<br/>

## 💡 서블릿 예외 처리 - 오류 페이지 작동 원리

##### 서블릿은 Exception이 발생해서 서블릿 밖으로 전달되거나 또는 response.sendError()가 호출되었을 때 설정된 오류 페이지를 찾는다.

#### 예외 발생 흐름

> ##### WAS(여기까지 전파) <- 필터 <- 서블릿 <- 인터셉터 <- 컨트롤러(예외발생)

#### sendError 흐름

> ##### WAS(sendError 호출 기록 확인 )  <- 필터 <- 서블릿 <- 인터셉터 <- 컨트롤러(response.sendError)

<br/>

##### WAS는 해당 예외를 처리하는 오류 페이지 정보를 확인한다.

> ##### new ErrorPage(RuntimeException.class, "/error-page/500")

<br/>

##### 예를 들어서 RuntimeException예외가 WAS 까지 전달되면, WAS는 오류 페이지 정보를 확인한다.

##### 확인해보니  RuntimeException의 오류 페이지로 "/error-page/500"이 지정되어 있다.

##### <span style="color:orange">WAS는 오류 페이지를 출력하기 위해 "/error-page/500"을 다시 요청</span>한다

<br/>

#### 오류 페이지 요청 흐름 

> ##### WAS "/error-page/500" 다시 요청 -> 필터 -> 서블릿 -> 인터셉터 -> 컨트롤러("/error-page/500") -> View 

<br/>

##### 중요한 점은 웹 브라우저(클라이언트)는 서버 내부에서 이런 일이 일어나는지 모른다는 것이다. 오직 서버 내부에서 오류 페이지를 찾기 위해 추가적인 호출을 한다.

<br/>

#### 정리

1. ##### 예외가 발생해서 WAS까지 전파한다

2. ##### WAS는 오류 페이지 경로를 찾아서 내부에서 오류 페이지를 호출한다. <span style="color:orange">이때 오류 페이지 경로로 필터, 서블릿, 인터셉터, 컨트롤러가 모두 다시 호출</span>된다.

<br/>

<br/>

### 🔎 오류 정보 추가

##### WAS는 오류 페이지를 단순히 다시 요청만 하는 것이 아니라, 오류 정보를 request의 attribute에 추가해서 넘겨준다. 

##### 필요하면 오류 페이지에서 이렇게 전달된 오류 정보를 사용할 수 있다.

<script src="https://gist.github.com/ShinDongHun1/8f86e731bfd30ebf1d5cb3340949cba6.js"></script>

<br/>

### 참고

#### ☀️ 서블릿 예외 처리 - 오류 페이지 등록

##### WebServerFactoryCustomizer\<ConfigurableWebServerFactory> 구현

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)