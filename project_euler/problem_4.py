import pandas as pd

# Find the largest palindrome made from the product of two 3-digit numbers.
arr = list(range(100, 1000))
arr_2 = list(range(100, 1000))
df = pd.DataFrame([x * y for y in arr_2 for x in arr])


def palindrome(x):
    if len(str(x)) % 2 == 1:
        # print(int(len(str(i))) // 2, end="\t")
        x, y = str(x)[: int(len(str(x))) // 2], str(x)[(int(len(str(x))) // 2) + 1 :]
        if x == y[::-1]:
            return True
        else:
            return False
    elif len(str(x)) % 2 == 0:
        x, y = str(x)[: int(len(str(x))) // 2], str(x)[int(len(str(x))) // 2 :]
        if x == y[::-1]:
            return True
        else:
            return False


df[1] = [palindrome(i) for i in df[0]]
df = df[df[1]]
print(max(df[0]))
