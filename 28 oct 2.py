rep=int(input())
lista = []

for c in range(rep):
    num = int(input())
    lista.append(num)

print(f"{lista.count(7)} {lista.count(5)}")