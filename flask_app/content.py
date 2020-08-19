#!/usr/bin/env python3

from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from .models import User
from . import db

content = Blueprint('content', __name__)

# ------------------ Some Pages ----------------------- #

@content.route("/")
def index():
	return render_template("index.html")

@content.route("/profile")
@login_required
def profile():
	return render_template("profile.html", user = current_user)