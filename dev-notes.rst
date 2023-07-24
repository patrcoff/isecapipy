A place for the devs to discuss project plans
=============================================

(This file was created early in the project's initial planning stage and was intended as a guide to a former colleague of mine.
As they no longer work with me and collaboration with colleagues is not currently forseen then this file may now be redundant and any useful content from it moved to newer planning documents or parts of the readme in general.
Anyone who does wish to contribute to the project however is encrouraged still to do so.)

A note to the public - if anyone happens across this project.

I am now a former TSE for Ivanti, having supported the product 'Ivanti Security Controls' (often referrd to simply as ISEC), and Gary is a former colleague who has moved on, but as chance has it, is now a customer of Ivanti's (and he will be responsible in his company for the administration of their ISEC instance)

As we are both keen to improve our programming experience (and Python is the best language, sorry-not-sorry), we thought a joint project to wrap the ISEC REST API would be a good first collaborative project for us both. This will provide the benefits of having both Ivanti Support and customer points of view, which will hopefully inspire a useful product which could be used by other users of ISEC hoping to automate tasks via the REST API using the Python language.

-----

.. note::
    **DISCLAIMER**

    It is important to note that while I am a **former** employee of Ivanti, this project is by no means affiliated with Ivanti (the company) in **any** way. It is solely an open source project, worked on in a voluntary capacity by the core contributers, outside of employed working hours. This project is not endoursed, sponsored or paid for in any way by Ivanti, or any other organisation.
    It is an opinionated implementation of the ISEC REST API and has no direct conenction to the developers of ISEC itself.
    We cannot guarantee this project will cause no damage to a production system and this module should only ever be used by professionals capable of understanding the code as well as the basic inner workings of the ISEC console itself. It is advised to perform extensive testing prior to implementing any code which makes use of this module.

-----

Useful Links and references
***************************

+---------------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Name                            |    Description                                                                      |  Link                                                                                                      |
+---------------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Python REST API Wrapper Tutorial|  An in depth guide on how to plan and implement a python wrapper for a REST API     | https://www.pretzellogix.net/2021/12/08/step-1-read-the-docs-and-use-postman-to-understand-the-rest-api/   |
+---------------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Collaborating on github         |  Youtube video outlining basic workflows to collaborate on github                   | https://youtu.be/HbSjyU2vf6Y                                                                               |
+---------------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| RestructuredText references     |  A decent resource for RestructuredText syntax (like what this is written in)       | https://docutils.sourceforge.io/docs/user/rst/quickref.html#section-structure                              |
|                                 +-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
|                                 |  A second resource which is specific to a certain platform but is still useful      | https://sublime-and-sphinx-guide.readthedocs.io/en/latest/indices.html                                     |
+---------------------------------+------------------------------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------+
|Good intermediate -> advanced    |  Al Sweigart is one of the best Python educators,    |Beyond the basics video course| https://youtu.be/VihLgySA6wU                                                                               |
|                                 |  catering to a wide range of                         +------------------------------+------------------------------------------------------------------------------------------------------------+
|Python resources                 |  abilities and he communicates very well.            |Beyond the basics book (free) | https://inventwithpython.com/                                                                              |
|                                 |  He has several books, all available for free and    |                              |                                                                                                            |
|                                 |  some youtube courses based on his books.            |                              |                                                                                                            |
+---------------------------------+------------------------------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------+
|Understanding python import      | How a module can be imported depends on a few different things, such as where the   | https://youtu.be/v6tALyc4C10                                                                               |
|statement and packaging modules. | module is installed, or if it simply exists in the current directory etc.           |                                                                                                            |
|                                 | All of this is explained well by this realpython code conversation video.           |                                                                                                            |
+---------------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

How to use this file
********************

First, it would be a good idea to get a little understanding of how RestructuredText works and research some tools which can be used to parse/view RestructuredText.

RestructuredText is a markup language (like HTML but nicer) which is designed to be readable both in it's raw form, but be parsable by various tools to be displayed nicely in a viewer or web browser.

