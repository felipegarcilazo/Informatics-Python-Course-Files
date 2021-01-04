#1 the key is the coins and the values are the value associated with the coin.
#2 the key is each word and the values are the the number of times the word appears.
#3 the key is nicknames and the values are the full names associated with the nickname.
txt_file = open('INCounties2015.txt', 'r')
lnes = txt_file.readlines()
txt_file.close()
dictionary = {}
population = 0
for line in lnes:
    key , value = line.split('\t ')
    dictionary[key] = int(value.strip().replace(',', ''))
    population += dictionary[key]
print('The counties in Indiana are:\n', ", ".join(sorted(dictionary.keys())))

print('The population of Monroe County as of 2015 was:', dictionary['Monroe'])
print('The total IN population as of 2015 was: ', population)
print('So Monroe county Accounts for', dictionary['Monroe']/population*100, "% of IN's population")

