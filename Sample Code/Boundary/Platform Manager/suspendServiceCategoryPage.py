from flask import Blueprint, redirect, session, flash, request
from csit314.controller.platformmanager.suspendServiceCategoryController import SuspendServiceCategoryController

suspendServiceCategoryPage = Blueprint('suspendServiceCategoryPage', __name__, template_folder='../templates', static_folder='../static')
suspendServiceCategoryController = SuspendServiceCategoryController()

@suspendServiceCategoryPage.route('/category/toggle_status/<int:id>')
def suspendCategoryStatus(id):
    if 'user_id' not in session or session['role'] != 'platformmanager':
        return redirect('/user_login')
    
    was_suspended = suspendServiceCategoryController.toggleCategoryStatus(id)
    
    if was_suspended:
        flash("Category suspended successfully.", "info")
    else:
        flash("Category activated successfully.", "success")
    
    return redirect('/categories')