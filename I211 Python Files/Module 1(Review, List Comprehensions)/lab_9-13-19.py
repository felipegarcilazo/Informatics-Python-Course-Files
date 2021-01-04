##result_list = [x**2 for x in range(10)]
##print(result_list)

##doubles = [x+x for x in range(10)]
##print(doubles)

##numbers = [x for x in range(100) if x % 10==0]
##print(numbers)

##words1 = [wrd.upper()  if len(wrd) < 4 else wrd for wrd in ["appple", "ball", "candle", "dog", "egg", "frog"]]
##print(words1)
##words2 = [wrd.upper() for wrd in ["appple", "ball", "candle", "dog", "egg", "frog"] if len(wrd) < 4]
##print(words2)

secret = input("Please enter the secret: ")
lst = ["-" if let.isalpha() else let for let in secret]
print("Redacted:", "".join(lst))
