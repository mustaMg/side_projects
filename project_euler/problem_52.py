def is_in(list1, list2):
    # checks if two list has all elements the same
    if all(item in list1 for item in list2) and all(item in list2 for item in list1):
        return True


for i in range(10 ** 7):
    number = list(str(i))
    double = list(str(i * 2))
    tripple = list(str(i * 3))
    fourth = list(str(i * 4))
    fifth = list(str(i * 5))
    sixth = list(str(i * 6))
    if (
        is_in(number, double)
        and is_in(number, tripple)
        and is_in(number, fourth)
        and is_in(number, fifth)
        and is_in(number, sixth)
    ):
        print(i, i * 2, i * 3, i * 4, i * 5, i * 6)
