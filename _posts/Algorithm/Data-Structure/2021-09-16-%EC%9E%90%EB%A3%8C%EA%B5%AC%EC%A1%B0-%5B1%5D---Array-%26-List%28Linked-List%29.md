---
title:  "자료구조 [1] - Array & List(Linked List)"
excerpt: "Array & LinkedList"
date:   2021-09-16 17:25:00 +0900
header:
  teaser: /assets/images/github-pages.jpg

categories: algorithm
tags:
  - algorithm
  - data structure
  - array
  - list
  
last_modified_at: 2021-09-16T17:25:00-05:00



---

<br/>

사실 오늘은 힙 정렬을 공부하기 위한 준비로 트리를 공부하려고 했었다. 근데 그럼 뭔가 순서가 꼬일 거 같아서...트리는 자료구조니까... 그래서 자료구조를 한번 공부한 뒤, 알고리즘으로 다시 넘어가기로 했다.

<br/>

<br/>

## 자료구조(Data Structure)

> **자료구조**는 **컴퓨터 과학**에서 **효율적인** 접근 및 수정을 가능케 하는 **자료의 조직, 관리, 저장**을 의미한다. 더 정확히 말해, 자료 구조는 데이터 값의 모임, 또 데이터 간의 관계, 그리고 데이터에 적용할 수 있는 함수나 명령을 의미한다

