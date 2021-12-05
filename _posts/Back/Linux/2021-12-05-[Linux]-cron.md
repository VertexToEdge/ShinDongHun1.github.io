---
title:  "[Linux] cron"
excerpt: "cron"
date:   2021-12-05 09:46:00 
header:
  teaser:

categories: linux
tags:
  - Linux
last_modified_at: 2021-12-05T09:46:00




---

<br/>

## cron - 정기적 실행

##### 정기적으로 실행해야 하는 명령을 실행하기 위해서는 cron을 사용하면 된다.

> ##### crontab -e  : 하고자 하는 명령 정의

<br/>

#### 실행파일 작성

> ##### m h dom mon dow command 

![Claus Ibsen (@davsclaus) riding the Apache Camel: Apache Camel 2.12 - Even  easier cron scheduled routes](http://2.bp.blogspot.com/--d9V7XzD9aU/UgzRLNXIgSI/AAAAAAAAAcM/cIzUHV665v0/s1600/cron.png)

- m : 분의 주기, 10이면 매시간 10분, /10이면 10분에 1번
- h : *이면 시간과는 상관없이 실행, 1이면 1시에 실행
- dom : (day of month), 매달 며칠에 실행하는지
- mon : 몇월에 실행하는지
- dow : 요일 (0~6, 0이 일요일)

<br/>

<br/>

### 📔 Reference

##### [인프런 - 생활코딩 - Linux](https://www.inflearn.com/course/%EC%83%9D%ED%99%9C%EC%BD%94%EB%94%A9-%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B0%95%EC%A2%8C/dashboard)

