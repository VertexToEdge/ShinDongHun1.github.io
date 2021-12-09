---
title:  "Github 블로그 만들기[3]"
excerpt: "게시글 작성하기"
date:   2021-09-11 21:03:00 +0900
header:
  teaser: /assets/images/github-pages.png

categories: blog
tags:
  - Github
  - blog
  - 블로그
last_modified_at: 2021-09-11T23:22:30-05:00
---

<br/>

이제 글쓰는 법을 배워보자. 

글쓰는법이 너무 어려워서 하다가 포기할 뻔 했다. 

<br/>

<br/>

#### 1. 마크다운 에디터 다운받기

<br/>

#####   여기서 마크다운이란??

>  - 마크다운(markdown)은 일반 텍스트 기반의 경량 마크업 언어다. 일반 텍스트로 서식이 있는 문서를 작성하는 데 사용되며, 일반 마크업 언어에 비해 문법이 쉽고 간단한 것이 특징이다.
>    HTML과 리치 텍스트(RTF) 등 서식 문서로 쉽게 변환되기 때문에 응용 소프트웨어와 함께 배포되는 README 파일이나 온라인 게시물 등에 많이 사용된다.
>
>  - ```null
>    출처 : https://ko.wikipedia.org/wiki/%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4
>    ```

Github 블로그에 글을 쓰려면 이 형식으로 작성해야 한다.

**마크다운 에디터**를 사용해야 하는데 나는 **타이포라**를 사용하기로 했다.

<br/>

<br/>

#### 2. 타이포라 다운받기

<br/>

[https://typora.io/](https://typora.io/)

이곳으로 이동해서 스크롤을 내리다 보면

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_232743.png" alt="20210911_232743" style="zoom:67%;" />



설치해주자.

선택하는거는 다 기본값으로 하면 설치가 딱 끝나고 실행시켜보자

<br/>



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_232910.png" alt="20210911_232910" style="zoom:67%;" />



너무 뭐가 없이 하얘서 놀랐다..

이제 **타이포라 사용법**을 검색해서 포스팅할 글을 써보자

<br/>

##### 글의 저장 위치는 다음과 같다.

<br/>

- ### **저장하는 위치**





<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20210911233100043.png" alt="image-20210911233100043" style="zoom: 80%;" />



저기 폴더 경로 보면 **username.github.io** 에 **_posts**라는곳이 있는데 이곳에 **저장**하면 된다.

일단 글 쓰기 전에 **깃허브**로 들어가서 우리가 만든 블로그의 **Repository**로 이동해보면

<br/>



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_233617.png" alt="20210911_233617" style="zoom:67%;" />

이렇게 있을것이다.  (빨간 사각형은 내 커밋 이름이 너무 웃겨서...)

아무튼 여기서 **_posts** 로 이동해보자.

<br/>



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_233801.png" alt="20210911_233801" style="zoom:80%;" />





난 파일명이 내가 만들어서 이건데 아마 무슨 기본 예시? 파일 하나 있을거다.

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_233826.png" alt="20210911_233826" style="zoom:80%;" />



대충 요런 뭐시기 쫙 나올건데 여기서 저기 빨간색 동그라미 친 부분을 클릭해보자.

<br/>



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_233842.png" alt="20210911_233842" style="zoom:50%;" />



그럼 이케 수정할 수 있게 나올텐데!!!!! 

위에 --- 으로 시작해서 ---으로 끝나는 부분이 이 파일의 설정값? 느낌의 그런 것 같다.

- ##### title:  제목

- ##### excerpt: 부제목? 내용? 설명?

- ##### date:  포스팅한 시간

- ##### header:
  -   teaser: 이 글의 이미지의 위치

- ##### categories: 이 글의 카테고리

- ##### tags: 태그들

등등이 있다.

<br/>



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_234225.png" alt="20210911_234225" style="zoom: 80%;" />



**username.github.io\_posts** 위치에 저장해 주고

**Github 블로그 만들기[2] **에서 했던것처럼 **Git Bash**를 키고



> git add .
>
> git commit -m “본인의 커밋 메세지”
>
> git push

를 통해 깃허브에 올려주자. 

한 1~2 분 있으면 적용되어 있을것이다.

<br/>



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_234601.png" alt="20210911_234601" style="zoom: 67%;" /><br/>

<br/>
