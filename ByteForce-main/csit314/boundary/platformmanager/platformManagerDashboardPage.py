from flask import Blueprint, render_template, redirect, session, flash
from csit314.controller.platformmanager.viewServiceCategoryController import ViewServiceCategoryController

platformManagerDashboardPage = Blueprint('platformManagerDashboardPage', __name__, template_folder='../templates', static_folder='../static')
viewServiceCategoryController = ViewServiceCategoryController()

@platformManagerDashboardPage.route('/platform_manager/dashboard')
def viewDashboard():
    # Check if user is logged in and is a platform manager
    if 'user_id' not in session or session['role'] != 'platformmanager':
        flash("Please login as platform manager to access this page.", "danger")
        return redirect('/user_login')
    
    # Get category statistics
    all_categories = viewServiceCategoryController.getAllCategories()
    active_categories = sum(1 for c in all_categories if c['status'] == 'active')
    suspended_categories = sum(1 for c in all_categories if c['status'] == 'inactive')
    
    return render_template('platform_manager_landing.html', 
                          active_categories=active_categories,
                          suspended_categories=suspended_categories,
                          total_categories=len(all_categories),
                          name=session.get('first_name'))
