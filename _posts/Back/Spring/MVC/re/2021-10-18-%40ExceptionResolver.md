---
title:  "@ExceptionHandler"
excerpt: "API์์ธ ์ฒ๋ฆฌ- ExceptionResolver"
date:   2021-10-18 16:20:00
header:
  teaser: /assets/images/spring.png

categories: MVC
tags:
  - Java
  - Spring
  - MVC
last_modified_at: 2021-10-18T16:20:00

---

<br/>

## ๐ก @ExceptionResolver

##### ์คํ๋ง์ API ์์ธ ์ฒ๋ฆฌ ๋ฌธ์ ๋ฅผ ํด๊ฒฐํ๊ธฐ ์ํด @ExceptionHandler ๋ผ๋ ์ ๋ธํ์ด์์ ์ฌ์ฉํ๋ ๋งค์ฐ ํธ๋ฆฌํ ์์ธ ์ฒ๋ฆฌ ๊ธฐ๋ฅ์ ์ ๊ณตํ๋ค.

##### ์ด๊ฒ์ ์ฒ๋ฆฌํ๋๊ฒ์ด ๋ฐ๋ก ExceptionHandlerExceptionResolver ์ด๋ค.

##### ์คํ๋ง์ ExceptionHandlerExceptionResolver ๋ฅผ ๊ธฐ๋ณธ์ผ๋ก ์ ๊ณตํ๊ณ , ๊ธฐ๋ณธ์ผ๋ก ์ ๊ณตํ๋ ExceptionResolver ์ค์ ์ฐ์ ์์๋ ๊ฐ์ฅ ๋๋ค. 

##### ์ค๋ฌด์์ API ์์ธ ์ฒ๋ฆฌ๋ ๋๋ถ๋ถ ์ด ๊ธฐ๋ฅ์ ์ฌ์ฉํ๋ค.

<br/>

#### ๐๋์ ์๋ฆฌ

##### @ExceptionResolver ์๋ธํ์ด์์ ์ ์ธํ๊ณ , ํด๋น ์ปจํธ๋กค๋ฌ์์ ์ฒ๋ฆฌํ๊ณ  ์ถ์ ์์ธ๋ฅผ ์ง์ ํด์ฃผ๋ฉด ๋๋ค. 

##### ํด๋น ์ปจํธ๋กค๋ฌ์์ ์์ธ๊ฐ ๋ฐ์ํ๋ฉด ์ด ๋ฉ์๋๊ฐ ํธ์ถ๋๋ค.

##### ์ฐธ๊ณ ๋ก ์ง์ ํ ์์ธ ๋๋ ๊ทธ ์์ธ์ ์์ ํด๋์ค๋ฅผ ๋ชจ๋ ์ก์ ์ ์๋ค.



<br/>

### ๐์ฌ์ฉํด๋ณด๊ธฐ

<script src="https://gist.github.com/ShinDongHun1/761d4e631e00afce4982a92ecc9928eb.js"></script>

##### ๐ ์ฐธ๊ณ  - ErrorResult ๋ ์ง์  ๋ง๋ค์ด์ค ํด๋์ค์ด๋ค.

```java
@Data
@AllArgsConstructor
public class ErrorResult {
    private String code;
    private String message;
}
```

<br/>

#### ๐ ์์ธ ์๋ต

##### @ExceptionHandler์ ์์ธ๋ฅผ ์๋ตํ  ์ ์๋ค. ์๋ตํ๋ฉด ๋ฉ์๋ ํ๋ผ๋ฏธํฐ์ ์์ธ๊ฐ ์ง์ ๋๋ค.

<br/>

#### ๐ ํ๋ฆฌ๋ฏธํฐ์ ์๋ต

##### @ExceptionHandler ์๋ ๋ง์น ์คํ๋ง์ ์ปจํธ๋กค๋ฌ์ ํ๋ผ๋ฏธํฐ ์๋ต์ฒ๋ผ ๋ค์ํ ํ๋ผ๋ฏธํฐ์ ์๋ต์ ์ง์ ํ  ์ ์๋ค.

##### ์์ธํ ํ๋ผ๋ฏธํฐ์ ์๋ต์ ๋ค์ ๊ณต์ ๋ฉ๋ด์ผ์ ์ฐธ๊ณ ํ์.

[https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annexceptionhandler-args](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-annexceptionhandler-args)

<br/>

#### ๐ ์คํ ํ๋ฆ

- ##### ์ปจํธ๋กค๋ฌ๋ฅผ ํธ์ถํ ๊ฒฐ๊ณผ IllegalArgumentException ์์ธ๊ฐ ์ปจํธ๋กค๋ฌ ๋ฐ์ผ๋ก ๋์ ธ์ง๋ค.

- ##### ์์ธ๊ฐ ๋ฐ์ํ์ผ๋ก ExceptionResolver ๊ฐ ์๋ํ๋ค. ๊ฐ์ฅ ์ฐ์ ์์๊ฐ ๋์ExceptionHandlerExceptionResolver ๊ฐ ์คํ๋๋ค.

- ##### ExceptionHandlerExceptionResolver ๋ ํด๋น ์ปจํธ๋กค๋ฌ์ IllegalArgumentException ์ ์ฒ๋ฆฌํ  ์ ์๋ @ExceptionHandler ๊ฐ ์๋์ง ํ์ธํ๋ค.

- ##### illegalExHandle() ๋ฅผ ์คํํ๋ค.

<br/>

<br/>

### ๐ Reference

##### [์คํ๋ง MVC 2ํธ](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-mvc-2/dashboard)

<br/>

