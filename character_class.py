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

