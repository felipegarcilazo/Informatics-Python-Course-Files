import tools
class Puppy(object):
    """A Virtual Puppy"""
    names = {}
    
    @staticmethod
    def dog_names():
        tools.table_print(("Name", "Times"), sorted(Puppy.names.items()), 10)

    def __init__(self, name):
        self.__name = name
        self.__counter = 0
        if self.__name in Puppy.names:
            Puppy.names[self.__name] += 1
        else:
            Puppy.names[self.__name] = 1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name:
            print("Name cannot be empty")
        else:
            self.__name = name
        

    def __str__(self):
        reply = "Puppy object\n"
        reply += "Name: " + self.__name + "\n"
        reply += "Bark Counter: " + str(self.__counter) + '\n'
        return reply
        
    def bark(self):
        print("Bark!\n", self.__name, "has barked", self.__counter, 'time(s).\n')



#Main
dog1 = Puppy("Spot")

dog1.set_name("")
print(dog1.get_name())
dog1.set_name("Rex")
print(dog1.get_name())

