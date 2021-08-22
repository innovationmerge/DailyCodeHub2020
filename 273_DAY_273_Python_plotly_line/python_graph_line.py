# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Plotting Different Type of Graphs

# Python program to plot Line Graph using Plotly
 
# **************** Prerequisites *****************
#        pip install plotly  
# ************************************************

import pandas as pd
import plotly.express as px
x = [10,20,30]    # X - Axis values
y = [20,30,20]    # Y - Axis values    
d = {'x': x, 'y': y}
df = pd.DataFrame(d)
print(df)
fig = px.line(df, x="x", y="y", 
              title='Plotly Line graph')
fig.show()
 
