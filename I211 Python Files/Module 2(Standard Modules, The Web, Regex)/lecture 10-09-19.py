import re, urllib.request, ssl

##website = "http://cgi.soic.indiana.edu/~dpierz/test.html"
##print("Searching:", website)
##context = ssl._create_unverified_context()
##web_page = urllib.request.urlopen(website, context=context)
##contents = web_page.read().decode(errors="replace")
##web_page.close()
##
##head = re.findall('(?<=head>).+(?=</head>)', contents, re.DOTALL)[0]
##print("Head:", head, sep="\n")
##
##body = re.findall('(?<=body).+(?=</body>)', contents, re.DOTALL)[0]
##print("body", body, sep ="\n")

website = "https://en.wikipedia.org/wiki/Wikipedia:General_disclaimer"
context = ssl._create_unverified_context()
web_page = urllib.request.urlopen(website, context=context)
contents = web_page.read().decode(errors="replace")
web_page.close()

body = re.findall('(?<=body).+(?=</body>)', contents, re.DOTALL)[0]
wiki_links = re.findall('(?<=href=")/wiki/.+?(?=")', body, re.DOTALL)
print(wiki_links)
