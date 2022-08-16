# Surfs_Up

## Project Overview: 
An analysis of June and December weather for Oahu, HI using SQLAlchemy to access a SQLite weather database.

## Background:

Our Investor "W. Avy" is considering opening a `Surf and Ice Cream shop in Oahu, HI.` In the past, he has invested in similar business opportunites which failed due to inclement weather. He has asked for a weather anaylsis of Oahu, specifically in the months of June and December to determine if this would be a viable investment year round. His business decision rides on the statistical analysis we will provide in this project.

<br />

<p align="center"> 
<image src="Images/Oahu.jpg" width= "70%" height="50%"

<br />


## Outline: 

`SQLAlchemy` was used to connect and generate the queries needed to pull out neccessary information from the `SQLite` wheather database (`"hawaii.sqlite"`) we were provided. Below is a sample of the dependencies and functions that were used to access the SQLite database and start our weather analysis.

<br />
<p align='center'>
<img src="Images/initial_code.png" width=/>

<br />

# June Weather Statistics:

The average temperature for June in Oahu, HI is 74.9°F <br />
- The highest temperature recorded was 85°F
- The lowest temperature recorded was 64°F
- Temperatures in June had a range of 21°F
<br />

<p align='center'>
<img src="Images/june_temp_stats_summary.tiff" width=250/> <img src='Images/june_temps_hist.png' width=625/>


<br />

# December Weather Statistics:

The average temperature for December in Oahu, HI is 71.0°F <br />
- The highest temperature recorded was 83°F
- The lowest temperature recorded was 56°F
- Temperatures in December had a range of 27°F

<br />

<p align='center'>
<img src="Images/dec_temp_stats_summary.tiff" width=275/> <img src='Images/dec_temps_hist.png' width=625/>

<br />
<br />

# Temperature Observation (TOBS):

I analyzed the number of weather stations that were actively collecting data. There was a total of (9) weather stations. Station USC00519281 showed the highest number of observations, therefore I graphed its recorded weather for a better visualization of the data. 

<br />

<p align='center'>
<img src="Images/temp_observ(tobs).png" width=/>

<br />
<br />

# Incorporating `Flask` into the Data Analysis:

<br />

I created the `app.py` python file to run a Flask application that easily allowed the sharing of my findings in an easy-to-interpret way. The code written for this task is below as well as the resulting website for the Flask routes created and the data it queried. 


<p align='center'>
<img src="Images/flask_code.png" width=550/> <img src="Images/webpage_flask_results.png" width=550/>



## Summary: <br />

This analysis has helped W.Avy determine that Oahu, HI is an ideal location to open his Surf n' Shake shop. The data from June and December weather suggests that there is no dramatic fluctuation in temperature throughout the year. This further supports that this investment would be a viable business year-round.


<br />

## Resources:

- hawaii.sqlite (Weather DataBase located in Resources folder)
- Software: Jupyter Lab, Pandas, Python, SQLite, SQLAlchemy, VS Code, FLASK, JSON, Matplotlib




