var GameList = React.createClass({
    render: function(){
        var games = this.props.games.map(function(game) {
            return <Game game={game} key={game.game_date} />
        });

        return (
            <div className="game-table">
                {games}
            </div>
        );
    }
});

var Game = React.createClass({
    render: function() {
        return (
            <div>
                <GameDetail game={this.props.game} />
                <TicketList tickets={this.props.game.tickets} />
            </div>
        );
    }
});

var GameDetail = React.createClass({
    // getTickets: function() {
    //     $.ajax({
    //         url: "/tickets",
    //         data: {"game_id": this.props.game.game_id},
    //         success: function(result) {
    //             var tickets = result;
    //         }
    //     })
    // },
    render: function() {
        var game = this.props.game;
        return (
            <div className="game-table-row">
                <table className="game-detail">
                    <tr>
                        <td className="game-detail-expand"><span className="game-expand" onClick={this.getTickets}>+</span></td>
                        <td className="game-detail-date">{game.game_date}</td>
                        <td className="game-detail-time">{game.time}</td>
                        <td className="game-detail-opponent">{game.opponent}</td>
                        <td className="game-detail-promotion">{game.promotion}</td>
                    </tr>
                </table>
            </div>
        );
    }
});

var TicketList = React.createClass({
    render: function() {
        if (this.props.tickets.length >= 1) {
            var tickets = this.props.tickets.map(function(ticket) {
                return <Ticket ticket={ticket} key={ticket.ticket_id} />
            });
            return (
                <div>
                    <table className="ticket-table">
                        <tbody>
                            <tr className="ticket-table-header-row">
                                <th>Status</th>
                                <th>Section</th>
                                <th>Row</th>
                                <th>Seat</th>
                                <th>Price</th>
                                <th>Purchase Date</th>
                                <th>Buyer</th>
                                <th>Purchase Price</th>
                                <th>Payment Type</th>
                            </tr>
                            {tickets}
                        </tbody>
                    </table>
                </div>
            );
        } else {
            return (
                <div></div>
            );
        }
    }
});

var Ticket = React.createClass({
    render: function() {
        return (
            <TicketDetail ticket={this.props.ticket} />
        );
    }
});

var TicketDetail = React.createClass({
    render: function() {
        var ticket = this.props.ticket;

        return (
            <tr className="ticket-table-row">
                <td>{ticket.status}</td>
                <td>{ticket.section}</td>
                <td>{ticket.row}</td>
                <td>{ticket.seat}</td>
                <td>{ticket.price}</td>
                <td>{ticket.purchase_date}</td>
                <td>{ticket.buyer}</td>
                <td>{ticket.purchase_price}</td>
                <td>{ticket.payment}</td>
            </tr>
        );
    }
});