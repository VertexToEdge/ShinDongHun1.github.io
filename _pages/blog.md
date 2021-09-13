---
title: "blog"
permalink: /categories/blog/
layout: category
author_profile: true
sidebar_main: true
taxonomy: blog
---

Github 블로그 만드는 과정들입니다 :D

{% assign posts = site.categories.blog%}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
