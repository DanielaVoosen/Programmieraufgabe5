
#!/usr/bin/env python
# coding: utf-8

# # Programmieraufgabe 5: QR-Zerlegung

# In[1]:


import numpy as np
from numpy import linalg


# ## a) der Anfang laeuft gut, aber er macht die letzte Untermatrix noch nicht

# In[2]:

def QR(A):
    M = np.zeros([len(A), len(A[0])]) #das ist die Matrix, die wir am Ende ausgeben wollen
    A_klein = A
 
    for n in range(0, len(A[0])):
        #len(A[0])=Anzahl der Spalten
        #len(A)=Anzahl der Zeilen
 
        if n>0: 
            A_klein = np.delete(A_klein, (0), axis=0)
            A_klein = np.delete(A_klein, (0), axis=1) 

        x=np.empty([len(A_klein), 1]) 
        for m in range(0, len(A_klein)):
            x[m] = A_klein[m][0]

        v = x + (x[0]/abs(x[0]))*linalg.norm(x)*np.eye(len(x),1) #np.eye gibt mir den Einheitsvektor
        v_Hut = 1/v[0]*v
        tau = (linalg.norm(x)+abs(x[0]))/linalg.norm(x)
        H = np.identity(len(A_klein))-tau[0]*v_Hut*np.transpose(v_Hut)
        A_klein = np.matmul(H, A_klein)

        for k in range(0, len(A_klein[0])): #die n-te Zeile wird ab der Diagonalen (inkl.) in M uebertragen
            M[n][n+k] = A_klein[0][k]

        for i in range(1, len(v_Hut)): #alle ELemente von v_Hut (bis auf das oberste) werden in M gespeichert
            M[i+n][n] = v_Hut[i]

    return M, tau

# ## b)

# In[3]:

A = np.array([[2., 0., 1.],
              [0., 2., 7.],
              [0., 6., 0.],
              [0., 3., 0.],
              [np.sqrt(12.), 0., np.sqrt(3)]])
M, tau = QR(A)

R = np.zeros([len(M[0]), len(M[0])])
for k in range(0, len(M[0])):
    v_Hut = np.zeros([len(M), 1])
    v_Hut[0]=1
    for i in range(0, len(M)):
        if i <= k: 
            R[i][k] = M[i][k]
        else:
            v_Hut[i] = M[i][k]
#    print('v_Hut_',k+1,': \n', v_Hut)

#print('R: ', R)

# ## c)

# In[4]:
#len(A[0])=Anzahl der Spalten
#len(A)=Anzahl der Zeilen

def QT_Produkt(b, M, tau):
    v_Matrix = np.copy(M) 

    #alle Einträge der Matrix oben rechts werden gelöscht; brauchen nur noch v
    for k in range(0, len(M[0])):
        for i in range(0, len(M)):
            if i <= k:
                v_Matrix[i][k] = 0
  
    Q = np.identity(len(v_Matrix[0]))
    for n in range(0, len(v_Matrix[0])):
        Q *= np.identity(len(v_Matrix[0]))-tau*v_Matrix*np.transpose(v_Matrix)

def R_Loesung(c, M):
    ## Ihr Code hier
    pass


# ## d)

# In[5]:

A = np.array([[-1., 1., -1.],
              [2., 4., 5.],
              [-2., -1., 1.]])
b = np.array([1., 1., 1.])

M,tau=QR(A)
print('M: ', M)
QT_Produkt(b,M,tau)


## Ihr Code hier


# ## e)

# In[6]:


A = np.array([[-1., 1.],
              [2., 4.],
              [-2., -1.]])
b = np.array([1., 1., 2.])

## Ihr Code hier


# In[ ]:




