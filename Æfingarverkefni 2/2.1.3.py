
low = int(input("sláðu inn tölu "))
high = int(input("sláði inn hærri tölu "))

summa = 0

for tala in range(low, high+1, 1):
    summa = summa+tala


print(summa)
    