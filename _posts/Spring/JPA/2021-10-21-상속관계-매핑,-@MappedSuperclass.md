---
title:  "상속관계 매핑, @MappedSuperclass"
excerpt: "상속관계 매핑, @MappedSuperclass"
date:   2021-10-21 18:07:00
header:
  teaser: /assets/images/spring.png

categories: JPA
tags:
  - Java
  - Spring
  - JPA
  - 영속성 컨텍스트
last_modified_at: 2021-10-21T18:07:00


---

<br/>

## 💡 상속관계 매핑

##### 관계형 데이터베이스에는 상속관계가 없다. 그나마 객체의 상속관계랑 비슷한 슈퍼타입, 서브타입 관계라는 모델링 기법이 있다. 

<br/>

#### 🔍상속관계 매핑 

#### => 객체의 상속관계 구조와 DB의 슈퍼타입, 서브타입 관계를 매핑하는 것

<br/>

#### 🔍 상속관계를 매핑하는 방법

- ##### 각각 테이블로 변환 -> 조인 전략

- ##### 통합 테이블로 변환 -> 단일 테이블 전략

- ##### 서브타입 테이블로 변환 -> 구현 클래스마다 테이블 전략

<br/>

<br/>

## 💡조인 전략

#### 🔍@Inheritance(strategy = InheritanceType.JOINED)

##### 부모 속성의 테이블을 만들고, 자식 객체만이 가지는 고유한 특성들로 각각의 테이블을 만들어서 join을 사용해 데이터를 가져온다.

![image-20211021173553741](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211021173553741.png)

<br/>

### 장점 

- ##### 테이블 정규화

- ##### 외래키 참조 무결성 제약조건 활용가능

- ##### 저장공간 효율화

### 단점  

- ##### 조회시 조인을 많이 사용, 성능 저하

- ##### 조회 쿼리가 복잡함

- ##### 데이터 저장시 INSERT SQL 2번 호출

<br/>

### 🔍DTYPE

##### @DiscriminatorColumn(name=“DTYPE”) - 부모 클래스에서 사용

##### @DiscriminatorValue("XXX") - 자식 클래스에서 사용

##### 조인 전략에서는 없어도 되긴 하지만, 있는데 좋다.

##### 아래에서 설명할 싱글 테이블 전략에는 꼭 필요하다

<br/>

<br/>

## 💡단일 테이블 전략

#### 🔍@Inheritance(strategy = InheritanceType.SINGLE_TABLE)

##### 논리 모델은 한 테이블에 모두 몰아넣은 후 DTYPE으로 구분한다.

![image-20211021173732245](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211021173732245.png)

<br/>

### 장점

- 조인이 필요 없으므로 일반적으로 조회 성능이 빠름
- 조회 쿼리가 단순함

### 단점

- 자식 엔티티가 매핑한 컬럼은 모두 null 허용
- 단일 테이블에 모든 것을 저장하므로 테이블이 커질 수 있고, 상황에 따라서 오히려 조회 성능이 느려질 수 있다.

<br/>

<br/>

## 💡 구현 클래스마다 테이블 전략

### 쓰지 말자

<br/>

<br/>

## 💡 @MappedSuperclass

##### 공통 매핑 전보가 필요할 때 사용한다. 예를 들어 모든 클래스가 name이과 id라는 공통 속성을 가지고 있다면 이 둘을 묶어서 공통 속성으로 만든 후, 이를 상속받아 속성만 사용하고 싶을 때 사용한다.

##### 즉 DB는 완전히 다르지만 속성만 상속받아 사용하고 싶을 때 사용한다.

![image-20211021180600907](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211021180600907.png)

##### 위 그림의 예시에서는 BaseEntity 클래스에 @MappedSuperclass를 붙여준 후, Member와 Seller에서 extends BaseEntity를 통해 상속받아 사용하면 된다.

<br/>

#### 🔍 정리

- ##### 상속관계 매핑 X

- ##### 엔티티X, 테이블과 매핑X

- ##### 부모 클래스를 상속 받은 자식 클래스에 매핑 정보만 제공

- ##### 조회, 검색 불가(em.find(BaseEntity)불가)

- ##### 직접 생성해서 사용할 일이 없으므로 추상 클래스 권장

<br/>

<br/>

### 📔 Reference

[인프런 - 자바 ORM 표준 JPA 프로그래밍](https://www.inflearn.com/course/ORM-JPA-Basic/dashboard)