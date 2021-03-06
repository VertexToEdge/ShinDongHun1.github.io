---
title:  "Aggregate Root"
excerpt: "DDDμ Aggregate Root"
date:   2021-10-22 20:07:00
header:
  teaser: /assets/images/spring.png

categories: rdb
tags:
  - λλ©μΈ
  - DDD
  - Aggregate Root

last_modified_at: 2021-10-22T20:07:00

---

<br/>

## π‘ Domain

##### λλ©μΈμ μ¬μ μ  μλ―Έλ "μμ­", "μ§ν©"μ΄λ€.

##### λΉμ¦λμ€μμλ ν΄κ²°νκ³ μ νλ λ¬Έμ  μμ­ νΉμ μ μ¬ν μλ¬΄μ μ§ν©μ λλ©μΈμ΄λΌ λΆλ₯Έλ€.

##### μλ₯Ό λ€μ΄ κ²μν μλΉμ€λ₯Ό κ΅¬ννκ³ μ νλ κ²½μ°μλ κ²μνμ΄ λλ©μΈμ΄ λλ€.

##### λλ©μΈμ νμ λλ©μΈμΌλ‘ λλ  μ μλλ°, κ²μν λλ©μΈμ κ²μκΈ, λκΈ λ±μ νμ λλ©μΈμΌλ‘ λλλ€.

<br/>

<br/>

## π‘ λλ©μΈ λͺ¨λΈ

##### λλ©μΈμ κ°λμ μΌλ‘ ννν κ².

##### λλ©μΈμ κ°λμ μΌλ‘ νννλ λ°©λ²μ λ€μνλ€. μλ₯Ό λ€μ΄  UML(ν΄λμ€/μν λ€μ΄μ΄κ·Έλ¨), κ·Έλν, μν κ³΅μ λ±μ΄ λλ©μΈ λͺ¨λΈμ΄ λ  μ μλ€.

<br/>

<br/>

## π‘ λλ©μΈ λͺ¨λΈ ν¨ν΄

##### λλ©μΈ κ³μΈ΅(Domain Layer)μ μ ν μ€ νλ.

##### κ°λ¨νκ² λ§νμλ©΄, λ°μ΄ν°μ λ°μ΄ν°μ νμκ° ν¨κ» κ°μ²΄λ₯Ό μ΄λ£¨λ ννμ΄λ€.

##### λλ©μΈ λͺ¨λΈ ν¨ν΄μ κ°μ²΄μ§ν₯ μμλ€μ λ μ κ·Ήμ μΌλ‘ νμ©νμ¬, λ€μκ³Ό κ°μ μ΄μ λ€μ μ κ³΅νλ€.

- ##### μ€κ³μ μ΄ν΄κ° μ¬μμ§λ€

- ##### μ€κ³λ₯Ό κ΄λ¦¬νκΈ° μ¬μμ§λ€

- ##### νμ€νΈνκΈ° μ¬μμ§λ€

- ##### Design Pattern λ±μ λμμ λ°μ μ μλ€.

<br/>

##### λλ©μΈ λͺ¨λΈ ν¨ν΄μ κ²°κ΅­ μν€νμ²μμ λλ©μΈ κ³μΈ΅(Domain Layer)μ κ°μ²΄ μ§ν₯ κΈ°λ²μΌλ‘ κ΅¬ννλ ν¨ν΄μ΄λ€.

<br/>

<br/>

## π‘ μν€νμ³ ν¨ν΄ - κ³μΈ΅ν ν¨ν΄(Layered pattern)

##### μ΄ ν¨ν΄μ **n-ν°μ΄ μν€νμ³ ν¨ν΄**μ΄λΌκ³ λ λΆλ¦°λ€. 

##### μ΄λ νμ λͺ¨λλ€μ κ·Έλ£ΉμΌλ‘ λλ μ μλ κ΅¬μ‘°νλ νλ‘κ·Έλ¨μμ μ¬μ©ν  μ μλ€. 

##### κ° νμ λͺ¨λλ€μ νΉμ ν μμ€μ μΆμνλ₯Ό μ κ³΅νλ€. 

##### κ° κ³μΈ΅μ λ€μ μμ κ³μΈ΅μ μλΉμ€λ₯Ό μ κ³΅νλ€.

<br/>

