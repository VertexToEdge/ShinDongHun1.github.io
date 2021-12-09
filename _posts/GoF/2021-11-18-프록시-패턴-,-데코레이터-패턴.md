---
title:  "프록시 패턴, 데코레이터 패턴"
excerpt: "프록시 패턴, 데코레이터 패턴"
date:   2021-11-18 15:30:00
header:
  teaser: /assets/images/spring.png

categories: GoF
tags:
  - GoF
last_modified_at: 2021-11-18T15:30:00



---

## 💡 프록시 패턴, 데코레이터 패턴

<br/>

일반적으로 클라이언트와 서버가 있으면, 클라이언트가 서버를 직접 호출하고, 처리 결과를 직접 받는다. 이것을 직접 호출이라 한다.

그런데 클라이언트가 요청한 결과를 서버에 직접 요청하는 것이 아니라 어떤 대리자를 통해서 간접적으로 서버에 요청할 수 있다.

##### 여기서의 대리자를 영어로 Proxy라고 한다.

<br/>

#### 프록시의 주요 기능

프록시를 통해서 할 수 있는 일은 크게 2가지로 구분할 수 있다.

##### 접근 제어

- 권한에 따른 접근 차단
- 캐싱 
- 지연 로딩

##### 부가 기능 추가

- 원래 서버가 제공하는 기능에 더해서 부가 기능을 수행한다.

<br/>

#### GOF 디자인 패턴

둘 다 프록시를 사용하는 방법이지만 GOF 디자인 패턴에서는 이 둘을 의도에 따라서 프록시 패턴과 데코레이터 패턴으로 구분한다.

##### 프록시 패턴  -> 접근 제어가 목적

##### 데코레이터 패턴 -> 새로운 기능 추가가 목적

<br/>

<br/>

### 프록시 패턴 예제

```java
public interface Subject {
    String operation();
}
```



##### Subject 구현

```java
@Slf4j
public class RealSubject implements Subject{

    @Override
    public String operation() {
        log.info("실제 객체 호출");
        sleep(1000);
        return null;
    }

    private void sleep(int millis) {
        try {
            Thread.sleep(millis);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

조회할 데이터의 용량이 커, 조회하는데 1초가 걸린다고 가정하고 코드를 작성했다



##### 클라이언트

```java
public class ProxyPatternClient {
    private Subject subject;

    public ProxyPatternClient(Subject subject) {
        this.subject = subject;
    }

    public void execute() {
        subject.operation();
    }
}
```



##### 테스트 코드

```java
public class ProxyPatternTest {

    @Test
    public void noProxyTest() throws Exception {
        RealSubject realSubject = new RealSubject();
        ProxyPatternClient client = new ProxyPatternClient(realSubject);
        client.execute();
        client.execute();
        client.execute();
    }
}
```

##### 위 테스트코드를 실행시키면 총 3초가 걸린다.

그런데 이 데이터가 한번 조회하면 변하지 않는 데이터라면, 어디엔가 보관해두고 이미 조회한 데이터를 사용하는 것이 성능상 좋으며, 이 방법을 캐시라고 한다.

프록시 패턴의 주요 기능은 접근 제어이다. 캐시도 접근 자체를 제어하는 기능 중 하나이다.

이미 개발된 로직을 전혀 수정하지 않고, 프록시 캐시를 통해서 캐시를 적용해보자.



#### 프록시 적용

```java
@Slf4j
public class CacheProxy implements Subject{
    private Subject target;
    private String cacheValue;

    public CacheProxy(Subject target) {
        this.target = target;
    }


    @Override
    public String operation() {
        log.info("프록시 호출");
        if(cacheValue == null){
            cacheValue = target.operation();
        }
        return cacheValue;

    }
}
```



##### 테스트 코드

```java
public class ProxyPatternTest {

    @Test
    public void noProxyTest() throws Exception {
        RealSubject realSubject = new RealSubject();
        ProxyPatternClient client = new ProxyPatternClient(realSubject);
        client.execute();
        client.execute();
        client.execute();
    }

    @Test
    public void cacheProxyTest() throws Exception {
        RealSubject realSubject = new RealSubject();
        CacheProxy cacheProxy = new CacheProxy(realSubject);
        ProxyPatternClient client = new ProxyPatternClient(cacheProxy);
        client.execute();
        client.execute();
        client.execute();


    }
}
```

##### 프록시 패턴의 핵심은 기존 코드는 전혀 변경하지 않고, 프록시를 도입해서 접근 제어를 했다는 점이다.

##### 클라이언트 입장에서는 프록시 객체가 주입되었는지, 실제 객체가 주입되었는지 알 수 없다.

<br/>

<br/>

<br/>

### 데코레이터 패턴

```java
public interface Component {
    String operation();
}
```

```java
@Slf4j
public class RealComponent implements  Component{
    @Override
    public String operation() {
        log.info("RealComponent 실행 ");
        return "Data";
    }
}
```



##### client

```java
@Slf4j
public class DecoratorPatternClient {

    private Component component;

    public DecoratorPatternClient(Component component) {
        this.component = component;
    }

    public void execute() {
        String result = component.operation();
        log.info("result = {}", result);
    }
}
```



##### test

```java
@Slf4j
public class DecoratorPatternTest {

    @Test
    public void noDecorator() throws Exception {
        Component realComponent = new RealComponent();
        DecoratorPatternClient client = new DecoratorPatternClient(realComponent);
        client.execute();

    }
}
```



#### 부가 기능 추가

```java
@Slf4j
public class MessageDecorator implements Component{

    private Component component;

    public MessageDecorator(Component component) {
        this.component = component;
    }

    @Override
    public String operation() {
        log.info("MessageDecorator 실행");

        String operation = component.operation();

        return operation + " Decorate";
    }
}
```

 

##### 테스트

```java
@Slf4j
public class DecoratorPatternTest {

    @Test
    public void noDecorator() throws Exception {
        Component realComponent = new RealComponent();
        DecoratorPatternClient client = new DecoratorPatternClient(realComponent);
        client.execute();

    }
    @Test
    public void decorator1() throws Exception {
        Component realComponent = new RealComponent();
        Component messageDecorator = new MessageDecorator(realComponent);
        DecoratorPatternClient client = new DecoratorPatternClient(messageDecorator);
        client.execute();

    }
}
```

<br/>

<br/>

### 프록시 패턴 vs 데코레이터 패턴

#### => 의도 (Intent)

사실 프록시 패턴과 데코레이터 패턴은 그 모양이 거의 같고, 상황에 따라 정말 똑같을 때도 있다. 그러면 둘을 어떻게 구분하는 것일까? 

디자인 패턴에서 중요한 것은 해당 패턴의 겉모양이 아니라 그 패턴을 만든 의도가 더 중요하다. 따라서 의도에 따라 패턴을 구분한다.

##### 프록시 패턴의 의도 : 다른 개체에 대한 접근을 제어하기 위해 대리자를 제공

##### 데코레이터 패턴의 의도 : 객체에 추가 책임(기능)을 동적으로 추가하고, 기능 확장을 위한 유연한 대안을 제공

<br/>

<br/>

## 📔 Reference

[인프런 - 스프링 핵심 원리 고급편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B3%A0%EA%B8%89%ED%8E%B8/dashboard)

