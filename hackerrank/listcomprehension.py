x = 2
y = 2
z = 2
n = 2

print(
    [
        [i, ii, iii]
        for i in range(x + 1)
        for ii in range(y + 1)
        for iii in range(z + 1)
        if i + ii + iii != n
    ]
)

