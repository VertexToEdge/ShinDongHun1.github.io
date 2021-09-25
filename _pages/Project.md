---
title: "Project"
permalink: /categories/project/
layout: archive
author_profile: true
sidebar_main: true
taxonomy: project

---

### ✏️ 내가 프로젝트 만들며 느꼈던 감정과, 과정, 그리고 코드들

{% assign posts = site.categories.project%}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

