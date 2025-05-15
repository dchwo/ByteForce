from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.cleaner.searchCleanerListingController import SearchCleanerListingController

searchCleanerListingPage = Blueprint('searchCleanerListingPage', __name__, template_folder='../templates', static_folder='../static')
searchCleanerListingController = SearchCleanerListingController()

# searchCleanerListingPage
@searchCleanerListingPage.route('/services', methods=['GET'])
def searchCleanerListing():
    if 'user_id' not in session:
        return redirect('/user_login')
    
    query = request.args.get('search')
    services = searchCleanerListingController.searchCleanerListing(session['user_id'], query)
    
    return render_template('services.html', services=services, name=session.get('first_name'))
