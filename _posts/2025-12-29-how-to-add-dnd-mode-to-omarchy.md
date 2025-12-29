---
layout: post
title: How to add DND mode to Omarchy.
---
I have been using web apps in Omarchy for all of the messaging apps that I use. Unfortunately there's no built in way to mute the desktop notifications other than disabling them from the web app settings from the browser. This approach isn't sustainable if you've a couple of web apps.

I was looking for something similar to what is on MacOS, a DND mode which when toggled will enable/disable all notifications.

Omarchy uses [mako](https://github.com/emersion/mako) to handle notifications and comes with only one mode by default, which is coincidentally called `default`. 

Checking the man page, mako allows us to add various modes using the command:

```
makoctl mode -a <mode>
```

We will name our mode `do-not-disturb` and add it with the following command:

```
makoctl mode -a do-not-disturb
```

The output of the command should look similar to this, which indicates we now have two modes we can work with.

```
default
do-not-disturb
```

Additionally we can remove a mode with the following command:

```
makoctl mode -r do-not-disturb
```

And finally we can toggle a mode using the following command. It will add the mode if not present, and remove the mode if present. This is the command we're going to use

```
makoctl mode -t do-not-disturb
```

### Configure Mako for DND Mode
Right, now that we can toggle our `do-not-disturb` mode, we need to actually silence the notifications. 

Add this to `~/.config/mako/config` to make notifications invisible in `do-not-disturb` mode:
```
[mode=do-not-disturb]
invisible=1
```

Then reload `mako` from the terminal:
```
makoctl reload
```

We can manually test this using the `notify-send` daemon, run
```
# toggle do-not-disturb mode 
makoctl mode -t do-not-disturb 

# Test notification (should be hidden if do-not-disturb mode is on) 
notify-send "Test" "Should be hidden"

# toggle do-not-disturb mode 
makoctl mode -t do-not-disturb 

# Test notification (should appear if do-not-disturb mode is off) 
notify-send "Test" "Should appear"
```

### Configure Omarchy for DND

We need to add a visual indicator and a way to toggle our `do-not-disturb` mode from the top bar.

Add this configuration to your `~/.config/waybar/config.jsonc` dotfile.

```
"custom/dnd": {
  "format": "{}",
  "exec": "<path-to-file>",
  "on-click": "makoctl mode -t do-not-disturb && pkill -RTMIN+10 waybar",
  "interval": 1,
  "signal": 10,
  "return-type": "json"
},

```

I want our `do-not-disturb` icon to sit on the right side of our top bar so we can easily see if it's on or off so I'll place it right next to the battery indicator icon. 

```
"modules-right": [
  ...
  "custom/dnd",
  "battery"
],

```

### Create the Script

We need to create a shell script to toggle our `do-not-disturb` mode. I have a folder `~/.local/bin` where all my scripts live, you can create a similar folder so use a separate folder. 

Create a file called `dnd-indicator.sh` in the folder and add the following commands

```
#!/bin/bash

if makoctl mode | grep -q "do-not-disturb"; then
  echo '{"text": "  ", "tooltip": "Do Not Disturb: ON\nClick to toggle", "class": "dnd-on"}'
else
  echo '{"text": "  ", "tooltip": "Do Not Disturb: OFF", "class": "dnd-off"}'
fi

```

We need to make it executable: 
```
chmod +x ~/.local/bin/dnd-indicator.sh
```

Restart Waybar (`pkill waybar && waybar &` or log out/in) to apply changes.

The top bar should now look something like this, you can click on the bell icon it to toggle DND.

<img width="1920" height="1080" alt="Pasted image 20251229174127" src="https://github.com/user-attachments/assets/634f7845-243b-4bb6-b474-0e8219088f5e" />


### Recommendations
I have not tested this with other installed applications other than the browsers but it works fine. Here's a couple of things we'd do to make this even better.

#### Indicator Icons
You can [search](https://www.nerdfonts.com/cheat-sheet) for different icons and choose which best fits your style. MacOS uses the suculent moon but I couldn't find a filled version of it.

#### Allow Critical Notifications
We can choose which notifications can bypass our `do-not-disturb` mode. Our mako configuration would look like this `~/.config/mako/config`

```
[mode=do-not-disturb]
invisible=1

[mode=do-not-disturb urgency=critical]
invisible=0
```

#### HotKeys
We can add a keyboard shortcut to turn on/off our `do-not-disturb` mode. 

### Conclusion
This was another fun piece to write, even a more fun thing to do especially during the holidays. I hope you found it useful & practical in case you were looking for something similar. Let me know if you have come across any other approach. Cheers!
