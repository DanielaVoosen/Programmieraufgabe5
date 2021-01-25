
#!/usr/bin/env python
# coding: utf-8

# # Programmieraufgabe 5: QR-Zerlegung

# In[1]:


import numpy as np
from numpy import linalg
from numpy.linalg import inv


# ## a)

# In[2]:

def QR(A):
    M = np.zeros([len(A), len(A[0])]) #das ist die Matrix, die wir am Ende ausgeben wollen
    A_klein = A
    tau = np.empty([len(A), 1])

    for n in range(0, len(A[0])):      
        if n>0: 
            A_klein = np.delete(A_klein, (0), axis=0)
            A_klein = np.delete(A_klein, (0), axis=1) 

        x=np.empty([len(A_klein), 1]) 
        for m in range(0, len(A_klein)):
            x[m] = A_klein[m][0]

        v = x + (x[0]/abs(x[0]))*linalg.norm(x)*np.eye(len(x),1) #np.eye gibt mir den Einheitsvektor
        v_Hut = 1/v[0]*v
        tau[n] = (linalg.norm(x)+abs(x[0]))/linalg.norm(x)
        H = np.identity(len(A_klein))-tau[n]*v_Hut*np.transpose(v_Hut)
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

R = np.zeros([len(M[0]), len(M[0])]) # der ganze Kram ist nur, damit die v und R einzeln ausgegeben werden
for k in range(0, len(M[0])):
    v_Hut = np.zeros([len(M), 1])
    v_Hut[0]=1
    for i in range(0, len(M)):
        if i <= k: 
            R[i][k] = M[i][k]
        else:
            v_Hut[i] = M[i][k]
    print('v_Hut_',k+1,': \n', v_Hut, '\n')

print('R: ', R)

# ## c)

# In[4]:

def QT_Produkt(b, M, tau):

# bauen uns Q
    for k in range(0, len(M[0])):
        v = np.zeros([len(M), 1])
        for i in range(0, len(M)): #baue mir meine v_Hut; da muss oben ja wieder eine 1 hinkommen
            if i == k:
                v[i] = 1
            if i > k:
                v[i] = M[i][k]

        if k==0: 
            Q = np.identity(len(v))-tau[k]*np.dot(v, np.transpose(v))
        else: 
            Q_neu =  np.identity(len(v))-tau[k]*np.dot(v, np.transpose(v))
            Q = np.dot(Q, Q_neu)

# berechnen Q^T*b
    Q_Tb = np.dot(np.transpose(Q),b).reshape(3,1)
    return Q_Tb

def R_Loesung(c, M):
   
#muessen aus M erst einmal R machen    
    R = np.copy(M)
    if len(M)>len(M[0]): #wenn die Matrix R nicht quadratisch ist, dann werden alle untersten Zeilen geloescht (auch von c)
        for l in range(len(M[0]), len(M)):
            R = np.delete(R, l, axis=0)
            c = np.delete(c, l)

    for k in range(0, len(M[0])): #die untere linke Dreicksmatrix wird genullt
        for i in range(0, len(M[0])):
            if i > k: 
                R[i][k] = 0

#berechnen die Loesung
    x = np.dot(inv(R), c)
    return x


# ## d)

# In[5]:

A = np.array([[-1., 1., -1.],
              [2., 4., 5.],
              [-2., -1., 1.]])
b = np.array([1., 1., 1.])

M,tau=QR(A)
Q_Tb = QT_Produkt(b,M,tau)
x = R_Loesung(Q_Tb, M)
print('\nDie Lösung des Gleichungssystems Ax=b lautet:\n', x)

# ## e)
 
# In[6]:

A = np.array([[-1., 1.],
              [2., 4.],
              [-2., -1.]])
b = np.array([1., 1., 2.])

M,tau=QR(A)
Q_Tb = QT_Produkt(b,M,tau)
x = R_Loesung(Q_Tb, M)
print('\nDie Lösung des Gleichungssystems Ax=b lautet:\n', x)

# In[ ]:




