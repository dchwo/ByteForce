from flask import Blueprint, render_template, redirect, session, flash
from csit314.controller.useradmin.userProfileController.viewUserProfileController import ViewUserProfileController

viewUserProfilePage = Blueprint('viewUserProfilePage', __name__, template_folder='../templates', static_folder='../static')
viewUserProfileController = ViewUserProfileController()

@viewUserProfilePage.route('/admin/profile/<int:id>')
def viewUserProfile(id):
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    # Get profile details
    profile = viewUserProfileController.ViewUserProfile(id)
    
    if not profile:
        flash("User profile not found.", "warning")
        return redirect('/admin/profiles')
    
    return render_template('admin_view_profile.html', profile=profile, name=session.get('first_name'))

@viewUserProfilePage.route('/admin/profiles')
def viewAllUserProfiles():
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    # Implement the method to get all profiles
    # You'll need to add a method to the controller to get all profiles
    profiles = viewUserProfileController.ViewAllProfiles()
    
    return render_template('admin_all_profiles.html', profiles=profiles, name=session.get('first_name'))
