---
title:  "EC2 서버에 스프링 부트 프로젝트 배포하기"
excerpt: "스프링 부트와 AWS로 혼자 구현하는 웹 서비스 7"
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

## EC2에 프로젝트 clone 받기

먼저 깃허브에서 코드를 받아올 수 있게 EC2에 깃을 설치하자.

EC2로 접근해서 다음과 같이 명령어를 입력한다

> sudo yum install git

설치가 완료되면 다음 명령어로 설치 상태를 확인한다

> git --version

깃이 성공적으로 설치되면 git clone으로 프로젝트를 저장할 디렉토리를 생성하자.

> mkdir ~/app && mkdir ~/app/step1

생성된 디렉토리로 이동

> cd ~/app/step1

본인의 깃허브 웹페이지에서 https 주소를 복사하자.

![image-20211126130213856](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211126130213856.png)

주소를 복사한 이후에 git clone을 진행하자

> git clone 복사한 주소

git clone이 끝났으면 클론된 프로젝트로 이동해서 파일들이 잘 복사되었는지 확인하자.

> cd 프로젝트명   (나의 경우 cd purplebook)
>
> ll

![image-20211126130425737](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211126130425737.png)

<br/>

코드들이 잘 수행되는지 테스트해보자

> ./gradlew test

만약 다음과 같은 오류가 뜬다면

![image-20211126130608565](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211126130608565.png)



> chmod +x gradlew

해당 명령어를 실행해주면 된다.

![image-20211126131126373](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211126131126373.png)

<br/>

##### 이제 이 프로젝트의 테스트, 빌드, 실행을 진행하자.

(참고로 EC2에는 그레이들을 설치하지 않았으나, Gradle Task를 수행할 수 있다. 이는 프로젝트 내부에 포함된 gradlew 파일 때문이다. 그레이들이 설치되지 않은 환경 혹은 버전이 다른 상황에서도 해당 프로젝트에 한해서 그레이들을 쓸 수 있도록 지원하는 Wrapper 파일이다.)

<br/>

<br/>

## 배포 스크립트 만들기

작성한 코드를 실제 서버에 반영하는 것을 배포라고 한다. 이 책에서 배포라 하면 다음의 과정을 모두 포괄하는 의미라고 보면 된다.

- git clone 혹은 git pull을 통해 새 버전의 프로젝트를 받음
- Gradle이나 Maven을 통해 프로젝트 테스트와 빌드
- EC2 서버에서 해당 프로젝트 실행 및 재실행

앞선 과정을 배포할 때마다 개발자가 하나하나 명령어를 실행하는 것은 불편함이 많아. 

##### 그래서 이를 쉘 스크립트로 작성해 스크립트만 실행하면 앞의 과정이 차례로 진행되도록 하겠다.

참고로 쉘 스크립트와 빔(Vim)은 서로 다른 역할을 한다. 쉘 스크립트는 .sh라는 파일 확장자를 가진 파일이다. 리눅스에서 기본적으로 사용할 수 있는 스크립트 파일의 한종류이다.

빔은 리눅스 환경과 같이 GUI가 아닌 환경에서도 사용할 수 있는 편집 도구이다.

##### 이제 편집을 진행하자.

<br/>

##### ~/app/step1에 deply.sh 파일을 하나 생성하자

> vim ~/app/step1/deploy.sh

##### 다음 코드를 추가하자

