def read():
    numbers = []
    with open("./archivos/numbers.txt","r", encoding="utf-8") as f:  # leer un archivo y con utf-8
        for line in f:  # Recorriendo cada linea
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["facundo","miguel", "pepe", "Carlos"]
    with open("./archivos/names.txt" ,"a", encoding="utf-8") as f:  # "w" para eliminar y crear - "a" dejar y agregar 
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()

if __name__ == '__main__':
    run()