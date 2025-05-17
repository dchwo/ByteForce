from flask import Blueprint, render_template, redirect, session, flash

adminDashboardPage = Blueprint('adminDashboardPage', __name__, template_folder='../templates', static_folder='../static')

@adminDashboardPage.route('/admin/dashboard')
def viewDashboard():
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    return render_template('admin_landing.html', name=session.get('first_name'))
