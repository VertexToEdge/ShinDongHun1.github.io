---
title:  "Github 블로그 만들기[6]"
excerpt: "같은 카테고리 내에서의 이전글, 다음글 이동"
date:   2021-09-17 00:35:00 +0900
header:
  teaser: /assets/images/github-pages.png

categories: blog
tags:
  - Github
  - blog
  - 블로그
last_modified_at: 2021-09-17T00:35:30-05:00

---

<br/>

<br/>

#### post_pagination.html

_includes 폴더 안에 있는데 이 파일의 내용을 전부 지우고!

<div class="colorscripter-code" style="color:#010101;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#fafafa;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #e5e5e5"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#666;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="line-height:130%">1</div><div style="line-height:130%">2</div><div style="line-height:130%">3</div><div style="line-height:130%">4</div><div style="line-height:130%">5</div><div style="line-height:130%">6</div><div style="line-height:130%">7</div><div style="line-height:130%">8</div><div style="line-height:130%">9</div><div style="line-height:130%">10</div><div style="line-height:130%">11</div><div style="line-height:130%">12</div><div style="line-height:130%">13</div><div style="line-height:130%">14</div><div style="line-height:130%">15</div><div style="line-height:130%">16</div><div style="line-height:130%">17</div><div style="line-height:130%">18</div><div style="line-height:130%">19</div><div style="line-height:130%">20</div><div style="line-height:130%">21</div><div style="line-height:130%">22</div><div style="line-height:130%">23</div><div style="line-height:130%">24</div><div style="line-height:130%">25</div><div style="line-height:130%">26</div><div style="line-height:130%">27</div><div style="line-height:130%">28</div><div style="line-height:130%">29</div><div style="line-height:130%">30</div><div style="line-height:130%">31</div><div style="line-height:130%">32</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#010101;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&lt;!--첫&nbsp;번째&nbsp;문단--</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399"></span>{<span style="color:#0066cc">%&nbsp;assign&nbsp;cat&nbsp;=&nbsp;page.categories[0]&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399"></span>{<span style="color:#0066cc">%&nbsp;assign&nbsp;cat_list&nbsp;=&nbsp;site.categories[cat]&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399"></span>{<span style="color:#0066cc">%&nbsp;for&nbsp;post&nbsp;in&nbsp;cat_list&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;if&nbsp;post.url&nbsp;==&nbsp;page.url&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0099cc">%&nbsp;assign&nbsp;prevIndex&nbsp;=&nbsp;forloop.index0&nbsp;|&nbsp;minus</span><span style="color:#ff3399">:</span><span style="color:#0066cc">&nbsp;1&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0099cc">%&nbsp;assign&nbsp;nextIndex&nbsp;=&nbsp;forloop.index0&nbsp;|&nbsp;plus</span><span style="color:#ff3399">:</span><span style="color:#0066cc">&nbsp;1&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;if&nbsp;forloop.first&nbsp;==&nbsp;false&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;assign&nbsp;next_post&nbsp;=&nbsp;cat_list[prevIndex]&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;endif&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;if&nbsp;forloop.last&nbsp;==&nbsp;false&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;assign&nbsp;prev_post&nbsp;=&nbsp;cat_list[nextIndex]&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;endif&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;break&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;endif&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399"></span>{<span style="color:#0066cc">%&nbsp;endfor&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&lt;!--두&nbsp;번째&nbsp;문단--</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399"></span>{<span style="color:#0066cc">%&nbsp;if&nbsp;prev_post&nbsp;or&nbsp;next_post&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&lt;nav&nbsp;class="pagination"</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;if&nbsp;prev_post&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;a&nbsp;href="</span>{<span style="color:#ff3399"></span>{<span style="color:#0066cc">&nbsp;prev_post.url&nbsp;</span>}<span style="color:#0066cc"></span>}<span style="color:#ff3399">"&nbsp;class="pagination--pager"</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span>{<span style="color:#ff3399"></span>{<span style="color:#0099cc">&nbsp;site.data.ui-text[site.locale].pagination_previous&nbsp;|&nbsp;default</span><span style="color:#ff3399">:</span><span style="color:#0066cc">&nbsp;"Previous"&nbsp;</span>}<span style="color:#0066cc"></span>}<span style="color:#ff3399">&lt;/a</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;else&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;a&nbsp;href="#"&nbsp;class="pagination--pager&nbsp;disabled"</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span>{<span style="color:#ff3399"></span>{<span style="color:#0099cc">&nbsp;site.data.ui-text[site.locale].pagination_previous&nbsp;|&nbsp;default</span><span style="color:#ff3399">:</span><span style="color:#0066cc">&nbsp;"Previous"&nbsp;</span>}<span style="color:#0066cc"></span>}<span style="color:#ff3399">&lt;/a</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;endif&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;if&nbsp;next_post&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;a&nbsp;href="</span>{<span style="color:#ff3399"></span>{<span style="color:#0066cc">&nbsp;next_post.url&nbsp;</span>}<span style="color:#0066cc"></span>}<span style="color:#ff3399">"&nbsp;class="pagination--pager"</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span>{<span style="color:#ff3399"></span>{<span style="color:#0099cc">&nbsp;site.data.ui-text[site.locale].pagination_next&nbsp;|&nbsp;default</span><span style="color:#ff3399">:</span><span style="color:#0066cc">&nbsp;"Next"&nbsp;</span>}<span style="color:#0066cc"></span>}<span style="color:#ff3399">&lt;/a</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;else&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;a&nbsp;href="#"&nbsp;class="pagination--pager&nbsp;disabled"</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span>{<span style="color:#ff3399"></span>{<span style="color:#0099cc">&nbsp;site.data.ui-text[site.locale].pagination_next&nbsp;|&nbsp;default</span><span style="color:#ff3399">:</span><span style="color:#0066cc">&nbsp;"Next"&nbsp;</span>}<span style="color:#0066cc"></span>}<span style="color:#ff3399">&lt;/a</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&nbsp;&nbsp;</span>{<span style="color:#0066cc">%&nbsp;endif&nbsp;%</span>}<span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399">&nbsp;&nbsp;&lt;/nav</span><span style="color:#4DA51B">&gt;</span><span style="color:#ff3399"></span></div><div style="padding:0 6px; white-space:pre; line-height:130%"><span style="color:#ff3399"></span>{<span style="color:#0066cc">%&nbsp;endif&nbsp;%</span>}</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#e5e5e5text-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#e5e5e5;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

이렇게 바꿔주자.

[참고블로그 -공부하는 식빵맘](https://ansohxxn.github.io/blog/prevnext/)

코드 막 가져다 써서 죄송합니다..!