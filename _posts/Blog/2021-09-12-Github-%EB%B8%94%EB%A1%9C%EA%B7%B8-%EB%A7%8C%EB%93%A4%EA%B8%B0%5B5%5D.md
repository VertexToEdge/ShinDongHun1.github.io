---
title:  "Github 블로그 만들기[5]"
excerpt: "상단 카테고리 만들기"
date:   2021-09-12 07:23:00 +0900
header:
  teaser: /assets/images/github-pages.png

categories: blog
tags:
  - Github
  - blog
  - 블로그
last_modified_at: 2021-09-12T07:07:30-05:00
---

<br/>

이미지는 어찌어찌 했는데...

이 카테고리 넘 어렵네요... 

아직 사이드바는 만드는법도 모르겠어요 ㅠㅠㅠㅠㅠㅠ

일단 상단 바 만드는법 알려드릴게요.

아 참고로 지금부터는 제가 쓰는 테마인 **minimal mistakes** 에서 상단바 만드는법을 알려드릴거라, 

다른 테마 쓰시는 분들은 아마 다를거예요. (생각보다 비슷할수도..??) 아무튼 그냥 저랑 같은 테마 아니면

각자 테마 카테고리 만드는 법 구글에 검색해보셔요..!

(참고로 아직 정확하게는 몰라서 틀린거 있으면 나중에 고치도록 할게요..) (저번에 했던 말 같은데..???)

<br/>

<br/>

<br/>

#### 1. navigation.yml 수정

<br/>

**Username.github.io** 파일로 이동

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_191651.png" alt="20210912_191651" style="zoom: 67%;" />

**_data -> navigation.yml**

<br/>



![image-20210912191852841](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20210912191852841.png)



**title** : 제목, 입력한 값이 표시됨.

**url** : 클릭 시 이동할 주소

![20210912_192045](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_192045.png)



<br/>

#### 2. _page 폴더 수정

<br/>

**_page 폴더가 없다면 새로 만들어주자**

<br/>

>  github.io 폴더 > _pages 폴더 > 카테고리를 지정할 md파일 생성

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_194310.png" alt="20210912_194310"  />

##### permalink : 위 파일의 카테고리에 속한 파일들을 보여줄 주소

##### taxonomy : post틔 categories와 값이 일치해야 함.

(**이 파일은 _pages 폴더 안에 만들어야 한다**)

파일 이름은 상관없다.

<br/>

<br/>



#### 3. _post 폴더에 게시물 생성

<br/>

![20210912_195523](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_195523.png)

categories는  taxonomy 와 일치해야 한다. 저 위에 none 대신에 taxonomy 와 일치하게 작성해주자.

(위의 예시에서는 WhatIsThis)

(**이 파일은 _posts 폴더안에 저장**)

<br/>

<br/>

#### 4. 다시 navigation.yml 파일 수정

<br/>

![20210912_195918](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_195918.png)

#####  navigation.yml

<br/>

이렇게 **navigation.yml** 파일에 

> -title: 테테테 Test
>
> url:  /test/TTT/

를 추가! (여기서 **url**은 저기 위에서 만든 **'[키킼.md]'**파일의 **permalink**랑 일치해야한다.)

<br/>

여기까지 변경한 파일들을 github에 저장.

조금 기다렸다 확인해보면

![20210912_203843](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_203843.png)





<br/>

### 결론

카테고리 링크를 누르면 **navigation.yml** 파일 속 **URL**에 설정한 위치로 이동한다.

<br/>

**_pages**폴더 안에 들어있는 **마크다운 파일** 의 **permalink**의 값과 **navigation.yml**파일의 **URL 값이 일치**하면 해당 **마크다운 파일**의 양식을 사용한 카테고리가 만들어진다!.

<br/>

해당 **마크다운 파일**의 **taxonomy**값과   **_posts**폴더 안의 **마크다운 파일**의 **catagories**값이 일치해야 해당 카테고리에 속하여 보여진다!

<br/>

#### 
