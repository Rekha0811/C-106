import pandas as pd
import plotly.express as px
import csv
df = pd.read_csv('data.csv')

fig = px.scatter(df,x="Temperature", y="Ice-cream Sales( ₹ )")
fig.show()