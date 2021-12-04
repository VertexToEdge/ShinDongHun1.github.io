---
title: "Diary"
permalink: /categories/diary/
layout: archive
author_profile: true
sidebar_main: true
taxonomy: diary
---



{% assign posts = site.categories.diary%}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
