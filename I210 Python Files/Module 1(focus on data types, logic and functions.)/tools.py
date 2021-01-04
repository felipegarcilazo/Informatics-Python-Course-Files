#--------------------------------------------------------------
#               Official Tools Module for I210
#                           Version 1
#--------------------------------------------------------------

#---------------------------------------------------------------------
#To use this file, place it in the same directory as your python code,
#then add the line:
#               from tools import *
#to the top of your python code. You can then use these functions.
#
#As you write new functions, add them to this file! If you keep this
#up-to-date and organized, it will help you tremendously!
#---------------------------------------------------------------------

#------------------------------
# string manipulation functions
#------------------------------

#prints out a birthday greeting, demonstrates default values
def birthday(name="Joe", age=21):
    print("Happy Birthday", name, "! You're", age, "!")
    
#Places dashes around every character of the string and returns it
def dasher(string):
    return "-" + "-".join(list(string)) + "-"

#pads a string out to 20 characters with dashes
def dasher2(string):
    if len(string) > 20:
        string = "Error"
    dashes =(20 - len(string))

    half = int(dashes/2)
    
    formatted = "-" * half + string + "-" * half

    if (dashes % 2 == 1):
        formatted += "-"
    return formatted



#------------------------------
# number manipulation functions
#------------------------------

#returns the sum and product of two numbers
def addmult(num1, num2):
    add = num1 + num2
    mult = num1 * num2
    return add, mult

#returns True if a number is odd, False otherwise
def odd(number):
    return number % 2 == 1

#returns True if the difference between two numbers is odd, False otherwise
def odd_diff(num1, num2):
    difference = num1 - num2
    return odd(difference)

#returns the sum of a list of numbers
def summation(numbers):
    total = 0
    for num in numbers:
	    total += num
    return total

#returns the average of a list of numbers
def mean(numbers):
    total = 0.0
    for num in numbers:
            total += num
    return total/len(numbers)



#------------------------------
# list manipulation functions
#------------------------------


# swap goes here




#------------------------------
# printing functions (no return)
#------------------------------


# print_range goes here
def print_range(low, high, factor):
    for i in range(low, high):
        if i % factor == 0:
            print(str(i) + ' is divisible by ' + str(factor))

#------------------------------
# validation functions
#------------------------------






#-----------------------------
# test code goes here
#-----------------------------

if __name__ == "__main__":
    print("Testing dasher:", dasher("this is a test") == "-t-h-i-s- -i-s- -a- -t-e-s-t-")
    print("Testing odd_diff:", odd_diff(18,9))

    nums = [1,2,3,4]

    print("Testing summation:", summation(nums) == 10)
    print("Testing mean:", mean(nums) == 2.5)



