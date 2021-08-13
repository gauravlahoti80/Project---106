#importing the modules
import plotly_express as px
import csv
import numpy as np

#making a function to read the csv
def getData(data_path):
    #making arrays
    coffee_in_ml = []
    sleep_in_hour = []

    #opening the csv
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)

        #making a for loop
        for row in csv_reader:
            #appending 
            coffee_in_ml.append(float(row["Coffee"]))
            sleep_in_hour.append(float(row["sleep"]))
    
    return {"x" : coffee_in_ml, "y": sleep_in_hour}

#making a function to find correlation
def findCorrelation(data_source):
    #defining a var to find correlation
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    #printing the correlation
    print("Correlation between Coffee in ml vs sleep in hour: \n-->" , correlation[0,1])

#setup function
def setup():
    #giving the path of the csv file
    data_path = "coffee.csv"
    #getting the data from the csv file
    data_source = getData(data_path)
    #calling the correlation function and findind the correlation
    findCorrelation(data_source)

#calling the setup function   
setup()