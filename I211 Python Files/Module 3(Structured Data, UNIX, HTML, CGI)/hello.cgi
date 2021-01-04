#! /usr/bin/env python3
print('Content-type: text/html\n')#necessary for it to work!
    
text = """<!doctype html><html><head><meta charset="utf-8">
    <link rel="stylesheet" href="https://cgi.sice.indiana.edu/~dpierz/i211.css">
    <title>First CGI</title></head><body><table>""""
for i in range(10):
    text += "<tr>"
    for x in range(10):
        text += "<td>ROW", i, "Column", x, "</td>"
    text += "</tr>"
"""</table></body></html>"""
print(text)
