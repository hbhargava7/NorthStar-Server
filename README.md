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

Crime Function
--------------
To find the crime risk at a particular location p, we look for crimes in a 100m radius and estimate a risk factor according to the equation:

![Gaussian Kernel](https://github.com/hbhargava7/NorthStar-Server/blob/master/images/Screen%20Shot%202016-11-13%20at%201.36.07%20AM.png) 

The risk along an edge of the graph is the integral over 1m segments along the edge. 
We route on a graph of Berkeley that takes into account the function above. 

Data Collection and Routing 
---------------------------
* Crime data from [Berkeley Open Data](https://data.cityofberkeley.info/Public-Safety/Berkeley-PD-Calls-for-Service/k2nh-s5h5)
* `CrimeDataParser.py` for parsing data from Berkeley Open Data API
* `CrimeDataParser2.py` for parsing json output from Berkeley Open Data
* `MapDataParser.py` for storage of nodes and edges in dictionaries, data from [OpenStreetMap](https://www.openstreetmap.org)
* `Routing.py` for A-star search algorithm. The function returns three different paths:
  * Path of shortest length (ignoring risk)
  * Safest path (weighing risk function heavily)
  * Optimal path (weighing both distance to destination and risk intelligently)
* `Utils.py` for Crime Density function and Haversine conversion 
  * The Haversine formula converts from degrees to meters, used for segmentation of edges:
  
   ![Haversine](https://github.com/hbhargava7/NorthStar-Server/blob/master/images/Screen%20Shot%202016-11-13%20at%201.55.29%20AM.png)
   
Dependencies
------------
This application relies upon the following dependencies, which are intended to be fully managed by `virtualenv` and `pip` (see Configuration):
* `numpy` for general mathematical computations
* `matplotlib` for graphics generation and data visualization
* `lxml` and `osmread` to read OpenStreetMap json files
* `mysql` to set up database and retrieve relevant information


