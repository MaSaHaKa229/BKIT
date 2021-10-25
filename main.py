from classes.circle import Circle
from classes.square import Square
from classes.rectangle import Rectangle
import numpy as np
from scipy import linalg


def main():
    figures = (
        Rectangle("blue", 2, 5),
        Square("red", 4),
        Circle("green", 7)
    )
    for fig in figures:
        print(fig)
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(linalg.det(matrix))


if __name__ == "__main__":
    main()
