# Felipe Garcilazo
# Team 15

## Open the file teams.txt with using list comprehension and read the lines in the fil while assigning them to a variable
## Display the team name and the number of games won
## Create a different list with list comprehension
## The new list should look to see if the names of the teams are shorter than 5 characters
## If so then place it into the new list
## Display the teams that are in the new list with relevant information
## Create a third list with list comprehension
## Sort through the list based on the wins.
## The top three should be tracked
## Display the team names of the top three winners.

teams_wins = [word.strip().split(" ") for word in open("teams.txt", "r")]

for team_and_win in teams_wins:
    print("The", team_and_win[0], "have won", team_and_win[1], "games")
    
let_fiv = [team[0] for team in teams_wins if len(team[0]) < 5]
print("Teams with names shorter than 5 letters:", let_fiv)

top_thr = sorted([(int(team[1]), team[0]) for team in teams_wins])
winners = [top_thr[i][1] for i in range(3, len(teams_wins))]
print("The three teams with the most wins are:", list(reversed(winners)))
