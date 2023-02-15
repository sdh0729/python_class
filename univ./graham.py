import math

class point:
  def __init__(self,x,y):
    self.x=x
    self.y=y

  def __lt__(self, other):
    return self.x < other.x if self.x != other.x else self.y < other.y

  def __sub__(self, other):
    return point(self.x - other.x, self.y - other.y)

  def incl(self, other):
    return math.inf if self.x == other.x else (self.y - other.y) / (self.x - other.x), self.x, self.y
  def cross(self, other):
    return self.x * other.y - self.y * other.x

earth=point(x=2,y=1)
mercury=point(x=1,y=2)
venus=point(x=1,y=3)
moon=point(x=2,y=4)
mars=point(x=3,y=2)
jupiter=point(x=3,y=3)

def CCW(p,a,b):
  return(a-p).cross(b-p)
def convexHull(arr):
  p=min(arr)
  idx=arr.index(p)
  arr[0], arr[idx] = arr[idx], arr[0]
  arr = arr[:1] + sorted(arr[1:], key=lambda a: a.incl(p))
  hull = []
  for item in arr:
    while len(hull) >= 2 and CCW(hull[-2], hull[-1], item) <= 0:
      hull.pop()
    hull.append(item)
  return hull

def distance(arr1,arr2):
  a=arr1.x -arr2.x
  b=arr1.y -arr2.y
  c = math.sqrt((a * a) + (b * b))
  return(c)

def solve():
  total_distance = 0
  arr = []
  arr.append(venus)
  arr.append(mars)
  arr.append(moon)
  arr.append(jupiter)
  arr.append(mercury)
  hull = convexHull(arr)
  hull.insert(0,earth)
  for i in range(5):
    total_distance += distance(hull[i],hull[i+1])
  print(total_distance)
solve()

