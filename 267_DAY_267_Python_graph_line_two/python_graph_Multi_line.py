# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Plotting Different Type of Graphs

# Python program to plot multi Line Graph using matplotlib
 
# **************** Prerequisites *****************
#        pip install matplotlib  
# ************************************************

from matplotlib import pyplot as plt    
from matplotlib import style    
style.use('ggplot')    
x = [10, 20, 30]    
y = [20, 30, 20]    
x2 = [10, 20, 30]    
y2 = [25, 25, 30]    
plt.plot(x, y, 'b',
        label='line one', linewidth=5)    
plt.plot(x2, y2, 'r',
        label='line two', linewidth=5)    
plt.title('Multi line plot')    
fig = plt.figure()    
plt.ylabel('Y axis')    
plt.xlabel('X axis')    
plt.show()  



