// var React = require('react')
// var ReactDOM = require('react-dom')
// var GameList = require('/components/Main');

// var HelloWorld = React.createClass({
//   render: function(){
//     return (
//       <div>
//         Hello World!
//       </div>
//     )
//   }
// });

function loadGames() {
	$.ajax({
		url: "/games",
		success: function(result) {
			var games = result;
			ReactDOM.render(<GameList games={games} />, document.getElementById('app'));
		}
	})
}

loadGames();