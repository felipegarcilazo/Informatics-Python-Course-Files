# pass is used to prevent Python from throwing an error
# when a method has no code. You can remove it when you
# implement each method. There is a LOT of test code below.

class Fish(object):
    school = []

    @staticmethod
    def remaining():
        print("Number of fish in the pond are", len(Fish.school))
        for fish in Fish.school:
            print(Fish.__str__(fish), "\n")

    @staticmethod
    def largest():
        l_fish = None
        large = 0
        for fish in Fish.school:
            if fish.length > large:
                l_fish = fish
                large = fish.length
        print("The largest fish is:", l_fish.name, "\n")
        
    def __init__(self, name, length):
        #your code here
        self.name = name
        self.length = length
        self.caught = False
        print("Fish put in pond:", self.name, end = "\n\n")
        Fish.school.append(self)

    def __str__(self):
        #your code here
        if not self.caught:
            reply = "Name: " + self.name + "\nLength: " + str(self.length) + \
                    "\"" + "\nStatus: FREE"
        else:
            reply = "Name: " + self.name + "\nLength: " + str(self.length) + \
                    "\"" + "\nStatus: Caught"
        return reply

    def __gt__(self, other):
        if self.length > other.length:
            return True
        else:
            return False

    def catch(self):
        #your code here
        print("You attempt to catch", self.name + ".", end = " ")
        if self.caught:
            print(self.name, "was already caught!")
        else:
            self.caught = True
            print("Success!", Fish.__str__(self))
        Fish.school.remove(self)
        print()
        
class StealthFish(Fish):
    def catch(self):
        print("You attempt to catch", self.name + ". But it can't be done!!!\n")

class FancyFish(Fish):
    def __init__(self, title, name, length):
        super().__init__(name, length)
        self.title = title

    def catch(self):
        super().catch()
        print("What a rude thing to do to", self.title, self.name + "!\n")

class NiceFish(Fish):
    def release(self):
        print("You attempt to release", self.name + ".", end = " ")
        if self.caught:
            print("Success!\n", Fish.__str__(self), "\n")
            self.caught = False
            Fish.school.append(self)
        else:
            print(self.name, "was already free!\n")

        
        
#MAIN

# Comment parts of this test code in as you implement them above

# test code for Part 1 ONLY
#fish1 = Fish("Bass", 10)
#fish2 = Fish("Goldfish", 2)
#fish3 = Fish("Shark", 50)
#print(fish3)

# This is the rest of the test code for Part 1, but it's easier
# to test without it first.

#print(fish1.name, "is longer than", fish2.name, ":", fish1 > fish2)
#print(fish1.name, "is longer than", fish3.name, ":", fish1 > fish3)
#print()
#fish1.catch()
#fish1.catch()


### test code for Part 2 - delete above test code

#fish1 = Fish("Bass", 10)
#fish2 = Fish("Goldfish", 2)
#fish3 = Fish("Shark", 50)
#Fish.remaining()
#Fish.largest()
#fish1.catch()
#Fish.remaining()

### test code for Part 3 - delete above test code

fish1 = StealthFish("007", 11)
fish2 = FancyFish("Lord","Grantham", 10)
fish3 = NiceFish("Nemo", 3)
fish1.catch()
fish2.catch()
fish3.catch()
fish3.release()
fish3.release()
Fish.remaining()


