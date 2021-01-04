import random
class Robot(object):
    robot_list = []

    @staticmethod
    def contenders():
        robots = len(Robot.robot_list)
        print("There are", robots, "robots.\n")
        if robots:
            print("Here is a list of them:")
            for robot in Robot.robot_list:
                print(robot)

    @staticmethod
    def weapon_check():
        dictionary = {}
        for i in range(len(Robot.robot_list)):
            if Robot.robot_list[i].weapon in dictionary.keys() and dictionary[key] == Robot.robot_list[i].weapon:
                for key in dictionary.keys():
                    if dictionary[key] == Robot.robot_list[i].weapon:
                        dictionary[key].append(Robot.robot_list[i].name)
            else:
                dictionary[Robot.robot_list[i].weapon] = Robot.robot_list[i].name
            print(dictionary)
        for key in dictionary.keys():
            print("The robots using the", key, "weapon are:", dictionary[key])

            
    def __init__(self, name, weapon, strength):
        print("Robot created!", name, "\n")
        self.name = name
        self.weapon = weapon
        self.strength = strength
        self.online = True
        Robot.robot_list.append(self)

    def __str__(self):
        reply = "-" * 20 + "\n"
        reply += "Fighting Robot\n"
        reply += "Name: " + self.name + "\n"
        reply += "Weapon: " + self.weapon + "\n"
        reply += "Strength: " + str(self.strength) + "\n"
        if self.online:
            reply += "Status: ONLINE\n"
        else:
            reply += "Status: OFFLINE\n"
        reply += "-" * 20 + "\n"
        return reply

    def fight(self, other):
        if self.online == False:
            print(self.name, "Cannot fight it is offline")
        elif other.online == False:
            print(other.name, "Cannot fight it is offline")
        else:
            print(self.name, "challenges", other.name,"\nClose Match!!!!")
            if self.strength > other.strength:
                winner = self
                other.online = False
            elif other.strength > self.strength:
                winner = other
                self.online = True
            else:
                winner = random.choice(Robot.robot_list)
                Robot.robot_list.remove(winner)
                Robot.robot_list[0].online = False
                Robot.robot_list.append(winner)
            print(winner.name, "Wins, using its", winner.weapon)
            for robot in Robot.robot_list:
                print(robot)
        
        

#main
r2d2 = Robot("R2D2", "Beeps", 2)
c3p0 = Robot("C3P0", "Conversation", 2)
bb8 = Robot("BB-8", "Beeps", 1)
j = Robot("Robot J", "Conversation", 2)
optimus = Robot("Optimus", "Fists", 10)
voltron = Robot("Voltron", "Sword", 10)
gipsy = Robot("Gipsy Danger", "Sword", 9)
Robot.weapon_check()
