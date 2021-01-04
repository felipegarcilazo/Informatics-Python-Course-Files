#! /usr/bin/env python3
print('Content-type: text/html\n')

import random

poke_lst = ["fire", "water", "grass"]
cpu_typ = random.choice(poke_lst)

html = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Pokemon winner</title>
</head>
<body>
<p>You CHose {user}</p>
<p>computer chose {comp}</p>
<h1>{message}</h1>
</body></html>
"""

form = cgi.FieldStorage()
usr_typ = form.getfirst("symbol", 'fire')
if usr_typ == "fire":
    print(html.format(user = "fire"))
    if cpu_typ == "fire":
        print(html.fomate(comp = "fire"))
        print(html.format(message = "DRAW"))
    elif cpu_typ == "water":
        print(html.fomate(comp = "water"))
        print(html.format(message = "SORRY YOU HAVE LOST"))
    else:
        print(html.fomate(comp = "grass"))
        print(html.format(message = "CONGRATULATIONS YOU WON"))
elif usr_typ == "water":
    print(html.format(user = "water"))
    if cpu_typ == "fire":
        print(html.fomate(comp = "fire"))
        print(html.format(message = "CONGRATULATIONS YOU WON")) 
    elif cpu_typ == "water":
        print(html.fomate(comp = "water"))
        print(html.format(message = "DRAW"))
    else:
        print(html.fomate(comp = "grass"))
        print(html.format(message = "SORRY YOU HAVE LOST"))
else:
    if cpu_typ == "fire":
        print(html.fomate(comp = "fire"))
        print(html.format(message = "SORRY YOU HAVE LOST"))
    elif cpu_typ == "water":
        print(html.fomate(comp = "water"))
        print(html.format(message = "CONGRATULATIONS YOU HAVE WON!!"))
    else:
        print(html.fomate(comp = "grass"))
        print(html.format(message = "DRAW"))
