---
layout: page
title: Blog
permalink: /blog/
---

<ol>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ol>


