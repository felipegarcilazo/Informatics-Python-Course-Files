# Problem 4.23

def average():
    usr_input = input("Enter a sentence: ")
    split = usr_input.split()
    wrd_len = 0
    for word in split:
        wrd_len += len(word)
    wrd_len /= len(split)
    print(wrd_len)
    
average()

# Problem 4.25

def vowelCount(string):
# to count both lower and upper case vowels
    consistent = string.lower()
# counts the number of each vowel
    a_num = consistent.count('a')
    e_num = consistent.count('e')
    i_num = consistent.count('i')
    o_num = consistent.count('o')
    u_num = consistent.count('u')
    return ('a, e, i, o, and u appear, respectively,', a_num, e_num, i_num,
            o_num, u_num)

print(vowelCount('Le Tour de France'))
