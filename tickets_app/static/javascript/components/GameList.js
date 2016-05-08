var GameList = React.createClass({
    render: function(){
        var games = this.props.games.map(function(game) {
            return <Game game={game} key={game.game_date} />
        });

        return (
            <ul>
                {games}
            </ul>
        );
    }
});

var Game = React.createClass({
    render: function() {
        var game = this.props.game;
        return (
            <li>
                {game.game_date}, {game.time}, {game.opponent}, {game.promotion}
            </li>
        );
    }
});