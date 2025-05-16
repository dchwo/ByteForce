from flask import Blueprint, render_template, redirect, session, flash
from csit314.controller.homeowner.viewShortlistedListingsController import ViewShortlistedListingsController

viewShortlistedListingsPage = Blueprint('viewShortlistedListingsPage', __name__, template_folder='../templates', static_folder='../static')
viewShortlistedListingsController = ViewShortlistedListingsController()

@viewShortlistedListingsPage.route('/my_shortlisted_services')
def viewShortlistedListings():
    """View all shortlisted services for the logged-in homeowner"""
    if 'user_id' not in session or session['role'] != 'homeowner':
        flash("Please login as a homeowner to access this page.", "danger")
        return redirect('/user_login')
    
    # Get shortlisted listings
    shortlisted_services = viewShortlistedListingsController.getShortlistedListings(session['user_id'])
    
    return render_template('homeowner_shortlisted_services.html', 
                          services=shortlisted_services, 
                          name=session.get('first_name'))
