import urllib.request, re, ssl, random, webbrowser

def wiki_list(website_url):
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen(website_url, context=context)
    contents = web_page.read().decode(errors="replace")
    web_page.close()

    body = re.findall('(?<=<body).+?(?=</body>)', contents, re.DOTALL)[0]
    hits = re.findall('(?<=href=").+?(?=")', body)
    wiki_links = [link for link in hits if "wiki" in link]
    return wiki_links

#Main
start = input("Where would you like to start? ")
num_jumps = input("How many Jumps?")
for i in range(int(num_jumps)):
    webbrowser.open(start)
    print("Jumping from:", start)
    start = "https://en.wikipedia.org" + random.choice(wiki_list(start))
    print("TO: ", start)
