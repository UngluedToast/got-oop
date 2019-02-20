# sssssh. these aren't "real" test

from character_class import Character

# Characters can be instantiated with name and avatar

Gandalf = Character("Gandalf the Grey", "Gandalf.png")
Frodo = Character("Frodo Baggins", "Keep_secrets.png")

print(Gandalf.name, Gandalf.avatar)
print(Frodo.name, Frodo.avatar)


# After adding 2 items to inventroy
# length of inventory should == 2


Gandalf.inventory.append('sword')
Gandalf.inventory.append('staff')


print(len(Gandalf.inventory))
print(Gandalf.inventory)


# Gandalf should have a 'greet' method
# and when I call it, it should return "FLY YOU FOOLS."

print(Gandalf.greet())