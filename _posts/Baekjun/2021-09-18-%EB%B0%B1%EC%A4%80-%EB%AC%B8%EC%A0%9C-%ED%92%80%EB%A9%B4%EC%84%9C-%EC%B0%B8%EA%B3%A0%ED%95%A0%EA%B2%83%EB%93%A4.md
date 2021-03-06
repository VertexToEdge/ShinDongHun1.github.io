---
title:  "백준 문제 풀면서 참고할것들"
excerpt: "백준 문제 풀면서 사용했던 메소드들"
date:   2021-09-18 10:00:00 +0900
header:
  teaser: /assets/images/github-pages.jpg

categories: baekjun
tags:
  - algorithm
  - 백준
  
last_modified_at: 2021-09-18T10:00:00-05:00




---

<br/>

<br/>

#### **ListIterator<E> 인터페이스** 

> #### ListIterator<E> 인터페이스
>
> ListIterator 인터페이스는 Iterator 인터페이스를 상속받아 여러 기능을 추가한 인터페이스입니다.
>
> Iterator 인터페이스는 컬렉션의 요소에 접근할 때 한 방향으로만 이동할 수 있습니다.
>
> 하지만 JDK 1.2부터 제공된 ListIterator 인터페이스는 컬렉션 요소의 대체, 추가 그리고 인덱스 검색 등을 위한 작업에서 양방향으로 이동하는 것을 지원합니다.
>
> 단, ListIterator 인터페이스는 List 인터페이스를 구현한 List 컬렉션 클래스에서만 listIterator() 메소드를 통해 사용할 수 있습니다.

[출처 - TPC School ,Iterator와 ListIterator](http://tcpschool.com/java/java_collectionFramework_iterator)

<br/>

<br/>

#### StringTokenizer 와 Split

이전에 StringTokenizer 대신 **split**을 사용하자 했었지만, 

입력받은 문자열을 바로 배열로 만드는 경우가 아니라,

**하나씩 빼서 쓸 경우에는 StringTokenizer가 더 효율적**이었다.

[참고 백준 2493번 - 탑](https://shindonghun1.github.io/baekjun/%EB%B0%B1%EC%A4%80-2493%EB%B2%88/)

<br/>

<br/>

#### StringTokenizer  반복하기

<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">StringTokenizer&nbsp;st&nbsp;<span style="color:#0086b3"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#ff3399">new</span>&nbsp;StringTokenizer(str);&nbsp;</div><div style="background-color:#303030; padding:0 6px; white-space:pre; line-height:130%"><span style="color:#4be6fa">System</span>.<span style="color:#4be6fa">out</span>.<span style="color:#4be6fa">println</span>(st.countTokens());&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">while</span>(st1.hasMoreTokens())&nbsp;{&nbsp;</div><div style="background-color:#303030; padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">System</span>.<span style="color:#4be6fa">out</span>.<span style="color:#4be6fa">println</span>(st.nextToken());&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">}</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#4f4f4ftext-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

<br/>

<br/>

#### String 배열(Array)을 int 배열로 변환

>  **int [] arr = Arrays.stream("Sting [] ").mapToInt(Integer::parseInt).toArray();** 
>

위의 String [] 위치에 br.readline().split(" "); 등을 사용하여 String 배열 넣어주기.

<br/>

<br/>

#### Comparator

* **정렬 가능한 클래스(Comparable 인터페이스를 구현한 클래스)들의 기본 정렬 기준과 다르게 정렬 하고 싶을 때 사용하는 인터페이스**
* **compare 메소드를 Override 하여 작성하고, compare 메소드의 작성법**
  * **첫 번째 파라미터로 넘어온 객체 < 두 번째 파라미터로 넘어온 객체: 음수 리턴**
  * **첫 번째 파라미터로 넘어온 객체 == 두 번째 파라미터로 넘어온 객체: 0 리턴**
  * **첫 번째 파라미터로 넘어온 객체 > 두 번째 파라미터로 넘어온 객체: 양수 리턴**
  * ***음수 또는 0이면 객체의 자리가 그대로 유지되며, 양수인 경우에는 두 객체의 자리가 변경된다.***
* **Arrays.sort(array, Comparator), Collections.sort(array, Comparator) 사용가능**

