from flask import Blueprint, render_template, redirect, session, flash
from csit314.controller.useradmin.userAccountController.viewUserAccountController import ViewUserAccountController

viewUserAccountPage = Blueprint('viewUserAccountPage', __name__, template_folder='../templates', static_folder='../static')
viewUserAccountController = ViewUserAccountController()

@viewUserAccountPage.route('/admin/user/<int:id>')
def viewUserAccount(id):
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    # Get user details
    user = viewUserAccountController.ViewUserAccount(id)
    
    if not user:
        flash("User account not found.", "warning")
        return redirect('/admin/users')
    
    return render_template('admin_view_user.html', user=user, name=session.get('first_name'))


@viewUserAccountPage.route('/admin/users')
def viewAllUserAccounts():
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    # Get all users
    users = viewUserAccountController.getAllUsers()  # You'll need to add this method to the controller
    return render_template('admin_all_users.html', users=users, name=session.get('first_name'))
