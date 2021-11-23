---
title:  "포맷터 - Formatter"
excerpt: "스프링 MVC 공부하기[34]"
date:   2021-10-18 22:10:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-18T22:10:00

---

<br/>

## 🌌 포맷터 - Formatter

##### Converter 는 입력과 출력 타입에 제한이 없는, 범용 타입 변환 기능을 제공한다.

이번에는 일반적인 웹 애플리케이션 환경을 생각해보자. 불린 타입을 숫자로 바꾸는 것 같은 범용 기능
보다는 개발자 입장에서는 문자를 다른 타입으로 변환하거나, 다른 타입을 문자로 변환하는 상황이 대부분이다.

##### 🔎  웹 애플리케이션에서 객체를 문자로, 문자를 객체로 변환하는 예

화면에 숫자를 출력해야 하는데, Integer String 출력 시점에 숫자 1000 문자 "1,000" 이렇게 1000 단위에 쉼표를 넣어서 출력하거나, 또는 "1,000" 라는 문자를 1000 이라는 숫자로 변경해야 한다.

##### 날짜 객체를 문자인 "2021-01-01 10:50:11" 와 같이 출력하거나 또는 그 반대의 상황

##### 🔎  Locale

여기에 추가로 날짜 숫자의 표현 방법은 Locale 현지화 정보가 사용될 수 있다.

#### 이렇게 객체를 특정한 포멧에 맞추어 문자로 출력하거나 또는 그 반대의 역할을 하는 것에 특화된 기능이 바로 포맷터( Formatter )이다. 포맷터는 컨버터의 특별한 버전으로 이해하면 된다.

<br/>

#### 🔎 Converter vs Formatter

- Converter는 범용 (객체 -> 객체)
- Formatter는 문자에 특화(객체 -> 문자, 문자 -> 객체) + 현지화(Locale)

<br/>

#### 🔎포맷터 - Formatter 만들기

##### 포맷터( Formatter )는 객체를 문자로 변경하고, 문자를 객체로 변경하는 두 가지 기능을 모두 수행한다.

- ##### String print(T object, Locale locale) : 객체를 문자로 변경한다.

- ##### T parse(String text, Locale locale) : 문자를 객체로 변경한다.

<br/>

#### 🔎 Formatter 인터페이스

```java
gpublic interface Printer<T> {
String print(T object, Locale locale);
}
public interface Parser<T> {
T parse(String text, Locale locale) throws ParseException;
}
public interface Formatter<T> extends Printer<T>, Parser<T> {
}
```

<br/>

<br/>

#### 🌌포맷터를 지원하는 컨버전 서비스

##### 컨버전 서비스에는 컨버터만 등록할 수 있고, 포맷터를 등록할 수 는 없다. 그런데 생각해보면 포맷터는 객체 문자, 문자 객체로 변환하는 특별한 컨버터일 뿐이다.

##### 포맷터를 지원하는 컨버전 서비스를 사용하면 컨버전 서비스에 포맷터를 추가할 수 있다. 내부에서 어댑터 패턴을 사용해서 Formatter 가 Converter 처럼 동작하도록 지원한다.

##### FormattingConversionService 는 포맷터를 지원하는 컨버전 서비스이다.

##### 🔎 DefaultFormattingConversionService 는 FormattingConversionService 에 기본적인 통화, 숫자 관련 몇가지 기본 포맷터를 추가해서 제공한다.

<br/>

<br/>

#### 🔎포맷터 만들기

<script src="https://gist.github.com/ShinDongHun1/2e9c5e20ba63b5c82391d046d5c41bcb.js"></script>

<br/>

<br/>

#### 🔎포맷터 적용하기

<script src="https://gist.github.com/ShinDongHun1/a1450957c44933c3c702e806f49ff1ad.js"></script>

<br/>

<br/>

## 🌌 스프링이 제공하는 기본 포맷터

##### 포맷터는 기본 형식이 지정되어 있기 때문에, 객체의 각 필드마다 다른 형식으로 포맷을 지정하기는 어렵다.

##### 스프링은 이런 문제를 해결하기 위해 애노테이션 기반으로 원하는 형식을 지정해서 사용할 수 있는 매 우 유용한 포맷터 두 가지를 기본으로 제공한다.

- ##### @NumberFormat : 숫자 관련 형식 지정 포맷터 사용, NumberFormatAnnotationFormatterFactory

- ##### @DateTimeFormat : 날짜 관련 형식 지정 포맷터 사용,
Jsr310DateTimeFormatAnnotationFormatterFactory

<br/>

##### 🔎 주의!

##### 메시지 컨버터( HttpMessageConverter )에는 컨버전 서비스가 적용되지 않는다.

##### 특히 객체를 JSON으로 변환할 때 메시지 컨버터를 사용하면서 이 부분을 많이 오해하는데,

##### HttpMessageConverter 의 역할은 HTTP 메시지 바디의 내용을 객체로 변환하거나 객체를 HTTP 메시지 바디에 입력하는 것이다. 

##### 예를 들어서 JSON을 객체로 변환하는 메시지 컨버터는 내부에서 Jackson 같은 라이브러리를 사용한다. 

##### 객체를 JSON으로 변환한다면 그 결과는 이 라이브러리에 달린 것이다. 

##### 따라서 JSON 결과로 만들어지는 숫자나 날짜 포맷을 변경하고 싶으면 해당 라이브러리가 제공하는 설정을 통해서 포맷을 지정해야 한다. 

##### 결과적으로 이것은 컨버전 서비스와 전혀 관계가 없다.

##### 컨버전 서비스는 @RequestParam , @ModelAttribute , @PathVariable , 뷰 템플릿 등에서 사용할 수 있다.

<br/>

<br/>

#### 🔎 자료 - [스프링 MVC 2편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

<br/>

