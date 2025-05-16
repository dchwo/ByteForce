from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.cleaner.searchServiceHistoryController import SearchServiceHistoryController

searchServiceHistoryPage = Blueprint('searchServiceHistoryPage', __name__, template_folder='../templates', static_folder='../static')
searchServiceHistoryController = SearchServiceHistoryController()

@searchServiceHistoryPage.route('/search_service_history', methods=['GET'])
def searchServiceHistory():
    if 'user_id' not in session or session['role'] != 'cleaner':
        return redirect('/user_login')
    
    service_type = request.args.get('service_type')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if not any([service_type, start_date, end_date]):
        return render_template('search_service_history.html', history=None)
    
    history = searchServiceHistoryController.searchCleanerServiceHistory(
        session['user_id'], 
        service_type,
        start_date,
        end_date
    )
    
    return render_template('search_service_history.html', 
                          history=history, 
                          name=session.get('first_name'),
                          filters={
                              'service_type': service_type,
                              'start_date': start_date,
                              'end_date': end_date
                          })