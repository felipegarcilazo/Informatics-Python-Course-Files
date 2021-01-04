import re, urllib.request, ssl
##
##usr_inp = input("Reading in from: ")
##file = open(usr_inp, "r")
##content = file.read()
##file.close()
##
##new_content = re.sub("[\w.-]+@[\w.-]+|[(]?[\d]{0,3}[)]?[ ][\d-]{8}|[A-Z][a-z]*[ ][A-Z][a-z]*",
##                     "Redacted", content)
##file_out= open("messageRedacted.txt", "w")
##file_out.write(new_content)
##file_out.close()

usr_inp = input("Searching: ")
context = ssl._create_unverified_context()
web_page = urllib.request.urlopen(usr_inp, context=context)
contents = web_page.read().decode(errors="replace")
web_page.close()

links = re.findall('(?<=href=").+?(?=")', contents)
print("Found the following the urls:")
for link in links:
    print(link)
