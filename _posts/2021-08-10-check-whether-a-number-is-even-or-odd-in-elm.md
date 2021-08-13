---
layout: post
---

# Check whether a number is even or odd in Elm

In this article I will be covering Elm basics using a simple program which checks whether a given number is even or odd.

Since this is a simple program, I will be using `elm repl`

Open your terminal and type `elm repl`

You should see the elm prompt.

![](/assets/images/Screenshot from 2021-08-13 03-14-34.png)

Elm uses the modBy function to perform modular operations. In the documentation it clearly states we can use this as a shortcut to find even or odd numbers.

Add the following code to elm repl


![](/assets/images/Screenshot from 2021-08-13 03-21-32.png)

We define a variable number, then pass it to modBy as well as an integer 2. Even numbers are numbers divisible by 2 with no reminder.

We can exit the elm repl ny typing `:exit`

![](/assets/images/Screenshot from 2021-08-13 03-23-11.png)

