from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.useradmin.userProfileController.createUserProfileController import CreateUserProfileController 

createUserProfilePage = Blueprint('createUserProfilePage', __name__, template_folder='../templates', static_folder='../static')
createUserProfileController = CreateUserProfileController()  

@createUserProfilePage.route('/admin/add_profile', methods=['GET', 'POST'])
def createUserProfile():
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    # Get all users for the dropdown
    user_controller = ViewUserProfileController()
    users = user_controller.getAllUsers()
    
    if request.method == 'POST':
        # Get form data
        user_id = request.form['user_id']
        role = request.form['role']
        description = request.form['description']
        
        # Create user profile
        result = createUserProfileController.createUserProfile(user_id, role, description)
        
        if result:
            flash("User profile created successfully.", "success")
            return redirect('/admin/profiles')
        else:
            flash("Failed to create user profile.", "danger")
            return render_template('admin_add_profile.html', name=session.get('first_name'), users=users)
    
    # If GET request, show the form
    return render_template('admin_add_profile.html', name=session.get('first_name'), users=users)
