

low = int(input("sláðu inn tölu "))
high = int(input("sláði inn hærri tölu "))

for tala in range(low, high+1, 1):
    if tala % 2 == 1:
        print(tala)