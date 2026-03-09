
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
