---
title:  "트랜잭션 격리 수준"
excerpt: "트랜잭션 격리 수준과, 발생할 수 있는 문제들 정리"
date:   2021-10-21 09:55:00 
header:
  teaser: /assets/images/spring.png

categories: rdb
tags:
  - DB
  - RDB
  - 트랜잭션
  - isolation level
last_modified_at: 2021-10-21T09:55:00

---

<br/>

## 💡 트랜잭션 격리 수준

##### 트랜잭션 격리 수준(isolation level)이란 동시에 여러 트랜잭션이 처리될 때, 트랜잭션끼리 얼마나 서로 고립되어 있는가를 나타내는 말이다.

##### 쉽게 말하자면 특정 트랜잭션이 다른 트랜잭션이 변경한 데이터를 볼 수 있도록 허용할지 말지를 결정한다.

##### 위에서 살펴본 트랜잭션의 ACID를 지키기 위해, Locking을 통해 트랜잭션이 DB를 다루는 동안 다른 트랜잭션이 관여하지 못하도록 막는 것이 필요하다.

##### 하지만 무조건 Locking으로 수많은 트랜잭션을 순서대로 처리한다면 데이터베이스의 성능은 당연하게도 저하될 것이다.

##### 우선 Lock에 대해 알아보자

<br/>

<br/>

### 💡 Lock

##### Lock이란 트랜잭션 처리의 순차성을 보장하기 위한 방법이다. (동시성 제어)

##### DBMS(데이터베이스 관리 시스템)마다 Lock을 구현하는 방식이 다르기 때문에, DBMS를 효과적으로 이용하기 위해서는 해당 DB의 Lock에 대해서 이해해야 한다.

<br/>

### 🔍 Lock의 종류

#### 🌌공유(Shared) Lock 

- ##### 데이터를 읽을 때 사용하는 Lock이다. 공유Lock은 공유Lock끼리 동시에 접근이 가능하다.  즉 하나의 데이터를 읽는 것은 여러 사용자가 동시에 할 수 있다는 것이다.

- ##### 공유Lock 이 설정된 데이터에 배타 락을 사용할 수 없다.

<br/>

#### 🌌배타(Exclusive) Lock 

- #####  데이터를 변경하고자 할 때 사용되며, 트랜잭션이 완료될 때까지 유지된다.

- #####  베타Lock이 해제될 때 까지 다른 트랜잭션(읽기 포함)은 해당 리소스에 접근할 수 없다.

- #####  해당 Lock은 다른 트랜잭션이 수행되고 있는 데이터에 대해서는 접근하여 함께 Lock을 설정할 수 없다.

<br/>

<br/>

## 💡 격리성(Isolation)으로 인해 나타날 수 있는 문제점

##### 격리성으로 인해 나타날 수 있는 문제점은 일반적으로 Dirty Read, Non-Repeatable Read, Phantom Read 가 있다.

<br/>

### **🌌Dirty Read** 

**Dirty Read는 다른 트랜잭션에 의해 수정됐지만 아직 커밋되지 않은 데이터를 읽는 것**을 말한다. 

##### 🔍 예시

> 1. #####  A 트랜잭션에서 10번 사원의 나이를 27살에서 28살로 변경함
>
> 2. #####  해당 데이터는 커밋되지 않았기 때문에 저장되지 않은 상태
>
> 3. #####  B 트랜잭션에서 10번 사원의 나이를 조회함
>
> 4. #####  28살이 조회됨
>
>    - ##### 이를 Dirty Read 라고 한다(수정되었으나 커밋되지 않은 데이터를 읽음)
>
> 5. #####  A 트랜잭션에서 문제가 발생하여 롤백함
>
> 6. #####  A 트랜잭션에서 롤백되었기 때문에 10번 사원의 나이는 27살이나, B 트랜잭션에서는 28살이라고 생각하고 로직을 수행함.

<br/>

### **🌌Non-Repeatable Read**

**한 트랜잭션 내에서 같은 Key를 가진 Row를 두 번 읽었는데 그 사이에 값이 변경되거나 삭제되어 결과가 다르게 나타나는 현상**을 말한다.

##### 🔍 예시

> 1. #####  B 트랜잭션에서 10번 사원의 나이를 조회 : 27살이 조회됨
>
> 2. #####  A 트랜잭션에서 10번 사원의 나이를 27살에서 28살로 바꾸고 커밋
>
> 3. #####  B 트랜잭션에서 10번 사원의 나이를 조회함 : 28살이 조회됨

