def run():
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]  # list comprehensions
    print(squares)

    squares_challenge = [i for i in range(1,9999)if i % 36 ==0]  # minimo comun multiplo
    print(squares_challenge)


if __name__ == '__main__':
    run()