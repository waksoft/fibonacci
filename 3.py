from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(input_value):
    if input_value == 1:
        return 1
    elif input_value == 2:
        return 1
    elif input_value > 2:
        return fibonacci(input_value -1) + fibonacci(input_value -2)

for i in range(1, 201):
     print("fib({}) = ".format(i), fibonacci(i))
