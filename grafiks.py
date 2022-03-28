import matplotlib
import matplotlib.pyplot as plt
x_koordinats=[ 2003, 2007, 2011, 2017, 2022] #gadi
y_koordinats=[0.90,1.11,1.39,1.78,2.01]#Dīzeļa cena
y_koordinats2=[0.95,1.23,1.56,1.82,1.90]#Benzīna cena
#plt.style.use("seaborn-dark-palette")
plt.plot(x_koordinats,y_koordinats)
plt.xlabel("Gadi")
plt.ylabel("Cenas")
plt.title("Ceņu izmaiņas pa gadiem")
plt.plot(x_koordinats, y_koordinats, label="Dīzeļa cena")
plt.plot(x_koordinats, y_koordinats2, label="Benzīna cena",linewidth=3,linestyle="dotted",color="red")
plt.legend(loc="upper left")
plt.show()