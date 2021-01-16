
#!/usr/bin/env python
# coding: utf-8

# # Programmieraufgabe 5: QR-Zerlegung

# In[1]:


import numpy as np
from numpy import linalg


# ## a) #der Anfang laeuft gut, aber er macht die letzte Untermatrix noch nicht

# In[2]:


def QR(A):
    M = np.zeros([len(A), len(A[0])]) #das ist die Matrix, die wir am Ende ausgeben wollen
    for n in range(0, len(A[0])):
        print('!!!!!: ', n)
        #len(A[0])=Anzahl der Spalten
        #len(A)=Anzahl der Zeilen
 
        A_klein = A[n:, n:]
        print('A_klein: ', A_klein)

        #Erstellung eines Vektors, der die n-te Spalte und die untersten m Zeilen speichert
        x=np.empty([len(A_klein), 1]) 
        for m in range(0, len(A_klein)):
            x[m] = A[m+n][n]

        print('x: ', x)
        v = x + (x[0]/abs(x[0]))*linalg.norm(x)*np.eye(len(x),1) #np.eye gibt mir den Einheitsvektor
        print('v: ', v)
        v_Hut = 1/v[0]*v
      #  print(x[0])
    #    print('Zähler: ', (linalg.norm(x)+abs(x[0])))
        tau = (linalg.norm(x)+abs(x[0]))/linalg.norm(x)
    #    print('Tau: ', tau[0])
     #   print('v: ', v)
        print('v_Hut', v_Hut)
     #   print('vv^t: ', v*np.transpose(v_Hut))
        H = np.identity(len(A_klein))-tau[0]*v_Hut*np.transpose(v_Hut)
        A_klein = np.matmul(H, A_klein)
        print('A_klein: ', A_klein)

        for k in range(n, len(A_klein[0])): #die n-te Zeile wird ab der Diagonalen (inkl.) in M uebertragen
            M[n][k] = A_klein[n][k]

        for i in range(n, len(A_klein)): #alle ELemente von v_Hut (bis auf das oberste) werden in M gespeichert
            M[i][n] = v_Hut[i]

        print('M: ', M)

# ## b)

# In[3]:


A = np.array([[2., 0., 1.],
              [0., 2., 7.],
              [0., 6., 0.],
              [0., 3., 0.],
              [np.sqrt(12.), 0., np.sqrt(3)]])
QR(A)

## Ihr Code hier


# ## c)

# In[4]:


def QT_Produkt(b, M, tau):
    ## Ihr Code hier
    pass

def R_Loesung(c, M):
    ## Ihr Code hier
    pass


# ## d)

# In[5]:


A = np.array([[-1., 1., -1.],
              [2., 4., 5.],
              [-2., -1., 1.]])
b = np.array([1., 1., 1.])

## Ihr Code hier


# ## e)

# In[6]:


A = np.array([[-1., 1.],
              [2., 4.],
              [-2., -1.]])
b = np.array([1., 1., 2.])

## Ihr Code hier


# In[ ]:




