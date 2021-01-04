def fib(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num-2)
for i in range(40):
    print(i, fib(i))



#def factorial(num):
#    if num == 1:
#        return 1
#    else:
#        return factorial(num - 1) * num
#print(factorial(20))







#def open_file(filename):

    # try to open the file with the filename given
#    while True:
#        try:
#            file = open(filename, 'r')
#            data = file.readlines()
#            file.close()
    # if that doesn't work, ask again until you get a good filename
#        except:
#            filename = input("That filename doesn't exist. Please enter a"
#                                  "filename:")
    # when you get a valid filename, open the file and read the contents into a list
#        else:


    # remove any newlines, then send the contents back
#            for i in range(len(data)):
#                data[i] = data[i].strip()
#            return data
#main

#data = open_file("doesn'texist.txt")
#print("The contents of the file:")
#print(data)




#while True:
#    try:
#        num = int(input("Enter an integer: "))
#    except:
#        print("That wasn't an integer")
#    else:
#        print("Integer entered")
#        break