##### μΌλ°μ μΈ μ λ³΄ μμ€νμμ κ³΅ν΅μ μΌλ‘ λ³Ό μ μλ κ³μΈ΅ 4κ°μ§λ λ€μκ³Ό κ°λ€.

- ##### **νλ μ  νμ΄μ κ³μΈ΅** (Presentation layer) - **UI κ³μΈ΅** (UI layer) μ΄λΌκ³ λ ν¨

  - ##### μ¬μ©μμ μμ²­μ λ°μ μ νλ¦¬μΌμ΄μ κ³μΈ΅μ μ λ¬νκ³ , κ·Έ κ²°κ³Όλ₯Ό μ¬μ©μμκ² λ³΄μ¬μ€λ€.

- ##### **μ νλ¦¬μΌμ΄μ κ³μΈ΅** (Application layer) - **μλΉμ€ κ³μΈ΅** (Service layer) μ΄λΌκ³ λ ν¨

  - ##### μ¬μ©μκ° μμ²­ν κΈ°λ₯μ μ€ννλ€. λ‘μ§μ μ§μ  κ΅¬ννλ κ²μ΄ μλλΌ, λλ©μΈ κ³μΈ΅μ μ‘°ν©ν΄μ κΈ°λ₯μ μ€ννλ€.

- ##### **λΉμ¦λμ€ λΌλ¦¬ κ³μΈ΅** (Business logic layer) - **λλ©μΈ κ³μΈ΅** (Domain layer) μ΄λΌκ³ λ ν¨

  - ##### μμ€νμ΄ μ κ³΅ν  λλ©μΈμ κ·μΉ, ν΅μ¬ λ‘μ§μ κ΅¬ννλ€.

- ##### **λ°μ΄ν° μ κ·Ό κ³μΈ΅** (Data access layer) - **μμ κ³μΈ΅** (Persistence layer) μ΄λΌκ³ λ ν¨

  - ##### DBλ λ©μμ§ μμ€νκ³Ό κ°μ μΈλΆ μμ€νκ³Όμ μ°λμ μ²λ¦¬νλ€.



