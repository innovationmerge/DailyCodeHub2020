#  iNNovationMerge

# pip install autoplotter


from autoplotter import run_app
import plotly.express as px
import pandas as pd
df = pd.read_csv('IOT-temp_1000.csv')
run_app(df)

