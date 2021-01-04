alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.',
        ' ', ';', ':', '!']

# PROBLEM 1
def encrypt(message, keyword, key_let):
    dictionary = {'A': '', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '',
                  'J': '', 'K': '', 'L': '', 'M': '', 'N': '', 'O': '', 'P': '', 'Q': '', 'R': '',
                  'S': '', 'T': '', 'U': '', 'V': '', 'W': '', 'X': '', 'Y': '', 'Z': '', '0': '',
                  '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '',
                  ',': '', '.': '', ' ': '', ';': '', ':': '', '!': ''}
    keyword_no_repeat = ''
    encrypted_mess = ''
    for char in keyword:
        if char not in keyword_no_repeat:
            keyword_no_repeat += char
    for i in range(alph.index(key_let), len(dictionary) + alph.index(key_let) + 1):
        if alph.index(key_let) + len(keyword_no_repeat) > i >= alph.index(key_let):
            dictionary[alph[i % 42]] = keyword_no_repeat[(i - alph.index(key_let)) % 42]
        for j in range(len(alph)):
            if i > alph.index(key_let) + len(keyword_no_repeat) and alph[j] not in dictionary.values():
                dictionary[alph[(i - 1) % 42]] = alph[j]
                break
    for char in message:
        encrypted_mess += dictionary[char]
        
    return encrypted_mess


def decrypt(enc_mess, keyword, key_let):
    dictionary = {'A': '', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '',
                  'J': '', 'K': '', 'L': '', 'M': '', 'N': '', 'O': '', 'P': '', 'Q': '', 'R': '',
                  'S': '', 'T': '', 'U': '', 'V': '', 'W': '', 'X': '', 'Y': '', 'Z': '', '0': '',
                  '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '',
                  ',': '', '.': '', ' ': '', ';': '', ':': '', '!': ''}
    dictionary2 = {}
    keyword_1 = ''
    dec_mess = ''
    for char in keyword:
        if char not in keyword_1:
            keyword_1 += char
    for i in range(alph.index(key_let), len(dictionary) + alph.index(key_let) + 1):
        if alph.index(key_let) + len(keyword_1) > i >= alph.index(key_let):
            dictionary[alph[i % 42]] = keyword_1[(i - alph.index(key_let)) % 42]
        for j in range(len(alph)):
            if i > alph.index(key_let) + len(keyword_1) and alph[j] not in dictionary.values():
                dictionary[alph[(i - 1) % 42]] = alph[j]
                break
    for x, y in dictionary.items():
        dictionary2[y] = x
    for char in enc_mess:
        dec_mess += dictionary2[char]
    return dec_mess


# PROBLEM 2

# DECYPHERED ANSWER: KEYWORD = "I231 IN THE SPRING OF 2018!" KEYLETTER = "A"
# IN 1929, FRIEDMAN WAS SELECTED TO BECOME THE CHIEF OF THE NEW SIGNAL INTELIGENCE SERVICE.
# THROUGHOUT THE EARLY AND MIDDLE 1930S, FRIEDMAN CREATED THE ORGANIZATIONAL FOUNDATIONS OF A
# CRYPTOLOGIC STRUCTUREQ WHICH INVOLVED INTO THE ARMY SECURITY AGENCY IN WORLD WAR II. FRIEDMAN
# LED THE TRANSITION FROM PENCIL AND PAPER CRYPTOLOGY INTO THE MODERN ERAQ CHARACTERIZED BY THE
# APPLICATION OF MACHINES TO BOTH CRYPTOGRAPHY AND CRYPTANALYSIS. HE DID THIS PRIMARILY BY
# CODIFYING WHAT HAD ALREADY BEEN WRITTEN AND BY APPLYING MATHEMATICQ PARTICULARLY STATISTICAL
# ANALYSISQ TO CRYPTOLOGY.

# 2A) No, it will not work because for the other cipher once you solve for one pair of letters
# then you can get the pairs for the encrypted and plaintext alphabet.
# 2b) My hacking strategy was to find the most common letters in the encrypted text and then pair
# them to the most occuring letter in the english alphabet which is the space character followed by
# 'E', 'T', and 'A'. I also noticed that there was ".I." in the text which I knew that "." were
# space characters as this was the most occuring ciphertext letter. Therefore, I could tell the "I"
# in the sequence was "A" in plaintext. Then, once you find a couple of these then you can slowly
# solve for words such as 'CH ' is 'THE' decrypted and once I get enough pairs then the ciphertext
# starts to take form and you can more easily deduce which letters pair with the others until you
# have the last few remaining.
# 2b) The strategy I used would work on an affine cipher as you can look for the most occuring text
# in that cipher and then pair them to the most occuring letters. However, this is a longer process
# and requires you to look for close matches of words and common pairs. 

