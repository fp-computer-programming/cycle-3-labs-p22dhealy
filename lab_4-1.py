# author: DMH 9/30/21

magic_charge = int(input("What is you magic power?"))
shield_charge = int(input("What is you shield charge?"))

if magic_charge < 90 or shield_charge < 75:
    print("The dragon burns you to a crisp.")
else:
    print("You defeated the dragon! But the princess is in another castle.")

