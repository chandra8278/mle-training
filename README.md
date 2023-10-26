#This change is for the Pull request

# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data. 

The following techniques have been used: 

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## How to install the package and import the methods
1. Install the package name = housing-library-5512==0.1 
 >> pip install housing-library-5512==0.1
2. In code file use these statements to import the required methods.
 >> from src import fetch_housing_data, load_housing_data
 >> 