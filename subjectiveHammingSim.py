import numpy as np

stuntmenData = np.array([
  ('tom', 175, 88, 7000, 6, 'feuer'),
  ('john', 180, 82, 3000, 3, 'springen'),
  ('mike', 190, 74, 5500, 17, 'feuer'),
  ('pete', 185, 88, 3800, 2, 'springen'),
  ('nick', 198, 102, 2300, 4, 'unfall')
  ])

weights = np.array([
  ('weights', 0.5, 0.4, 0.6, 0.3, 0.7)
  ])

def simpleSim(x,y):
  "calculates sim value on non binary attributes"
  return 1-(abs(x-y)/x+y)

def binarySim(x,y):
  "calculates a similarity value on binary attributes"
  if(x == y):
    return 1
  else:
    return 0

def subjectiveSim(a, b, w):
  "calculates similarity between two stuntment"
  test = simpleSim(float(a.item(1)),float(b.item(1)))
  print(test)
  # print(simpleSim(a[1], b[1]))

subjectiveSim(stuntmenData[0], stuntmenData[1], weights[0])
