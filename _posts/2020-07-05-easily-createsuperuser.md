---
layout: post
---

Easily create a superuser for your django project using this simple line. 

I found this trick on the Quickstart guide from the django-rest-framework [docs](https://www.django-rest-framework.org/tutorial/quickstart/) 

```
$ python manage.py createsuperuser --username admin --email admin@example.com
Password: **********
Password (again): **********
Superuser created successfully.
```

I originally wrote this as a gist and used [gist.io](https://gist.io/) to [publish it](https://gist.io/@stuartelimu/53258c427310bdfce430deac39971e93). It's a really nice utility
