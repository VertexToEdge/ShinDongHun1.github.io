---
title:  "세션 사용시 영속성 컨텍스트 오류"
excerpt: "LazyInitializationException"
date:   2021-10-18 19:03:00 +0900
header:
  teaser: /assets/images/spring.png

categories: error
tags:
  - Java
  - Spring
  - 오류
  - error
last_modified_at: 2021-10-18T19:03:00-05:00




---

<br/><br/>

#### org.hibernate.LazyInitializationException: failed to lazily initialize a collection of role: 주소.주소.주소.주소, could not initialize proxy - no Session



에러가 난 코드는 다음과 같다.

<script src="https://gist.github.com/ShinDongHun1/55ebbb343baac232d96a26284a1c48fd.js"></script>

@Login Member member으로 가져온 member는 영속성 컨텍스트에서 관리되는 member가 아니다. 

uploadPost를 따라가다 보면 해당 메소드가 실행되는데

```java
//== 연관관계 편의 메소드 ==//
public void confirmWriter(Member member){
    this.writer=member;
    writer.getPosts().add(this);
}
```

 writer.getPosts()를 하는 부분에서, member가 가진 post를 가져올 때 오류가 발생하였다.

```java
@PostMapping("/main/posts")
public ResponseEntity<?> makePost(@RequestBody MakePostDto makePostDto){
    
    Post post= makePostDto.toEntity();
    Member requestMember = memberService.findByUsername(makePostDto.getUsername());

    postService.uploadPost(requestMember, post);

    log.info("POST 등록에 성공했습니다. 회원이름 = {}, 포스트 id= {}", requestMember.getName(), post.getId());

    return new ResponseEntity<>( HttpStatus.OK);

}
```

다음과 같이 수정해주면 해결된다.