---
title: "내가 읽은 책들"
permalink: /categories/db/
layout: archive
author_profile: true
taxonomy: db
sidebar_main: true


---

### ✏️ 관계형 데이터베이스 공부하기

(관계형 모델, SQL 등등....)

{% assign posts = site.categories.db%}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

