guest = ["Indra", "John", "Lisa", "Ann"]
print(guest)
guest[0]="Sina"# Sina is taking palce of Indra
print(guest)

guest.insert(0, "Mark") # insert mark in the beginning
print(guest)

guest.insert(3, "Jose") # insert mark in the middle
print(guest)

guest.append("Li") # append at the end
print(guest)

length = len(guest)
for i in range(2,length,1):
    reject=guest.pop()
    print("Sorry", f"{reject} I can not invite to dinner for now")
