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

normFactor = (0.5+0.4+0.6+0.3+0.7)
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
  height = simpleSim(float(a.item(1)),float(b.item(1)))*float(w.item(1))
  weight = simpleSim(float(a.item(2)), float(b.item(2)))*float(w.item(2))
  specialSim = int(binarySim(a.item(5), b.item(5)))
  special = float(0)
  if(specialSim == 1):
    special = float(w.item(5))

  salary1 = float(a.item(3))
  salary2 = float(b.item(3))
  salaryweight = float(w.item(3))
  salary = float(smallerThanBinarySim(salary1, salary2))*salaryweight
  ex1 = float(a.item(4))
  ex2 = float(b.item(4))
  exWeight = float(w.item(4))
  experience = float(greaterThanBinarySim(ex1, ex2))*exWeight
  results = [height, weight, salary, experience,special]
  return (results)

t1wantedMan = np.array([
  ('t1wanted', 180, 85, 4000, 4, 'feuer')
  ])

t2wantedMan = np.array([
  ('t2wanted', 175, 80, 3000, 5, 'springen')
  ])

print("similarities for T1: ")
print("-----------data-----------")
print(t1wantedMan[0])
for man in stuntmenData:
  print(man)

print("---------similarites----------")
for man in stuntmenData:
  x = subjectiveSim(man, t1wantedMan[0], weights[0])
  print(man.item(0), ":  ",(sum(x)/normFactor))
  # print(x)

print("similarities for T2: ")
print("-----------data-----------")
print(t2wantedMan[0])
for man in stuntmenData:
  print(man)

print("---------similarites----------")
for man in stuntmenData:
  x = subjectiveSim(man, t2wantedMan[0], weights[0])
  print(man.item(0), ":  ",(sum(x)/normFactor))
  print(x)
