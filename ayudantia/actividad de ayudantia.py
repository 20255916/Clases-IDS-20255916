manzanas = int(input())
clientes = 0

while manzanas != 1:
    if manzanas % 2 == 0:
        manzanas = manzanas //2 
    else:
        manzanas = 3 * manzanas +1
    clientes+=1
