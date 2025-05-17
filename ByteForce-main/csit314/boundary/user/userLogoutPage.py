from flask import Blueprint, render_template, request, redirect, session, flash, url_for

userLogoutPage = Blueprint('userLogoutPage', __name__, template_folder='../templates', static_folder='../static')

@userLogoutPage.route('/user_logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    flash("Logged out.", "info")

    #return render_template('user_login.html')
    return redirect(url_for('userLoginPage.login'))
