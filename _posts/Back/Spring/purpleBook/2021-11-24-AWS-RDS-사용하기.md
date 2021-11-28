---
title:  "AWS RDS 사용하기"
excerpt: "스프링 부트와 AWS로 혼자 구현하는 웹 서비스 6"
date:   2021-11-26 12:36:00 
header:
  teaser: /assets/images/spring.png

categories: purpleBook
tags:
  - Java
  - Spring
last_modified_at: 2021-11-26T12:36:00




---

<br/>

<img src="https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211124204433310.png" alt="image-20211124204433310" style="zoom:30%;" />

<br/>

## AWS RDS

웹 서비스의 백엔드를 다룬다고 했을 때 애플리케이션 코드를 작성하는 것만큼 중요한 것이 데이터베이스를 다루는 일입니다. 규모 있는 회사에서는 데이터베이스를 전문적으로 처리하는 DBA라는 직군 담당자들이 있다. 해당 전문분야의 담장자가 있기에 상대적으로 개발자가 데이터베이스를 전문적으로 다룰 일이 적다.

다만 그건 대용량/대량의 데이터를 다루기 때문에 전문성이 필요한 것이지, 백엔드 개발자가 데이터베이스를 몰라도 된다는 말을 아니다. 스타트업이나 개발 인원수가 적은 서비스에선 개발자가 데이터베이스를 다뤄야만 한다.

데이터베이스를 직접 설치한다면 **모니터링, 알람, 백업, HA구성** 등을 모두 직접 해야만 한다. 이는 처음 구축할 때 며칠이 걸릴 수 있는 일이다.

AWS에서는 앞에서 언급만 작업을 모두 지원하는 관리형 서비스인 RDS를 제공한다.

<br/>

<br/>

## RDS 인스턴스 생성하기

![image-20211125181849156](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125181849156.png)

##### 다음과 같이 검색창에 rds를 입력하여 선택하자.

<br/>

![image-20211125181932416](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125181932416.png)

##### [대시보드] -> [데이터베이스 생성]

<br/>

![image-20211125182335559](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125182335559.png)

##### [표준 생성] , [MariaDB] 클릭

#### 여기서 잠깐!

왜 마리아 DB를 선택하느냐..

RDS에는 오라클, MSSQL, PostgreSQL등이 있으며, 당연히 본인이 가장 잘 사용하는 데이터베이스를 고르면 되지만, 이 책의 필자는 꼭 다른 데이터베이스를 선택해야 할 이유가 있는 것이 아니라면 MySQL, MariaDB, PostgreSQL중에 고르는것을 추천한다.

그 이유는 다음과 같다.

- ##### 가격

- ##### Amazon Aurora 교체 용이성

RDS의 가격은 라이센스 비용 영향을 받는다. 상용 데이터베이스인 오라클 , MSSQL이 오픈소스인 MySQL, MariaDB, PostgreSQL보다는 동일한 사양 대비 더 가격이 높다. 결국 프리티어 기간인 1년이 지나면 비용을 지불하면서 RDS를 사용해야 한다. 비용 문제를 생각해 볼 필요가 있다.

두 번째로 Amazon Aurora 교체 용이성이다. 오로라는 AWS에서 MySQL과 PostgreSQL을 클라우드 기반에 맞게 재구성한 데이터베이스이다. 공식 자료에 의하면 RDS MySQL 대비 5배, RDS PostgreSQL보다 3배의 성능을 제공한다. 더군다나 AWS에서 직접 엔지니어링하고 있기 때문에 계속해서 발전하고 있다. 현재도 다른 데이터베이스와 비교해 다양한 기능을 제공한다.

클라우드 서비스에 가장 적합한 데이터베이스이기 때문에 많은 회사가 Amazon Aurora를 선택한다. 그러다 보니 호환 대상이 아닌 오라클, MSSQL을 굳이 선택할 필요가 없다. 이렇게 보면 Aurora를 선택하면 가장 좋을 거 같지만, 시작하는 단계에서 Aurora를 선택하기는 어렵다.

프리티어 대상이 아니며, 최저 비용이 월 10만원 이상이기 때문에 부담스럽다.

(차후 서비스 규모가 일정 이상 커진 후에 Maria DB에서 오로라로 이전하면 된다)

<br/>

#### Maria DB

