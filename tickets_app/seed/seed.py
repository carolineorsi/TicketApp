from ..models import Game, Ticket
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
		game.game_date = datetime.strptime(row[0], "%m/%d/%y")
		game.time = datetime.strptime(row[1], "%I:%M %p")
		game.opponent = row[2]
		game.promotion = row[3]
		
		games_list.append(game)	
		session.add(games_list[i])
		i += 1

def load_tickets(session):
	f = open("./tickets_app/seed/tickets.csv", "r")
	f.readline()
	data = csv.reader(f, delimiter=",")
	ticket_list = []
	i = 0

	for row in data:
		ticket = Ticket()
		ticket.game_id = row[0]
		ticket.section = row[2]
		ticket.row = row[3]
		ticket.seat = row[4]
		ticket.price = float(row[5])
		ticket.is_purchased = 0
		ticket.hold_for_us = 0

		ticket_list.append(ticket)
		session.add(ticket_list[i])
		i += 1


def main():
	session = seed.connect()
	load_games(session)
	load_tickets(session)
	session.commit()

if __name__ == "__main__":
	main()