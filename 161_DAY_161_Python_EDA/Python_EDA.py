# "iNNovationMerge DailyCodeHub"

# Theme : Exploratory analysis week with python

# Exploratory Data Analysis using python Autoplotter

# pip install autoplotter

from autoplotter import run_app
import plotly.express as px
import pandas as pd
df = pd.read_csv('IOT-temp_1000.csv')
run_app(df)

