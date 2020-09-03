
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

max_int = 0


while num_int >= 0:    #á meðan num_int er stærra en 0 þá keyrir loop
    if num_int > max_int:     #num_int er stærra en max_int
        max_int = num_int     #max_int fær num_int valueið
    num_int = int(input("Input a number: ")) 
print("The maximum is", max_int)    # Do not change this line
