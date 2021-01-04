list_input = eval(input("Enter a List of numbers?"))
while True:
    swaps = False
    for i in range(len(list_input)-1):
        if list_input[i+1] < list_input[i]:
            list_input[i], list_input[i+1] = list_input[i+1], list_input[i]
            swaps = True
    if swaps == False:
        break
print(list_input)