For example, you can generate static websites using a static site generator (SSG) such as the python 3rd party module pelican - which will take in rst files and output themed HTML

Github itself will automatically attempt to parse files ending with the .rst extension when viewed on github.com in the browser. That is why I have chosen this format for this document.

However, the syntax does need to be followed, for example it is very easy to break the table above by ommiting one of the boarder characters. This will result in the unparsable component not showing on github.com unless you view the raw text.

Therefore, if you make any changes to any of the rst files in this project, you should verify they are parsable before committing to github. I'm sure there are some simple tools to validate via a quick commandline command but if like me you also want to
see the formatted text to confirm it looks like you expect (as I am also learning the syntax myself), then a live viewer tool would be better.

I am using the python module "restview" - https://pypi.org/project/restview/

You can pip or pipx install it into your environment or virtual environment and use it to dynamically preview the file in the browser.

Once installed, you simply call "restview [filename.rst]" from the commandline (or "py -m restview [filename.rst]" if you have issues modifying your PATH evnironment variables on a system you don't fully control) and it will open a live preview in the browser.

When you make changes to the file it will auto refresh. It also will highlight errors in the text with really useful messaging to fix them.

-----

Tips:

- Any useful resources you find, remember to add them to the table in the first section (also, please keep this reference table as the top section of this file)
- Remember to always preview your edits using a tool such as restview prior to comitting
- Can't think of any off the top of my head right now but I'm sure I'll think of more. If you've any questions and your name is in ['Gary', 'Emmannuel'], just shoot me a message. Else: google it, lol.

-----

Project structure explanation
*****************************

- The top level dir "isecapipy" is the "project folder" which contains both the code, packaging tools, info for devs and metadata
- "src" is where the main code will live (core project code inside src/isecapipy). I understand this may look a little confusing at first but it is a fairly common structure used on collaborative projects and projects designed to be packaged (which is ultimately my plan)
- Why would we package it? Ivanti customers are not going to want to just clone the repo, this adds a few too many hurdles creating a barrier of entry. A pip installable package makes life much easier for the end user.
- to begin with, I propose we perform some initial testing and proof of concepts in the folder src/planning in order to keep this code separate from the actual project
- pyproject.toml is used for making the module installable via pip locally from the source code (see link in table for 'understanding python import statement...') (and later for creating a package we can upload to pypi so it can be pip installable anywhere)
- Inside src/isecapipy/__main__.py will be the main entry point to the module - this is a common convention for python applications and although not necessary for modules if they are to be solely imported into other python code, it will allow us to add a commandline usage of the module. For example, a "test-connection" command to confirm the API can be reached or some one-liner tasks like "patch x_machinegroup" etc

-----

Below this point is not yet formatted nicely, just taking some notes for now as I think of them but will organise better later on!

-----

useful dev workflows, commands, tools etc



    py -m venv venv --prompt isecapi 

    venv/source/activate

    restview - python module for viewing restructured text (rst files) so you can preview on the fly before commiting changes to this file


-----

Stage One Plan
==============

The core deliverable initially is to simply make a 1-1 mapping of the ISEC api endpoints in a python module wrapper complete with parameters, json body field mappings and accepted request methods for each API endpoint.
This should also contain tests (within the module but not the type of tests which would run pre-commit when we get to that stage of CI/CD) which verify the current version of the wrapper is not behind the current version of ISEC in terms of available 
Initial plan is to support the latest version of the console's API at any point in time, backword compatability work will be handled in a later stage


Desirable features for future stages
====================================

- Implement commonly requested Workflows, examples below
    - Patch to zero feature (if this isn't included for Windows in 2023.3)
    - Trigger patch scan of x machine group based on y scan template 
- Implement automations of existing GUI workflows which currently need to be performed manually, examples below
    - Generate patch group based on 'smart filter' type logic.
    - Return list of machine objects based on 'smart filter logic'
    - ...
- Simple interface for automating/scheduling the reassignments of agent policies
- Local SQLite db of console config for quick referencing without using API - to be synced periodically or prior to specific tasks