mess = "EO.V7W78.NAE 1GIO.KIB.B R 3C 1.CF.2 3FG .CH .3HE N.FN.CH .O K.BETOIR.EOCRET O3 .B AJE3 ,.CHAFDT"\
       "HFDC.CH . IARM.IO1.GE11R .V7XUB8.NAE 1GIO.3A IC1.CH .FATIOEQICEFOIR.NFDO1ICEFOB.FN.I.3AM0CFRFTE"\
       "3.BCAD3CDA 8.KHE3H.EOJFRJ 1.EOCF.CH .IAGM.B 3DAECM.IT O3M.EO.KFAR1.KIA.EE,.NAE 1GIO.R 1.CH .CAI"\
       "OBECEFO.NAFG.0 O3ER.IO1.0I0 A.3AM0CFRFTM.EOCF.CH .GF1 AO. AI8.3HIAI3C AEQ 1.2M.CH .I00RE3ICEFO."\
       "FN.GI3HEO B.CF.2FCH.3AM0CFTAI0HM.IO1.3AM0CIOIRMBEB,.H .1E1.CHEB.0AEGIAERM.2M.3F1ENMEOT.KHIC.HI1"\
       ".IRA I1M.2  O.KAECC O.IO1.2M.I00RMEOT.GICH GICE3B8.0IACE3DRIARM.BCICEBCE3IR.IOIRMBEB8.CF.3AM0CF"\
       "RFTM,"
def repeating_chars(message):
    common_let = {' ':0 , 'E':0 , 'T':0, 'A':0}
    num_occur = 0
    sec_num_occur = 0
    third_occur = 0
    fourth_occur = 0
    for i in range(3*len(alph)):
        if message.count(alph[i % 42]) >= num_occur:
            num_occur = message.count(alph[i % 42])
            common_let[' '] = alph[i % 42]
        elif num_occur >= message.count(alph[i % 42]) >= sec_num_occur:
            sec_num_occur = message.count(alph[i % 42])
            common_let['E'] = alph[i % 42]
        elif sec_num_occur >= message.count(alph[i % 42]) >= third_occur:
            third_occur = message.count(alph[i % 42])
            common_let['T'] = alph[i % 42]
        elif third_occur >= message.count(alph[i % 42]) >= fourth_occur:
            fourth_occur = message.count(alph[i % 42])
            common_let['A'] = alph[i % 42]
    return common_let
print(repeating_chars(mess))
def bigraphs(message):
    dictionary = {'TH': 0, 'ER': 0, 'ON': 0}
    lis = []
    lis2 = []
    full_list = []
    for i in range(0, len(message), 2):
        lis.append(message[i:i+2])
    for i in range(1, len(message), 2):
        lis.append(message[i:i+2])
    full_list += lis + lis2
    occur1 = 0
    occur2 = 0
    occur3 = 0
    for i in full_list:
        print(full_list.count(i), i)
        if full_list.count(i) > occur1:
            occur1 = full_list.count(i)
            dictionary['TH'] = i
        elif occur1 > full_list.count(i) > occur2:
            occur2 = full_list.count(i)
            dictionary['ER'] = i
        elif occur2 > full_list.count(i) > occur3:
            occur3 = full_list.count(i)
            dictionary['ON'] = i
    return dictionary

def trigraphs(message):
    dicti = {"THE": 0, "AND": 0, "THA": 0}
    lis3 = []
    for i in range(0, len(message), 3):
        lis3.append(message[i:i+3])
    for i in range(1, len(message), 3):
        lis3.append(message[i:i+3])
    for i in range(2, len(message), 3):
        lis3.append(message[i:i+3])
    count1 = 0
    count2 = 0
    count3 = 0
    for i in lis3:
        if lis3.count(i) > count1:
            count1 = lis3.count(i)
            dicti["THE"] = i
        elif count1 > lis3.count(i) > count2:
            count2 = lis3.count(i)
            dicti['AND'] = i
        elif count2 > lis3.count(i) > count3:
            count3 = lis3.count(i)
            dicti['THA'] = i
    return dicti
