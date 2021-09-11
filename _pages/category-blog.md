---
title: "blog"
permalink: /categories/blog/
layout: archive
author_profile: true
toc_sticky: true
toc_ads : true
taxonomy: blog
sidebar_main: true
---

```
{% assign posts = site.categories.blog %}
{% for post in posts %} {% include archive-single2.html type=page.entries_layout %} {% endfor %
```

