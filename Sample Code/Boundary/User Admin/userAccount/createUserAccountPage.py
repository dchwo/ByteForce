from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.useradmin.createUserAccountController import CreateUserAccountController

createUserAccountPage = Blueprint('createUserAccountPage', __name__, template_folder='../templates', static_folder='../static')
createUserAccountController = CreateUserAccountController()

@createUserAccountPage.route('/admin/add_user', methods=['GET', 'POST'])
def createUserAccount():
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        role = request.form['role']
        password = request.form['password']
        sex = request.form.get('sex', 'other')
        birth_date = request.form.get('birth_date')
        
        # Create user account
        result = createUserAccountController.createUserProfile(role, first_name, last_name, email, password, sex, birth_date)
        
        if result:
            flash("User account created successfully.", "success")
            return redirect('/admin/users')
        else:
            flash("Failed to create user account. Email may already exist.", "error")
            return render_template('admin_add_user.html', name=session.get('first_name'))
    
    # If GET request, show the form
    return render_template('admin_add_user.html', name=session.get('first_name'))