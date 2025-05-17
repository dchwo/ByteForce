from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.cleaner.viewCleanerListingController import ViewCleanerListingController

viewCleanerListingPage = Blueprint('viewCleanerListingPage', __name__, template_folder='../templates', static_folder='../static')
viewCleanerListingController = ViewCleanerListingController()

@viewCleanerListingPage.route('/services/<int:service_id>')
def viewCleanerListing(service_id):
    """View a specific service offered by the logged-in cleaner"""
    if 'user_id' not in session or session['role'] != 'cleaner':
        flash("Please login as a cleaner to access this page.", "danger")
        return redirect('/user_login')
    
    service = viewCleanerListingController.getCleanerListing(service_id, session['user_id'])
    
    if not service:
        flash("Service not found or you don't have permission to view it.", "warning")
        return redirect('/my_services')
    
    return render_template('cleaner_service_detail.html', 
                          service=service, 
                          name=session.get('first_name'))
