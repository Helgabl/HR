

setning = ("A Santa at Nasa")
reverse = setning[::-1]

print(setning)
print("---------------")
print(reverse)

for letter in setning:
    print(letter)

print("---------------")
for i in range(len(setning)-1, -1, -1):
    print(setning[i])
print("---------------")
for i in reversed(setning):
    print(i)