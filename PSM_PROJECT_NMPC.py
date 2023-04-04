#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# ![image.png](attachment:image.png)

# In[19]:


CA1 = 2.0
CA2 = 10.0
Cp, Cp_j = 4184.0, 4184.0
F1 = 0
F2, F3 = 4.0, 4.0
Ea_R = 10080
k0 = 6.20e14
r = .232
V0 = 4.2e-3
T1, T2 = 21 + 273, 21 + 273
Tj0 = 26 + 273
U = 900
V_j = 0.014
a_j = 7.0e5
a_r = 0
del_Hr = -33488.0
rho, rho_j = 1000, 1000


# ![image.png](attachment:image.png)

# In[30]:


def state_eqn(t, var, Fj):
    h, CA, Tr, Tj = var
    V = V0 + (3.14 * (r**2) * h)
    A = 3.14 * r * (r + 2 * h)
    Br = rho * Cp* V + a_r
    Bj = rho_j * Cp_j * V_j + a_j
    
    dh = (F1 + F2 - F3)/(3.14 * (r**2))
    dCA = (F1/V)* (CA1-CA) + (F2/V)* (CA2-CA) - k0 * np.exp(-Ea_R/Tr)

    Qr = -rho*Cp*F1*(T1-Tr) - rho*Cp*F2*(T2-Tr) +U*A*(Tr-Tj)  # Tj = (Tj0 + Tj2)/2
    Qg = -del_Hr * V * k0 * np.exp(-Ea_R/Tr)
    
    dTr = (1/Br) * (-Qr + Qg)
    dTi = (1/Bj) * (rho_j * Cpj * Fj * (Tj0 - Tj) + U*A* (Tr - Tj))
    
    return dh, dCA, dTr, dTi


# In[37]:


sol = solve_ivp(state_eqn, [0,10], (10,5,30+273,28+273), args=(20,))


# In[ ]:


def NMPC():
    

