##import os
##def files_bytes(folder):
##    add = 0
##    contents = [file for file in os.listdir(folder)]
##    for content in contents:
##        if os.path.isdir(content):
##            new_directory = os.path.join(folder, content)
##            files_bytes(new_directory)
##        else:
##            add += os.path.getsize(content)
##    return add
##
### Main
##usr_direct = input("Please ente a file location: ")
##print(files_bytes(usr_direct))

##import datetime
##now = datetime.date(2015, 1, 1)
##print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B"))


import datetime, time, random
start = time.clock()
while True:
    year, month, day = random.randrange(1900, 2001), random.randrange(1, 13), random.randrange(1, 32)
    try: 
        print(datetime.date(year, month, day).strftime("%d %b %Y is a %A on the %d day of %B"))
        if datetime.date(year, month, day).strftime("%A")=="Thursday" and year%7 == 0 and month==2:
            print("Found one!")
            break
    except:
        print("Tried a date that couldn't work.")
end = time.clock()
print("Total Time:", end-start, "seconds")
