# pocket-tools


## Overview
---

Pocket-tools is a simple API wrapper for link management app [Pocket](https://app.getpocket.com/). Idea of this project is to create a simple module, that will return different sets of data about your saved articles collection in json format. There is also a plan for implemating a functionality of creating new entries and modyfing existing ones.

You can use this module as a simple tool set for other applications to create more complexed automations with pocket. If you need some inspiration for how to use this tool, you can find them in this [blogpost]().


## TODO

List of functionalities to implement

* save output to file
* automatic mode - pass all variables as file
* access token generator
* retrieve artickles by tags

## How to use it
---

There are few use cases.

### **Retrieve all data from pocket account**

This operation will return json file with all information gathered in pocket (also with tags). This can be used as a backup, data dump for migration or for further processing. Issue command:

```
python3 app.py -m <consumer_key> <access_token> --get-all-data --pretty
```
