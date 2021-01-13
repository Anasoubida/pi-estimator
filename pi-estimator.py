#Importation des bibliothèques nécessaires

from pyspark import SparkContext,SparkConf
import numpy as np
from time import time
from random import random
from operator import add

# Estimation de pi et le temps de calcul par spark 
conf = pyspark.SparkConf().setAppName('estimation_pi').setMaster('local')
sc = SparkContext(conf=conf)

#Le point est dans le cercle ou pas 
def is_point_inside_unit_circle(p):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0

#Estimation de Pi et du temps d'execution 

def pi_estimator_spark(n):
    t=time()
    count = sc.parallelize(range(0, n))\
        .map(is_point_inside_unit_circle)\
        .reduce(add)
    pi= count/n*4
    t_dex=np.round(time()-t,2)
    print ("Le temps d'execution est égale à : ", t_dex ,". Pi est éstimé à: ",pi)
    return pi

n = input('Donner la taille de l echantillon aleatoire : ')

tmps_debut = time()
pi = pi_estimator_numpy(int(n))
tmps_fin = time()
print('----------------------------------------------------------------------')
print ("Le temps de calcul est de: ",tmps_fin -tmps_debut ,". Pi est éstimé à: ",pi)
print('----------------------------------------------------------------------')



# Estimation de pi et le temps de calcul par numpy 

#Fonction qui estime pi

def pi_estimator_numpy(n):
    n_1= 0 
    for i in range(n):
      x = random()
      y = random()
      if (x**2 + y**2) < 1.0:
        n_1 += 1
    pi = (4* float(n_1))/n  
    return pi    

n = input('Donner la taille de l echantillon aleatoire : ')

tmps_debut = time()
pi = pi_estimator_numpy(int(n))
tmps_fin = time()
print('----------------------------------------------------------------------')
print ("Le temps de calcul est de: ",tmps_fin -tmps_debut ,". Pi est éstimé à: ",pi)
print('----------------------------------------------------------------------')



