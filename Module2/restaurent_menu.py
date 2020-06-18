menu= ("Chicken Curry","Burger","Yakisoba","Bulgogi", "Ham")
list_menu=list(menu)

list_menu [0]=("Fries")
list_menu [1]=("Soup")

new_menu=tuple(list_menu)
for i in new_menu:
    print(i)