[출처-https://ko.wikipedia.org/wiki/%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0](https://ko.wikipedia.org/wiki/%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0)

자료 구조들로는 

- Array
- Stack
- Queue
- List
- Tree
- Graph

등이 있다. 

## 자료구조의 분류

![image-20210916152209499](https://raw.githubusercontent.com/ShinDongHun1/image_repo/main/img/image-20210916152209499.png)

<br/>

## 1. Array (배열)

배열이란 인덱스로 접근 가능한 **순차 리스트(선형 리스트)**이다.

#### 특징

- 같은 타입의 데이터를 저장하는 자료구조
- 인덱스 (Index)로 데이터 접근



<br/>

#### 배열의 장점

- 구현이 간단하다.
- 인덱스를 이용한 무작위 접근(random acess)이 가능하므로 검색 성능이 좋다(=데이터 접근이 빠르다). 
- 순차 접근(sequential access)의 경우에도 배열은 데이터를 하나의 연속된 메모리 공간에 할당하므로 연결 리스트(Linked List)보다 빠르다.
- 참조를 위한 추가적인 메모리 할당이 필요없다.

#### <br/>배열의 단점

- 크기를 변경할 수 없기 때문에 새로운 배열을 생성해서 데이터를 복사하는 작업이 필요하다.
- 실행속도를 향상시키기 위해서는 충분히 큰 크기의 배열을 생성해야 하므로 메모리가 낭비된다.
- 자료의 삽입과 삭제에 비효율적이다. 삽입과 삭제시 다음 모든 요소를 이동시켜야 하므로, 비효율적이며 자료가 많아질수록 성능이 떨어진다.



<br/>

## 2. Linked List

**Linked List** 는 위 **배열(Array)의 문제점을 해결**한다. 

Linked List 는 각 Node가 **데이터**와 포인터를 가지고 한 줄로 연결되어 있는 방식으로 데이터를 저장하는 자료구조이다. 데이터를 중간에 **추가**하거나, **삭제**하는 경우에 속도가 굉장히 빠르것이 장점이다.

<br/>

#### Linked List의 장점

- **삽입과 삭제가 간단하다.** **(시간복잡도 O(1))**
- 크기가 고정적이지 않다.
- 메모리의 재사용이 가능하다.

<br/>

#### Linked List의 단점

- 구현이 상대적으로 복잡하다.
- **검색을 할 경우 처음 값부터 순차적으로 탐색해야 하므로 비효율적이다**.**(시간복잡도(O(n)))**
- 참조를 위한 메모리가 필요하다

<br/>

#### Linked List의 종류

Linked List의 종류로는 단방향과 양방향 Linked List가 있다.

우선 단방향 Linked List는 내 이전 Node는 모르고 단지 다음 Node에 대한 정보만 알고 있기 때문에, **한 방향으로밖에 이동**할 수 없다. 따라서 **다음 Node 에 대한 접근은 쉬우나, 이전 Node에 대해서 접근하기가 어렵다**. 

이를 보안한 것이 **양방향 Linked List** 이다. Node 하나에 이전 노드를 향한 포인터와, 다음 노드를 향한 포인터를 가지고 있어서 이전 Node에 대한 접근이 용이해졌다. 

(참고로 **doubly circular linked list** 라는 양방향 linked list의 양 끝 요소를 서로 연결시킨 자료구조도 있다고 하니 궁금하면 찾아보자)

대신 양방향은 저장공간을 그만큼 더 차지하기 때문에 우리가 필요한 자료구조가 무엇인지 잘 생각해보고 쓰도록 하자.. 

<br/>

**Node Class 구현**

<div class="colorscripter-code" style="color:#010101;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#fafafa;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #e5e5e5"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#666;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div><div style="line-height:130%">18</div><div style="line-height:130%">19</div><div style="line-height:130%">20</div><div style="line-height:130%">21</div><div style="line-height:130%">22</div><div style="line-height:130%">23</div><div style="line-height:130%">24</div><div style="line-height:130%">25</div><div style="line-height:130%">26</div><div style="line-height:130%">27</div><div style="line-height:130%">28</div><div style="line-height:130%">29</div><div style="line-height:130%">30</div><div style="line-height:130%">31</div><div style="line-height:130%">32</div><div style="line-height:130%">33</div><div style="line-height:130%">34</div><div style="line-height:130%">35</div><div style="line-height:130%">36</div><div style="line-height:130%">37</div><div style="line-height:130%">38</div><div style="line-height:130%">39</div><div style="line-height:130%">40</div><div style="line-height:130%">41</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#010101;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#a71d5d">public</span>&nbsp;<span style="color:#a71d5d">class</span>&nbsp;Node&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">private</span>&nbsp;<span style="color:#066de2">int</span>&nbsp;data;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">private</span>&nbsp;Node&nbsp;next<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#066de2">null</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;Node(<span style="color:#066de2">int</span>&nbsp;data){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">this</span>.data&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;data;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">void</span>&nbsp;append(<span style="color:#066de2">int</span>&nbsp;nextData){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Node&nbsp;endNode&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;<span style="color:#a71d5d">new</span>&nbsp;Node(nextData);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Node&nbsp;n<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;<span style="color:#a71d5d">this</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">while</span>&nbsp;(n.next&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">!</span><span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;<span style="color:#066de2">null</span>){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>n.next;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<span style="color:#999999">//n.next가&nbsp;널이면</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n.next<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>endNode;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">void</span>&nbsp;delete(<span style="color:#066de2">int</span>&nbsp;data){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Node&nbsp;temp&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;<span style="color:#a71d5d">this</span>;<span style="color:#999999">//임시로&nbsp;저장해둘&nbsp;node</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">while</span>(temp.next<span style="color:#0086b3"></span><span style="color:#a71d5d">!</span><span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#066de2">null</span>){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">if</span>(temp.next.data&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;data){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp.next<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>temp.next.next;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<span style="color:#a71d5d">else</span>&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>temp.next;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">void</span>&nbsp;retrieve(){<span style="color:#999999">//출력</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Node&nbsp;n&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#a71d5d">this</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">while</span>&nbsp;(n.next&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">!</span><span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#066de2">null</span>){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#066de2">System</span>.<span style="color:#066de2">out</span>.<span style="color:#066de2">print</span>(n.data<span style="color:#0086b3"></span><span style="color:#a71d5d">+</span><span style="color:#63a35c">"&nbsp;-&gt;&nbsp;"</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>n.next;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#066de2">System</span>.<span style="color:#066de2">out</span>.<span style="color:#066de2">println</span>(n.data);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#e5e5e5text-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#e5e5e5;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

간단하게 Node class를 구현해 보았다. 

참고로 위의 delete 메소드는 만약 지우려는 값이 맨 처음에 있으면 그 값은 지우지 못하는데, 뒤에 이 문제점을 해결해보기로 하겠다.

위 Node class는 큰 문제점이 하나 있는데, 맨 처음 Node 값, 즉 헤더가 Linked List의 **대표이면서 첫번째 값**이기도 하다. 어떤 프로세스에서 이 헤더값이 더이상 필요가 없어져서 지운다고 했을 때, 다른 오브젝트가 이 헤더값을 가지고 있는 경우에 문제가 생긴다.

이런 문제를 해결하기 위해 Node 클래스를 Linked List 클래스로 감싸서, Linked List의 헤더를 데이터가 아닌,  **Linked List의 시작을 알려주는 용도**로만 하나 저장해주도록 하겠다.  
<br/>

**Linked List 구현**

<div class="colorscripter-code" style="color:#010101;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#fafafa;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #e5e5e5"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#666;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div><div style="line-height:130%">18</div><div style="line-height:130%">19</div><div style="line-height:130%">20</div><div style="line-height:130%">21</div><div style="line-height:130%">22</div><div style="line-height:130%">23</div><div style="line-height:130%">24</div><div style="line-height:130%">25</div><div style="line-height:130%">26</div><div style="line-height:130%">27</div><div style="line-height:130%">28</div><div style="line-height:130%">29</div><div style="line-height:130%">30</div><div style="line-height:130%">31</div><div style="line-height:130%">32</div><div style="line-height:130%">33</div><div style="line-height:130%">34</div><div style="line-height:130%">35</div><div style="line-height:130%">36</div><div style="line-height:130%">37</div><div style="line-height:130%">38</div><div style="line-height:130%">39</div><div style="line-height:130%">40</div><div style="line-height:130%">41</div><div style="line-height:130%">42</div><div style="line-height:130%">43</div><div style="line-height:130%">44</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#010101;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#a71d5d">public</span>&nbsp;<span style="color:#a71d5d">class</span>&nbsp;LinkedList&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;Node&nbsp;header;<span style="color:#999999">//header&nbsp;Node에는&nbsp;data가&nbsp;들어있지&nbsp;않다</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">static</span>&nbsp;<span style="color:#a71d5d">class</span>&nbsp;Node{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#066de2">int</span>&nbsp;data;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Node&nbsp;next&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#066de2">null</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;LinkedList(){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#a71d5d">new</span>&nbsp;Node();</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">void</span>&nbsp;append(<span style="color:#066de2">int</span>&nbsp;data){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Node&nbsp;endNode&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;<span style="color:#a71d5d">new</span>&nbsp;Node();</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endNode.data<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>data;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Node&nbsp;n<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;header;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">while</span>&nbsp;(n.next&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">!</span><span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;<span style="color:#066de2">null</span>){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>n.next;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<span style="color:#999999">//n.next가&nbsp;널이면</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n.next<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>endNode;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">void</span>&nbsp;delete(<span style="color:#066de2">int</span>&nbsp;data){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Node&nbsp;temp&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;header;<span style="color:#999999">//header를&nbsp;할당</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">while</span>(temp.next<span style="color:#0086b3"></span><span style="color:#a71d5d">!</span><span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#066de2">null</span>){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">if</span>(temp.next.data&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>&nbsp;data){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp.next<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>temp.next.next;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<span style="color:#a71d5d">else</span>&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>temp.next;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">void</span>&nbsp;retrieve(){<span style="color:#999999">//출력</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Node&nbsp;n&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>header.next;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a71d5d">while</span>&nbsp;(n.next&nbsp;<span style="color:#0086b3"></span><span style="color:#a71d5d">!</span><span style="color:#0086b3"></span><span style="color:#a71d5d">=</span><span style="color:#066de2">null</span>){</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#066de2">System</span>.<span style="color:#066de2">out</span>.<span style="color:#066de2">print</span>(n.data<span style="color:#0086b3"></span><span style="color:#a71d5d">+</span><span style="color:#63a35c">"&nbsp;-&gt;&nbsp;"</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n<span style="color:#0086b3"></span><span style="color:#a71d5d">=</span>n.next;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#066de2">System</span>.<span style="color:#066de2">out</span>.<span style="color:#066de2">println</span>(n.data);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">}</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#e5e5e5text-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#e5e5e5;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

LinkedList는 header를 갖고있으며, 데이터는 가지고 있지 않다. 이를 통해 Linked List의 시작을 알려주는 용도로서 사용할 수 있게 되었고, 이전 Node 클래스에서 delete로는 첫번째 값을 지울 수 없는 문제도 해결했다. 

> 어떤 프로세스에서 이 헤더값이 더이상 필요가 없어져서 지운다고 했을 때, 다른 오브젝트가 이 헤더값을 가지고 있는 경우에 문제가 생긴다.



<br/>

#### List 시간복잡도

 |                          | **Add** | **Remove** | **Get** | **Contains** | **Data Structure** |
  | ------------------------ | ------- | ---------- | ------- | ------------ | ------------------ |
  | **LinkedList**           | O(1)    | O(1)       | O(n)    | O(n)         | LinkedList         |

add와 remove가 1인 이유는, 데이터를 삽입하거나 삭제하는 행위 그 자체만 보았을때이다. 만약 삽입하거나 삭제할 대상을 탐색하는 동작까지 합친다면 O(N)이 나오게 된다.

<br/>

<br/>

### 오늘은 Array(배열)와, Linked List에 대해 공부하고, 구현해 보았다.!

### 조금 단순하게 구현하긴 했지만 예전에 배웠었던 기억이 조금 나면서, 그리 어렵지 않았다 ㅎㅎ

