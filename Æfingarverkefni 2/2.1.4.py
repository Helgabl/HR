
low = int(input("sláðu inn tölu "))
high = int(input("sláði inn hærri tölu "))

summa_sléttra = 0

for tala in range(low, high+1):
    if tala % 2 == 0:
        summa_sléttra += tala 
  
    
print(summa_sléttra)