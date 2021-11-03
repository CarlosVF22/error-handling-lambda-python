# crear un dictionario en donde las llaves sean los primeros numeros y valores los numeros elevados al cubo
import math


def run():
    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}  # dict_comprehensions
    print(my_dict)

    my_dict_challenge = {i:math.sqrt(i) for i in range(1, 1000)}
    print(my_dict_challenge)


if __name__ == '__main__':
    run()