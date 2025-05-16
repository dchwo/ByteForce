from flask import Blueprint, render_template, redirect, session, flash
from csit314.controller.cleaner.viewListingViewsController import ViewListingViewsController

viewListingViewsPage = Blueprint('viewListingViewsPage', __name__, template_folder='../templates', static_folder='../static')
viewListingViewsController = ViewListingViewsController()

@viewListingViewsPage.route('/my_service/<int:listing_id>/views')
def viewListingViews(listing_id):
    """View detailed view stats for a specific service"""
    if 'user_id' not in session or session['role'] != 'cleaner':
        flash("Please login as a cleaner to access this page.", "danger")
        return redirect('/user_login')
    
    # Get view stats for the specific listing
    listing_views = viewListingViewsController.getListingViewsById(listing_id, session['user_id'])
    
    if not listing_views:
        flash("Service not found or you don't have permission to view it.", "warning")
        return redirect('/my_services/views')
    
    return render_template('cleaner_service_views_detail.html', 
                          listing_views=listing_views,
                          name=session.get('first_name'))
