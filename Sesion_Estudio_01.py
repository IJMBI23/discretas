def s_rec(n:int)-> int:
    if n == 0 or n == 1:
        return 2
    return s_rec(n-1) + 2*s_rec(n-2)

def s_iter(n:int)->int:
    num1, num2 =  2, 2
    for element in range(2,n+1,1):
        num1,num2 = num2,num2 + 2*num1
    return num2
s_iter(2)

def s_fiborec(n:int)->int:
    if n == 0 or n == 1:
        return 1
    return s_fiborec(n-1)+s_fiborec(n-2)

s_fiborec(4)

def s_fiboriter(n:int)->int:
    num1,num2 =1,1
    for elements in range(2 , n+1):
        num1,num2 = num2 , num2 + num1
    return num2

s_fiboriter(4)
