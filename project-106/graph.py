import plotly_express as px
import csv

with open("Student Marks.csv",  newline="") as data:
    df = csv.DictReader(data)
    scatter_graph = px.scatter(df , x = "Marks" , y = "Present")
    scatter_graph.show()

with open("coffee.csv",  newline="") as data:
    df = csv.DictReader(data)
    scatter_graph = px.scatter(df , x = "Coffee" , y = "sleep")
    scatter_graph.show()