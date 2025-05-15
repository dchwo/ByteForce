from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.homeowner.viewListingController     import ViewListingController

viewListingPage = Blueprint('viewListingPage', __name__, template_folder='../templates', static_folder='../static')
viewListingController     = ViewListingController()

# viewListingPage
@viewListingPage.route('/service_detail/<int:id>')
def viewListing(id):
    if 'user_id' not in session:
        return redirect('/user_login')
        
    service = viewListingController.viewListing(id)
    if not service:
        flash("Service not found.", "warning")
        return redirect('/browse_services')
    
    return render_template('service_detail.html', service=service)
