def fibonacci(count):
    fib = [0,1]
    any(map(lambda x:fib.append(sum(fib[-2:])),range(2,count)))
    return fib[:count]
print(fibonacci(14))