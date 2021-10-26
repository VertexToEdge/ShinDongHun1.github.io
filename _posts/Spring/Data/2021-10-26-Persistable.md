---
title:  "Persistable"
excerpt: "새로운 엔티티를 구별하는 방법"
date:   2021-10-26 09:30:00
header:
  teaser: /assets/images/spring.png

categories: DATA
tags:
  - Java
  - Spring
  - JPA
  - DATA JPA
last_modified_at: 2021-10-26T09:30:00



---

<br/>

## 💡 새로운 엔티티를 판단하는 기본 전략

- ##### 식별자가 객체일 때 null 로 판단 

- ##### 식별자가 자바 기본 타입일 때 0 으로 판단 

- ##### Persistable 인터페이스를 구현해서 판단 로직 변경 가능

<br/>

#### 🐹 Persistable  인터페이스 구현

```java
@Entity
@EntityListeners(AuditingEntityListener.class)
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Item implements Persistable<String> {
    
	@Id
	private String id;
    
	@CreatedDate
	private LocalDateTime createdDate;
		public Item(String id) {
		this.id = id;
	}
	@Override
	public String getId() {
		return id;
	}
	@Override
	public boolean isNew() {
		return createdDate == null;
	}
}
```

<br/>

<br/>

### 📔 Reference

[인프런 - 실전! 스프링 데이터 JPA](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EB%8D%B0%EC%9D%B4%ED%84%B0-JPA-%EC%8B%A4%EC%A0%84/dashboard)

