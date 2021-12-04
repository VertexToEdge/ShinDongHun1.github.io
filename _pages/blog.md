---
title: "blog"
permalink: /categories/blog/
layout: archive
author_profile: true
sidebar_main: true
---

### Github 블로그 만드는 과정들

{% assign posts = site.categories.blog%}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

