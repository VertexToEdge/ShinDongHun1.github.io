---
title: "Diary"
permalink: /categories/diary/
layout: archive
author_profile: true
sidebar_main: true
taxonomy: diary
---

### ✏️ 매일매일 있었던 일들 사소하게 적는 일기장 :D

{% assign posts = site.categories.diary%}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
