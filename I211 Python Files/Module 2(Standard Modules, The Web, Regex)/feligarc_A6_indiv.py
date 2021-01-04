## Felipe Garcilazo
## Group 15

## Question 1
## Pattern: #[/w]+

## Question 2
## First Import re, urllib.request, and ssl
## Next you want to open the webpage using urllib.request
## Then you will retrieve the contents(HTML text) from the webpage
## Using Regular Expressions you will look for a pattern that tells if they won or lost
## You will then count these appearances using a loop
## Then print out the appropriate information

## Question 3
import re, urllib.request, ssl
web_page = urllib.request.urlopen("http://cgi.soic.indiana.edu/~dpierz/mbball.html")
contents = web_page.read().decode(errors="replace")
web_page.close()

win_lose = re.findall("(?<=class='schedule_game_results'><div>). ..-..(?=</div>)", contents)
win_count = 0
lose_count = 0
for outcome in win_lose:
    if "W" in outcome:
        win_count += 1
    else:
        lose_count += 1
print("WINS:", win_count, "\nLOSSES:", lose_count)


## Bonus
difference = 0
for outcome in win_lose:
    score = re.findall("..-..", outcome)[0].split("-")
    if int(score[0]) < int(score[1]):
        score[0], score[1] = score[1], score[0]
    difference += int(score[0]) - int(score[1])
print("Difference:", difference)
    
