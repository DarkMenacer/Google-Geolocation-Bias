import matplotlib.pyplot as plt
 
def showbar(query,cities,rbo):
    plt.figure(figsize = (10, 5))
    
    plt.bar(cities, rbo, color ='maroon', width = 0.4)
    
    plt.xlabel("Cities")
    plt.ylabel("RBO")
    plt.title(query)
    plt.show()