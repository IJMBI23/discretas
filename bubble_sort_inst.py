
## Tuples
t = (1, "hola", [666,777])
print (len(t))
print (t[2])
one, _, last = t
print(one, last)

def bubble_sort_inst(a: list) -> list[int]:
    """
    Implements the bubble sort
    Arg a: a list of numbers
    Returns a list of numbers
    """
    swaps = 0
    def swap(i:int, j:int):
        nonlocal swaps
        if i != j:
            a[i], a[j] = a[j], a[i]
            swaps += 1

    n = len(a)
    
    
    for limit in range(n, 0, -1): #Generates n,n-1,n-2,...,2,1
        for i in range(0, limit - 1): #generates 0,1,...,limit-2
            if a[i] > a[i + 1]:
                swap(i, i + 1)

    return a, swaps

a = [666,665,664]
print(bubble_sort_inst(a))

N = [] #values for n
SN = [] #seaps for n
EN = [] # estimates for n

for n in range(5,50,5):
    a = list(range(n, -1, -1))
    _, swaps = bubble_sort_ints(a)
    la = len(a))
    N.append(la)
    SN.append(swaps)
    EN.append( la*(la - 1) // 2 )

def foo(x, y = 1): # y es un valor opcional
    return x / y

print(foo(10, 20))
print(foo(y = 20, x = 10))
print(foo(10))
    
import matplotlib.pyplot as plt
plt.figure(figsize=(5,6))
plt.title("Data fro bubble sort swaps")
plt.plot(N, SN,  labels = "$T_{es}(n)$")
plt.scatter(N, EN, colors = "black", marker = "x", labels = "$n()n-1$/2")
plt.legend()
plt.show()
