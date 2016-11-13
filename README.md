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
To find the crime risk at a particular location p, we look for crimes in a 100m radius and estimate a risk factor according to the equation:
![Gaussian Kernel](https://github.com/hbhargava7/NorthStar-Server/blob/master/images/Screen%20Shot%202016-11-13%20at%201.36.07%20AM.png)
The risk along an edge of the graph is the integral over 1m segments along the edge. 
We route on a graph of Berkeley that takes into account the function above. 
