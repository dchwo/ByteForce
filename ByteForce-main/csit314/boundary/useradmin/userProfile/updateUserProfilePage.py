from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.useradmin.userProfileController.updateUserProfileController import UpdateUserProfileController
from csit314.controller.useradmin.userProfileController.viewUserProfileController import ViewUserProfileController

updateUserProfilePage = Blueprint('updateUserProfilePage', __name__, template_folder='../templates', static_folder='../static')
updateUserProfileController = UpdateUserProfileController()
viewUserProfileController = ViewUserProfileController()

@updateUserProfilePage.route('/admin/profile/edit/<int:id>', methods=['GET', 'POST'])
def updateUserProfile(id):
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    if request.method == 'POST':
        # Get form data
        bio = request.form.get('bio')
        avatar = request.form.get('avatar')
        preferences = request.form.get('preferences')
        
        # Update profile
        result = updateUserProfileController.UpdateUserProfile(id, bio, avatar, preferences)
        
        if result:
            flash("User profile updated successfully.", "success")
            return redirect('/admin/profiles')
        else:
            flash("Failed to update user profile.", "danger")
            # Get profile for the form
            profile = viewUserProfileController.ViewUserProfile(id)
            return render_template('admin_edit_profile.html', profile=profile, name=session.get('first_name'))
    
    # If GET request, show the form with profile data
    profile = viewUserProfileController.ViewUserProfile(id)
    
    if not profile:
        flash("User profile not found.", "warning")
        return redirect('/admin/profiles')
    
    return render_template('admin_edit_profile.html', profile=profile, name=session.get('first_name'))