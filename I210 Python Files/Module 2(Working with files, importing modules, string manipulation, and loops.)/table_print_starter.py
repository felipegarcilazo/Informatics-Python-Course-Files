# Table Print v2

def table_print(headers, data, formt):
    output = "{:>{}}" 
    # Add your code here!
    for header_title in headers:
        print(output.format(header_title, formt), end = '')
    print('\n' + '-' * formt*3)
    output2 = "{:>{}}" + "{:>{}}"
    for entry in data:
        city, state = entry
        print(output2.format(city, formt, state, formt))
    print('')
    # Nothing else in the file should change

#main - Don't change this part!
labels = ["Name", "Score"]
scores = [("Abe", 200), ("Bill", 180), ("Mary", 215)]

table_print(labels, scores, 8)

labels2 = ["Capital", "State"]
state_data = [("Atlanta", "GA"), ("Boise", "ID"), ("Boston", "MA"), ("Austin", "TX")]

table_print(labels2, state_data, 8)

