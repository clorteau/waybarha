
A module for [Waybar](https://github.com/Alexays/Waybar) that can show and toggle sensors from Home Assistant

![screenshot](https://github.com/clorteau/waybarha/blob/main/.github/screenshot.png?raw=true)

# Dependencies
- Python
- Home Assistant with enabled Rest API <em>([link1](https://developers.home-assistant.io/docs/api/rest/) and [link2](https://www.home-assistant.io/integrations/api/) to the docs)</em>

# Download

Download [waybarha.py](https://raw.githubusercontent.com/clorteau/waybarha/refs/heads/main/waybarha.py) anywhere you have permission to read it

# Usage
Edit the file to set your server's URL and the access token.

In your waybar's .jsonc, add one entry per entity you want to read/toggle. Examples:
```
 "custom/ha1": {
    "format": "󰌵 {text}",
    "exec": "/path/to/waybarha.py switch.lamp",
    "on-click": "/path/to/waybarha.py --toggle switch.lamp",
    "return-type": "json", /* this script outputs json; if you omit this the label will be a json output*/
    "interval": 5
  },
  "custom/ha2": {
    "format": "󰌵 {text}",
    "exec": "/path/to/waybarha.py switch.floor_lamp",
    "on-click": "/path/to/waybarha.py --toggle switch.floor_lamp",
    "return-type": "json",
    "interval": 5
  },
  "custom/ha3": {
    "format": "  {text}",
    "exec": "/path/to/waybarha.py sensor.2022_santa_cruz_fuel_level",
    "return-type": "json",
    "interval": 600 // 10 minutes
  }
```
_Hint: if "format": "󰌵 {text}" has a square instead of a proper character you need to install and use a [nerd font](https://www.nerdfonts.com/)._

This plugin exposes the entity's state as 'text', unless the entity's name starts with "switch" in which case the on/off states are exposed via css classes for styling.

Example of `style.css`:
```
#custom-ha1 {
	background: @background-primary;
	color: @sapphire;
	border-left: 4px solid @sapphire;
	margin: 6px 0;
	padding: 8px 12px;
}
#custom-ha1.on {
	background: @sapphire;
	color: @background-primary;
}
#custom-ha1.off {
	opacity: 0.7;
}
#custom-ha2 {
	background: @background-primary;
	color: @teal;
	border-left: 4px solid @teal;
	margin: 6px 0;
	padding: 8px 12px;
}
#custom-ha2.on {
	background: @teal;
	color: @background-primary;
}
#custom-ha2.off {
	opacity: 0.7;
}
#custom-ha3 {
	background: @background-primary;
	color: @lavender;
	border-left: 4px solid @lavender;
	margin: 6px 0;
	padding: 8px 12px;
	border-radius: 12px 0 0 12px;
}
```

The script takes 2 arguments:
- optional - - toggle means this is a switch to toggle and can be omitted
- the entity's id

```
./waybarha.py --help
usage: waybarha.py [-h] [-t] entity

Waybar home assistant module to query/toggle an entity

positional arguments:
  entity        entity to read or toggle - ex: 'switch.lamp'

options:
  -h, --help    show this help message and exit
  -t, --toggle  toggle entity on/off; entity's state will be read if omitted
```




