def fibonacci(n):


    num1 = 0
    num2 = 1
    while num1 < n:
        print(num1, end=' ')
        num1, num2 = num2, num1 + num2
        print()
fibonacci(10)