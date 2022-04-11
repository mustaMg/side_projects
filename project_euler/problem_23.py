def proper_div(num1):
    n = 1
    divisors = []
    while n < num1:
        if num1 % n == 0:
            divisors.append(n)
            n += 1
        else:
            n += 1
    return divisors


abundant = []
for i in range(10 ** 4):
    if sum(proper_div(i)) > i:
        abundant.append(i)
    else:
        pass

print(abundant)
