# ubuntu_cli

At the time of this repository creation, Ubuntu is my primary OS. 

I also like using CLI, as well as automating my workflow. 

This results in various scripts using Ubuntu Terminal as the primary interface.

Below is a collection of such scripts.

<div align=center margin=auto> 
  <img src="images/timer_sample.png" width=80%>
</div>


## Table of Contents
1. [Prerequisites](README.md#prerequisites)
2. [Installation on Linux](README.md#installation-on-linux)
    * [Standard dependencies](README.md#standard-dependencies)
    * [Repository import](README.md#repository-import)
    * [Project-specific dependencies](README.md#project-specific-dependencies)
3. [Script descriptions](README.md#script-descriptions)
    * [timer](README.md#timer)
    * [update_sw](README.md#update_sw)
3. [How to run](README.md#how-to-run)


## Prerequisites
To run the program, you need the following components installed:

**Standard dependencies**
- Python 3.x
- Git 

**Project-specific dependencies**
- speech-dispatcher (for the timer to announce the end of a countdown; should be preinstalled in Ubuntu 14.04+)


## Installation on Linux

### Standard dependencies
Please refer to the corresponding official sources for:
- Python: https://www.python.org/downloads/
- Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

### Repository import
- Go to the directory you'd like to have this repository in and open the 
directory in terminal
- Enter the following command:

```
>>> git clone https://github.com/okharkevych/ubuntu_cli.git
```

### Project-specific dependencies
Enter the following command:

```
>>> sudo apt-get install -y speech-dispatcher
```


## Script descriptions

### timer
- A simple CLI countdown tool
- Upon script execution, a small dedicated terminal window 
is opened for user input and countdown tracking (accordingly, it only works if 
GUI is available)
- User can specify an optional timer name (useful when running a number of such 
windows simultaneously), as well as the number of hours/minutes/seconds for the 
countdown
- When the countdown is over, the corresponding feedback message is printed, 
and its text is voiced via text-to-speech tool to attract additional attention
- The script is based on the code from https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html

### update_sw
- All the commands I use to update system components gathered in one place:

```
snap-store --quit
sudo snap refresh
sudo apt update
sudo apt upgrade -y
sudo apt-get update
sudo apt-get upgrade -y
sudo apt autoremove -y
```
- Most of the commands are commonly used ('refresh'/'update'/'upgrade'), as far 
as I am aware.
- The 'autoremove' command isn't 100% safe in this situation as you automatically 
confirm the removal of all the dependencies marked as no longer used by the system; 
there may be a situation where you want to keep a package installed as a dependency
despite its main package having been deleted already. I haven't had any issues with
autoremoving everything suggested; however, if you feel more comfortable checking
the list of the packages to be removed, better remove that ' -y' next to 'autoremove'
in modules/update_sw.py
- The uncommon one among these commands is 'snap-store --quit'. On multiple occasions,
my app/package updates have been interrupted or simply failed to start due to 
Snap Store processes running in the background. Hence, this addition to the script.

## How to run
- Open ubuntu_cli directory downloaded earlier in terminal
- Enter the following command:

```
>>> python3 -m scripts.script_name
```
