import  matplotlib.pyplot as plt 

# x axis values 
x = [1,2,3] 
# corresponding y axis values 
y = [2,4,1] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.savefig(".\.github\workflows\My_first_graph.jpg")


# x axis values 
x = [11,12,13] 
# corresponding y axis values 
y = [12,44,41] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My Second graph!') 
  
# function to show the plot 
plt.savefig(".\.github\workflows\My_Second_graph.jpg")