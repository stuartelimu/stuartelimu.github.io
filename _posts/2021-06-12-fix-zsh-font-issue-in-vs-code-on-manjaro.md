---
layout: post
title:  "How to fix zsh font issue in VS Code on Manjaro Linux."

---

# How to fix zsh font issue in VS Code on Manjaro Linux.

One of the things I love about using Manjaro Linux is the zsh terminal. It's quite a whole vibe having auto complete and some really nice icons in the terminal.

When I installed VS Code, I was shocked that the integrated terminal wasn't looking as nice as the one on my terminal. I found this really odd and unpleasant. I did try to find a solution and I came across this article and this solution on stackoverflow.

I got to know the problem; which was VS Code had a default font family for the integrated terminal. Now all the solutions above require us to download a new font family but I didn't see it necessary since I was comfortable with the font family my terminal was using. 

Alright, I then had to figure out which font was being used in the terminal. A casual google search didn't yield much of a result but I have customized my terminal more than a few times. 

I opened my terminal and clicked on the more context menu on the top right of the window. Then I clicked on Preferences

In the Preferences window, I clicked the 'manjaro' profile and there it was, the default font family used for the terminal. I copied this and opened vs code
![Screenshot from 2021-07-06 18-06-18](https://user-images.githubusercontent.com/41069456/124642390-77b9e980-de98-11eb-9e8e-8a66451807ae.png)


I love using keyboard shortcuts, 
I will open `User Settings` by pressing `CTRL + Shift + P` then typing `settings`, select `User Settings` from the dropdown menu.

Using the search bar on the settings page, type `integrated terminal` and scroll down to `Font Family` section, then paste my copied font family; in my case it was `NotoSansMono Nerd Font`

Open the integrated terminal using CMD + P. the font issue should be fixed now.

![Screenshot from 2021-07-06 18-17-17](https://user-images.githubusercontent.com/41069456/124626401-4f75bf00-de87-11eb-9091-73c567edea49.png)
