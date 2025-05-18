from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.cleaner.searchCleanerListingController import SearchCleanerListingController
from csit314.controller.platformmanager.searchServiceCategoryController import SearchServiceCategoryController

searchCleanerListingPage = Blueprint('searchCleanerListingPage', __name__, template_folder='../templates', static_folder='../static')
searchCleanerListingController = SearchCleanerListingController()
searchServiceCategoryController = SearchServiceCategoryController()

# searchCleanerListingPage
@searchCleanerListingPage.route('/services', methods=['GET'])
def searchCleanerListing():
    if 'user_id' not in session:
        return redirect('/user_login')
    
    query = request.args.get('search')
    services = searchCleanerListingController.searchCleanerListing(session['user_id'], query)
    
    categories = searchServiceCategoryController.searchServiceCategories(None, "active")
    category_lookup = {c['id']: c['name'] for c in categories}

    for s in services:
        category_id = s.get('category_id')
        s['category_name'] = category_lookup.get(category_id, 'Unknown')
    
    return render_template('services.html', services=services, name=session.get('first_name'))
