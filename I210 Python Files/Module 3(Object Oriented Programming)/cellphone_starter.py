class Puppy(object):

    def __init__(self, name):
        self.name = name
        self.counter = 0

    def __str__(self):
        reply = "Puppy object\n"
        reply += "Name: " + self.name + "\n"
        reply += "Bark Counter: " + str(self.counter) + '\n'
        return reply
        
    def bark(self):
        print("Bark!\n", self.name, "has barked", self.counter, 'time(s).\n')



#Main
dog1 = Puppy("Spot")
for x in range(1, 6):
    dog1.counter = x
    dog1.bark()

print(dog1)




#class CellPhone(object):
#    """A virtual cell phone"""

    #add your code here, as described below
#    """A cell phone has these attributes:
#       owner (string) 
#       minutes remaining (integer)

#    1) Write a constructor to set the attributes listed above.

#    2) Add an info() method that outputs the name of the
#   owner and the number of minutes remaining."""
#    def __init__(self, owner, minutes):
#        self.owner = owner
#        self.minutes = minutes

#    def info(self):
#        print('The owner is', self.owner, 'and the minutes remaining is',
#             self.minutes)

    

#main section of the code
#phone1 = CellPhone("Amelia", 500)
#phone1.info()

#phone2 = CellPhone("Bob", 300)
#phone2.info()

#""" The output of the main section should be:
#My owner is Amelia. Amelia has 500 minutes left.
#My owner is Bob. Bob has 300 minutes left. """




