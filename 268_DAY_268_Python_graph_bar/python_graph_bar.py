# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Plotting Different Type of Graphs

# Python program to plot Bar Graph using matplotlib
 
# **************** Prerequisites *****************
#        pip install matplotlib  
# ************************************************

from matplotlib import pyplot as plt    
x = [1,2,3,4]    
y = [51,87,45,67]    
plt.bar(x,y,color = 'blue')    
plt.title('Users Count')    
plt.xlabel('Date')    
plt.ylabel('Users')    
plt.show()    




