import string

alphabet = string.ascii_lowercase
rows = []
pattern = []


def rangoli(size):
    rows = []
    alph = list(alphabet[:size])[::-1]
    empty = "-" * ((2 * size) - 2) + alph[0]
    for i in range(1, len(alph)):
        rows.append(empty)
        empty = empty[2:]
        empty = empty + f"-{alph[i]}"

    upper_half = [row[:-1] + alph[i] + row[-2::-1] for i, row in enumerate(rows)]
    for i in upper_half:
        print(i)
    print(empty + empty[-2::-1])
    for i in upper_half[::-1]:
        print(i)


rangoli(12)
