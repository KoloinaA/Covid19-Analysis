import matplotlib
import numpy as np;
matplotlib.use('Agg')
import matplotlib.pyplot as plt;
#plt.plot([1,2,3,4])
#plt.ylabel('label Y')
#plt.show()
#plt.savefig('graphe.png')

# courbe 
x = np.linspace(0,10,100)
y = np.sin(x)
#plt.plot(x,y)
#plt.savefig('courbe.png')

# nuage de points
# plt.scatter(x,y, color='red', marker ='o')
# plt.savefig('nuage_de_points.png')

# barres
categories = ['A','B','C']
values = [15, 20, 10]
# plt.bar(categories, values)
# plt.savefig('barre.png')

# pie chart
# plt.pie(values, labels=categories, autopct = '%1.1f%%')
# plt.savefig('pie.png')

# boite à moustaches
plt.boxplot([np.random.normal(0,1,100), np.random.normal(1,1, 100)])
plt.savefig('boite_a_moustaches.png')