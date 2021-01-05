from flask import session, redirect, url_for, render_template, request, make_response
from . import main
from .forms import LoginForm
import uuid

@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data