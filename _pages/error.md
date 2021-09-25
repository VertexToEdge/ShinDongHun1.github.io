---
title: "Error"
permalink: /categories/error/
layout: archive
author_profile: true
sidebar_main: true
taxonomy: error
---

### ✏️오류 모음집 : (

{% assign posts = site.categories.error%}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}