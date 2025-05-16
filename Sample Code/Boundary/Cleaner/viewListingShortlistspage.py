from flask import Blueprint, render_template, redirect, session, flash
from csit314.controller.cleaner.viewListingShortlistsController import ViewListingShortlistsController

viewListingShortlistsPage = Blueprint('viewListingShortlistsPage', __name__, template_folder='../templates', static_folder='../static')
viewListingShortlistsController = ViewListingShortlistsController()

@viewListingShortlistsPage.route('/my_service/<int:listing_id>/shortlists')
def viewListingShortlists(listing_id):
    """View detailed shortlist stats for a specific service"""
    if 'user_id' not in session or session['role'] != 'cleaner':
        flash("Please login as a cleaner to access this page.", "danger")
        return redirect('/user_login')
    
    # Get shortlist stats for the specific listing
    listing_shortlists = viewListingShortlistsController.getListingShortlistsById(listing_id, session['user_id'])
    
    if not listing_shortlists:
        flash("Service not found or you don't have permission to view it.", "warning")
        return redirect('/my_services/shortlists')
    
    return render_template('cleaner_service_shortlists_detail.html', 
                          listing_shortlists=listing_shortlists,
                          name=session.get('first_name'))
