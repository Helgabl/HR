

a, b, c = int(input("sláðu inn  heildtölu")), int(input("sláðu inn  heildtölu")), int(input("sláðu inn  heildtölu"))


summa_pósitifra = 0
summar_negatívra = 0

if a < 0:
    summar_negatívra += a
else:
    summa_pósitifra += a 

if b < 0: 
    summar_negatívra += b
else: 
    summa_pósitifra += b 

if c < 0: 
    summar_negatívra += c
else:
    summa_pósitifra += c


print("summa jákvæðra talna var:", summa_pósitifra)
print("summa neikværða talna var;", summar_negatívra)