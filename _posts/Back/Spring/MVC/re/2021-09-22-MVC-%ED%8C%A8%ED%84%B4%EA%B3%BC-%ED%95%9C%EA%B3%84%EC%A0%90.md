---
title:  "MVC 패턴과 한계점"
excerpt: "스프링 MVC 공부하기[5]"
date:   2021-09-22 20:40:00 
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-12T14:40:00


---

<br/>

## 💡 MVC 패턴 - 개요

#### 서블릿과 jsp의 문제점?

#### ☀️너무 많은 역할

##### 서블릿이나 jsp로만 개발을 하게 되면, 비지니스 로직과 화면을 처리하는 부분을 하나의 서블릿이나 jsp에서 하게 되는데, 역할이 너무 많다.

#### ☀️변경의 라이프 사이클

##### UI를 일부 수정한다고 자바 코드에 영향을 주는것도 아니고, 반대로 자바 코드를 바꾼다고 UI에 영향을 주는것도 아니다. 이렇게 변경의 라이프 사이클이 다른 부분을 하나의 코드로 관리하는 것은 유지보수의 관점에서 좋지 않다.

#### ☀️기능 특화

##### JSP같은 뷰 템플릿은 화면을 렌더링하는데 최적화되어 있고 서블릿은 자바 코드를 실행하는데 최적화

<br/>

<br/>

### 💡 Model View Controller

##### 지금까지 JSP나 서블릿을 통해 하나로 처리하던 것을 <span style="color:orange">컨트롤러</span>(Controller)와 <span style="color:orange">뷰</span>(View)라는 영역으로 서로 역할을 나눈 것.

<br/>

#### ☀️Controller

HTTP 요청을 받아서 파라미터를 검증하고, 비즈니스 로직을 실행. 그리고 뷰에 전달할 결과 데이터를 조회해서 모델(Model)에 담아준다.

#### ☀️모델 (Model)

뷰에 출력할 데이터를 담아둔다. 뷰가 필요한 데이터를 모두 모델에 담아서 전달해준 덕분에, 뷰는 비즈니스 로직이나 데이터 접글을 몰라도 되고, 화면 렌더링에 집중할 수 있다.

#### ☀️뷰

모델에 담겨있는 데이터를 사용해서 화면을 렌더링. 여기서는 HTML을 생성

![image-20210922190503361](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20210922190503361.png)

<br/>

<br/>

## 💡 MVC 패턴의 한계

##### 뷰는 화면을 그리는 역할에 충실해진 덕분에, 코드가 깔끔해졌다.

##### 그런데 컨트롤러는 [스프링 MVC 실습 3](https://shindonghun1.github.io/mvc/%EC%8A%A4%ED%94%84%EB%A7%81-MVC-%EC%8B%A4%EC%8A%B5-3/)에서 보았듯이 중복되는 코드가 너무 많고, 불필요한 코드들도 많다.

<br/>

#### ☀️포워드 중복

- ##### View로 이동하는 코드가 항상 중복 호출되어야 한다. 물론 이 부분을 메서드로 공통화해도 되지만, 해당메서드도 항상 직접 호출해야 한다.

> **RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);**
> **dispatcher.forward(request, response);**

#### ☀️ViewPath 중복

> **String viewPath = "/WEB-INF/views/new-form.jsp";**

**/WEB-INF/views/ 와<br/>.jsp가 항상 붙으며**

**만약 jsp가 아닌 thymeleaf같은 다른 뷰로 변경하려면 전체 코드를 다 수정해야 한다**

#### ☀️사용하지 않는 코드

다음 코드를 사용할 때도 있고, 사용하지 않을 때도 있다. 

> **HttpServletRequest request, HttpServletResponse response**

#### ☀️공통 처리가 어렵다.

**기능이 복잡해질수록 컨트롤러에서 공통으로 처리해야 하는 부분이 점점 더 많이 증가할 것이다.** 

**단순히공통 기능을 메서드로 뽑으면 될 것 같지만, 결과적으로 해당 메서드를 항상 호출해야 하고, 실수로 호출하지 않으면 문제가 될 것이다. 그리고 호출하는 것 자체도 중복이다.**

<br/>

<br/>

## 💡 해결방안 - 프론트 컨트롤러

##### <span style="color:orange">컨트롤러 호출 전</span>에 먼저 <span style="color:orange">공통 기능을 처리</span>함으로써 문제를 해결

##### 소위 수문장 역할을 하는 기능이 필요

**<span style="color:orange">프론트 컨트롤러(Front Controller) 패턴</span>을 도입하면 이런 문제를 깔끔하게 해결할 수 있다.**

##### 이것이 스프링 MVC의 핵심

![image-20211013232226217](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211013232226217.png)

<br/>

<br/>

## 🧾 정리

### ☀️ MVC 패턴

- ##### MVC 패턴의 기본은 항상  <span style="color:orange">컨트롤러</span>를 통해서  <span style="color:orange">뷰로 이동</span>하는것이다



### ☀️  MVC 패턴의 한계

- ##### 그러나 MVC패턴은 여러 문제점들이 있고 특히 공통 처리가 어렵다

- ##### 이를 <span style="color:orange">프론트 컨트롤러(Front Controller) 패턴</span>을 사용하여 해결한다.

<br/>

<br/>

### 📔 Reference

##### [스프링 MVC 1편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-1/dashboard)
