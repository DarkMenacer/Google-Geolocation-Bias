import matplotlib.pyplot as plt
 
def showbox(data, cities):
    fig = plt.figure(figsize =(10, 7))
    
    ax = fig.add_axes([0.15, 0.1, 0.7, 0.7])
    ax.set_xticklabels(cities)
    
    # Creating plot
    ax.boxplot(data)
    plt.show()  