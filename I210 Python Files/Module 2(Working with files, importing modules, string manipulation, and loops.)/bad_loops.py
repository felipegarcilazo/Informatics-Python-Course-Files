
for i in range(11):
        for j in range(11):
                if (i == 0) and (j == 0):
                        print('\t *', end = '')
                elif (i == 0) or (j == 0):
                        print('\t', i+j, end = '')
                else:
                        print('\t', i * j, end = '')
        print()





#rows = int(input("How many rows should we have?"))
#cols = int(input("How many columns should we have?"))
#
#for i in range(rows):
#        print("Row", i, ":", end = ' ')
#        for j in range(cols):
#                print(j, end = ' ')
#        print()
