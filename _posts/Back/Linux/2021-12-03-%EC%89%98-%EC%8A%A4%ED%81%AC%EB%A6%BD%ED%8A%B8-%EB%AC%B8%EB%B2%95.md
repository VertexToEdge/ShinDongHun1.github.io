---
title:  "[Linux] 쉘 스크립트 문법"
excerpt: "쉘 스크립트 공부하기"
date:   2021-12-03 17:45:00 
header:
  teaser:

categories: linux
tags:
  - Linux
last_modified_at: 2021-12-03T17:45:00


---

<br/>

### 시작하기 전에..

쉘 스크립트는 쉘에게 무슨 명령들을 실행할지를 알려주는 스크립트 파일입니다. 쉘에는 bash, zsh 등과 같이 여러 종류가 있으나 여기서는 가장 흔하게 사용되는 bash쉘을 사용하는 쉘 스크립트를 설명하겠습니다.

<br/>

<br/>

## 쉘 스크립트 기본 문법

### #!/bin/bash

##### 쉘 스크립트의 최상단에는 항상 이 구분이 적혀있어야 합니다. 쉘의 종류가 bash가 아니라면 bash자리에 zsh 등과 같이 쉘의 이름을 적어주시면 됩니다.

```sh
#!/bin/bash

#echo는 줄바꿈, printf는 줄바꿈 하지 않음
echo "hello, shellScript"      
printf "hello, shellScript \n"
```

<br/>

### 변수

변수를 선언할 때는 <span style="color:orange">**변수명=값**</span>으로 선언하고, 사용할때는 앞에  <span style="color:orange">**$**</span>을 붙여 사용한다. 중괄호를 사용할 수도 있다.  <span style="color:orange">**${변수}**</span>처럼 말이다.

##### 참고로 변수의 default 값은 문자열이므로 ""를 생략해 주어도 된다

```sh
#!/bin/bash

h="hello"
s="shellScript"
echo "${j}, ${s}"
```

<br/>

### 환경변수

<span style="color:orange">**export**</span>를 사용하면 환경변수를 지정할 수 있다.

```sh
#!/bin/bash
#이 파일은 exam.sh 파일입니다.
export NAME="shindonghun"

#exam2 실행
./exam2.sh
```

```sh
#!/bin/bash
#이 파일은 exam2.sh 파일입니다.

echo ${NAME}
```

<br/>

### 매개변수

#### 전달 시

##### ./쉘 스크립트 매개변수1 매개변수2 

**예시: ./exam.sh "var1" "var2"**

매개변수를 전달할 때는 다음과 같이 실행할 쉘 스크립트 이후에 인자들을 넘겨주면 된다.

#### 사용 시

```sh
#!/bin/bash

echo "script name:${0}"
echo "매개변수 갯수 :${#}"
echo "전체 매개변수  값 : ${*}"
echo "전체 매개변수 값2 : ${@}"
echo "매개변수 1 : ${1}"
echo "매개변수 2 : ${2}"
```

![image-20211203175718464](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211203175718464.png)

<br/>

### 예약변수

쉘 스크립트에서는 이미 정의되어 사용자가 만들 수 없는 변수가 존재합니다. 그것을 예약 변수라고 하는데 몇가지 예약 변수들을 알아보자.



| **변수**     | 설명                                                         |
| ------------ | ------------------------------------------------------------ |
| **HOME**     | 사용자 홈 디렉토리를 의미합니다.                             |
| **PATH**     | 실행 파일의 경로입니다. 여러분이 chmod, mkdir 등의 명령어들은 /bin이나 /usr/bin, /sbin에 위치하는데, 이 경로들을 PATH 지정하면 여러분들은 굳이 /bin/chmod를 입력하지 않고, chmod 입력만 해주면 됩니다. |
| **LANG**     | 프로그램 실행 시 지원되는 언어를 말합니다.                   |
| **UID**      | 사용자의 UID입니다.                                          |
| **SHELL**    | 사용자가 로그인시 실행되는 쉘을 말합니다.                    |
| **USER**     | 사용자의 계정 이름을 말합니다.                               |
| **FUNCNAME** | 현재 실행되고 있는 함수 이름을 말합니다.                     |
| **TERM**     | 로그인 터미널을 말합니다.                                    |

<br/>

<br/>

### 배열(Array)

쉘 스크립트에서 배열은 **<span style="color:orange">1차원 배열만 지원</span>**하며 <span style="color:orange">**중괄호를 사용**</span>해야 합니다.

배열 원소는 소괄호 안에 공백으로 구분하여 주고, 배열 안 원소는 문자열이든 정수든 상관 없이 쓸 수 있는 특징이 있다.

```sh
#!/bin/bash

arr=("hello" 1 2 3)

echo "배열 전체 : ${arr[@]}"
echo "배열 원소의 객수 : ${#arr[@]}"
echo "배열 첫번째 : ${arr}, 혹은 ${arr[0]}"
echo "배열 인덱스 3 : ${arr[3]}"

arr[3]="30"
arr[4]="40"
arr[6]="60"

echo "배열 인덱스 3 : ${arr[3]}"

echo "배열 인덱스 4 : ${arr[4]}"
echo "배열 인덱스 5 : ${arr[5]}"
echo "배열 인덱스 6 : ${arr[6]}"

echo "배열 전체 : ${arr[@]}"
echo "배열 원소의 객수 : ${#arr[@]}"
#2번 원소 해제
unset arr[2]
echo "2번 원소 삭제 후"
echo "2번 index를 갖는 배열의 원소 ${arr[2]}"

echo "배열 전체 : ${arr[@]}"
echo "배열 원소의 객수 : ${#arr[@]}"
```

![image-20211203183123769](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211203183123769.png)

조금 놀랐던 점은 중간에 빈 인덱스가 있더라도 상관이 없었다는 것이다. (인덱스가 1, 2, 3, 4, 6 처럼 5 없이도 가능!)

<br/>

<br/>

### 함수

쉘 스크립트에서도 다른 프로그래밍 언어와 같이 함수를 사용할 수 있습니다. 

##### 함수 호출 전에 함수가 정의되어 있어야 하며, 함수를 호출할 때는 괄호를 생략하고 호출해 주어야 한다.

```sh
function 함수명(){
...내용...
}

#함수 호출
함수명

#============================
function func(){
	echo "호출"
}
func

#function은 생략 가능하다
func(){
	echo "호출"
}
func
```

<br/>

<br/>



### 📔 Reference

##### [인프런 - 생활코딩 - Linux](https://www.inflearn.com/course/%EC%83%9D%ED%99%9C%EC%BD%94%EB%94%A9-%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B0%95%EC%A2%8C/dashboard)

##### [쉘 스크립트(SHELL SCRIPT) 기본 문법, 작성방법(변수,반복문,비교문,종료상태 등)](https://reakwon.tistory.com/136)

##### [인자, 파라미터 사용법](https://jink1982.tistory.com/36)

##### [Bash Shell Script - 함수(Function)](https://codechacha.com/ko/shell-script-function/)
