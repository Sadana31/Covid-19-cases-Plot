import pandas as pd
import plotly.express as px

df = pd.read_csv("covidData.csv")

fig = px.scatter(df,x = "Date", y = "Cases",
                color = "Country", title="Covid-19 Cases around the world")
fig.show()