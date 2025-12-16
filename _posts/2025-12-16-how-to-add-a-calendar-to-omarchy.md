---
layout: post
title: How to Add a Calendar to Omarchy 
---
Unlike windows or even MacOS, the default expectation when you click on the clock is that the calendar is displayed or something of the sort but this doesn’t happen for Omarcy. Instead, a click toggles a different date format which includes the week and month. 

In fact, if you search for the term calendar in the Omarchy manual, you’ll be hit with the recommendation to use HEY, an email and calender service but I’m not comfortable signing up for that yet. 

I wasn’t sure what calendar app to install but I came across this [post](https://x.com/raphaelschaad/status/1999104234432733460) on twitter showing how modern day TUIs had gotten incredibly good and one of them was a calendar. So I figured I could give opt for a TUI given that Omarchy already has a couple of TUIs that I like already. 

I did a simple google search and settled on calcure. then when I went to search for a tui I can use one that I’d seen on the post popped up

### Installation  
Calcure has an AUR package available so using the Omarchy Menu (Super + Alt + Space) and go to Install > AUR . .  then type calcure and press enter. Upvote to support the project!

Once the installation is complete, open your terminal and type calcure and you have a beautiful calendar. 

Customization
Omarchy uses Impala TUI to manage WIfi and you can open when you click the wiif icon.. so we can follow the same pattern. Under the Dotfiles section in the Omarchy manual we can see `~/.config/waybar/config.jsonc`  controls the top bar.

This is my first time working with dotfiles so I copied everything and pasted it in Claude then I prompted it until I got the desired result.

We need to add an on-click action to your clock module.

```
"clock": {
  "format": "{:L%A %H:%M}",
  "format-alt": "{:L%d %B W%V %Y}",
  "tooltip": false,
  "on-click": "omarchy-launch-or-focus-tui calcure",
  "on-click-right": "omarchy-launch-floating-terminal-with-presentation omarchy-tz-select"
},
```

We also need to get rid of the alt text, you can simply comment it out or delete the line entirely

```
"clock": {
  "format": "{:L%A %H:%M}",
  "tooltip": false,
  "on-click": "omarchy-launch-or-focus-tui calcure",
  "on-click-right": "omarchy-launch-floating-terminal-with-presentation omarchy-tz-select"
},
```
You'll need to restart wayland for this to work

Now when we click on the clock, it launches calcure which is perfect but we can make it better, we need it to open right in the center of the screen and not in a different full sized window

```
"clock": {
  "format": "{:L%A %H:%M}",
  "tooltip": false,
  "on-click": "omarchy-launch-floating-terminal-with-presentation calcure",
  "on-click-right": "omarchy-launch-floating-terminal-with-presentation omarchy-tz-select"
},
```
After making this change, reload Waybar again. This should give it a similar floating window style to the wifi window.

I like the clock to have day, date, month and time so let us format of the time as well
```
"clock": {
  "format": "{:%A, %d %B %H:%M}",
  "tooltip": false,
  "on-click": "omarchy-launch-floating-terminal-with-presentation calcure",
  "on-click-right": "omarchy-launch-floating-terminal-with-presentation omarchy-tz-select"
},
```

If you've followed everything untill this point and restarted wayland, you should have something like this when you click the clock in the top bar. 

<img width="1920" height="1080" alt="screenshot-2025-12-15_21-01-54" src="https://github.com/user-attachments/assets/daace82d-c2fb-4b86-8dfd-d51392c9bc33" />


You can also make a couple of changes to calcure this file

### Conclusion.
It has been a while since I did something like this and honestly it felt good solving this as it was weirdly getting annoying each time I wanted a calendar I had to open google calendar or reach for my phone. This is one of those things that makes Linux ( and open source in general ) so cool, if there’s something annoying, you can fix it.

This is now at a good place but later on I’d honestly like to sync my google calendar but this should work for now.  Also when you click the clock more than once, it launches calcure even when it's open already, I'll need to figure out a fix for that.

That's all for now, cheers!



PS: I didn’t know the right click on the clock triggered the timezone selection until I went through this exercise. 
