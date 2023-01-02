---
layout: page
title: Blog
permalink: /blog/
---

# Blog

<div class="card border">
  <div style="display: flex; align-items: center; flex-wrap: wrap">
    <div class="col-md-3 p-2">
      <img src="/assets/images/rijksmuseum.jpg" class="img-fluid rounded-1" alt="...">
    </div>
    <div class="col-md-9 p-2">
      <div class="card-body">
        <h2 class="card-title">{{ site.posts[0].title }}</h2>
        <p class="card-text">{{ site.posts[0].excerpt }}</p>
        <p class="card-text"><small class="text-muted">{{ site.posts[0].date | date: "%-d %B %Y" }}</small></p>
      </div>
    </div>
  </div>
</div>

<ol>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ol>

      
<!-- revue -->

<!-- 
  <div id="revue-embed">
    <form action="https://www.getrevue.co/profile/stuartelimu/add_subscriber" method="post" id="revue-form" name="revue-form"  target="_blank">
    <div class="revue-form-group">
      <label for="member_email">Email address</label>
      <input class="revue-form-field" placeholder="Your email address..." type="email" name="member[email]" id="member_email">
    </div>
    <div class="revue-form-group">
      <label for="member_first_name">First name <span class="optional">(Optional)</span></label>
      <input class="revue-form-field" placeholder="First name... (Optional)" type="text" name="member[first_name]" id="member_first_name">
    </div>
    <div class="revue-form-group">
      <label for="member_last_name">Last name <span class="optional">(Optional)</span></label>
      <input class="revue-form-field" placeholder="Last name... (Optional)" type="text" name="member[last_name]" id="member_last_name">
    </div>
    <div class="revue-form-actions">
      <input type="submit" value="Subscribe" name="member[subscribe]" id="member_submit">
    </div>
    <div class="revue-form-footer">By subscribing, you agree with Revue’s <a target="_blank" href="https://www.getrevue.co/terms">Terms of Service</a> and <a target="_blank" href="https://www.getrevue.co/privacy">Privacy Policy</a>.</div>
    </form>
  </div>
-->

      
<!-- convertkit -->
<script async data-uid="3df2bee2cc" src="https://wondrous-speaker-8686.ck.page/3df2bee2cc/index.js"></script>

