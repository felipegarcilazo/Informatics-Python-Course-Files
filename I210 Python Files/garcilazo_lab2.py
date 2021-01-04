# 1a)
# You can launch an attack without using a frequency table, which would be more of a brute force attack.
# Trying every possible combination of mutiplication key with every addition keys. However, this method
# would take more time with longer messages
#
# 1b)
# You can use the computer to identify plausible message such as splitting the encrypted text into sections
# a certain length such as 3 letters and comparing it to commonly used three letter words such as 'the' and 'and'
#
# 1c)
# My program checks to see if there is known ciphertext and plaintext combination. If there is then it uses this to
# solve the issue. By using extended euclidean in to solve for the mutiplication key and inverse, which automatically
# assumes the gcd between the two numbers is 1. If there is no plaintext and ciphertext provided then it counts the 
# most occuring letters in the ciphertext and matches them to the ' ' character and 'E' respectively. However, if
# 'THE' is not found in the sentence then the program replaces 'E' with 'T', 'A', 'I', 'N', 'O', 'S' until it finds
# 'THE' is in the decrypted string. When 'THE' is found in the string then that is the decrypted message that is
# returned.
import math
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', ' ',
        ';', ':', '!']
encr_mess1 = 'TB242520C48GVV4S,0247J,04TB245,JTBZ'
encr_mess2 = 'X0N30NL8Q98G4N1T0G8I4M83QNR8WR8D  .8WR8IQNLXWRYLQR,8WR1W4R498X'\
              '08I4M84PPQWRL0182XW0Z8QZ8LX08R0I82NGPLQ4R4TGLW28KRWL,8SW 9'
encr_mess3 = '!QR7LVTR7TQ7T1R3LVGX2T R73!TQ3TRN;7R8L QRLX2RLOR2ETRNL 5RLQR3'\
              ' DG2L;Q;0D:!QJR2ETRJT V;QRTQ!JV;RV;3E!QTW'


def euclidean(x0, y0, d = 1):
    div = []
    copy_div = []
    if y0 > x0:
        y = y0
        y0 = x0
        x0 = y
    while y0 != 0:
        div.append(math.floor(x0 / y0))
        x1 = y0
        y1 = x0 - math.floor(x0 / y0) * y0
        if y1 == 0:
            break
        div.append(math.floor(x1 / y1))
        x0 = y1
        y0 = x1 - math.floor(x1 / y1) * y1
    copy_div += div
    a0 = 1
    b0 = 0
    while True:
        if not div:
            break
        a1 = b0
        b1 = a0 - div[-1] * b0
        div.pop()
        if not div:
            break
        a0 = b1
        b0 = a1 - div[-1] * b1
        div.pop()
    if len(copy_div) % 2 == 1:
        return a1, b1
    else:
        return a0, b0
        

def decrypter(string, plain_txt = '', ciph_txt = ''):
    len_alph = len(alph)
    decrypted_string = ''
    if ciph_txt == '':
        num_let1 = 0
        num_let2 = 0
        com_let1 = ''
        com_let2 = ''
        for letter in string:
            if string.count(letter) > num_let1:
                num_let1 = string.count(letter)
                com_let1 = letter
            elif num_let1 > string.count(letter) > num_let2:
                num_let2 = string.count(letter)
                com_let2 = letter
        encr = (alph.index(com_let1) - alph.index(com_let2)) 
        plain = (alph.index(' ') - alph.index('E')) % len_alph
        if plain % 2 == 0:
            plain /= 2
            len_alph /= 2
            encr /= 2
        if plain % 7 == 0:
            plain /= 7
            len_alph /= 7
            encr /= 7
        if plain % 3 == 0:
            plain /= 3
            len_alph /= 3
            encr /= 3
        z, m = euclidean(len_alph, plain)
        multi_key = (m * encr) % len(alph)
        add_key = (alph.index(com_let1) - multi_key * alph.index(' ')) % len(alph)
        z, multi_inverse = euclidean(len(alph), multi_key)
        multi_inverse = multi_inverse % len(alph)
        for letter in string:
            dec_num_let = ((alph.index(letter) - add_key) * multi_inverse) % len(alph)
            decrypted_string += alph[int(dec_num_let)]
        counter = 0
        while 'THE' not in decrypted_string:
            decrypted_string = ''
            poss_sec_let = ['T', 'A', 'I', 'N', 'O', 'S']
            encr = (alph.index(com_let1) - alph.index(com_let2)) 
            plain = (alph.index(' ') - alph.index(poss_sec_let[counter])) % len(alph)
            z, m = euclidean(len(alph), plain)
            multi_key = (m * encr) % len(alph)
            add_key = (alph.index(com_let1) - multi_key * alph.index(' ')) % len(alph)
            z, multi_inverse = euclidean(len(alph), multi_key)
            counter += 1
            for letter in string:
                dec_num_let = ((alph.index(letter) - add_key) * multi_inverse) % len(alph)
                decrypted_string += alph[int(dec_num_let)]
    else:
        encr = (alph.index(ciph_txt[0]) - alph.index(ciph_txt[1]))
        plain = (alph.index(plain_txt[0]) - alph.index(plain_txt[1])) % len_alph
        z, m = euclidean(len_alph, plain)
        multi_key = (m * encr) % len_alph
        add_key = (alph.index(ciph_txt[0]) - multi_key * alph.index(plain_txt[0])) % len_alph
        z, multi_inverse = euclidean(len_alph, multi_key)
        for letter in string:
            dec_num_let = ((alph.index(letter) - add_key) * multi_inverse) % len_alph
            decrypted_string += alph[dec_num_let]
    return decrypted_string
print(decrypter(encr_mess1, 'ATTACK', 'ITTISQ'))
print(decrypter(encr_mess2))
print(decrypter(encr_mess3))
