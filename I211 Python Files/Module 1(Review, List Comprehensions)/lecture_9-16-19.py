##file_name = input("Please enter a file name: ")
##sentences = [sent.strip() for sent in open(file_name, "r")]
##print("All lines in the file:", sentences)
##two_v_words = [word for line in sentences for word in line.split(" ") if len([let for let in word if let in "aeiou"]) >= 2]
##print("The words in the file that contain 2 or more vowels:", two_v_words)

phrase = input("Please enter the phrase to translate: ")
dictionary = {
    "1" : "i",
    "3" : "e",
    "4" : "a",
    "5" : "s",
    "7" : "t",
    }
lst_comp = [dictionary.get(let, let) for let in phrase]
print("Output:", ''.join(lst_comp))
