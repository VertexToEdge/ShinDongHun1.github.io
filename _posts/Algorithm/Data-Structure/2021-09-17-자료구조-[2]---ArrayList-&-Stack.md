---
title:  "자료구조 [2] - ArrayList & Stack"
excerpt: "ArrayList & Stack"
date:   2021-09-17 18:13:00 +0900
header:
  teaser: /assets/images/github-pages.jpg

categories: algorithm
tags:
  - algorithm
  - data structure
  - arrayList
  - stack
  
last_modified_at: 2021-09-17T18:13:00-05:00


---

<br/>

오늘은 어제에 이어서 ArrayList와, 스택에 대해서 공부해보겠습니당.

<br/>

<br/>

## ArrayList

자바의 ArrayList는 List 인터페이스를 상속받은 클래스로, 일반 Array와 유사하지만, **크기가 가변적으로 변하는 선형리스트**다. (참고로 선형 리스트란 배열과 같이 연속되는 기억장소에 저장되는 리스트를 말한다.) <br/>그럼에도 불구하고, **검색시간은 여전히 배열과 같은 O(1)**이다. <br/>ArrayList는 배열방이 다 차면, 배열방의 크기를 두배로 늘려준다! 이 행위를 Doubling 이라고 한다. <br/>현재 배열방의 크기가 n인 ArrayList를 생각해보자. 그 이전 배열방의 상황에서 배열의 크기 조정 후 원소를 복사하는데 드는 시간은 2/n 이고, 그 전 상황에서는 n/4, ...... 2, 1 이므로, 모두 합쳐야 n보다 작거나 같다.
$$
n >= 2/n + 4/n + ... + 2 + 1
$$
따라서 원소의 개수가 n인 배열방의 크기를 늘려주는 행위는 O(n)만큼의 시간복잡도를 가지게 된다.

<br/>

<br/>

### ArrayList와 LinkedList 선택하기

일반적으로 **get/set을 많이 사용**하는 경우에는 **ArrayList,**

처음이나 끝에 **잦은 삽입, 삭제**가 발생한다면 **LinkedList.**

(참고로 실무에서는 일반적인 상황은 인덱스기반 선형구조로 충분한경우가 많아서 ArrayList를 많이 쓴다고들 한다)

<br/>

<br/>

#### List 시간복잡도

|                | **Add** | **Remove** | **Get** | **Contains** | **Data Structure** |
| -------------- | ------- | ---------- | ------- | ------------ | ------------------ |
| **ArrayList**  | O(1)    | O(n)       | O(1)    | O(n)         | Array              |
| **LinkedList** | O(1)    | O(1)       | O(n)    | O(n)         | LinkedList         |

Linked List에서 add와 remove가 1인 이유는, 데이터를 삽입하거나 삭제하는 행위 그 자체만 보았을때이다. 만약 삽입하거나 삭제할 대상을 **탐색하는 동작**까지 합친다면 **O(N)**이 나오게 된다.

ArrayList에서 삽입 시 시간복잡도가 O(1)인 경우는 **배열의 크기가 충분한 경우**이다. 여유 공간이 없을 때는 Doubling의 과정이 필요하므로 시간 복잡도는 **O(n)** 이 된다.

<br/>

<br/>

## Stack

stack이란 이름 그대로 데이터를 하나씩 쌓아 올리는 Data Structure이다. 쌓아 올린다면 꺼낼때는 맨 위에있는 애부터 꺼낼 수 있으니까, 후입선출(Last In First Oot) 형식의 자료구조이다. 

#### Stack 의 기능

- **pop()** : 맨 마지막(가장 위)에 넣은 데이터를 가져온다
- **push()** : 새로운 데이터를 넣는다
- **peek()** : 맨 마지막(가장 위) 데이터를 본다.
- **inEmpty()** : 스택이 비어 있을 때에 true를 반환한다.

<br/>

스택은 연결 리스트로 구현이 가능하고, 아래는 자바로 구현한 코드이다.

