---
title:  "데이터베이스 방언 설정"
excerpt: "JPA사용할 때 데이터베이스 방언 설정하기"
date:   2021-10-21 13:07:00
header:
  teaser: /assets/images/spring.png

categories: setting
tags:
  - Spring
  - JPA
last_modified_at: 2021-10-21T13:07:00

---

<br/><br/>

## 🌌 데이터베이스 방언 설정

### 💻 application.properties

```properties
spring.jpa.hibernate.database-platform=org.hibernate.dialect.MariaDB103Dialect
```

- H2 : org.hibernate.dialect.H2Dialect
- Oracle 10g : org.hibernate.dialect.Oracle10gDialect
- MySQL : org.hibernate.dialect.MySQL5InnoDBDialect

<br/>

<br/>

## 🌌 데이터베이스 스키마 자동 생성

JPA는 매핑정보만 보고 어떤 테이블을 만들어야 할 지 알 수 있다. 따라서 JPA에서는 애플리케이션 로딩 시점에 데이터베이스 테이블을 생성해주는 기능을 지원해준다(운영에서는 사용하지 말 것)

데이터베이스 방언을 활용해서, 데이터베이스에 맞는 적절한 DDL을 생성해준다.

운영서버에서는 사용하지 않거나, 적절히 다듬은 후 사용할 것을 추천한다.

#### 💻application.properties

```properties
spring.jpa.hibernate.ddl-auto=create
```

#### 옵션

- create : 기존테이블 삭제 후 다시 생성
- create-drop : create와 같으나 종료시점에 테이블  DROP
- update : 변경분만 반영(운영 DB에서 사용 금지)
- validate : 엔티티와 테이블이 정상 매핑되었는지만 확인
- none : 사용하지 않음 