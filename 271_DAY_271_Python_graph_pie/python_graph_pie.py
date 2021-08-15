# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Plotting Different Type of Graphs

# Python program to plot Pie Graph using matplotlib
 
# **************** Prerequisites *****************
#        pip install matplotlib  
# ************************************************

from matplotlib import pyplot as plt        
users = [25, 41, 58, 21]    
date = [1, 2, 3, 4]
explode = (0.1, 0, 0, 0)
fig1, ax1 = plt.subplots()    
ax1.pie(users, explode=explode, labels=date,
        autopct='%1.1f%%', 
        shadow=True, startangle=90)    
ax1.axis('equal')  
plt.show()       






