# avatar
# name
# inventory

# def do_stuff():
    # pass


class Character():
    #'dunder init' method is the constructor
    def __init__(self, new_name, new_avatar):
        #'self' is a customary way to the instance being built
        #in some other languages, they use 'this'
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []
#`someone=None` is a default argument
#`None` is equivalent to `null` in other languages
    def greet(self, someone=None):
        if someone is not None:
            return "Hello, %s, I am %s. Fly you fool." % (someone.name, self.name,)
        else:
            return "Hello, I am %s. Fly you fool." % (self.name,)

# Hero is a kind of Character
# Hero is a subclass of Character
# Hero inherits from Character
# Character is the super class of Hero
class Hero(Character):
    pass

class Monster(Character):
    def greet2(self, someone=None):
        if someone is not None:
            return "Greetings %s, I am %s, prepare to die!" % (someone.name, self.name,)
        else:
            return "I am %s, and I really wish I was fighting right now" % (self.name,)