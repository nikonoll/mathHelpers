import numpy as np

def distH(x,y):
  "calculates the distance between two data points"
  return sum([abs(xi-yi) for xi, yi in zip(x,y)])

def simH(y, x):
  "calculates the hamming similarity for 2 points"
  return 1-0.1*distH(x,y)

# TODO: import test data via csv
cinemaData = np.array([
  (1,0,1,0,1,1,1,0,1,1),
  (0,1,1,0,0,0,1,0,0,0),
  (0,1,0,0,1,0,0,0,0,1),
  (0,1,1,0,1,0,0,0,0,0),
  (0,1,1,0,0,0,0,0,0,0),
  (1,0,1,1,0,1,0,0,1,1),
  (0,1,1,0,0,0,1,1,0,1),
  (0,1,0,0,1,0,1,0,0,1),
  (0,1,1,1,0,0,1,1,0,1),
  (0,1,1,1,0,0,1,0,0,0),
  (1,1,1,0,1,1,0,0,0,0),
  (0,1,0,0,1,0,1,1,0,0),
  (1,0,1,0,1,0,0,0,0,0),
  (0,1,1,1,1,1,0,0,1,1),
  (0,1,1,0,0,0,1,0,0,0)
  ])

testData = np.array([
  (0,0,0,1,1,1,1,0,0,0)
  ])

# ---------------------------

i = 1
for d in cinemaData:
  print "x", i, ": ", (simH(d, testData[0]))
  i = i + 1
