a =[1,2,3,4,5,6]

def f(a):
    b =[]
    b.extend(a)
    return b

b = f(a)
b[0]=100
print(a)
print(b)