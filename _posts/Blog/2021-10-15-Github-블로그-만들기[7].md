---
title:  "Github 블로그 만들기[7]"
excerpt: "폰트 적용하기"
date:   2021-10-15 16:35:00 +0900
header:
  teaser: /assets/images/github-pages.png

categories: blog
tags:
  - Github
  - blog
  - 블로그
last_modified_at: 2021-10-15T16:35:30-05:00


---

<br/>

<br/>

#### 폰트 고르기

-  [눈누](https://noonnu.cc/index)
- [구글](https://fonts.google.com/)

등등

<br/>

원하는 폰트를 골랐으면, 

![image-20211015162836837](C:/Users/huipu/AppData/Roaming/Typora/typora-user-images/image-20211015162836837.png)

웹폰트로 사용에 있는 코드를 복사하자.

<br/>

<br/>

#### 적용하기

##### assets -> css -> main.scss 이동

```scss
@font-face {
  font-family: 'Cafe24Oneprettynight';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.1/Cafe24Oneprettynight.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
html {
  font-family: 'Cafe24Oneprettynight';
 }
```



여러 방법이 있지만 난 이렇게 적용해주었다.