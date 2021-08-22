# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Plotting Different Type of Graphs

# Python program to plot Pie Graph using plotly
 
# **************** Prerequisites *****************
#        pip install plotly  
# ************************************************

import plotly.express as px
import pandas as pd
users = [25, 41, 58, 21]    
date = [1, 2, 3, 4]  
d = {'users': users, 'date': date}
df = pd.DataFrame(d)
fig = px.pie(df, values='users', names='date')
fig.show()



