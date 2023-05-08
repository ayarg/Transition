import numpy as np
Temp = np.linspace(16,25,19)
n=19
cost=[1,0]
print(cost)

def transitionHeatON (n):
  PheatON = np.zeros((n,n))

  for i in range(n):
    for j in range(n):
      if (j==i+2):
        PheatON[i,j] = 0.2 
      else if (j==i+1):
        PheatON[i,j] = 0.5
      else if (j==i):
        PheatON[i,j] = 0.2
      else if (j==i-1):
        PheatON[i,j] = 0.1
  PheatON[0,0]=0.3
  PheatON[n-2,n-1] = 0.7
  PheatON[n-1, n-1] = 0.9

  return PheatON 

P = transitionHeatON(n)
print(P)
