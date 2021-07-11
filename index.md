# Hello, world!

[Readme](./README) - [Books](./books/reading-list)

1. [How Fix zsh font issue in VS Code on Manjaro](./articles/fix-zsh-font-issue-in-vs-code-on-manjaro)
2. [How I am using Github for Blogging in 2021](./articles/using-github-for-blogging)
3. [Test](./articles/test)

<ol>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ol>
