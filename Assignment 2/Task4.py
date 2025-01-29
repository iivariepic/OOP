def factorials(n:int):
    result = {}
    for current_factorial in range(1,n+1):
        result[current_factorial] = factorial(current_factorial)
    return result

def factorial(n):
    result = 1
    for current_multiplier in range(n, 0, -1):
        result = result * current_multiplier

    return result

def main():
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])

if __name__ == '__main__':
    main()