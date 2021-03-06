from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models.meta import DBSession
from ..models import Game, Price, Purchase, Ticket


@view_config(route_name='home', renderer='templates/dashboard.jinja2')
def my_view(request):
    try:
        # games = DBSession.query(Game).all()
        tickets = DBSession.query(Ticket).order_by(Ticket.game_id)
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'tickets': tickets}


@view_config(route_name='games', renderer='json')
def get_games(request):
    try:
        games = DBSession.query(Game).all()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)

    game_list = []
    for game in games:
        game_data = {}
        game_data['game_id'] = game.game_id
        game_data['game_date'] = game.game_date.strftime('%b %d')
        game_data['time'] = game.time.strftime('%l:%M %p')
        game_data['opponent'] = game.opponent
        game_data['promotion'] = game.promotion

        game_data['tickets'] = []

        game_list.append(game_data)

    fake_ticket1 = {
        'ticket_id': 1,
        'status': 'Available',
        'section': 'VR317',
        'row': 4,
        'seat': 21,
        'price': 10,
        'purchase_date': None,
        'buyer': None,
        'purchase_price': None,
        'payment': None
    }

    fake_ticket2 = {
        'ticket_id': 2,
        'status': 'Sold',
        'section': 'VR317',
        'row': 4,
        'seat': 22,
        'price': 10,
        'purchase_date': '5/11/16',
        'buyer': 'Bob',
        'purchase_price': 15,
        'payment': 'Cash'
    }

    game_list[0]['tickets'] = [fake_ticket1, fake_ticket2]
    
    return game_list


@view_config(route_name='tickets', renderer='json')
def get_tickets(request):
    game_id = request.GET.get('game_id')
    try:
        tickets = DBSession.query(Ticket).filter(Ticket.game_id == game_id)
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)

    ticket_list = []
    for ticket in tickets:
        ticket_data = {}
        ticket_data['ticket_id'] = ticket.ticket_id
        ticket_data['game_id'] = ticket.game_id
        ticket_data['section'] = ticket.section
        ticket_data['row'] = ticket.row
        ticket_data['seat'] = ticket.seat
        ticket_data['price'] = ticket.price
        ticket_data['is_purchased'] = ticket.is_purchased
        ticket_data['hold_for_us'] = ticket.hold_for_us

        ticket_list.append(ticket_data)
    
    return ticket_list


@view_config(route_name='add_purchase', renderer='templates/purchase.jinja2')
def add_purchase(request):

    import ipdb
    ipdb.set_trace()
    try:
        games = DBSession.query(Game).all()
        tickets = DBSession.query(Ticket).order_by(Ticket.game_date)
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'games': games,
            'tickets': tickets}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_tickets_app_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