국내외를 가리지 않고 오픈소스 데이터베이스 중 가장 인기 있는 제품을 고르라고 하면 MySQL을 꼽습니다. 단순 **쿼리 처리 성능**이 어떤 제품보다 압도적이며 이미 오래 사용되어 왔기 때문에 성능과 신뢰성 등에서 꾸준히 개선되어 온 것도 장점이다.

Maria DB는 MySQL을 기반으로 만들어졌으며, 그렇기 때문에 쿼리를 비롯한 전반적인 사용법은 MySQL과 유사하니 사용 방법에 대해서는 크게 걱정할 필요가 없다.

비슷한 사용법 외에도 MariaDB는 MySQL대비 다음의 장점이 있다.

- 동일 하드웨어 사양으로 MySQL보다 향상된 성능
- 좀 더 활성화된 커뮤니티
- 다양한 기능
- 다양한 스토리지 엔진

이외에도 [MYSQL에서 MARIADB로 마이그레이션 해야 할 10가지 이유](https://xdhyix.wordpress.com/2016/03/24/mysql-%EC%97%90%EC%84%9C-mariadb-%EB%A1%9C-%EB%A7%88%EC%9D%B4%EA%B7%B8%EB%A0%88%EC%9D%B4%EC%85%98-%ED%95%B4%EC%95%BC%ED%95%A0-10%EA%B0%80%EC%A7%80-%EC%9D%B4%EC%9C%A0/)

<br/>

![image-20211125184531758](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125184531758.png)

##### [프리 티어] 선택

<br/>

![image-20211125184749886](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125184749886.png)

##### 본인만의 DB 인스턴스 이름과 사용자 정보를 등록한다. 여기서 사용된 사용자 정보로 실제 데이터베이스에 접근하게 되니 어딘가에 메모해 놓아도 좋다.

<br/>

![image-20211125184942844](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125184942844.png)

<br/>

![image-20211125185123302](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125185123302.png)

##### 퍼블릭 액세스를 [예]로 변경한다.

<br/>

![image-20211125185437592](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125185437592.png)

##### [초기 데이터베이스 이름]을 지정해주자

<br/>

![image-20211125185227767](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125185227767.png)

##### [데이터베이스 생성]을 클릭하자.

<br/>

##### 데이터 베이스 생성이 다 끝났다면 이제 설정을 해보자

<br/>

<br/>

## RDS 운영환경에 맞는 파라미터 설정하기

RDS를 처음 생성하면 몇 가지 설정을 필수로 해야 한다. 우선 다음 3개의 설정을 차례로 진행해 보자.

- ##### 타임존

- ##### Character Set

- ##### Max Connection

### 타임존 설정

##### 왼쪽 카테고리에서 [파라미터 그룹]탭을 클릭해서 이동한다.

![image-20211125185936499](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125185936499.png)

##### [파라미터 그룹 생성]을 클릭하자.

<br/>

#### 파라미터 그룹 생성

![image-20211125190239081](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125190239081.png)

파라미터 그룹 패밀리는, 방금 생성한 MariaDB와 같은 버전을 맞춰주어야 한다.

<br/>

![image-20211125190600652](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125190600652.png)

생성이 완료되면, 해당 파라미터 그룹을 클릭하여 상세 페이지로 들어가자.

<br/>

![image-20211125190642213](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125190642213.png)

##### [파라미터 편집] 버튼을 클릭한 후, time_zone을 검색하자.

<br/>

![image-20211125190802614](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125190802614.png)

##### Aisa/Seoul 을 선택한다.

<br/>

<br/>

### Character Set 설정

- ##### character_set_client

- ##### character_set_connection

- ##### character_set_database

- ##### character_set_filesystem

- ##### character_set_results

- ##### character_set_server

- ##### collation_connection

- ##### collation_server

##### character 항목들은 모두 utf8md4로, collation 항목들은 utf8md4_general_ci로 변경한다

utf8은 이모지를 저장할 수 없지만, utf8md4는 이모지를 저장할 수 있으므로, 보편적으로 utf8md4을 많이 사용한다.

<br/>

![image-20211125191048110](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125191048110.png)

<br/>

![image-20211125191208978](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125191208978.png)

<br/>

<br/>

### Max Connection 설정

![image-20211125191620249](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125191620249.png)

RDS의 Max Connection은 인스턴스 사양에 따라 자동으로 정해진다. 현재 프리티어 사양으로는 약 60개의 커넥션만 가능해서 좀 더 넉넉한 값으로 지정한다.

##### 모든 설정을 마쳤다면 [변경 사항 저장]버튼을 클릭해 최종 저장한다.

<br/>

<br/>

### 데이터베이스에 연결하기

![image-20211125192410073](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125192410073.png)

##### [데이터베이스] -> [수정]

<br/>

![image-20211125192659094](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125192659094.png)

##### DB 파라티머 그룹을 방금 생성한 신규 파라미터 그룹으로 변경한다.

<br/>

![image-20211125192745535](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125192745535.png)

##### [즉시 적용]을 선택하자

<br/>

<br/>

### 내 PC에서 RDS에 접속해보기

로컬 PC에서 RDS로 접근하기 위해서 RDS의 보안 그룹에 본인 PC의 IP를 추가하겠다.

RDS의 세부정보 페이지에서 [보안 그룹]항목을 클릭한다.

![image-20211125193058824](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125193058824.png)

<br/>

##### RDS의 보안 그룹 정보는 그래도 두고, 브라우저를 새로 열어 보안 그룹 목록 중 EC2에 사용된 보안 그룹의 그룹ID를 복사한다.

![image-20211125193514854](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125193514854.png)



<br/>

![image-20211125193609158](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125193609158.png)

##### [인바운드 규칙]->[인바운드 규칙 편집]

<br/>

![image-20211125194030034](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125194030034.png)

##### 보안 그룹 첫 번째 줄: EC2의 보안 그룹을 추가한다.

##### 보안 그룹 두 번째 줄: 현재 내 PC의 IP를 등록한다

이렇게 하면 EC2와 RDS간에 접근이 가능하다.

<br/>

<br/>

## 데이터베이스 연결

#### 엔드포인트 확인

![image-20211125194643256](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125194643256.png)

##### RDS 정보 페이지에서 엔드 포인트를 확인한다.

<br/>

##### 인텔리제이 좌측 Database -> + -> DataSourse -> MariaDB클릭

![image-20211125195143785](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125195143785.png)

<br/>

![image-20211125195334786](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125195334786.png)

- ##### Host : RDS의 엔드 포인트를 등록한다 

- ##### User, Password : 마스터 사용자 이름과 암호

##### Test Connection을 눌러 성공했다면 [Apply]-> [OK]를 눌러 저장하자.

<br/>

![image-20211125195727611](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125195727611.png)

콘솔로 들어오자.

<br/>

##### SQL 실행하기

> use 웹 콜솔에서 지정한 데이터베이스명;

![image-20211125195929364](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125195929364.png)

<br/>

##### 데이터베이스가 선택된 상태에서 현재의 character_set, collation 설정을 확인

> show variables like 'c%';

![image-20211125200128737](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211125200128737.png)

보면 character_set_database가 latin1로 되어있다. 이 항목은 MariaDB에서만 RDS 파라미터 그룹으로는 변경이 안된다. 그래서 직접 변경한다.

> ALTER DATABASE shinD_SpringBoot_DB
> character set = 'utf8mb4'

<br/>

#### 타임존 확인

> select @@time_zone, now();

<br/>

#### 한글이 잘 들어가는지 확인

> create table test (
>     id bigint(20) not null auto_increment,
>     content varchar(255) default null,
>     primary key (id)
> ) engine =InnoDB;



> insert into test(content) values ('테스트');



> select * from test;

##### 이렇게 해서 RDS에 대한 모든 설정이 끝났다!

이제 이렇게 설정된 RDS가 EC2와 잘 연동되는지 확인해보자.

<br/>

<br/>

## EC2에서 RDS에서 접근 확인

EC2에 접속한다.(putty 사용)

MySQL 접근 테스트를 위해 MySQL CLI를 설치한다.

> sudo yum install mysql

##### 설치가 다 되었으면 RDS에 접속해보자

> mysql -u 계정 -p -h Host주소

나의 경우

##### mysql -u shinD -p -h 엔드포인트

를 입력하면 된다.

<br/>

![image-20211126123546371](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211126123546371.png)

<br/>

우리가 생성했던 shinD_SpringBoot_DB가 있음을 확인했다. 이제 EC2에 스프링 부트를 배포하고 RDS에 접근해보자!

<br/>

<br/>

### 📔 Reference

##### [스프링 부트와 AWS로 혼자 구현하는 웹 서비스] 264P~ 293P
