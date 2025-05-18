from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.homeowner.searchShortlistController import SearchShortlistController
from csit314.controller.homeowner.searchListingController   import SearchListingController
from csit314.controller.platformmanager.searchServiceCategoryController import SearchServiceCategoryController

searchListingPage = Blueprint('searchListingPage', __name__, template_folder='../templates', static_folder='../static')
searchShortlistController = SearchShortlistController()
searchListingController   = SearchListingController()
searchServiceCategoryController = SearchServiceCategoryController()

# searchListingPage
@searchListingPage.route('/browse_services')
def searchListing():
    if 'user_id' not in session:
        return redirect('/user_login')

    user_id = session['user_id']
    first_name = session['first_name']
    shortlisted_only = request.args.get('shortlisted')

    name = request.args.get('name')
    email = request.args.get('email')
    service_name = request.args.get('service_name')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    type = request.args.get('type')
    category_id = request.args.get('category_id')

    categories = searchServiceCategoryController.searchServiceCategories(None, "active")

    shortlisted_services = searchShortlistController.searchShortlist(user_id)
    shortlisted_ids = [service['id'] for service in shortlisted_services] if shortlisted_services else []

    if shortlisted_only:    
        if not shortlisted_ids:
            services = []
        else:
            all_services = searchListingController.searchListing(name, email, service_name, min_price, max_price, type, category_id)
            services = [s for s in all_services if s['id'] in shortlisted_ids]
    else:
        services = searchListingController.searchListing(name, email, service_name, min_price, max_price, type, category_id)

    return render_template('browse_services.html', services=services, shortlisted_ids=shortlisted_ids, categories=categories, first_name=first_name)
