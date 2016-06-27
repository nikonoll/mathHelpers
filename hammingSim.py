import numpy as np

def distH(x,y):
  "calculates the distance between two data points"
  return sum([abs(xi-yi) for xi, yi in zip(x,y)])

def simH(y, x):
  "calculates the hamming similarity for 2 points"
  n = testData.size
  return 1-(1/n)*distH(x,y)

def weightedSimH(x,y,w):
  "calculates the weighted hamming similarity"
  simVal = 0
  for xi, yi, wi in zip(x,y,w):
    if(xi != yi):
      simVal = simVal + wi
  sumWeights = sum(w)
  return (1-simVal/sumWeights)


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

weights = np.array([
  (0.5,0,0.5,1,0.5,0.5,0.5,0.5,0,1)
  ])
# ---------------------------

i = 1
for d in cinemaData:
  # print("x", i, ": ", (simH(d, testData[0])))
  print("weighted sim to x",i,": ",weightedSimH(d, testData[0], weights[0]))
  i = i + 1
