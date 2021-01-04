import urllib.request, re

# SECTION 1: opening the webpage and storing the html code in contents
web_page = urllib.request.urlopen("https://sice.indiana.edu/news/index.html")
contents = web_page.read().decode(errors="replace")

# SECTION 2
print("Searching: https://sice.indiana.edu/news/index.html")
# looks for the pattern that will get the news articled headline
news_article = re.findall('(?<=head5">).+?(?=</div>)', contents)
# loops through all the articles found to print them out as a string instead of a list
for article in news_article:
    print("\n" + article)

# SECTION 3
print("\nSearching: https://sice.indiana.edu/news/index.html\n")
usr_date = input("Please enter a date to search for: ")
# looks for the pattern that matches the dates that is unique
all_dates = re.findall('(?<=<div class="small meta">).+?(?=</div>)', contents)
# prints out the news article that mathes that date
for i in range(len(all_dates)):
    if usr_date.lower() in all_dates[i].lower():
        print("\n" + news_article[i])
