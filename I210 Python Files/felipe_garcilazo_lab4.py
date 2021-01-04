#Problem 1
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', ' ', ';', ':', '!']
#Encryption function
def encrypt(message, key):
    encrypted_str = ''
    for i in range(len(message)):
        enc_num = alph.index(message[i]) + alph.index(key[i % len(key)])
        encrypted_str += alph[enc_num % len(alph)]
    return encrypted_str

# Decryption Function
def decrypt(enc_message, key):
    dec_message = ""
    for i in range(len(enc_message)):
        dec_num = alph.index(enc_message[i]) - alph.index(key[i % len(key)])
        dec_message += alph[dec_num % len(alph)]
    return dec_message

# Problem 2
# Key length: 5
# Key: C231S
# Decrypted Message:
# IN 1938, THE JAPANESE REPLACED THE RED MACHINE WITH THE TYPE B MACHINE, WHICH CAME TO BE KNOWN AS PURPLE. IT TOOK A MUCH LARGER TEAM UNDER FRANK ROWLETTS DIRECTION EIGHTEEN MONTHS
# TO BREAK INTO THIS SYSTEM; THE FIRST TRANSLATION WAS PRODUCED IN SEPTEMBER 1940. IT CAME ONE WEEK AFTER A CRUCIAL KEY TO THE PUZZLE HAD BEEN SUGGESTED BY GENEVIEVE GROTJAN, AN SIS
# JUNIOR CRYPTANALYST. AN ANALOG WAS CONSTRUCTED UNDER THE DIRECTION OF LEO ROSEN, AN SIS ENGINEER, AND WHEN IT WAS OPERATIONAL, THE US HAD ACCESS TO ALL OF THE HIGH LEVEL JAPANESE
# DIPLOMATIC COMMUNICATIONS. MR. ROWLETTS AWARDS INCLUDE NSA EXCEPTIONAL CIVILIAN SERVICE AWARD, THE NATIONAL INTELLIGENCE DISTINGUISHED SERVICE MEDAL, THE PRESIDENTS AWARD FOR
# DISTINGUISHED FEDERAL CIVILIAN SERVICE, THE NATIONAL SECURITY MEDAL, AND IN 1964 CONGRESS AWARDED HIM 100,000 FOR HIS INVENTIONS HELD SECRET BY THE GOVERNMENT.
text = "Q!ZML.UXX.P6Z,SX2A5,MYE57T255VEF,5OZ66X4I4,95MYJ9.PYG8WEFLAWE3Z;SK9.:WCYJ80K9Z3SU6ZE6E37X2VAJ:OIEZA ZB:5NE,GX.WA;XSE:H3ZE;3CYMDZEWI:ZF5L6EXXZ2A.OZAJ W1FFXVQD73.Q"\
       "AAXWQ8,EWM!Z;6VF,DO1AZ29M2;X0VFBX.P,FX,6EG54FYG8WE7.C,1YGCSVE:1.QAAX:IEZA9W5H3WLY.:O06CEWU37CO9VRLNE,GXUI:7X6V6ZHWM Z1X16EXSE4EFUQ2:X2MKZE6EF,5OXGMK3MY,1VE3755E"\
       "EH7YMEG5VE3LXYM!7G0MH7XYZAG,SVWZ15EE.DORGA96ZY5CAXF3:STKFENE2AXSV2:!YEI3DOKAAD.ZG5EWLYH:VMDZEZMY699M4G96VYB6OT6BX9WE7:ME2AX,QEZ55O,A5WZWZ15LYJ8WVY.EO42FX6X6E1."\
       "QAA13CYG8WEGFXZI5Z1UK6FDO1AZ13TYB6O197XZQ8,X3MH7 OR2C15ME7XVQB:!4IF.3OKA!; V,51.QAADNE:EWOZAJ W1FFXS42E4,E,A33257X502Z5!K6CE0W!3 OK,I93Q2AX,MDI9UMY3HSZ5XX.P6Z:S1,B"\
       ":STY.:.M;:9YM!55OL,FE0V8H9,P66X,MDI9UMY!5VI;XX.P6ZA9ME.4WVFFXS42E4ONAEXVQEG95OG.DZM5Z6WL6E13E4.G0T,3:O06EG0K6XX.P6Z:S1,B:STYF5U2D.EAE:74STWZ15LY.:O9VTPOKAA79ME"\
       "FXS42E4WLY,94ENNLM8MNXXWDZ800Y.:;M!G96VEZ8WT5ZDWKD7EOJKZEZMY9!;MDA;WVFY"
n = len(text)

#Finds the index of coincidence
ic = 0
for let in alph:
    ni = text.count(let)
    ic += (ni/n) * ((ni-1)/(n-1))
    
#Finds the length of the keyword through the use of the index of coincedence
# The key length is 5
r = (.027*n)/((n-1)*ic-.038*n+.065)

# Frequency attack on the suggetested key length
def columns(enc, num_col):
    for i in range(num_col):
        string = ''
        counter = i
        comm_num = 0
        comm_let = ''
        while counter < len(text):
            string += text[counter]
            counter += 5
        for x in range(len(alph)):
            if string.count(alph[x]) > comm_num:
                comm_num = string.count(alph[x])
                comm_let = alph[x]
        print((alph.index(comm_let) - alph.index(" "))%len(alph))
columns(text, 5)

# These are the characters that you get when you set the values equal to the space character in the alphabet.
print(alph[16], alph[28], alph[29], alph[27], alph[18])

# From this you get Q231S, however when you use the decoder function, However you get some incorrect words or not correct words. So I decided to change it to C231S as it looked similar
# to C231 the course.
print(decrypt(text, "Q231S"))
print(decrypt(text, "C231S"))

# However this was still incorrect as some words were mispelled so I tried I231 as the key word as this is the other course associated with C231.
print()
print(decrypt(text, "I231S"))
