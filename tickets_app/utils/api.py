def get_games():
	try:
        games = DBSession.query(Game).all()
        tickets = DBSession.query(Ticket).order_by(Ticket.game_date)
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'tickets': tickets}