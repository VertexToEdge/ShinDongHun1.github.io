---
title:  "[Linux] 파일 찾는 법"
excerpt: "파일 찾는 법"
date:   2021-12-04 09:46:00 
header:
  teaser:

categories: linux
tags:
  - Linux
last_modified_at: 2021-12-04T09:46:00


---

<br/>

## 파일 찾는 법

### locate  

> ##### locate 이름.확장자

locate는 데이터베이스를 뒤져서 파일을 찾는다. locate가 사용하는 데이터베이스를 **mlocate**라고 한다. 

sudo updatedb라는 명령어를 통해 현재 디렉토리의 상태를 db에 저장하는데, 많은 리눅스 시스템에서 하루에 한번 자동으로 이 명령어를 수행하게 되어있다.

<br/>

<br/>

### find 

> ##### [https://www.tecmint.com/35-practical-examples-of-linux-find-command/](https://www.tecmint.com/35-practical-examples-of-linux-find-command/) 이곳을 참고하자

locate와는 다르게 디렉토리를 뒤져서 파일을 찾는다. 따라서 최신 상태의 파일을 찾아올 수 있다.

<br/>

<br/>

### whereis

> ##### whereis find 
>
> #결과
>
> ##### 	find: /bin/find /usr/bin/find /usr/share/man/man1/find.1.gz

실행파일의 위치, 소스위치, man페이지 파일의 위치를 찾아준다.

<br/>

<br/>

### 📔 Reference

##### [인프런 - 생활코딩 - Linux](https://www.inflearn.com/course/%EC%83%9D%ED%99%9C%EC%BD%94%EB%94%A9-%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B0%95%EC%A2%8C/dashboard)

