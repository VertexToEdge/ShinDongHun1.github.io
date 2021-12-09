---
title:  "Github 블로그 만들기[9]"
excerpt: "사이드바 적용(카테고리)"
date:   2021-10-16 21:30:00 
header:
  teaser: /assets/images/github-pages.png

categories: blog
tags:
  - Github
  - blog
  - 블로그
last_modified_at: 2021-10-15T21:30:30


---

<br/>

#### _config.yml 파일에 다음을 추가하자

<script src="https://gist.github.com/ShinDongHun1/b9bc88609c7222333aae0d46d9d4760d.js"></script>

sideber_main이 추가되었다.

<br/>

<br/>

#### _pages 폴더 안에 있는 카테고리별로 나눠줄 md파일을 설정한다.

![image-20211016212502499](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211016212502499.png)

<br/>

##### permalink는 해당 카테고리에 해당하는 게시물들이 보여질 주소이다.

<br/>

```markdown
{% assign posts = site.categories.blog %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
```

해당 코드를 통해 blog 카테고리에 존재하는 게시물들을 가져올 수 있게된다.

<br/>

<br/>

#### 사이드바로 띄우기

**_include** 폴더 안에 **nav_list_main** 파일을 만든다(마크다운 파일이 아닌 일반 파일이다.)

<script src="https://gist.github.com/ShinDongHun1/c0c59f2f5b1f377b86611f4f191ad80c.js"></script>

보고 대충 알아서 수정하길 바란다.

**\<span class="nav__sub-title">상위 \</span>** 를 통해 상위 위치에 상위 카테고리의 이름을 지정할 수 있다.

![image-20211016213356696](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211016213356696.png)

다음과 같이 생성된다!
