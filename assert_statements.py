def divisors(num):
    divisors =[]
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
        num = input("ingresa un numero: ")
        assert num.isnumeric() and int(num) > 0, "Debes ingresar solo numeros positivos"  # Si es != int retorna falso
        print(divisors(int(num)))
        print("termino el programa")


if __name__ == '__main__':
    run()