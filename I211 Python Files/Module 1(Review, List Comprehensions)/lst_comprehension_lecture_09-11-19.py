##set_a = [2 * i for i in range(1,5)]
##print(set_a)

##def squares(num):
##    lst_nums = [i**2 for i in range(0, num)]
##    return lst_nums
##print(squares(10))

##low_bnd = int(input("Please enter a lower bound (int): "))
##up_bnd = int(input("Please enter a Upper bound (int): "))
##div = int(input("Please enter a number to divide by (int): "))
##lst = [i for i in range(low_bnd, up_bnd) if i % div == 0]
##print("All of the numbers between", low_bnd, "and", up_bnd, "that are divisible by",
##      str(div) + ":", lst)

fle_name = input("Please enter a file name: ")
all_words = [word.strip() for word in open(fle_name, "r")]
two_v_words = [word for word in all_words if len([let for let in word if let in "aeiou"])>=2]
print("All words in the file:", all_words)
print("The words in the file that contain 2 or more vowels:", two_v_words)
