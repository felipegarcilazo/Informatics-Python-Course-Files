#! /usr/bin/env python3

import cgi

print('Content-type: text/html\n')

form = cgi.FieldStorage()

html = """
<!doctype HTML>
<head>
	<meta charset="utf-8">
	<title>guess my card</title>
	<link rel="stylesheet" href="http://cgi.soic.indiana.edu/~dpierz/i211.css">
</head>
<body>
	<h1>You guessed:</h1>
	{0}
	<h2>Suit:</h2>
	{1}
	<h2>Rank:</h2>
	{2}
</body>
</html>
"""

rank_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

cpu_rank = "9"
cpu_suit = "C"

rank_ch = form.getfirst("rank", "2")
suit_ch = form.getfirst("suit", "C")
image = '<img src="cards/'+str(rank_ch)+suit_ch+'.jpg">'

if suit_ch == cpu_suit:
	message1 = "<p>Correct Suit!</p>"
else:
	message1 = "<p>Wrong Suit!</p>"
	
if rank_ch == cpu_rank:
	message2 = "<p>Correct Rank!</p>"
elif rank_list.index(rank_ch) < rank_list.index(cpu_rank):
	message2 = "<p>Too Low!</p>"
else:
	message2 = "<p>Too High!</p>"

if message1 != "<p>Correct Suit!</p>" or message2 != "<p>Correct Rank!</p>":
	html += """
	<form method="post" action="guessmycard.cgi">
	<h2>Try to guess the card!</h2>
	<p>Rank:
		<select name="rank">
			<option>2</option>
			<option>3</option>
			<option>4</option>
			<option>5</option>
			<option>6</option>
			<option>7</option>
			<option>8</option>
			<option>9</option>
			<option>10</option>
			<option>J</option>
			<option>Q</option>
			<option>K</option>
			<option>A</option>
		</select>
	</p>
	<p>Suit:
		<br><input type="radio" name="suit" value="C" checked="">Clubs
		<br><input type="radio" name="suit" value="D">Diamonds
		<br><input type="radio" name="suit" value="H">Hearts
		<br><input type="radio" name="suit" value="S">Spades
	</p>
	<button type="submit">Submit</button>
	</form>
	"""

print(html.format(image, message1, message2))