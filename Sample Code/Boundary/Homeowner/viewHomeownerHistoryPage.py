from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.homeowner.viewHomeownerHistoryController import ViewHomeownerHistoryController

viewHomeownerHistoryPage = Blueprint('viewHomeownerHistoryPage', __name__, template_folder='../templates', static_folder='../static')
viewHomeownerHistoryController = ViewHomeownerHistoryController()

@viewHomeownerHistoryPage.route('/my_service_history')
def viewHomeownerHistory():
    if 'user_id' not in session or session['role'] != 'homeowner':
        return redirect('/user_login')
    
    service_type = request.args.get('service_type')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    history = viewHomeownerHistoryController.getHomeownerServiceHistory(
        session['user_id'], 
        service_type,
        start_date,
        end_date
    )
    
    return render_template('homeowner_service_history.html', 
                          history=history, 
                          name=session.get('first_name'),
                          filters={
                              'service_type': service_type,
                              'start_date': start_date,
                              'end_date': end_date
                          })

@viewHomeownerHistoryPage.route('/my_service_history/<int:id>')
def viewHomeownerHistoryDetail(id):
    if 'user_id' not in session or session['role'] != 'homeowner':
        return redirect('/user_login')
    
    detail = viewHomeownerHistoryController.getServiceHistoryDetail(id)
    
    if not detail or detail['homeowner_id'] != session['user_id']:
        flash('Service history record not found.', 'warning')
        return redirect('/my_service_history')
    
    return render_template('homeowner_history_detail.html', history=detail)