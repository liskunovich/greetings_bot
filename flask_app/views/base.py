from flask import request, render_template, Blueprint, redirect, url_for
from ..utils.forms import UserForm

base_page = Blueprint('base_page', __name__)


@base_page.route('/', methods=['GET', 'POST'])
def base_route():
    form = UserForm()
    if form.validate_on_submit():
        from flask_app.utils.db import insert_user_data
        insert_user_data(
            name=form.name.data,
            city=form.city.data,
            tg_username=form.username.data
        )
        return redirect(url_for('base_page.base_route'))
    return render_template('index.html', form=form)
