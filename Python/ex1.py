import math

n = 0
C = int(input("enter no.of cars "))

x = [0 for i in range(C)]
y = [0 for i in range(C)]
v = [0 for i in range(C)]
d = [0 for i in range(C)]
t = [0 for i in range(C)]

for j in range(C):
    x[j],y[j],v[j] = int(input()), int(input()), int(input())

for j in range(C):
    d[j] = math.sqrt((x[j]**2)+(y[j]**2))
    t[j] = d[j]/v[j]

for a in range(C):
    for b in range(a+1,C):
        if t[a] == t[b]:
            n = n+1
    
print(n)
