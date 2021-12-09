---
title:  "[IntelliJ] 테스트코드 한글 깨짐"
excerpt: "인텔리제이 테스트코드 인코딩 설정"
date:   2021-11-24 02:43:00
header:
  teaser: /assets/images/spring.png

categories: setting
tags:
  - Java
last_modified_at: 2021-11-24T02:43:00


---

<br/>

<br/>

## 인텔리제이 JUnit 한글 깨짐 문제

![image-20211124180830104](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124180830104.png)

[출처 https://adg0609.tistory.com/33](https://adg0609.tistory.com/33)

이런 식으로 테스트코드의 이름을 한글로 작성했을때 깨질때가 종종 있다.

<br/>

##### 상단의 Help 클릭

![image-20211124180937200](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124180937200.png)

<br/>

##### Edit Custom VM Options.. 클릭

![image-20211124180953439](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124180953439.png)

<br/>

##### 다음 코드 추가

```
-Dfile.encoding=UTF-8
```

![image-20211124181036463](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124181036463.png)

<br/>

#### 해결!

![image-20211124181047825](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124181047825.png)

<br/>

<br/>

### 📔 Reference

[\[IntelliJ] 인텔리J junit 한글 깨짐 문제 해결](https://adg0609.tistory.com/33)