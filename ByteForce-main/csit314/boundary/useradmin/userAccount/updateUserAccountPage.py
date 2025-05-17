from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.useradmin.userAccountController.updateUserAccountController import UpdateUserAccountController
from csit314.controller.useradmin.userAccountController.viewUserAccountController import ViewUserAccountController

updateUserAccountPage = Blueprint('updateUserAccountPage', __name__, template_folder='../templates', static_folder='../static')
updateUserAccountController = UpdateUserAccountController()
viewUserAccountController = ViewUserAccountController()

@updateUserAccountPage.route('/admin/user/edit/<int:id>', methods=['GET', 'POST'])
def updateUserAccount(id):
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    if request.method == 'POST':
        # Get form data
        role = request.form['role']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        
        # Update user
        result = updateUserAccountController.UpdateUserAccount(id, role, first_name, last_name, email, password)
        
        if result:
            flash("User account updated successfully.", "success")
            return redirect('/admin/users')
        else:
            flash("Failed to update user account.", "danger")
            # Get user for the form
            user = viewUserAccountController.ViewUserAccount(id)
            return render_template('admin_edit_user.html', user=user, name=session.get('first_name'))
    
    # If GET request, show the form with user data
    user = viewUserAccountController.ViewUserAccount(id)
    
    if not user:
        flash("User account not found.", "warning")
        return redirect('/admin/users')
    
    return render_template('admin_edit_user.html', user=user, name=session.get('first_name'))