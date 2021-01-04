class Robot(object):
    """Robot with a name, weapon, strength, and rating"""
    robot_list = []
    @staticmethod
    def contenders():
        if len(Robot.robot_list) == 0:
            print("There are", len(Robot.robot_list), 'robots.\n')
        else:
            print("There are", len(Robot.robot_list), 'robots.\n')
            for i in range(len(Robot.robot_list)):
                print(Robot.robot_list[i])
    
    def __init__(self, name, weapon, strength_rat):
        self.name = name
        print("Robot Created!", self.name)
        self.weapon = weapon
        self.strength_rat = strength_rat
        self.online = True
        Robot.robot_list.append(self)


    def __str__(self):
        if self.online:
            status = "Online"
        else:
            status = "Offline"
        text = "---------------\nFighting Robot:\nName: " + self.name + \
               '\nWeapon: ' + self.weapon + \
               "\nStrength Rating: " + str(self.strength_rat) + \
               "\nStatus: " + status + "\n---------------"
        return text


# MAIN
Robot.contenders()

r2d2 = Robot("R2D2", "Beeps", 2)
c3p0 = Robot("C3P0", "Conversations", 2)

Robot.contenders()


#class Card(object):
#    """This creates a card"""
#    def __init__(self, suit, rank):
#        self.suit = suit
#        self.rank = rank


#class Container(object):
#    """This is a container that has a max capacity"""
#    def __init__(self, max_cap):
#        self.max_cap = max_cap
#        self.current_cap = 0
        

#class Course(object):
#    """This is a class with its associated information"""
#    def __init__(self, course_num, num_cred, time, location, instructor):
#       self.course_num = course_num
#        self.num_cred = num_cred
#        self.time = time
#        self.location = location
#        self.instructor = instructor


#card1 = Card('Heart', "Nine")
#container1 = Container(60)
#course1 = Course("I210", 3, "12:15", "Ballantine", "Duncan")
