#!/usr/bin/env python3

from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

security = Blueprint('security', __name__)

# ------------------ Authentication Page Rendering ------------------ #

@security.route('/login')
def login():
	return render_template('login.html');

@security.route('/signup')
def signup():
	return render_template('signup.html');

@security.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('content.index')) # "content" is a blueprint with index as a route-wrapped function

# ------------------- API For Authorization (POST) ------------------ #

@security.route('/signup', methods=["POST"])
def signup_post():
	# Here fields should match the database i.e. models.User
	username = request.form.get('username') # Here the string is the name attribute of the desired field in the form
	email = request.form.get('email')
	password = request.form.get('password')
	
	# Security checks for uniqueness
	existing_user = User.query.filter_by(email=email).first()
	if existing_user:
		flash("email or username already exists") # This message is contained in th get_flashed_messages() function with can be called in the jinja format
		return redirect(url_for("security.login"))
	
	## ADD: Here there could be other security measure as email validation of user validation
	
	new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'));
	db.session.add(new_user)
	db.session.commit();
	
	# ADD: Flash a message to be displayed on the login page once the signup is done
	return redirect(url_for("security.login"))

@security.route('/login', methods=["POST"])
def login_post():
	email = request.form.get("email")
	password = request.form.get("password")
	remember = True if request.form.get("remember") else False

	user = User.query.filter_by(email=email).first()

	if not user or not check_password_hash(user.password, password):
		flash("Please Check the your login details and try again.. ")
		return redirect(url_for('security.login'))
	
	# Some other constraints from the database to filter login

	login_user(user, remember=remember)

	return redirect(url_for('content.profile')) # Here this redirect is privilages to a logined user only

