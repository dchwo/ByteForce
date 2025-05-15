from flask import Blueprint, render_template, request, redirect, session
from csit314.controller.platformmanager.searchServiceCategoryController import SearchServiceCategoryController

searchServiceCategoryPage = Blueprint('searchServiceCategoryPage', __name__, template_folder='../templates', static_folder='../static')
searchServiceCategoryController = SearchServiceCategoryController()

@searchServiceCategoryPage.route('/search_categories', methods=['GET'])
def searchServiceCategory():
    if 'user_id' not in session or session['role'] != 'platformmanager':
        return redirect('/user_login')
    
    query = request.args.get('query')
    status = request.args.get('status')
    
    if not query and not status:
        return render_template('search_categories.html', categories=None)
    
    categories = searchServiceCategoryController.searchServiceCategories(query, status)
    
    return render_template('search_categories.html', 
                          categories=categories,
                          filters={
                              'query': query,
                              'status': status
                          })