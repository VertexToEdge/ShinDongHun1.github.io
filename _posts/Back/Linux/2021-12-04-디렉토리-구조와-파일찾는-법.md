---
title:  "[Linux] 디렉토리 구조"
excerpt: "디렉토리 구조"
date:   2021-12-04 09:45:00 
header:
  teaser:

categories: linux
tags:
  - Linux
last_modified_at: 2021-12-04T09:45:00



---

<br/>

## 디렉토리 구조

![image-20211204091706237](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211204091706237.png)

<br/>

#### 1. /  : Root 

- 최상위 디렉토리

<br/>

#### 2. /bin : User Binaries

- 사용자가 사용하는 명령들
- 기본적인 명령어가 저장되어 있다.
- root 사용자와 일반 사용자가 함께 사용할 수 있는 명령어 디렉토리이다.

<br/>

#### 3. /sbin : System Binaries

- 시스템을 관리할 목적을 가진 사용자들이 사용하는 프로그램들

<br/>

#### 4. /etc : Configuration Files

- 시스템의 거의 모든 설정파일들이 존재한다.
- /etc/sysconfig(시스템 제어판용 설정파일), /etc/passwd(사용자관리 설정파일), /etc/named.conf(DNS 설정파일) 등과 같은 파일들이 존재한다.

<br/>

#### 5. /dev : Device Files

- 시스템 디바이스 파일을 저장

<br/>

#### 6. /proc : Process Information

- 일명 "가상파일시스템"이라고 하는 곳으로 현재 메모리에 존재하는 모든 작업들이 파일형태로 존재한다.
- 실제 운용상태를 정확하게 파악할 수 있는 중요한 정보를 제공하며 여기에 존재하는 파일들 가운데 현재 실행중인 커널(kernel)의 옵션 값을 즉시 변경할 수 있는 파라미터파일들이 있기 때문에 시스템 운용에 있어 매우 중요한 의미를 가진다.

<br/>

#### 7. /var : Variable Files

- 시스템운용중에 생성되었다가 삭제되는 데이터를 일시적으로 저장하기 위한 디렉토리. 
- 거의 모든 시스템 로그 파일은 /var/log 에 저장되고, DNS 의 zone 설정파일은 /var/named 에 , 메일파일은 /var/spool/mail 에 저장되며, 크론설정파일은 /var/spool/cron 디렉토리에 각각 저장됨.

<br/>

#### 8. /tmp : Temporary Files

- 임시 파일 디렉토리. 
- linux에서 프로그램들은 임시 파일을 만들 때 일반적으로 해당 디렉토리에 임시 파일들을 만든다.
- 이 디렉토리안의 모든 파일은 재부팅 할 때 제거된다.

<br/>

#### 9. /usr : User Programs

- 모든 프로그램들이 설치되는 디렉토리이다. 보통 `/usr` 디렉토리에는 배포판에서 제공하는 파일들이 들어 있으며, 그 밖에 따로 설치되는 프로그램들과 내부적 용도의 프로그램들은 `/usr/local`에 들어가는 것이 일반적이다.

<br/>

#### 10. /home : Home Directories

- 사용자들의 디렉토리.
- 만약 shin이라는 사용자가 있다면 /home 하위에 /shin이라는 디렉토리가 존재한다.
- 사용자의 홈 디렉토리로 빠르게 이동하고 싶다면 `cd ~` 을 입력하자

<br/>

#### 11. /boot : Boot Loader Files

- 부팅에 필요한 정보를 가진 파일들이 있는 디렉토리.

<br/>

#### 12. /lib : System Libraries

- 라이브러리 정보들이 있다.
- 부팅과 시스템 운영에 필요한 공유 라이브러리 및 커널 모듈이 있는 디렉토리

<br/>

#### 13. /opt : Optional add-on Applications

- 소프트웨어 파일들을 가지고 있다.

<br/>

#### 14. /mnt : Mount Directory

- 시스템 관리자들이 보통 임시적으로 파일시스템 마운트할 때 사용하는 디렉토리
- 마운트는 파일을 다른 공간과 연결한다는 뜻

<br/>

#### 15. /media : Removable Media Devices

- DVD, CD-ROM, USB 등과 같은 탈부착이 가능한 장치들의 마운트포인트로 사용되는 디렉토리.

<br/>

#### 16. /srv : Service Data

- 시스템에서 제공되는 특정 사이트들의 데이터를 기본적으로 저장한다.

<br/>

<br/>

### 📔 Reference

##### [인프런 - 생활코딩 - Linux](https://www.inflearn.com/course/%EC%83%9D%ED%99%9C%EC%BD%94%EB%94%A9-%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B0%95%EC%A2%8C/dashboard)

##### [Linux Directory Structure (File System Structure) Explained with Examples](https://www.thegeekstuff.com/2010/09/linux-file-system-structure/)

##### [리눅스 디렉토리 구조](https://webdir.tistory.com/101)

##### [리눅스 디렉토리 구조](https://www.morenice.kr/31)

##### ['/'안 주요 디렉토리 용도](https://it-serial.tistory.com/42)