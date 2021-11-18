

[스프링 핵심 원리 - 고급편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B3%A0%EA%B8%89%ED%8E%B8/dashboard)



## 로그 남기기



하나의 요청에 대해서 같은 id를 남길 것이고, 메소드를 호출할 때마다 깊이를 늘려서 표현하는 로그를 만들어 보자!



#### 깊이와 id를 상태로 가지고 있는 TraceId

<script src="https://gist.github.com/ShinDongHun1/8eb9c957ab97b670e787db2ac4fd8fcc.js"></script>



#### 걸린 시간과, 메세지, TraceId를 상태로 가지는 TraceStatus

<script src="https://gist.github.com/ShinDongHun1/c4c28156668c318d10fad8601a285462.js"></script>





## 쓰레드 로컬 

해당 쓰레드만 접근할 수 있는 특별한 저장소를 말한다.

<script src="https://gist.github.com/ShinDongHun1/3018bdd5803a0e144e37fba759357879.js"></script>

