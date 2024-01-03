import  matplotlib.pyplot as plt 

# x axis values 
x = [1,2,3,8] 
# corresponding y axis values 
y = [2,4,1,7] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.savefig("one.jpg", bbox_inches='tight')


# x axis values 
x = [11,12,13,20] 
# corresponding y axis values 
y = [12,44,41,26] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My Second graph!') 
  
# function to show the plot 
plt.savefig("two.jpg", bbox_inches='tight')