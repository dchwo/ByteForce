from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from csit314.controller.user.userLoginController import UserLoginController

userLoginPage = Blueprint('userLoginPage', __name__, template_folder='../templates', static_folder='../static')
controller = UserLoginController()

@userLoginPage.route('/user_login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        user = controller.verifyAccount(email, password, role)
        if user:
            session['user_id'] = user['user_id']
            session['first_name'] = user['first_name']
            session['role'] = user['role']

            flash("Logged in!", "success")

            if role == "cleaner":
                return redirect(url_for('searchCleanerListingPage.searchCleanerListing'))
            elif role == "homeowner":
                return redirect(url_for('searchListingPage.searchListing'))
            if role == "admin":
                return redirect(url_for('adminDashboardPage.viewDashboard'))
            elif role == "platformmanager":
                return redirect(url_for('platformManagerDashboardPage.viewDashboard'))
            else:
                flash("Invalid role specified", "danger")
                return redirect(url_for('userLoginPage.login'))
                    
        flash("Invalid credentials", "danger")
        return render_template('user_login.html')
            
    return render_template('user_login.html')


