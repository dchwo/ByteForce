from flask import Blueprint, redirect, session, flash, request
from csit314.controller.useradmin.suspendUserProfileController import SuspendUserProfileController

suspendUserProfilePage = Blueprint('suspendUserProfilePage', __name__, template_folder='../templates', static_folder='../static')
suspendUserProfileController = SuspendUserProfileController()

@suspendUserProfilePage.route('/admin/profile/toggle_status/<int:id>', methods=['POST'])
def toggleUserProfileStatus(id):
    # Check if user is logged in and is an admin
    if 'user_id' not in session or session['role'] != 'admin':
        flash("Please login as admin to access this page.", "danger")
        return redirect('/user_login')
    
    # Toggle profile status (returns True if suspended, False if activated)
    was_suspended = suspendUserProfileController.SuspendUserProfile(id)
    
    if was_suspended:
        # True means it was active and now suspended
        flash("User profile has been suspended.", "info")
    else:
        # False means it was suspended and now active
        flash("User profile has been activated.", "success")
    
    # Redirect back to the previous page
    return redirect(request.referrer or '/admin/profiles')