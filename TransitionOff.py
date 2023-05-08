import numpy as np
Temp = np.linspace(16,25,19)
n=19
cost=[1,0]
print(cost)

def transitionHeatOFF (n):
  PheatOFF = np.zeros((n,n))

  for i in range(n):
    for j in range(n):
      if (j==i+1):
        PheatOFF[i,j] = 0.1
      else if (j==i):
        PheatOFF[i,j] = 0.2
      else if (j==i-1):
        PheatOFF[i,j] = 0.7
  PheatOFF[0,0]=0.9
  PheatOFF[n-1, n-1] = 0.3
  return PheatOFF 

Q=transitionHeatOFF(n)
print(Q)
