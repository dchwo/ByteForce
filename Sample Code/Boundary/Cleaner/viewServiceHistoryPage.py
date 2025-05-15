from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.cleaner.viewServiceHistoryController import ViewServiceHistoryController

viewServiceHistoryPage = Blueprint('viewServiceHistoryPage', __name__, template_folder='../templates', static_folder='../static')
viewServiceHistoryController = ViewServiceHistoryController()

@viewServiceHistoryPage.route('/service_history')
def viewServiceHistory():
    if 'user_id' not in session or session['role'] != 'cleaner':
        return redirect('/user_login')
    
    service_type = request.args.get('service_type')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    history = viewServiceHistoryController.getCleanerServiceHistory(
        session['user_id'], 
        service_type,
        start_date,
        end_date
    )
    
    return render_template('cleaner_service_history.html', 
                          history=history, 
                          name=session.get('first_name'),
                          filters={
                              'service_type': service_type,
                              'start_date': start_date,
                              'end_date': end_date
                          })

@viewServiceHistoryPage.route('/service_history/<int:id>')
def viewServiceHistoryDetail(id):
    if 'user_id' not in session or session['role'] != 'cleaner':
        return redirect('/user_login')
    
    detail = viewServiceHistoryController.getServiceHistoryDetail(id)
    
    if not detail or detail['cleaner_id'] != session['user_id']:
        flash('Service history record not found.', 'warning')
        return redirect('/service_history')
    
    return render_template('service_history_detail.html', history=detail)