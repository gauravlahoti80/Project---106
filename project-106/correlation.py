#imoprting the modules
import plotly_express as px
import csv
import numpy as np

#making the function to get the data from the csv file
def getData(data_path):
    #making arrays
    student_marks = []
    days_present = []

    #reading the csv file
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            #appending the student marks
            student_marks.append(float(row["Marks"]))
            #appending days present of student
            days_present.append(float(row["Present"]))

    #returning the values
    return {"x": student_marks, "y": days_present}

#making a function to find correlation
def findCorrelation(data_source):
    #making a var correlation and defining it to find correlation
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    #printing the correlation of given data
    print("Correlation between Marks vs Days Present: \n-->" , correlation[0,1])

#setup function
def setup():
    #defining the data path of the csv
    data_path = "Student Marks.csv"

    #defining the data source and calling the path of the csv
    data_source = getData(data_path)

    #finding the correlation of the csv file
    findCorrelation(data_source)

#calling the setup function()
setup()
