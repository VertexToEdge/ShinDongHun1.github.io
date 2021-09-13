---
title: "Algorithm"
permalink: /categories/algorithm/
layout: category
author_profile: true
taxonomy: algorithm
---

{% assign posts = site.categories.algorithm%}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
