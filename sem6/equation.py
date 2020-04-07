"""Bisquare equation solutor"""
import sys
from math import sqrt

def print_solution(sol):
    """Prints solution"""
    if sol < 0:
        return
    if sol == 0:
        print(sol)
    else:
        print(sqrt(sol))
        print(-sqrt(sol))

if __name__ == "__main__":
    A, B, C = [float(item) for item in sys.argv[1:]]
    D = B * B - 4 * A * C
    if D < 0:
        print("No solution")
    elif D == 0:
        X = B * (-1) / (2 * A)
        print_solution(X)
    else:
        X1 = (B * (-1) + sqrt(D)) / (2 * A)
        X2 = (B * (-1) - sqrt(D)) / (2 * A)

        print_solution(X1)
        print_solution(X2)
         