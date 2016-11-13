# SafeNavigation-Server
This repository contains the backend components of the SafeNavigation app project.

Configuration
------------
This project was developed using `virtualenv` to manage Python dependencies. Environment can be initialized from the root directory by:
```
source virtualenvironment/bin/activate
```
To exit the virtual environment:
```
deactivate
```

Dependencies
------------
This application relies upon the following dependencies, which are intended to be fully managed by `virtualenv` and `pip` (see Configuration):
* `numpy` for general mathematical computations
* `matplotlib` for graphics generation and data visualization
* `lxml` and `osmread` to read OpenStreetMap json files
* `mysql` to set up database and retrieve relevant information

Crime Function
--------------
Given a crime function $f(x)$
