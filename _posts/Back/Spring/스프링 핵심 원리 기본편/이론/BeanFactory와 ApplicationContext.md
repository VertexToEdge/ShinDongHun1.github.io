컨테이너에 등록된 모든 빈 조회부터





## BeanFactory와 ApplicationContext

### BeanFactory

스프링 컨테이너의 **최상위 인터페이스**

> **스프링 빈을 관리하고 조회하는 역할을 담당**
>
> **getBean() 을 제공**

<br/>

<br/>

### ApplicationContext

BeanFactory의 기능을 모두 상속받아 제공하며, 추가적인 기능들도 제공한다.

> **메시지소스를 활용한 국제화 기능** - 예를 들어서 한국에서 들어오면 한국어로, 영어권에서 들어오면 영어로 출력 
>
> **환경변수** - 로컬, 개발, 운영등을 구분해서 처리 
>
> **애플리케이션 이벤트** - 이벤트를 발행하고 구독하는 모델을 편리하게 지원 
>
> **편리한 리소스 조회** - 파일, 클래스패스, 외부 등에서 리소스를 편리하게 조회

참고로 개발 환경에는 로컬 개발환경(내 PC), 테스트 서버, 실제 운영환경

<br/>

<br/>

## 스프링 컨테이너 설정 형식

### 애노테이션 기반 자바 코드 설정

지금까지 했던 것들은 모두 <span style="color:orange">**애노테이션 기반 자바 코드 설정을 사용한 것이다.**</span>

> **<span style="color:orange">new </span>AnnotationConfigApplicationContext(AppConfig.class)**

<br/>

### XML 설정 사용

최근에는 스프링 부트를 많이 사용하면서 xml 기반 설정은 잘 사용하지 않는다.

사용법은 GenericXmlApplicationContext를 사용해서 xml 설정 파일을 넘기면 된다.

> **<span style="color:orange">new</span> GenericXmlApplicationContext("appConfig.xml")**

파일 위치는 resources에 넣어주면 된다!

<br/>

**appConfig.xml**

<script src="https://gist.github.com/ShinDongHun1/a6ac4e06746900789b1cfdcbc510448f.js"></script>

**class**는 **패키지명까지 모두** 적어줘야 한다!

> class="springbasic.core.member.MemberServiceImpl" 

**constructor-arg name**는 **생성자를 통해 주입받는**경우에 사용!

> \<constructor-arg name="memberRepository" ref="memberRepository" >

<br/>

<br/>

## BeanDefinition

**스프링 빈 설정 메타 정보**

위에서 본 것 처럼, 스프링은 다양한 설정 형식을 지원한다. 이것을 가능하게 해주는 것에는 바로

BeanDefinition이라는 **추상화**가 있다.

결국 무슨 파일이던 읽어서 **BeanDefinition**을 만들면 되는것이다.

@Bean, \<bean> 하나당 각각 하나의 메타 정보가 생성된다.

스프링 컨테이너는 이 메타정보를 기반으로 스프링 빈을 생성한다.

<br/>

**BeanDefinition의 정보**

- **BeanClassName**: 생성할 빈의 클래스 명(자바 설정 처럼 팩토리 역할의 빈을 사용하면 없음)
- **factoryBeanName**: 팩토리 역할의 빈을 사용할 경우 이름, 예) appConfig
- **factoryMethodName**: 빈을 생성할 팩토리 메서드 지정, 예) memberService
- **Scope**: 싱글톤(기본값)
- **azyInit**: 스프링 컨테이너를 생성할 때 빈을 생성하는 것이 아니라, 실제 빈을 사용할 때 까지 최대한 생성을 지연처리 하는지 여부
- **InitMethodName**: 빈을 생성하고, 의존관계를 적용한 뒤에 호출되는 초기화 메서드 명
- **DestroyMethodName**: 빈의 생명주기가 끝나서 제거하기 직전에 호출되는 메서드 명
- **Constructor arguments, Properties**: 의존관계 주입에서 사용한다. (자바 설정 처럼 팩토리 역할의 빈을 사용하면 없음)

<br/>

<br/>

##### 좀 어려운 내용이니 스프링이 다양한 형태의 설정 정보를 BeanDefinition으로 추상화해서 사용한다는 것 정도만 이해하자!

<br/>

<br/>