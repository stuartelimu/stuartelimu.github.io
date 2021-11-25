---
layout: post
---

# How to handle multiple images using django-rest-framework

We were tasked to handle multiple images using django rest framework. The images could come from front end reach or mobile flutter and should be handled as is 

I’ll use an existing model 

We Ser the image field to be a text field such that it can have a link to the image file let’s say saved on cloudinary 

We can now create our serilzer we overdue the field to be a list field such that it can take a list of char fields 

We’ll create a view that will handle image creating 
I’ll use the list o create view which will allow me to use both post and get methods to the same url 

When we post , looks good. We can post multiple images 

But when we run a get request . Oh my what’s this it seems the images but they’re strings 

Let’s inspect what’s going on here, when we open the terminal 

We can clearly see the iMage field is saved as a string but what causes the rest 

When we try to convert the string to list , we’ll looks firmiliar to the postman response 

So this happens in the serializer so how do we handle this ; we’ll create a separate serializer to handle get 

This serializer wil keep the fields as is 

We can now edit our views and override the get serializer method and determine what serializer is used depending on the type of request 

We can check with postman and this has been solved. 

If you found this helpful. Do share a way you have Haskell multiple images 
