from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.useradmin.userAccountController.searchUserAccountController import SearchUserAccountController

searchUserAccountPage = Blueprint('searchUserAccountPage', __name__, template_folder='../templates', static_folder='../static')
searchUserAccountController = SearchUserAccountController()

@searchUserAccountPage.route('/admin/search_users', methods=['GET'])
def searchUserAccounts():
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    # Get search parameters
    id = request.args.get('id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    email = request.args.get('email')
    role = request.args.get('role')
    
    # If any search parameter provided, perform search
    if any([id, first_name, last_name, email, role]):
        users = searchUserAccountController.SearchUserAccount(id, first_name, last_name, email, role)
    else:
        users = None
    
    return render_template('admin_search_users.html', 
                          users=users, 
                          search_criteria={
                              'id': id,
                              'first_name': first_name,
                              'last_name': last_name,
                              'email': email,
                              'role': role
                          },
                          name=session.get('first_name'))