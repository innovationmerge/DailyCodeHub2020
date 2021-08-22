# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Plotting Different Type of Graphs

# Python program to plot Histogram Graph using plotly
 
# **************** Prerequisites *****************
#        pip install plotly  
# ************************************************

import pandas as pd
import plotly.express as px
x = [21, 85, 5, 25, 5]
y =  [0, 25, 50, 75, 100]  
d = {'x': x, 'y': y}
df = pd.DataFrame(d)
fig = px.histogram(df, x="x",
                   category_orders=dict(day=y))
fig.show()



