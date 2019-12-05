# Madlib CLI Game

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
This is a madlibs command line interface game. This application uses the command line interface to prompt the user for imputs like adjectives, nouns, verbs, etc. After taking in all of the necessary imputs this app returns a completed MadLibs™ style story using the user inputs!

## Getting Started

First, make sure that you have python3 installed:
```
$ python3 --version
Python 3.7.5
```
If you do not:
```
$ brew install python
```
You need to have the files locally. Click on the green clone or download button and Download ZIP:

![Click_to_download](/assets/Click_to_download_x6c0g16lz.png)


In your command line, navigate to this directory:
```
$ cd ~  ##this is your root directory
$ cd Downloads  ##by default: Downloads is a directory inside of your root; and where your file will be downloaded
$ cd madlib-cli ##and now you are in this directory
```
This application is a CLI prompt game and needs to be started in the command line in order to run.

From the file directory:
```
$ python3 madlib.py
```
A welcome message will appear. Follow the instructions. Have fun!


## Functionality/Architecture
This module requires a template file. Inside the template, required imputs are defined inside of curly braces '{ }'.
The template MadLib™ file is opened, read by a function and turned into a string usable by the module.
From the string the defined imputs are read and stored in a list to be used to prompt the user for a response.
The complete list is used to ask the user for imput, then the resulting imput is appended in the place of the imput definitions (from the template, inside of the curly braces).
After all imputs are handled, the resulting Madlib™ is printed in the CLI.
Additionally a new file, new_madlib.txt, is written in the directory with the resulting Madlib™ as its contents.

## Change Log
-- Wed Dec 04 2019 16:40:05 --<br>Built out print_and_create_madlib_file, print_intro_message, construct_the_madlib, create_list_of_inputs functions. Sucessful testing.

