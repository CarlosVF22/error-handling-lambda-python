from functools import reduce

my_list = [1, 2, 3, 4, 5]

squares_filter = list(filter(lambda x: x%2 !=0, my_list)) # lambda filtra en my_list
squares_map = list(map(lambda x: x**2, my_list))  # lambda recorre la lista y ejecuta la operacion o condicion en cada item
square_reduce = list(reduce(lambda a,b: a*b, my_list))  # ejecutamos en cada iteracion, devolvemos un solo valor

print(squares_filter)
print(squares_map)
print(square_reduce)