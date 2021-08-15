# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Plotting Different Type of Graphs

# Python program to plot Histogram Graph using matplotlib
 
# **************** Prerequisites *****************
#        pip install matplotlib  
# ************************************************

from matplotlib import pyplot as plt    
x = [21, 85, 5, 25, 56, 73, 65, 54, 48, 20, 49, 9, 69, 25, 16]
y =  [0, 25, 50, 75, 100]
plt.hist(x, y, histtype='bar', rwidth=0.9)    
plt.title('Users Count')    
plt.xlabel('Date')    
plt.ylabel('Users')    
plt.show()    