> #!/bin/bash
>
> 
>
> REPOSITORY=/home/ec2-user/app/step1
>
> PROJECT_NAME=purplebook
>
> 
>
> cd $REPOSITORY/$PROJECT_NAME/
>
>  
>
> echo "> Git Pull"
>
>  
>
> git pull
>
>  
>
> echo "> 프로젝트 Build 시작"
>
> 
>
> ./gradlew build 
>
> 
>
> echo ">step1 디렉토리로 이동" 
>
> 
>
> cd $REPOSITORY
>
>  
>
> echo "> Build 파일 복사"
>
>  
>
> cp $REPOSITORY/$PROJECT_NAME/build/libs/*.jar $REPOSITORY/
>
> 
>
> echo "> 현재 구동중인 애플리케이션 pid 확인"
>
> 
>
> CURRENT_PID=$(pgrep -f ${PROJECT_NAME}.*.jar)
>
> 
>
> echo "> 현재 구동중인 애플리케이션 pid: $CURRENT_PID"
>
> 
>
> if [ -z "$CURRENT_PID" ];then 
>
> ​	echo "> 현재 구동중인 애플리케이션이 없으므로 종료하지 않습니다."
>
> else
>
> ​	echo "> kill -15 $CURRENT_PID"
>
> ​	kill -15 $CURRENT_PID
>
> ​	sleep 5
>
> fi
>
> 
>
> echo "> 새 애플리케이션 배포"
>
>  
>
> JAR_NAME=$(ls -tr $REPOSITORY/ |grep jar | tail -n 1)
>
>  
>
> echo "> JAR Name: $JAR_NAME"
>
>  
>
> nohup java -jar $REPOSITORY/$JAR_NAME 2>&1 &

<br/>

ESC를 눌러 입력모드 종료 후 :wq 로 저장하자.

##### 이렇게 생성한 스크립트에 실행 권한을 추가하자

> chmod +x ./deploy.sh

<br/>

##### 이제 이 스크립트를 다음 명령어로 실행한다.

> ./deploy.sh

![image-20211126135806215](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211126135806215.png)

<br/>

##### 잘 실행되었으니 nohup.out 파일을 열어 로그를 보자. nohub.out은 실행되는 애플리케이션에서 출력되는 모든 내용을 갖고 있다.

> vim nohup.out

![image-20211126140226474](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211126140226474.png)

##### 왜 위와같은 오류가 떴을까?

<br/>

<br/>

## 외부 Security 파일 등록하기

이유는 다음과 같다. ClientRegistrationRepository를 생성하려면 clientId와 clientSecret이 필수이다. 로컬 PC에서 실행할 때는 application.oauth.properties가 있어 문제가 없었다.

##### 하지만 이 파일은 .gitignore로 git에서 제외 대상이라 깃허브에는 올라가지 않는다.

##### 애플리케이션을 실행하기 위해 공개된 저장소에 ClientId와 ClientSecret을 올릴 수는 없으니 서버에서 직접 이 설정들을 가지고 있게 하자

<br/>

##### 먼저 step1이 아닌 app 디렉토리에 properties 파일을 생성한다.

> ##### vim /home/ec2-user/app/application-oauth.properties

<br/>

그리고 로컬에 있는 application.oauth.properties파일을 그대로 붙여넣기한다.

해당 파일을 저장하고 종료한다(:wq)

그리고 방금 생성한 application.oauth.properties을 쓰도록 deploy.sh 파일을 수정한다.

<br/>

> vim ~/app/step1/deploy.sh

<br/>

> nohup java -jar \
>
> ​	-Dspring.config.location=classpath:/application.properties,/home/ec2user/app/application-oauth.properties \
>
> ​	$REPOSITORY/$JAR_NAME 2>&1 &

<br/>

![image-20211126142954985](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211126142954985.png)

<br/>

<br/>

그리고 다시 실행시켜보면 잘 작동한다.!

![image-20211126143230498](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211126143230498.png)

<br/>

<br/>

## RDS에 연결하자

RDS로는 MariaDB를 사용중이다. 이 MariaDB에서 스프링부트 프로젝트를 실행하기 위해선 몇 가지 작업이 필요하다. 진행할 작업은 다음과 같다.

- 테이블 생성
- 프로젝트 설정
- EC2 (리눅스 서버)설정: 데이터베이스의 접속 정보는 중요하게 보호해야 할 정보이다. 공개되면 외부에서 데이터를 모두 가져갈 수 있기 때문이다. 프로젝트 안에 접속 정보를 갖고 있다면 깃허브와 같이 오픈된 공간에선 누구나 해킬할 위험이 있다. EC2 서버 내부에서 접속 정보를 관리하도록 설정하자.

<br/>

<br/>

### RDS 테이블 생성

```
create table posts (
posts_id bigint not null auto_increment, 
created_date datetime, 
modified_date datetime, 
author varchar(255), 
content TEXT not null, 
title varchar(500) not null, 
primary key (posts_id)
)

create table user (
user_id bigint not null auto_increment, 
created_date datetime,
modified_date datetime,
email varchar(255),
name varchar(255),
picture varchar(255),
role varchar(255) not null,
username varchar(255),
primary key (user_id)
)




CREATE TABLE SPRING_SESSION (
	PRIMARY_ID CHAR(36) NOT NULL,
	SESSION_ID CHAR(36) NOT NULL,
	CREATION_TIME BIGINT NOT NULL,
	LAST_ACCESS_TIME BIGINT NOT NULL,
	MAX_INACTIVE_INTERVAL INT NOT NULL,
	EXPIRY_TIME BIGINT NOT NULL,
	PRINCIPAL_NAME VARCHAR(100),
	CONSTRAINT SPRING_SESSION_PK PRIMARY KEY (PRIMARY_ID)
) ENGINE=InnoDB ROW_FORMAT=DYNAMIC;

CREATE UNIQUE INDEX SPRING_SESSION_IX1 ON SPRING_SESSION (SESSION_ID);
CREATE INDEX SPRING_SESSION_IX2 ON SPRING_SESSION (EXPIRY_TIME);
CREATE INDEX SPRING_SESSION_IX3 ON SPRING_SESSION (PRINCIPAL_NAME);

CREATE TABLE SPRING_SESSION_ATTRIBUTES (
	SESSION_PRIMARY_ID CHAR(36) NOT NULL,
	ATTRIBUTE_NAME VARCHAR(200) NOT NULL,
	ATTRIBUTE_BYTES BLOB NOT NULL,
	CONSTRAINT SPRING_SESSION_ATTRIBUTES_PK PRIMARY KEY (SESSION_PRIMARY_ID, ATTRIBUTE_NAME),
	CONSTRAINT SPRING_SESSION_ATTRIBUTES_FK FOREIGN KEY (SESSION_PRIMARY_ID) REFERENCES SPRING_SESSION(PRIMARY_ID) ON DELETE CASCADE
) ENGINE=InnoDB ROW_FORMAT=DYNAMIC;



```

위 코드를 사용해 차례대로 테이블을 생성해주자.

![image-20211128200223175](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211128200223175.png)

이곳에 입력해주면 된다.

<br/>

<br/>

### 프로젝트 설정

마리아DB 드라이버를 build.gradle에 등록하자

```java
implementation 'org.mariadb.jdbc:mariadb-java-client'
```

<br/>

그리고 서버에서 구동될 환경을 하나 추가하자. scr/main/resources에 application-real.properties 파일을 추가하자.

이는 profile=real인 환경을 구성하는 것이며, 실제 운영될 환경이기 때문에, 보안/로그상 이슈가 될 만한 설정들을 모두 제거하며 RDS환경 profile 설정을 추가한다.

```properties
spring.profiles.include=oauth, real-db
spring.jap.properties.hibernate.dialect=org.hibernate.dialect.MariaDB10Dialect
spring.session.store-type=jdbc
```

모든 설정이 되었다면 깃허브로 푸쉬하자.

<br/>

<br/>

### EC2 설정

OAuth와 마찬가리조 RDS 접속 정보도 보호해야 할 정보이니 EC2서버에 직접 설정 파일을 둔다.

app 디렉토리에 application-real-db.properties 파일을 생성한다.

> vim ~/app/application-real-db.properties

다음과 같은 내용을 추가한다

> spring.jpa.hibernate.ddl.auto=none
>
> spring.datasource.url=jdbc:mariadb://3306/shinD_SpringBoot_DB
>
> spring.datasource.username=shinD
>
> spring.datasource.password=tlsehdgns2
>
> spring.datasource.driver-class-name=org.mariadb.jdbc.Driver

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

### 📔 Reference

##### [스프링 부트와 AWS로 혼자 구현하는 웹 서비스] 264P~ 293P