<br/>

### **🌌Phantom Read**

**한 트랜잭션 내에서 같은 쿼리를 두 번 수행했는데, 첫 번째 쿼리에서 없던 유령(Phantom) 레코드가 두 번째 쿼리에서 나타나는 현상**을 말합니다.

##### Non-Repeatable Read와 헷갈릴 수 있는데, Non-Repeatable Read는 1개의 Row의 데이터의 값이 변경되는 것이며, Phantom Read는 여러 Row의 데이터를 조회하였을 때, Row의 수가 바뀌는 것이다.

##### 🔍 예시

> 1. #####  B 트랜잭션에서 나이가 27살인 회원을 모두 조회 : 10번 사원 한명이 나옴.
>
> 2. #####  A 트랜잭션에서 나이가 27살인 22번 사원을 추가하여 커밋
>
> 3. #####  B 트랜잭션에서 나이가 27살인 회원을 모두 조회 : 10번 사원과 22번 사원 2명이 나옴

<br/>





### 💡 트랜잭션 격리 수준 (ISOLATION LEVEL)

### **🌌 LV.0 : Read Uncommitted**

##### 트랜잭션에서 처리중인 커밋되지 않은 데이터를 다른 트랜잭션이 읽는 것을 허용한다.

##### 해당 수준에서는 Dirty Read, Non-Repeatable Read, Phantom Read 문제가 발생할 수 있다.

##### Read Uncommitted는 데이터베이스의 일관성을 유지하는 것이 불가능하다.

<br/>

### **🌌 LV.1 : Read Committed**

##### 트랜잭션이 커밋되어 확정된 데이터만 다른 트랜잭션이 읽도록 허용한다

##### 커밋 되지 않은 데이터에 대해서는 실제 DB 데이터가 아닌 Undo 로그에 있는 이전 데이터를 가져온다.

##### 해당 수준에서는 Non-Repeatable Read, Phantom Read 문제가 발생할 수 있다.

##### Oracle DB에서 기본으로 사용하는 Isolation Level이다.

<br/>

### **🌌 LV.2 : Repeatable Read**

##### 트랜잭션 내에서 삭제, 변경에 대해서 Undo 로그에 넣어두고 앞서 발생한 트랜잭션에 대해서는 실제 데이터가 아닌 Undo 로그에 있는 백업 데이터를 읽게 한다.

##### 이렇게 함으로써 트랜잭션 중 값의 변경에 대해서 일정한 값으로 처리할 수 있다.

즉 Non-Reapeatable Read를 해소할 수 있다.

> 1. ##### B 트랜잭션이 10번 사원의 나이를 조회 : 27살이 조회됨
>
> 2. ##### A 트랜잭션이 10번 사원의 나이를 28살로 바꾸고 커밋
>
> 3. ##### B 트랜잭션이 10번 사원의 나이를 다시 조회 : undo 영역에 백업된 데이터(27살) 반환

##### 즉, 자신의 트랜잭션 번호보다 낮은 트랜잭션 번호에서 변경(커밋)된 데이터만 볼 수 있다.

##### 해당 수준에서는 Phantom Read, UPDATE 부정합 문제가 발생할 수 있다.

##### MySQL에서 기본으로 사용하는 Isolation Level이다.

<br/>

### **🌌 LV.3 : Serializable Read**

트랜잭션이 완료될 때까지 SELECT 문장이 사용되는 모든 데이터에 Shared Lock이 걸린다.

가장 엄격한 격리 수준으로 완벽한 읽기 일관성 모드를 제공한다.

<br/>

<br/>

### 📔 Reference

[https://dar0m.tistory.com/225](https://dar0m.tistory.com/225)

[https://sabarada.tistory.com/117](https://sabarada.tistory.com/117)

[https://joont92.github.io/db/%ED%8A%B8%EB%9E%9C%EC%9E%AD%EC%85%98-%EA%B2%A9%EB%A6%AC-%EC%88%98%EC%A4%80-isolation-level/](https://joont92.github.io/db/%ED%8A%B8%EB%9E%9C%EC%9E%AD%EC%85%98-%EA%B2%A9%EB%A6%AC-%EC%88%98%EC%A4%80-isolation-level/)

[https://www.infoq.com/articles/Isolation-Levels/](https://www.infoq.com/articles/Isolation-Levels/)

[https://itpenote.tistory.com/616](https://itpenote.tistory.com/616)

[https://augustines.tistory.com/68](https://augustines.tistory.com/68)