

my_list = []

size = int(input("hvað viltu slá inn margar tölur?"))


for x in range(1,size+1):
   current = int(input("sláðu inn næstu tölu"))
   my_list.append(current)

print(my_list)