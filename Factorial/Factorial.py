def factorial(num):
    result = 1
    for i in range(num, 0, -1):
        fact = lambda x, y: x * y
        result = fact(result, i)
    return result