---
title:  "Github 블로그 만들기[4]"
excerpt: "이미지 삽입하기"
date:   2021-09-12 07:03:00 +0900
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

이미지 삽입하는거는 한 한시간정도 뒤지니까 되던데...

뭐 어쩔때는 오류나기도 하고... 잘 모르겠지만..

일단 시작해봅시다..!

(참고로 아직 정확하게는 몰라서 틀린거 있으면 나중에 고치도록 할게요..)

#### (10-15 수정)

<br/>

<br/>

#### 1. 환경설정 이동하기



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_062037.png" alt="20210912_062037" style="zoom:50%;" />

**파일 -> 환경설정**으로 들어가주세용

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20210912062542433.png" alt="image-20210912062542433" style="zoom: 50%;" />

**이미지**로 들어가서 **When Insert** 는 **Upload image**, 체크박스는 저렇게 설정하고, 

**Image Upload Setting**에서는 **PicGo-Core**로 선택하고,

**Download or Upgrade**를 눌러서 다운로드 한다.

그담에 **Open Config File**을 열어보면

<br/>

```json
{
  "picBed": {
    "current": "github",
    "github": {
      "repo": "github_user_name/repo_name",
      "token": "token을 생성해서 넣어야함.",
      "path": "img/",
      "branch": "main"
    }
  },
  "settings": {
    "showUpdateTip": true,
    "autoStart": true,
    "uploadNotification": true,
    "miniWindowOntop": true
  },
  "needReload": false,
  "picgoPlugins": {}
}
```

이 파일을 작성해야 한다.

 **"repo": "github_user_name/repo_name",** 

**"token": "token을 생성해서 넣어야함.",** 

**branch** : username.github.io가 main 브랜치로 되어있어서 main으로 셋팅해줌, 혹시 master라면 master로 세팅해주자

![20210912_065205](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_065205.png)

<br/>

#### 2. repo 작성하기

**repo**에는 (ShinDongHun1/image_repo) 처럼 github_user_name에 repository 이름을 넣어야 한다.

새로운 깃허브 저장소를 하나 만들어주자.

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_063228.png" alt="20210912_063228" style="zoom: 50%;" />

위 사진에 보이는 img 폴더는 내가 만든것이 아니라 **Config File** 을 보면**path**에 "img/" 있는데 이미지를 삽입하면 저기에 알아서 올라간다.

<br/>

이제 **token**을 만들자.

#### 3. token 생성하기



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_063711.png" alt="20210912_063711" style="zoom: 50%;" />

<br/>

**Github** 로 이동해서 **우측 상단 프로필 아이콘** -> **Settings**

<br/>



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_064154.png" alt="20210912_064154" style="zoom: 50%;" />

왼쪽 아래 **Developer settings**

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_064449.png" alt="20210912_064449" style="zoom: 50%;" />



**Personal access tokens** -> **Generate new token** 

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_064634.png" alt="20210912_064634"  />

##### 위와 같이 체크하자

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210912_065722.png" alt="20210912_065722" style="zoom:50%;" />

<br/>

토큰은 1번만 보여주니 복사한 후 안전한 곳에 저장한다.

혹시 실수로 복사를 못했다면 다시 토큰을 만들어주면 된다.

복사 했으면 **Config File** 에서 **"token"** 부분을 세팅해주자.

<br/>

<br/>

이렇게 세팅이 끝났으면 이미지를 타이포라에 삽입하시면 자동으로 업로드가 된다.

