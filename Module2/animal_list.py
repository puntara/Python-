animals=["cow","elephant","dog","hippo", "parrot","mouse","rat", "chicken","pig"]
lentgh=len(animals)
for animal in animals:
    print(animal)

print("The FIRST 3 animals in the list are: ")
for animal in range(0,3,1):
    print(animals[animal])


print("The MIDDLE 3 animals in the list are: ")
for animal in range(3,6,1):
    print(animals[animal])

print("The LAST 3 animals in the list are: ")
for animal in range(6,9,1):
    print(animals[animal])