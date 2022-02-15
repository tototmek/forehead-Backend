from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import pickle

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class GameModel(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	tags = db.Column(db.String, nullable=False)
	created_by = db.Column(db.String(100), nullable=False)
	cards = db.Column(db.String, nullable=False)
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Game(name = {self.name}, views = {self.views}, likes = {self.likes})"
	
	def jsonify(self):
		return {
			"id": self.id,
			"name": self.name,
			"tags": self.tags,
			"created_by": self.created_by,
			"cards": self.cards,
			"views": self.views,
			"likes": self.likes
		}

game_put_args = reqparse.RequestParser()
game_put_args.add_argument("name", type=str, help="Name of the game is required", required=True)
game_put_args.add_argument("tags", type=str, help="Tags are required", required=True)
game_put_args.add_argument("created_by", type=str, help="Creator of the game", required=True)
game_put_args.add_argument("cards", type=str, help="Cards are required", required=True)
game_put_args.add_argument("views", type=int, help="Views of the game", required=True)
game_put_args.add_argument("likes", type=int, help="Likes on the game", required=True)

game_update_args = reqparse.RequestParser()
game_put_args.add_argument("name", type=str, help="Name of the game is required")
game_put_args.add_argument("tags", type=str, help="Tags are required")
game_put_args.add_argument("created_by", type=str, help="Creator of the game")
game_put_args.add_argument("cards", type=str, help="Cards are required")
game_put_args.add_argument("views", type=int, help="Views of the game")
game_put_args.add_argument("likes", type=int, help="Likes on the game")

game_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'tags': fields.String,
	'created_by': fields.String,
	'cards': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}

class Game(Resource):
	@marshal_with(game_fields)
	def get(self, game_id):
		result = GameModel.query.filter_by(id=game_id).first()
		if not result:
			abort(404, message="Could not find a game with that id")
		return result

	@marshal_with(game_fields)
	def put(self, game_id):
		args = game_put_args.parse_args()
		game = GameModel(
            name=args['name'],
            tags=args['tags'],
            created_by=args['created_by'],
            cards=args['cards'],
            views=args['views'],
            likes=args['likes'])
		db.session.add(game)
		db.session.commit()
		return game, 201

	@marshal_with(game_fields)
	def patch(self, game_id):
		args = game_update_args.parse_args()
		result = GameModel.query.filter_by(id=game_id).first()
		if not result:
			abort(404, message="Game doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['tags']:
			result.tags = args['tags']
		if args['created_by']:
			result.created_by = args['created_by']
		if args['cards']:
			result.cards = args['cards']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']
		db.session.commit()

		return result

api.add_resource(Game, "/game/<int:game_id>")

class UserModel(db.Model):
	name = db.Column(db.String(100), primary_key=True, nullable=False)

	def __repr__(self):
		return f"User(name = {self.name})"

user_fields = {
	'name': fields.String,
}

class User(Resource):
	@marshal_with(user_fields)
	def get(self, user_name):
		result = UserModel.query.filter_by(name=user_name).first()
		if not result:
			abort(404, message="Could not find a user with that name")
		return result

	@marshal_with(user_fields)
	def put(self, user_name):
		result = UserModel.query.filter_by(name=user_name).first()
		if result:
			abort(409, message="Name already taken...")

		user = UserModel(
            name=user_name)
		db.session.add(user)
		db.session.commit()
		return user, 201

api.add_resource(User, "/user/<string:user_name>")



search_args = reqparse.RequestParser()
search_args.add_argument("name", type=str)
search_args.add_argument("tags", type=str)
search_args.add_argument("created_by", type=str)
search_args.add_argument("page", type=int)

class SearchGame(Resource):
	def get(self):
		args = search_args.parse_args()
		name = (args["name"].lower() if args["name"] else None)
		tags = (args["tags"].lower().split(",") if args["tags"] else None)
		created_by = args["created_by"]
		page = args["page"]
		results = []
		queries = sorted(GameModel.query.all(), key=lambda x: -x.views)
		for result in queries:
			if name is None or any (word in name for word in result.name.lower().split(" ")) or any (word in result.name for word in name.split(" ")):
				game_tags = result.tags.split(",")
				if tags is None or all (tag in game_tags for tag in tags):
					if created_by is None or result.created_by == created_by:
						results.append(result.jsonify())
		return results

api.add_resource(SearchGame, "/search")


if __name__ == "__main__":
	app.run(debug=True)