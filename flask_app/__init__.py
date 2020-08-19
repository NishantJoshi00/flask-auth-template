#!/usr/bin/env python3

from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .generator import keygen
db = SQLAlchemy()


def create_app() -> Flask:
	app = Flask(__name__);
	app.config['SECRET_KEY'] = keygen()
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

	db.init_app(app)

	login_manager = LoginManager()
	login_manager.login_view = 'security.login'
	login_manager.init_app(app)

	from .models import User

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))
	
	from .security import security as sec_blueprint
	app.register_blueprint(sec_blueprint)

	# Insert All the others blueprint here for adding functionality to the website

	return app

