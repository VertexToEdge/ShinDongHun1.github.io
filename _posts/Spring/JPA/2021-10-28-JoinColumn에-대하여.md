---
title:  "JoinColumn에 대하여"
excerpt: "중복 컬럼 설정, Repeated column in mapping for entity에러 등에 관하여"
date:   2021-10-28 05:07:00
header:
  teaser: /assets/images/spring.png

categories: JPA
tags:
  - Java
  - Spring
  - JPA
  - JoinColumn
last_modified_at: 2021-10-28T05:07:00


---

<br/>

<br/>

## 💡 JoinColumn에 대해서

나는 지금까지 joinColumn(name="xxx") 에 대해서, "이름이 xxx인 컬럼을 찾아서 매핑하겠다" 라는 의미로 알고있었다.

##### 즉 joinColumn의 name 설정의 값과, 매핑되는 테이블의 PK 컬럼명이 반드시 일치해야 한다고 생각했었다.

##### 하지만 아니었다.

##### <span style="color:orange">JoinColumn은 어노테이션이 붙은 필드의 엔티티를 추적해서, 그 엔티티의 PK를 찾아 Join시켜주는 역할</span>을 하는 것이었다.

##### 즉 joinColumn의 name 설정의 값과, 매핑되는 테이블의 PK 컬럼명이 반드시 일치해야 하는것이 아니었던 것이다.

##### JoinColumn의 name 설정은, 매핑될 대상 엔티티의 컬럼 name을 정해주는 것이 아닌, FK로 사용할 내 컬럼의 이름을 지정해주는 것이었다.

즉 name 속성에는 이름을 아무렇게나 지을 수 있다는 것이다.

<br/>

#### 참고

##### 그럼 내가 처음에 생각했던 오해와 같이, joinColumn으로 매핑되는 대상의 컬럼을 지정해주는 방법은 없을까?

##### referencedColumnName을 사용해주면 가능하다.

<br/>

다시 돌아와서, 어쩌다 이것에 대해 찾아보게 되었는지 설명하겠다.

나는 어떤 프로그렘을 만들고 있는데, 해당 프로그램에서는 **추상 클래스인 Member와, Member를 상속받는 Student, Professor 클래스**가 있다.

##### Student와 Professor 모두 PK로는 Member에 정의된 공통 필드인 id를 사용한다.

```java
public abstract class Member extends BaseTimeEntity {
    @Id @GeneratedValue
    @Column(name = "member_id")
    private Long id;
    
    ...
}
```

이런식으로 말이다.

<br/>

그리고 Student와 Professor 모두와 연관관계를 가진 LinkedLecture 클래스가 있다.

여기서 고민이 생겼다. 

##### Student와 Professor은 둘 다 PK로 member_id 를 사용하는데, 어떻게 이 둘을 구분시켜서 매핑시켜주지?

```java
@Getter
@Entity
@AllArgsConstructor
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class ListenedLecture extends BaseTimeEntity {

    @Id @GeneratedValue
    @Column(name = "listend_lecture_id")
    private Long id;

    //TODO : 어떤식으로 작동되나.?
    @ManyToOne
    @JoinColumn(name = "member_id")
    private Student student;

    @ManyToOne
    @JoinColumn(name = "member_id")
    private Professor professor;

    @ManyToOne
    @JoinColumn(name = "lecture_id")
    private Lecture lecture;
}
```

##### 코드로 보면 다음과 같이 professor와 student 모두 member_id란 컬럼에 매핑시켜야 하는 것이었다!

그러나 이를 진행하면 당연하게도 오류가 발생했다.

참고로 오류의 내용은 이러하다.

##### <span style="color:red">nested exception is org.hibernate.MappingException: Repeated column in mapping for entity</span>

그래서 해결방안을 찾아보다 글의 처음에 작성했던 JoinColumn에 대한 내용을 알게되었던 것이다.

그럼 위의 코드를 어떻게 수정할까? 

##### 간단하다, name을 따로 지정해주거나, 그냥 JoinColumn 자체를 생략할 수 있다.

```java
@Getter
@Entity
@AllArgsConstructor
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class ListenedLecture extends BaseTimeEntity {

    @Id @GeneratedValue
    @Column(name = "listend_lecture_id")
    private Long id;

    @ManyToOne
    //@JoinColumn(name = "student_id")
    private Student student;

    @ManyToOne
    //@JoinColumn(name = "professor_id")
    private Professor professor;

    @ManyToOne
    @JoinColumn(name = "lecture_id")
    private Lecture lecture;
}
```

위처럼 JoinColumn을 지정해주지 않으면 어떻게 생성되는지 한번 보자.

![image-20211028052935577](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20211028052935577.png)

다음과 같이 자식엔티티명_부모엔티티명\_ID 로 생성이 되는것을 볼 수 있다!

<br/>

<br/>

### 📔 Reference

##### [JPA 중복 칼럼 에러](https://cantcoding.tistory.com/52)

##### [[JPA] PK가 아닌 필드를 참조하는 FK를 만들 때](https://velog.io/@kir3i/JPA-PK%EA%B0%80-%EC%95%84%EB%8B%8C-%ED%95%84%EB%93%9C%EB%A5%BC-%EC%B0%B8%EC%A1%B0%ED%95%98%EB%8A%94-FK%EB%A5%BC-%EB%A7%8C%EB%93%A4-%EB%95%8C)

##### [인프런 - 앤티티에서 두개의 같은 앤티티를 매핑하는 법에 대해 질문드립니다.](https://www.inflearn.com/questions/62998)

<br/>

<br/>