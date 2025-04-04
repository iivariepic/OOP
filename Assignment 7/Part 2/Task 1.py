#map()
def map_replacement(iterables):
    return [mapping(iteration) for iteration in iterables]

def mapping(x):
    return x**2

#filter()
def filter_replacement(iterables):
    result = []
    for iterable in iterables:
        if filter_condition(iterable):
            result.append(iterable)

    return result

def filter_condition(x):
    if x % 2 == 0:
        return True
    return False

#reduce()
def reduce_replacement(iterables):
    result = iterables[0]
    for iterable in iterables[1:]:
        result = reducing(result, iterable)
    return result

def reducing(x, y):
    return x * y

#sorted()
def sorted_replacement(iterables):
    result = iterables[:]
    length = len(result)

    for i in range(length):
        for j in range(0, length - i - 1):
            if not result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result

#enumerate()
def enumerate_replacement(iterables):
    result = []
    index = 0
    for iterable in iterables:
        result.append((index, iterable))
        index += 1
    return result

def main():
    my_list = [1,2,3,4]
    print(map_replacement(my_list))
    print(filter_replacement(my_list))
    print(reduce_replacement(my_list))
    print(sorted_replacement(my_list))
    print(enumerate_replacement(my_list))


if __name__ == '__main__':
    main()