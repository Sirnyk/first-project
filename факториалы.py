def factorial(n):
    tr = n
    num = 1
    while tr > 0:
        num = num * tr
        tr -= 1
    return num

factorial(5)
print(factorial(5))