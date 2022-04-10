# How many such routes are there through a 20×20 grid?
from scipy.special import comb


def lattice_path(n):
    return comb(n * 2, n)


print(lattice_path(20))
