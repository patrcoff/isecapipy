# ISECAPIPY README

## DISCLAIMER: This project is in pre-alpha stage, end users should not attempt to implement this project in live environments!

Contributers, please review the 'planning' folder and dev-notes.rst

## Installation

As is customary in the modern Python world, I would highly recommend first setting up a virtual environment before installing any dependencies or the package itself. My personal preference and what I use in actual development is to simply use `python -m venv .venv --prompt a_nice_prompt_name_here` which works nicely with vscode. '.venv' and 'venv' are both included in the gitignore file, if you wish to use a different name for your venv and locate it within the project strucutre, please add your venv directory name to the gitignore file before committing any changes!

Installation will soon be possible using `pip install isecapipy` once version 1.0.0 is defined and packaged. Until then, if you require to work on the project (you should only do so if you wish to contribute to the project for the time being) then you should simply git clone the repo and install dev-requirements.txt with `pip install -r dev-requirements.txt` from the main project folder location. You can then install the package in editable mode with `pip install -e ./isecapipy` again from the project folder.


## A Simple Example

```py
import isecapipy

isec = isecapipy.handler(auth_type = 'kerberos', console_fqdn = 'uwm-isec-01.uwm.local')

agents = isec.agents.get()  # returns a list of AgentDetail instances

for agent in agents:
    isecpipy.checkin(agent)
    isecapipy.

#> 123
```

## Requirements

