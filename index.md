---
layout: page
title: Home
---

<div class="py-3">
  <span class="hello">Inside Stue's Brain - Decoding Stuart Elimu</span>
</div>

<ol class="post-list my-2">
  {% for post in site.posts limit:5 %}
    <li>
      <div class="card">
        <div class="card-body px-2">
          <p class="card-title h3"><a class="post-link" href="{{ post.url }}">{{ post.title }}</a></p>
        </div>
      </div>
    </li>
  {% endfor %}
</ol>

<script async data-uid="3df2bee2cc" src="https://wondrous-speaker-8686.ck.page/3df2bee2cc/index.js"></script>
