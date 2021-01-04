# 1(a) The size of the alphabet would be 68 including lower-case, upper-case letters, 10 digits, and 6 punctuation signs.
# 1(b) You would encode by first translating each number to a unique integer and a unique integer when encrypted. You encrypt the text by having an additive key and 
#       multiplitive key. These keys are used to encrypt the message by changing the integer into a different integer. The equation used for an affine cipher to
#       encrypt is K*M+L=C(mod n). Where K is the multiplitive key, L is the additive key, n is the total number of symbals and letters, and C is the encrytped integer.
#       This encrypted integer then can be used to translate it back into a letter.
# 1(c) You decode the encrypted message by getting the integer of the encrypted letter. The decryption process uses the equation of M = (K^-1) * (C-L)[mod n]. Where (K^-1)
#       is the inverse of the multiplication key.
# 1(d) If you encounter some leetter that is not in the alphabet then you can either add it to the extended alphabet and also change the inverse of the
#       multiplicative key as it will not be the same and will change accordingly. If it is not added to the alphabet then it will throw the algorithim off and not
#       decrypt the message correctly.
# 1(e) You pick the encryption key based on K*x[mod n] = 1 where x is the inverse and K is the multiplication Key. You also have to make sure that you do not use an integer
#       that is a divisor of the length of the alphabet or a gcd(k, n) that is other than 1. Therefore the GCD(k, n) has to be 1. If it does not meet this criteria then it
#       will not properly encrypt and decrypt the message.


# the alphabet and message
message = input('Enter a phrase to be encrypted: ')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', ' ',
            ';', ':', '!']
length = len(alphabet)
multiply_key = 19
add_key = 12
inverse = 43

# encoding and encryption.
cipher_text = ''
for letter in message:
    encrypt_num = ((alphabet.index(letter) * multiply_key) + add_key) % length
    cipher_text += alphabet[encrypt_num]
print('The encrypted message is: ' + cipher_text)

# decoding and decryption
decrypted_message = ''
for letter in cipher_text:
    decode_num = ((alphabet.index(letter) - add_key) * inverse) % length
    decrypted_message += alphabet[decode_num]
print('The decoded message is: ' + decrypted_message)
