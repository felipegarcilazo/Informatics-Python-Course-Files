import urllib.request, ssl, os
##context = ssl._create_unverified_context()
##web_page = urllib.request.urlopen("http://www.soic.indiana.edu/", context=context)
##contents = web_page.read().decode(errors="replace")
##web_page.close()
##
##file_out = open("page.html", "w", encoding="utf-8")
##file_out.write(contents)
##file_out.close()
##
##print("All done! Open page.html in your browser! ")


def getContent(url):
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen (url, context=context)
    contents = web_page.read().decode(errors="replace")
    web_page.close()
    print("Attempting to access the page at this URL:\n" + url)
    
    if os.path.basename(url):
        print("All done! Open", os.path.basename(url), "in your browser")
        file_out = open(os.path.basename(url), "w", encoding="utf-8")
    else:
        print("All done! Open index.html in your browser")
        file_out = open("index.html", "w", encoding="utf-8")
    file_out.write(contents)
    file_out.close()

#6
#39
#<p>
#<h3>
#
    
