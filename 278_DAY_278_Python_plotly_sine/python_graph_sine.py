# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Plotting Different Type of Graphs

# Python program to plot sine Graph using plotly
 
# **************** Prerequisites *****************
#        pip install plotly  
# ************************************************


import plotly.express as px
import numpy as np
x = np.arange(0, np.pi*4, 0.1)
y = np.sin(x)
fig = px.line(x=x, y=y, 
              labels={'x':'t', 'y':'sin(t)'})
fig.show()




