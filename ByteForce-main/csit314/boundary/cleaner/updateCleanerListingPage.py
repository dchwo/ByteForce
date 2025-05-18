from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.cleaner.updateCleanerListingController import UpdateCleanerListingController
from csit314.controller.cleaner.viewCleanerListingController import ViewCleanerListingController

updateCleanerListingPage = Blueprint('updateCleanerListingPage', __name__, template_folder='../templates', static_folder='../static')
updateCleanerListingController = UpdateCleanerListingController()
viewCleanerListingController = ViewCleanerListingController()

@updateCleanerListingPage.route('/service/edit/<int:id>', methods=['GET', 'POST'])
def updateCleanerListing(id):
    if 'user_id' not in session:
        return redirect('/user_login')
    
    service = viewCleanerListingController.getCleanerListing(id, session['user_id'])
    if not service:
        return redirect('/services')
    
    if request.method == 'POST':
        updateCleanerListingController.updateCleanerListing(
            id,
            session['user_id'],
            request.form['service_name'],
            request.form['price'],
            request.form.get('type', ''),
            request.form.get('description', ''),
            request.form.get('category_id')
        )
        flash("Service updated.", "success") 
        return redirect('/services')
    
    # Get all categories for the dropdown
    categories = updateCleanerListingController.getAllCategories()
    return render_template('service_form.html', action='Update', service=service, categories=categories)
