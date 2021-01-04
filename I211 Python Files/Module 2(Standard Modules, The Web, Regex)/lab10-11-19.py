import re, urllib.request, ssl

def get_page(website_url):
    web_page = urllib.request.urlopen(website_url)
    contents = web_page.read().decode(errors="replace")
    web_page.close()
    return contents

table = re.findall('(?<=Highest-grossing films of 2019).+?(?=</table>)', get_page("https://en.wikipedia.org/wiki/2019_in_film"), re.DOTALL)[0]
links = re.findall('(?<=<i><a href=").+?(?=")', table)
for link in links:
    print(link)

usr_link = input("Enter on one of the top 10 movies: ")
link = "https://en.wikipedia.org" + usr_link
plot = re.findall('(?<=id="Plot").+?(?=<h2)', get_page(link), re.DOTALL)
print(plot[0])
