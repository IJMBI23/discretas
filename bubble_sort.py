rango = list(range(10,0, -1))

def bubble_sort(a: list) -> list[int]:
    """
    Implements the bubble sort
    Arg a: a list of numbers
    Returns a list of numbers
    """

    def swap(i:int, j:int):
        if i != j:
            a[i], a[j] = a[j], a[i]

    n = len(a)

    for limit in range(n, 0, -1): #Generates n,n-1,n-2,...,2,1
        for i in range(0, limit - 1): #generates 0,1,...,limit-2
            if a[i] > a[i + 1]:
                swap(i, i + 1)

    return a

a = []
print(a, bubble_sort)
a = [666]
print(a, bubble_sort)
a = [666,665,664]
print("before", a)
print(a, bubble_sort)


