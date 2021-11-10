def divisors(num):
    try:
        divisors =[]
        if num < 0:
            raise ValueError("debes ingresar un numero positivo")
        else:
            for i in range(1, num+1):
                if num % i == 0:
                    divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        num = int(input("ingresa un numero: "))
        print(divisors(num))
        print("termino el programa")
    except ValueError:
        print("Debes ingresar un numero")

if __name__ == '__main__':
    run()