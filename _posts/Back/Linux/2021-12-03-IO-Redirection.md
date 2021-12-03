---
title:  "IO Redirection"
excerpt: "입출력에 대하여"
date:   2021-12-03 07:40:00 
header:
  teaser:

categories: linux
tags:
  - Linux
last_modified_at: 2021-12-03T07:40:00


---

## Output (출력)

ls -l 을 입력해보자. 그럼 파일과 디렉토리들의 리스트가 출력될 것이다. 이제 이 화면에 출력되는 내용을, 출력하는 대신 파일에 저장해보자.

##### ls -l > result.txt 

위 명령어를 입력하면 result.txt란 파일이 생성되고, 그곳에는 ls -l의 결과가 담겨있다.

바로 이것이 출력을 Redirection(화면 -> 파일)시킨것이다.

#### (1)>  :  1은 생략 가능

위 명령어는 출력의 방향을 바꿀 수 있다. 조금 쉽게 설명하자면, 결과를 파일에 저장해주는 명령어이다.

#### 2>   :  오류 발생 시 파일에 저장

**rm rename2.txt 1> result.txt 2> error.log**

rm rename2.txt 를 실행하였을 때, 오류가 발생하지 않고 정상 처리되었을 때의 결과를 result.txt에 저장하고, 오류가 발생했을 경우에는 error.log에 저장한다.

<br/>

<br/>

## Input (입력)

#### < : 파일의 내용을 입력

##### cat hello.txt 와 cat < hello.txt의 차이

- cat hello.txt : cat 뒤에 파일 이름이 오면, 해당 파일의 내용을 출력해준다
- cat < hello.txt : cat 뒤에 파일 이름이 아닌 일반 문자가 오면, 해당 문자를 그대로 출력 해 주는데, 이 경우에는 hello.txt속에 존재하는 내용을 입력으로 준 것이다.

<br/>

<br/>

## IO Redirection과 관련된 추가적인 기능들

**> 시 덮어쓰기가 아닌 이어쓰기를 하고싶을 때**

### \>>

> ex : ls -al >> result.txt

<br/>

<br/>

**여러 줄의 내용을 입력받고 싶을 때**

#### <<[문자]

위에서 입력한 문자가 다시 나올 때까지 작성한 모든 내용을 입력 값으로 전달한다.

> ex: mail huipulci1@naver.com <<**eot**
>
> hi
>
> my
>
> name
>
> is
>
> donghun
>
> **eot**

<br/>

<br/>

**실행 결과를 화면에도 출력하지 않고 화면에도 출력하고 싶지 않을 경우**

#### \> /dev/null

<br/>

<br/>

### 📔 Reference

##### [인프런 - 생활코딩 - Linux](https://www.inflearn.com/course/%EC%83%9D%ED%99%9C%EC%BD%94%EB%94%A9-%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B0%95%EC%A2%8C/dashboard)

