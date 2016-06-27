import numpy as np
# import hammingSim as hs

relevanceMatrix = np.array([
  ((4/15),(1/3)),
  ((1/3),(2/9)),
  ((2/5),(4/9))
  ])

column = relevanceMatrix[:, [0]]
e1 = sum(column[[0],:],column[[2],:])
c1 = 0
u1 = (1/3)
a1 = 0

def patexSim(e,c,u,a):
  "patdex2 sim with given index values"
  res = (e/(e+2*c+0.5*u+a))
  return res

e2 = 0
c2 = (1/3)+(4/9)
u2 = (2/9)
a2 = 0

e3 = (2/5)
c3 = (4/15)
u3 = (1/3)
a3 = 0

print("patexSim for x1: ",patexSim(e1, c1, u1, a1))
print("patexSim for x2: ", patexSim(e2, c2, u2, a2))
print("patexSim for x3: ", patexSim(e3, c3, u3, a3))