<div class="colorscripter-code" style="color:#010101;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#fafafa;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #e5e5e5"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#666;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div><div style="line-height:130%">18</div><div style="line-height:130%">19</div><div style="line-height:130%">20</div><div style="line-height:130%">21</div><div style="line-height:130%">22</div><div style="line-height:130%">23</div><div style="line-height:130%">24</div><div style="line-height:130%">25</div><div style="line-height:130%">26</div><div style="line-height:130%">27</div><div style="line-height:130%">28</div><div style="line-height:130%">29</div><div style="line-height:130%">30</div><div style="line-height:130%">31</div><div style="line-height:130%">32</div><div style="line-height:130%">33</div><div style="line-height:130%">34</div><div style="line-height:130%">35</div><div style="line-height:130%">36</div><div style="line-height:130%">37</div><div style="line-height:130%">38</div><div style="line-height:130%">39</div><div style="line-height:130%">40</div><div style="line-height:130%">41</div><div style="line-height:130%">42</div><div style="line-height:130%">43</div><div style="line-height:130%">44</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#010101;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#a71d5d">package</span>&nbsp;List;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#a71d5d">import</span>&nbsp;java.util.EmptyStackException;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#a71d5d">public</span>&nbsp;<span style="color:#a71d5d">class</span>&nbsp;Stack<span style="color:#0086b3"></span><span style="color:#a71d5d">&lt;</span>T<span style="color:#0086b3"></span><span style="color:#a71d5d">&gt;</span>&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">class</span>&nbsp;Node<span style="color:#0086b3"></span><span style="color:#a71d5d">&lt;</span>T<span style="color:#0086b3"></span><span style="color:#a71d5d">&gt;</span>{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">private</span>&nbsp;T&nbsp;data;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">private</span>&nbsp;Node&nbsp;next;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">public</span>&nbsp;Node(T&nbsp;data){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">this</span>.data<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>data;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">private</span>&nbsp;Node<span style="color:#0086b3"></span><span style="color:#a71d5d">&lt;</span>T<span style="color:#0086b3"></span><span style="color:#a71d5d">&gt;</span>&nbsp;top;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">public</span>&nbsp;T&nbsp;pop(){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">if</span>(top&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;<span style="color:#066de2">null</span>){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">throw</span>&nbsp;<span style="color:#a71d5d">new</span>&nbsp;EmptyStackException();</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T&nbsp;result&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;top.data;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;top<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>top.next;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">return</span>&nbsp;result;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">public</span>&nbsp;<span style="color:#a71d5d">void</span>&nbsp;push(T&nbsp;data){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Node<span style="color:#0086b3"></span><span style="color:#a71d5d">&lt;</span>T<span style="color:#0086b3"></span><span style="color:#a71d5d">&gt;</span>&nbsp;temp<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;<span style="color:#a71d5d">new</span>&nbsp;Node<span style="color:#0086b3"></span><span style="color:#a71d5d">&lt;</span><span style="color:#0086b3"></span><span style="color:#a71d5d">&gt;</span>(data);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp.next<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>top;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;top&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;temp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">public</span>&nbsp;T&nbsp;peek(){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">if</span>(top&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;<span style="color:#066de2">null</span>){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">throw</span>&nbsp;<span style="color:#a71d5d">new</span>&nbsp;EmptyStackException();</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T&nbsp;result&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;top.data;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">return</span>&nbsp;result;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">public</span>&nbsp;<span style="color:#066de2">boolean</span>&nbsp;isEmpty(){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">return</span>&nbsp;top<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#066de2">null</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#e5e5e5text-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#e5e5e5;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

<br/>

### 스택(Stack)의 사용 사례

재귀 알고리즘을 사용하는 경우 스택이 유용하다.

- **재귀 알고리즘**
  
  - 재귀적으로 함수를 호출해야 하는 경우에 임시 데이터를 스택에 넣어준다.
  - 재귀함수를 빠져 나와 퇴각 검색(backtrack)을 할 때는 스택에 넣어 두었던 임시 데이터를 빼 줘야 한다.
  - 스택은 이런 일련의 행위를 직관적으로 가능하게 해 준다.
  - 또한 스택은 재귀 알고리즘을 반복적 형태(iterative)를 통해서 구현할 수 있게 해준다.
  
- 역추적을 해야할 때

- 웹 브라우저 방문기록 (뒤로가기)

- 실행 취소 (undo)

- 역순 문자열 만들기

- 수식의 괄호 검사 (연산자 우선순위 표현을 위한 괄호 검사)
         Ex) **올바른 괄호 문자열(VPS, Valid Parenthesis String) 판단하기**
     
- 후위 표기법 계산

  

[출처 - https://gmlwjd9405.github.io/2018/08/03/data-structure-stack.html](https://gmlwjd9405.github.io/2018/08/03/data-structure-stack.html)

<br/>

<br/>

### 오늘은 ArrayList와 Stack에 대해서 공부해 보았다.!

### 시간이 없어서 큐랑 덱은 다음에 계속해서 공부해 보도록 하겠다.
