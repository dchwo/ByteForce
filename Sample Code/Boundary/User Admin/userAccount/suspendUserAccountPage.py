from flask import Blueprint, redirect, session, flash, request
from csit314.controller.useradmin.suspendUserAccountController import SuspendUserAccountController

suspendUserAccountPage = Blueprint('suspendUserAccountPage', __name__, template_folder='../templates', static_folder='../static')
suspendUserAccountController = SuspendUserAccountController()

@suspendUserAccountPage.route('/admin/user/toggle_status/<int:id>', methods=['POST'])
def toggleUserAccountStatus(id):
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    # Call controller method which returns:
    # True if user was active and is now suspended
    # False if user was inactive and is now activated
    was_suspended = suspendUserAccountController.SuspendUserAccount(id)
    
    # Based on the return value, show appropriate message
    if was_suspended:
        flash("User account has been suspended.", "info")
    else:
        flash("User account has been activated.", "success")
    
    # Redirect back to the referring page
    return redirect(request.referrer or '/admin/users')