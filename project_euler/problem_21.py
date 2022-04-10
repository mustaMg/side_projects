# find proper divisors
# Evaluate the sum of all the amicable numbers under 10000.


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


amicable_numbers = []
for i in range(10001):
    first_n = sum(proper_div(i))
    sec_n = sum(proper_div(first_n))
    if i == sec_n and first_n != sec_n:
        print(i, first_n)
        amicable_numbers.append(i)

print(sum(amicable_numbers))
