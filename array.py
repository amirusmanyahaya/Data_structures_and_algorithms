# strings = ['a','b','c','d']

# """the append fuction of a list
# has a constant time complexity with
# a O(1), since it only add to the end of the list"""
# strings.append('e')
# print(strings)

# """ the pop function of a list
# has a constant time complexity
# with a O(1), since it removes an element
# from the end of the list"""
# strings.pop()
# print(strings)

# """ the insert function of a list
# has a linear complexity with a O(n),
# since it inserts into the list at any
# index"""
# strings.insert(3,'f')
# print(strings)

# """ the remove function of a list
# has a linear complexity with a O(n),
# since it has to find the item to be removed"""
# strings.remove('f')
# print(strings)

class myArray:
  """creating an array class"""
  def __init__(self,length=0,data={}):
    self.length = length
    self.data = data

  # complexity: O(1)
  def get(self,index):
    return self.data[index]
  
  # complexity: O(1)
  def push(self,item):
    self.data[self.length] = item
    self.length = self.length + 1

  # complexity: O(1)
  def pop(self):
    del self.data[self.length-1]
    self.length = self.length - 1

  # complexity: O(n)
  def insert(self,index,item):
    for i in range(self.length,index,-1):
      self.data[i] = self.data[i-1]
    self.data[index] = item
    self.length = self.length + 1
  # complexity: O(n)
  def delete(self,index):
    for i in range(index,self.length-1):
      self.data[i] = self.data[i+1]
    self.length = self.length - 1
array1 = myArray()
array1.push(1)
array1.push(2)
array1.push(3)
array1.push(4)

print(array1.data)

print(array1.get(2))

array1.pop()
print(array1.data)

array1.insert(1,'a')
array1.insert(2,'b')
array1.insert(3,'c')
print(array1.data)

array1.delete(1)
array1.delete(1)
array1.delete(1)

print(array1.data)
