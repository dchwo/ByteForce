from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.cleaner.createCleanerListingController import CreateCleanerListingController

createCleanerListingPage = Blueprint('createCleanerListingPage', __name__, template_folder='../templates', static_folder='../static')
createCleanerListingController = CreateCleanerListingController()

@createCleanerListingPage.route('/service/add', methods=['GET', 'POST'])
def createCleanerListing():
    if 'user_id' not in session:
        return redirect('/user_login')
    
    if request.method == 'POST':
        createCleanerListingController.createCleanerListing(
            session['user_id'],
            request.form['service_name'],
            request.form['price'],
            request.form.get('type', ''),
            request.form.get('description', ''),
            request.form.get('category_id')
        )
        flash("Service added.", "success")
        return redirect('/services')
    
    # Get all categories for the dropdown
    categories = createCleanerListingController.getAllCategories()
    return render_template('service_form.html', action='Add', service={}, categories=categories)
