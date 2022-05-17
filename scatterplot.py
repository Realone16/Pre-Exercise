import matplotlib.pyplot as plt
from matplotlib import style

style.use('classic')

x=[5, 10, 15, 20, 25, 30]
y=[96, 83, 78, 60, 52, 30]

plt.scatter(x,y)
plt.title('The graph of y against x')
plt.xlabel('x values')
plt.ylabel('y values')

plt.show()