![img](https://miro.medium.com/max/700/1*9y2cUynZoq1KbarwlzEW9w.png)

<br/>

<br/>

## π‘ DDD (Domain Driven Design)

##### DDD(λλ©μΈ μ£Όλ μ€κ³)λ λλ©μΈ μ λ¬Έκ°μ κ°λ°μκ° βλλ©μΈμ μ΄ν΄βλ₯Ό λͺ©μ μΌλ‘ λ§λ€μ΄λΌ μ μλ μ λΉμΏΌν°μ€ μΈμ΄, λλ©μΈ λͺ¨λΈ(κ°λμ μΈ κ·Έλ¦Ό/κ·Έλν)μ κΈ°λ°μΌλ‘ νλ μ€κ³ λ°©μμ μλ―Ένλ€.

> ##### μ°Έκ³  : Domain Modelμ μ΄ν΄λ₯Ό μν κ°λμ  λͺ¨λΈμ΄λ©°, Domain Model Patternμ λλ©μΈ λ μ΄μ΄μ βκ°μ²΄μ§ν₯μ  κ΅¬νβμ μλ―Έν©λλ€. λ μ©μ΄κ° μ¬μ©λλ λ§₯λ½μ΄ λ€λ¦λλ€.

##### μ΄ λλ©μΈ μ£Όλ μ€κ³λ λλ©μΈ λ μ΄μ΄λ₯Ό κ΅¬νν  λ μ€μν μ§μΉ¨μΌλ‘ νμ©λ  μ μλ€.

<br/>

##### spring κ°λ°μ νμλ€λ©΄, Entity/Repository/Service λ±μ΄ μ€μ λ‘λ DDDμμ λΉλ‘―ν annotationλ€μ΄κΈ° λλ¬Έμ, μ΄λμ λλ DDDλ₯Ό ν΄μ¨ μμ΄λ€.

<br/>

<br/>

## π‘  Aggregate Root

##### Aggregateμ μ€μ¬ κ°μ²΄

<br/>

### Aggregateλ?

##### λ°μ΄ν° λ³κ²½μ λ¨μλ‘ λ€λ£¨λ μ°κ΄ κ°μ²΄μ λ¬Άμ

##### μ΄λ¬ν μ°κ΄ κ°μ²΄μ λ¬Άμμ AggregateλΌκ³  νλ€,

##### μλ₯Ό λ€λ©΄, μ£Όλ¬Έμ΄λΌλ Entityμ μ£Όλ¬ΈμλΌλ Value Objectλ€μ΄ κ²°ν©νμ¬ μ£Όλ¬Έ Aggregateλ₯Ό λ§λ€ μ μλ€.

<br/>

##### Aggregateμλ Aggregate RootλΌλ μ€μ¬ κ°μ²΄κ° μ‘΄μ¬νλλ°, μμ μμμμλ μ£Όλ¬Έ Entityκ° Aggregate Rootμ΄λ€.

##### μ¬λ¬ μν°ν°λ₯Ό λ¬Άμ΄μ κ°μ Έμ€λ κ²½μ°κ° λ§μ λ κ°λ°μμ Aggregate Rootμ ν΄λΉλλ Entityμ λν΄μλ§ Repositoryλ₯Ό λ§λλ κ²½μ°κ° λ§λ€.

#### <br/>

### μμμ± μ μ΄μμ κ΄κ³?

##### μ€νλ§μμ κ³΅λΆνλ CascadeType.ALL + orphanRemoval = true  μ΄ μ΅μλ€μ΄ Aggregate Rootλ₯Ό κ΅¬νν  λ μ μ©ν κ²μ, λΆλͺ¨μ μμ κ΄κ³μμ λΆλͺ¨κ° Aggregate Rootκ° λκ³  λΆλͺ¨ λ ν¬μ§ν λ¦¬λ§ λ§λ€μ΄μ κ°λ°ν  μ μλλ‘ λ§λ€μ΄ μ£ΌκΈ° λλ¬Έμ΄λ€.

<br/>

<br/>

<br/>

### π Reference

[Layered Architecture](https://herbertograca.com/2017/08/03/layered-architecture/)

[10κ°μ§ μν€νμ² ν¨ν΄ μμ½](https://mingrammer.com/translation-10-common-software-architectural-patterns-in-a-nutshell/)

[λλ©μΈ μ£Όλ μ€κ³(DDD-Domain Driven Design) - λλ©μΈ λͺ¨λΈ](https://gnidoc.tistory.com/entry/%EB%8F%84%EB%A9%94%EC%9D%B8-%EC%A3%BC%EB%8F%84-%EC%84%A4%EA%B3%84DDD-Domain-Driven-Design-%EB%8F%84%EB%A9%94%EC%9D%B8-%EB%AA%A8%EB%8D%B8)

[DDD μμνκΈ°](https://sgc109.github.io/2020/08/09/ddd-basic/)

[Spring μ½λμ ν¨κ» λ³΄λ λ°±μλ μλ² μν€νμ² β μλ¦¬μ¦ μκ°, κΈ°λ³Έ κ΅¬μ‘°](https://tech.junhabaek.net/spring-boot-%EC%BD%94%EB%93%9C%EC%99%80-%ED%95%A8%EA%BB%98-%EB%B3%B4%EB%8A%94-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%84%9C%EB%B2%84-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98-%EC%8B%9C%EB%A6%AC%EC%A6%88-%EC%86%8C%EA%B0%9C-%EA%B8%B0%EB%B3%B8-%EA%B5%AC%EC%A1%B0-bbf814e1b4e3)

[λ°±μλ μλ² μν€νμ² β Domain Layer1. Domain Layerμ DDD](https://tech.junhabaek.net/%EB%B0%B1%EC%97%94%EB%93%9C-%EC%84%9C%EB%B2%84-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98-domain-layer1-domain-layer%EC%99%80-ddd-e97a7587a7b0)

[λ°±μλ μλ² μν€νμ² β Application Layer 1. κ°μμ κΈ°λ³Έ Variation](https://tech.junhabaek.net/%EB%B0%B1%EC%97%94%EB%93%9C-%EC%84%9C%EB%B2%84-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98-application-layer-1-%EA%B0%9C%EC%9A%94%EC%99%80-%EA%B8%B0%EB%B3%B8-variation-9fac801ddba8)

[DDD, Aggregate Root λ?](https://eocoding.tistory.com/36)

[DDD ν΅μ¬λ§ λΉ λ₯΄κ² μ΄ν΄νκΈ°](https://happycloud-lee.tistory.com/94)

[DDD Aggregate Pattern](https://www.secmem.org/blog/2020/02/19/ddd-aggregate-pattern/)