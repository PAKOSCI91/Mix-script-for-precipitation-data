# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 22:22:21 2021

@author: pasqu
"""

import pandas as pd
import numpy as np

#Import hourly data
df = pd.read_csv('.csv')

# Show dataframe
#print(df)

list_=df.iloc[:,0].tolist()

#print(list_)
print('Numero totale di valori in INPUT: ', len(list_))

#ATTENZIONE 
#ELIMINA DATI SBALLATI 
y= [0 if x<0 else x for x in list_]
z= [0 if x>=500 else x for x in y]
        
#print(z)
Massimo=np.sum(z)
print('Somma pioggia per delta_t = 10 minuti: ', Massimo)

#passi da 10 min a n ore
#[(np.sum((list_[i:i+T]))) for i in range(0,10800,T)]

# T = 1 (10 min) - 2 (20 min) - 3 (30 min) - 6 (1 ora) - 12 (2 ore) 
# T = 18 (3 ore) - 36 (6 ore) - 72 (12 ore) - 108 (18 ore) - 144 (24 ore)

T= 1
a=[]
for i in range(0,len(z),T):
    a.append(np.sum((z[i:i+T])))
print('Numero totale di valori in OUTPUT: ', len(a))
#print(a)

print(len(list_)/len(a))

m2=np.sum(a) 
print('Somma pioggia per delta_t considerato: ', m2)
m1=np.max(a) 
m1=str(m1)
print('PIOGGIA ESTREMA PER DELTA_T CONSIDERATO: ', m1)
b=str(a)

#scrivere su un file:
with open('Charact events','a') as writer:
    writer.write(m1 + '\n')


 