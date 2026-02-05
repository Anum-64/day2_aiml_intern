'''.add()
.remove()  it will throw error once we delete and check for o/p 
.discard()  it will just ignore the error if element not foud
.pop()
.clear()
A.union(B)
A.intresection(B)
A.difference(B)'''

a = [1,2,3,7,8,9] #a = {1,2,3,7,8,9} 
b = {5,6,4,0,1,9} 
s=set(a)
print(s)
s.add(10)
print(s)
s.remove(7)
print(s)
s.remove(15)
print(s)
s.discard(15)
print(s)
s.pop()
print(s)
s.clear()
print(s)
print(s.union(b))
print(s.intersection(b))
print(s.difference(a))