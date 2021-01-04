import minecraft

## Part Two: Mine stuff
def dig(mine):
# We'll return anything we found as a dictionary
# {name_of_ore : count}
        materials_found = {}
# First ask how deep to dig.
# Print out input to test this part of your program
# Use try/except for this part
# If the user doesn't enter expected input, quit out by returning {}
        try:
                deep = int(input("How deep would you like to dig? "))
        except ValueError:
                print("Try Again you did not enter a number.")

# Then, do the digging.
# Note: this code should only run if the "how deep" checks out
        else:
                if 10 > deep or deep > 100:
                        print("Please choose a depth between 10 and 100!")
                        return materials_found
                for i in range(deep):
                        try:
                                item = mine[i]
                        except IndexError:
                                print("YOU HIT LAVA! \nAll of your materials\n"\
                                      "were destroyed.\nYOu died.")
                                materials_found = {}
                                return materials_found
                        else:
                                print("You found", item)
                                if item in materials_found.keys():
                                        materials_found[item] += 1
                                else:
                                        materials_found[item] = 1
        return(materials_found)


## Main

# 1A: READ IN MATERIALS LIST
try:
        file = open("mining_list.txt", 'r')
        content = file.readlines()
        file.close()
        for i in range(len(content)):
                content[i] = content[i].strip()
except:
        print("Can't find the file.")

# 1B: CREATE MINE
# Hint: temporarily print out your mine to see what the list looks like
# Module function create_mine returns a random list of materials 
# The length of this list will be between 10 and 100 materials
else:
        print("Materials Found")
        mined = minecraft.create_mine(content)
# 2: MINE MATERIALS
        final = dig(mined)

# 3: LOOK THROUGH THE LOOT
# If you found some ore, did you find any rare items 
# like obsidian, diamonds or gold?
        if final:
                if 'gold' in final.keys():
                        print('Excellent, you found', final['gold'], 'gold.')
                if 'diamond' in final.keys():
                        print("Excellent, you found", final['gold'],
                              'diamond.')
                if 'obsidian' in final.keys():
                        print('yes! you found the rarest mineral obsidian')
                        





