

low = int(input("sláðu inn tölu "))
high = int(input("sláði inn hærri tölu "))

counter = low 
summa = 0 

while counter <= high:
     if summa % 2==0:
        print("summarn er:", summa)
        summa += counter 
        counter += 1 
        