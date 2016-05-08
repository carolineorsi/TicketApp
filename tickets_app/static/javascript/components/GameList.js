var GameList = React.createClass({
    render: function(){
        var games = this.props.games.map(function(game) {
            return <Game game={game} key={game.game_date} />
        });

        return (
            <table className="game-list">
                <tbody>
                    <tr className="game-list-header-row">
                        <th>Date</th>
                        <th>Time</th>
                        <th>Opponent</th>
                        <th>Promotion</th>
                    </tr>
                    {games}
                </tbody>
            </table>
        );
    }
});

var Game = React.createClass({
    render: function() {
        var game = this.props.game;
        return (
            <tr className="game-list-row">
                <td>{game.game_date}</td>
                <td>{game.time}</td>
                <td>{game.opponent}</td>
                <td>{game.promotion}</td>
            </tr>
        );
    }
});