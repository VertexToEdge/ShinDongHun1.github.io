---
title:  "Github 블로그 만들기[2]"
excerpt: "테마 적용하기"
date:   2021-09-11 20:03:00 +0900
header:
  teaser: /assets/images/github-pages.png

categories: blog
tags:
  - Github
  - blog
  - 블로그
last_modified_at: 2021-09-11T21:11:00-05:00
---

<br/>

이제 테마를 적용해 보겠다. 



<br/><br/><br/>

#### 1. Jekyll 설치하기

<br/>

>  gem install jekyll bundler 

을 실행하면 설치가 된다는데, 대체 어디에 치라는건지 몰랐었다.

[https://rubyinstaller.org/downloads/](https://rubyinstaller.org/downloads/)

이곳에 들어가서 

<br/>



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-2021091121354321.png" alt="image-2021091121354321" style="zoom:50%;" />

저기 동그라미 친 부분을 눌러 다운받아주자.

조금 오래 걸린다!!!

다운 다 받으면 실행하면 또 막 이것저것 선택하는게 나왔던거 같은데 그냥 다 기본값으로 해주면 된다.

설치가 끝났으면 **Start Command Prompt with Ruby** 를 실행한 후 명령어(gem install jekyll bundler)를 쳐준다.

<br/>

<br/>

<br/>

#### 2. **Jekyll 생성** 

<br/>

**Ruby Prompt** 에서**[Github 블로그 만들기[1]](https://shindonghun1.github.io/blog/Github-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-1/)** 에서 clone 한 폴더로 이동하자.

( **cd username.github.io** 입력하면 폴더로 이동될것이다.)

(물론 자기가 저장한 위치에 따라 달라질 수 있다.)

이동했으면

> jekyll new ./

를 입력해주면 된다. 

<br/>

난 여기서 오류가 났는데 파일을 비워줘야 한다길래 username.github.io에 들어있는 파일을 모두 삭제했다.

<br/>

<br/>

#### 3. build install

<br/>

> bundle install

입력해주자. 

<br/>

<br/>

#### 4.  Jekyll을 로컬서버에 띄우기

<br/>

> bundle exec jekyll serve

를 입력해주면 된다길래 했는데 나는 오류가 떴다.

<br/>

![20210911_225312](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_225312.png)



뭐 대충 이런 오류였는데 찾아보니까

<br/>

> bundle add webrick

를 입력해준 후 다시 

> bundle exec jekyll serve

를 입력해주면 해결된다.



![20210911_225530](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_225530.png)

<br/>

그럼 이렇게 뜰텐데 ***이 주소***를 브라우저 주소창에 입력해서 들어가보면!!!!

잘 될거다.

<br/>

이제 **Git Bash**를 키고

> cd username.github.io

위 명령어를 쳐서 clone한 파일이 있는 곳으로 가서,

<br/>

> git add . 
>
> git commit -m "본인의 커밋 메세지"
>
> git push 

를 쳐주쟈

(만약에 여기서 안되면 github 사용법 검색해서 고고)

아마 git push만 하면 안될거에여!! 검색 기기!! 아마 git push origin main 하면 됐던걸로 기억하는데.. 아무튼 해봐요 한번!

이건 쉬워서 그냥 하란대로 하면 쭉쭉 될거임

<br/>

다시 아까 ***이 주소*** 를 브라우저 검색창에 쳐주면!!!

**username.github.io** 로 되어있을거임!!!!! 와 굳!!

<br/>

<br/>

<br/>

#### 5. 테마 선택하기

<br/>

- **[jamstackthemes.dev](https://jamstackthemes.dev/ssg/jekyll/)**
- **[jekyllthemes.org](http://jekyllthemes.org/)**
- **[jekyllthemes.io](https://jekyllthemes.io/)**
- **[jekyll-themes.com](https://jekyll-themes.com/)**

<br/>

등의 사이트들이 있는데 아무거나 맘에 드는거 골라욤!

나는 [minimal mistakes](https://github.com/mmistakes/minimal-mistakes) 테마를 사용했다. (블로그 봤는데 이거 추천해주더라)

<br/>

아무튼 저기 들어가면 github Repository로 이동될텐데 

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_230454.png" alt="20210911_230454" style="zoom:50%;" />

<br/>

여기 Download ZIP을 클릭해서 다운받은 후



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_230622.png" alt="20210911_230622" style="zoom:50%;" />

<br/>전체선택을 해준다음에



<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/20210911_230726.png" alt="20210911_230726" style="zoom: 80%;" />



[현재 내 github.io 폴더] 에 그대로 **붙여넣기**를 해주자!

몇개 파일 겹친다면 그냥 다 **덮어쓰기** 하자!

<br/>

그다음에

> bundle install
>
> bundle add webrick
>
> bundle exec jekyll serve

을 해주자. 

(웃긴게 나만 그런지 모르겠는데 아까 **bundle add webrick** 이걸 해줬는데도 또 오류가 나서 다시 해줌. 오류 안나면 님들은 이거 안 해도 될거에여 아마.)

<br/>

이제 다시

> git add . 
>
> git commit -m "본인의 커밋 메세지" 
>
> git push

를 쳐주면 끝!!!!

이제 username.github.io 로 검색해서 확인해보자!!!
