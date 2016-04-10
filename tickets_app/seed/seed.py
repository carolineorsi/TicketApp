from ..models import Game
import csv
from datetime import datetime

def load_games(session):
	f = open("./tickets_app/seed/games.csv", "r")
	f.readline()
	data = csv.reader(f, delimiter=",")
	games_list = []
	i = 0

	for row in data:
		game = Game()
		game.date = datetime.strptime(row[0], "%m/%d/%y")
		game.time = datetime.strptime(row[1], "%I:%M %p")
		game.opponent = row[2]
		game.promotion = row[3]
		game.price = float(row[4])
		
		games_list.append(game)	
		session.add(games_list[i])
		i += 1

def main():
	session = seed.connect()
	load_games(session)
	session.commit()

if __name__ == "__main__":
	main()