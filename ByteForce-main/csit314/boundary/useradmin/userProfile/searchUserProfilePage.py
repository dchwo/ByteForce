from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.useradmin.userProfileController.searchUserProfileController import SearchUserProfileController

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
    status = request.args.get('status')
    uid = request.args.get('uid')
    role = request.args.get('role')
    email = request.args.get('email')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    
    # If any search parameter provided, perform search
    if any([id, status, uid, role, email, first_name, last_name]):
        profiles = searchUserProfileController.SearchUserProfile(id, status, uid, role, email, first_name, last_name)
    else:
        profiles = None
    
    return render_template('admin_search_profiles.html', 
                          profiles=profiles, 
                          search_criteria={
                              'id': id,
                              'status': status,
                              'uid': uid,
                              'role': role,
                              'email': email,
                              'first_name': first_name,
                              'last_name': last_name
                          },
                          name=session.get('first_name'))
