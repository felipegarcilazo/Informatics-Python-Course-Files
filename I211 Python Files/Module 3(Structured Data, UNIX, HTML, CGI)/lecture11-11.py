import urllib.request, ssl, os

page = ""

for i in range(0, 9):
    digit1 = i
    for x in range(0, 9):
        digit2 = x
        for y in range(0, 9):
            digit3 = y
            for z in range(0, 9):
                digit4 = z
                url = "http://cgi.soic.indiana.edu/~dpierz/secret_vault.cgi?groupname=Group+15&num1=" + str(digit1) + "&num2=" + str(digit2) + \
                       "&num3=" + str(digit3) + "&num4=" + str(digit4)

                print(url)

                web_page = urllib.request.urlopen(url)
                lines = web_page.read().decode(errors="replace")
                web_page.close()

                print(lines)
                if "Wrong!" not in lines:
                    break
