import re, urllib.request, ssl
##statement = "test loon etta planet aaw meek ziiim trt"
##print("Original:", statement)
##print("Match:", re.findall("[\w]*[aeiouAEIOU][aeiouAEIOU][\w]*", statement))

url_search = input("Search what Page?")
context = ssl._create_unverified_context()
web_page = urllib.request.urlopen (url_search, context=context)
contents = web_page.read().decode(errors="replace")
web_page.close()

emails = re.findall("[\w]*[@][\w]*\.[\w]*", contents)
print("The email addresses in", url_search)
for email in emails:
    print(email)
