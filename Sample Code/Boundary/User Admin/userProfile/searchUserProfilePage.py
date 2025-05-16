from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.useradmin.searchUserProfileController import SearchUserProfileController

searchUserProfilePage = Blueprint('searchUserProfilePage', __name__, template_folder='../templates', static_folder='../static')
searchUserProfileController = SearchUserProfileController()

@searchUserProfilePage.route('/admin/search_profiles', methods=['GET'])
def searchUserProfiles():
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    # Get search parameters
    id = request.args.get('id')
    role = request.args.get('role')
    
    # If any search parameter provided, perform search
    if any([id, role]):
        profiles = searchUserProfileController.SearchUserProfile(id, role)
    else:
        profiles = None
    
    return render_template('admin_search_profiles.html', 
                          profiles=profiles, 
                          search_criteria={
                              'id': id,
                              'role': role
                          },
                          name=session.get('first_name'))