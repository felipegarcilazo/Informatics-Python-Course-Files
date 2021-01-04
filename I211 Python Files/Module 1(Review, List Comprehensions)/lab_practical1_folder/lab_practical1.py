#List comprehension that loads passwords.txt
load_file = [password.strip() for password in open("passwords.txt", "r")]

# This is the show list function
def show_list(all_passwords):
    print("The current possible passwords are:", "-"*30, sep="\n")
# Prints out 5 passwords per line.
    for i in range(len(all_passwords)):
        print(all_passwords[i], end = " ")
        if (i+1)%5 == 0:
            print()

# main
show_list(load_file)

#list comprehension that checks to see if there is at least 6 characters
least_six = [password for password in load_file if len(password) >= 6]
print("\nClue 1: The password is at least 6 characters long\n")
show_list(least_six)

#Checks to see if there is at least a single letter in the password.
least_let = [password for password in least_six \
             if len([let for let in password if let not in "1234567890"])>=1]
print("\nClue 2: The password contains at least one letter\n")
show_list(least_let)

#Checks to see if it starts with a consonant and second starts with a vowel
start_sec_char = [password for password in least_let \
                  if password[0] not in "aeiou" and password[1] in "aeiou"]
print("\nClue 3: The password does not start with a vowel and the second character is\n")
show_list(least_six)

#Checks to see if there are double the amount of consonat than there are vowels.
cons_vs_vow = [password for password in start_sec_char \
               if len([let for let in password if let not in "aeiou"]) >= 2 *\
               len([let for let in password if let in "aeiou"])]
print("\nClue 4: The password has at least twice as many consonants as vowels\n")
show_list(cons_vs_vow)

# Checks to see if vowels are in alphabetical order.BONUS
vow_alphabet = [password for password in cons_vs_vow \
                if [let for let in password if let in "aeiou"] == \
                sorted([let for let in password if let in "aeiou"])]
print("\n\nPassword Found!", "-"*30, vow_alphabet, sep="\n")
