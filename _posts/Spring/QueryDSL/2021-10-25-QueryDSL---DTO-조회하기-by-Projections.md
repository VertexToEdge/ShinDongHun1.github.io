---
title:  "DTO 조회하기 by Projections"
excerpt: "Projections 를 사용한 DTO 조회"
date:   2021-10-25 00:30:00
header:
  teaser: /assets/images/spring.png

categories: QueryDSL
tags:
  - Java
  - Spring
  - JPA
  - QueryDSL
  - Projections
last_modified_at: 2021-10-25T00:30:00

---

<br/>

## 💡 쿼리 DSL - DTO로 조회하기

### com.querydsl.core.types.Projections 사용

<br/>

```java
@Data
@AllArgsConstructor
public class OrderDto {
    private Long orderId;
    private String name;
    private LocalDateTime localDateTime;
    private OrderStatus orderStatus;
    private Address address;

}
```

<br/>

##### Projections 사용

```java
public List<OrderDto> searchDTO(OrderSearch orderSearch) {

    query = new JPAQueryFactory(em);


    return query
            .select(
                    Projections.constructor(OrderDto.class,
                    o.id,
                    o.member.name,
                    o.orderDate,
                    o.orderStatus,
                    o.delivery.address))
            .from(o)
            .where(

                    eqStatus(orderSearch.getOrderStatus()),
                    eqName(orderSearch.getMemberName())
            )
            .fetch();

}
```

<br/>

### 주의

##### 생성자가 존재해야하며, 상성자의 매개변수의 순서와 동일한 순서로 값을 넣어주어야 한다!