import numpy as np

"relevant factors for car buying decision"
"location, km, ps, wheels, color, drivebelt, tuv, seats"

cardata = np.array([
  ('muc', 90469, 105, 1, 1, 0, 0, 1),
  ('sindelfingen', 155000, 102, 0, 0.5, 1, 1, 0),
  ('sulz', 123000, 80, 0, 1, 0, 1, 1)
    ])

weights = np.array([
  ('weights', 1.0, 0.6, 0.4, 0.6, 0.3)
  ])

normFactor = (2.9)
print(normFactor)

def simpleSim(x,y):
  "calculates sim value on non binary attributes"
  return float(1-(abs(x-y)/(x+y)))

def binarySim(x,y):
  "calculates a similarity value on binary attributes"
  if(x == y):
    return 1
  else:
    return 0

def greaterThanBinarySim(x,y):
  "calculates a similarity value if value greater or equal than threshold"
  if(x >= y):
    return 1
  else:
    return 0

def smallerThanBinarySim(x,y):
  "calculates a similarity value if value smaller or equal than threshold"
  if(x <= y):
    return 1
  else:
    return 0

def subjectiveSim(a, b, w):
  "calculates similarity between two stuntment"
  "a is the actual stuntman, b the wanted specification"
  "description, km, ps, wheels, color, drivebelt, tuv, seats"
  km = simpleSim(float(a.item(1)),float(b.item(1)))*float(w.item(1))
  ps = simpleSim(float(a.item(2)), float(b.item(2)))*float(w.item(2))
  wheels = int(binarySim(a.item(3), b.item(3)))
  color = int(binarySim(a.item(4), b.item(4)))
  drivebelt = int(binarySim(a.item(4), b.item(4)))
  tuv = int(binarySim(a.item(4), b.item(4)))
  seats = int(binarySim(a.item(4), b.item(4)))

  results = [km, ps, wheels, color, drivebelt, tuv, seats]
  return (results)

wantedCar = np.array([
  ('wantedCar', 90000, 100, 1, 1, 1, 1, 1)
  ])

print("similarities for T1: ")
print("-----------data-----------")
print(wantedCar[0])
for car in carData:
  print(car)

print("---------similarites----------")
for car in carData:
  x = subjectiveSim(car, wantedCar[0], weights[0])
  print(car.item(0), ":  ",(sum(x)/normFactor))
  # print(x)
