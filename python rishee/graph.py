import matplotlib.pyplot as plt
plt.title("The result of IInd unit test")
L = [10, 20, 15, 18, 25]
plt.pie(L, labels=['maths','eng', 'comp', 'phy', 'chemis'], autopct="%0.2f%%", colors=['red', 'green', 'blue', 'pink', 'yellow'],
        explode=[0,0,0,0,.2])
plt.legend(loc='lower right')
plt.show()


