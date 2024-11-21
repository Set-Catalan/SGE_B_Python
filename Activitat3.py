nombres = range(1,11)

for i in nombres:
    print(i)

suma = 0

for i in nombres:
    suma += i

print(suma)

fruits = ["poma","pera","raïm","plàtan"]

for i in fruits:
    print(i)

num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
parells = []
imparells = []

for i in num:
    if i % 2 == 0:
        parells += [i]
    else:
        imparells += [i]
    
print("Números Parells: ", parells)
print("Números Imparells: ", imparells)

sum_parells = 0
sum_imparells = 0

for i in num:
    if i % 2 == 0:
        sum_parells += i
    else:
        sum_imparells += i
    
print("Suma dels Números Parells: ", sum_parells)
print("Suma dels Números Imparells: ", sum_imparells)

x = 0
suma = 0

while x < 100:
    suma += x
    x += 1

print(suma)

num = 234

while num >= 100:
    if num <= 400:
        print("El nombre esta entre 100 i 400")
        break
    else:
        print("El nombre no esta entre 100 i 400")