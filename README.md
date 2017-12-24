# What's your Problem? - An Analysis of Urban Conditions in New York

By Cassidy Haas, Chelsea Chandler, Annika Muehlbrad, and Bryce Wilson


Introduction:
New York is one of the largest metropolitan areas in the United States; it is home to more than 8 million people of diverse heritage, age, identity, and interests, and more than 2 million businesses. As a melting pot, the city frequently experiences friction between its inhabitants. New York City (NYC) officials receive thousands of 311 service requests a day, and hundreds of complaints are filed with the New York City Police Department (NYPD). By reporting these complaints, inhabitants are providing a detailed account of the conditions of urban life. So what is urban life like in New York City?
To explore this question, local government, newspapers, and journals have investigated New York City’s urban condition. The New York Times has looked at the city’s noise distribution, I Quant NY investigated NYC property taxes, and the New York City Department of Health and Mental Hygiene has tracked air quality over several decades. While these are interesting factors to explore, the analysis of these individual conditions reveals little about urban life in the city. 311 service call data and NYPD complaint data offer insights about the city’s daily hustle and bustle by exposing residents’ accounts of the city’s affairs. Analyzing this data can inform us about the urban condition, about urban trends and unique events.
This project seeks to explore the urban condition of New York City through an in depth analysis of 311 service call data and NYPD complaint data. We plan to analyze and map the spatial and temporal distribution of residents’ complaints to asses which NYC neighborhoods offer the best living condition. We also want to  provide strong association rules on resident behavior. By understanding normal patterns of behavior, we can make inferences about anomalies and assess if these anomalies correspond with specific events. 

Contents of the Project Repository:

Correlation: Contains all work pertinent to correlation analysis. This includes an R script for finding correlations and an assortment of visualizations created from the output of this analysis.
    
Outlier_analysis: Contains all the work pertinent to exploring outliers. In particular, scripts for performing k-Nearest Neighbor clustering and various mulitvariate distribution plots in JMP Pro 13.0. It also contains a number of visualizations of the analysis.

subsets_work: Contains all work pertinent to subsets analysis. Specifically, it includes a viz folder that holds all visualizations made, a folder of shapefiles used to visualize the data, and an assortment of .py and .ipynb used for data exploration.

Zipshape: Contains shapefiles used to create spacial distribution visualizations by New York City zipcode.

Base Level Directory: Contains all of the scripts for loading the data into MongoDB and performing data preprocessing, namely filling in missing values, removing tuples, and removing attributes. It also contains spatial distribution visualization scripts and some preliminary visualizations.
