def double(n):
    return n + n


def add(n, myfunction):
    res = myfunction(n)
    return n + res


a = add(2, double)
print(a)
