#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()

html = """
<!DOCTYPE html>
<html>
<head>
	<meta charset='utf-8'>
	<link rel='stylesheet' href='http://cgi.soic.indiana.edu/~dpierz/i211.css'>
	<title>Alphabet Practice</title>
</head>
<body>
	{img}
	{message}
	<form method='post' action='labpractical3.cgi'>
            <p>The letter:
            <select name='letter'>
                <option>a</option>
                <option>b</option>
                <option>c</option>
                <option>d</option>
                <option>e</option>
                <option>f</option>
                <option>g</option>
                <option>h</option>
                <option>i</option>
                <option>j</option>
                <option>k</option>
                <option>l</option>
                <option>m</option>
                <option>n</option>
                <option>o</option>
                <option>p</option>
                <option>q</option>
                <option>r</option>
                <option>s</option>
                <option>t</option>
                <option>u</option>
                <option>v</option>
                <option>w</option>
                <option>x</option>
                <option>y</option>
                <option>z</option>
            </select>
            </p>
            <p>Is for: <input type='text' name='guess'></p>
        <button type='submit'>Submit</button>
</body>
</html>
"""

dictionary = {
	"a" : "Ackbar",
	"b" : "Bossk",
	"c" : "Chewie or C-3PO",
	"d" : "Dash Rendar",
	"e" : "Ewoks",
	"f" : "Fett",
	"g" : "Greedo",
	"h" : "Han Solo",
	"i" : "IG-88",
	"j" : "Jabba",
	"k" : "Kyle Katarn",
	"l" : "Luke and Leia",
	"m" : "Mara Jade",
	"n" : "Nien Nunb",
	"o" : "Obi-Wan",
	"p" : "Palpatine",
	"q" : "Quinlan Vos",
	"r" : "R2-D2",
	"s" : "Storm Troopers",
	"t" : "Thrawn",
	"u" : "Ulic Qel-droma",
	"v" : "Vader",
	"w" : "Wedge",
	"x" : "Xizor",
	"y" : "Yoda",
	"z" : "Zuckuss"
}

let = form.getfirst("letter", "a")
guess = form.getfirst("guess", "")
image = "<img src='images/" + let + ".jpg'>"
if dictionary[let] == guess:
	mes = "<h2>That's Correct</h2>"
else:
	mes = "<h2>Sorry, the correct response was " + dictionary[let] + "</h2>"

print(html.format(img = image, message = mes))

