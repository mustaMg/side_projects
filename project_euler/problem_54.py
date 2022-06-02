# too complicated must think hard, needs engineering
import pandas as pd
import ctypes
import numpy as np

hands = pd.read_csv("poker.txt", sep=" ", header=None)

player_1 = hands.T[:5].T
player_2 = hands.T[5:].T

# So in order to count point of players we need to assign values to letter
# card so that we can compare everthing with eachother


player1 = player_1.iloc[1003].to_numpy()
player2 = player_2.iloc[1003].to_numpy()

numbers = list(range(2, 10)) + ["A", "K", "Q", "J"]
types = ["C", "S", "H", "D"]


def get_highes(list1, list2):
    # first must chechk the pairs
    pair1 = set([i for i in [ii for ii in list1 if list1.count(ii) >= 2]])
    pair2 = set([i for i in [ii for ii in list2 if list2.count(ii) >= 2]])
    print(pair1, pair2)
    if len(pair1) and len(pair2) == 0:
        point1 = 0
        point2 = 0
        a, b = max(list1), max(list2)
        return
    elif len(pair1) and len(pair2) != 0:
        a, b = max(list1), max(list2)
        print(a, b)

    elif len(pair1) != 0 and len(pair2) == 0:
        x = next(iter(pair1))
        return x, len([i for i in list1 if i == x])

    elif len(pair2) != 0 and len(pair1) == 0:
        x = next(iter(pair2))
        return x, len([i for i in list2 if i == x])


def mark_hand(hand1, hand2):
    point = 0
    num_1, type_1 = list(zip(*hand1))
    num_2, type_2 = list(zip(*hand2))
    if len(set(type_1)) == 1:
        print("player1")
    elif len(set(type_2)) == 1:
        print("player2")
    else:
        if get_highes(num_1, num_2) == num_1:
            print("player1")
        elif get_highes(num_1, num_2) == num_2:
            print("player2")
        else:
            print(get_highes(num_1, num_2))
    # second = list(zip(*hand))
    # for i in numbers:
    #     if first.count(i) > 1:
    #         print(i)
    return point


print("mark:", mark_hand(player1, player2))

