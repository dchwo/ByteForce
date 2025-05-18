from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from datetime import date
from csit314.controller.homeowner.bookServiceController import BookServiceController
from csit314.controller.homeowner.viewListingController import ViewListingController

bookServicePage = Blueprint('bookServicePage', __name__, template_folder='../templates', static_folder='../static')
bookServiceController = BookServiceController()
viewListingController = ViewListingController()

@bookServicePage.route('/book_service/<int:listing_id>', methods=['GET', 'POST'])
def bookService(listing_id):
    if 'user_id' not in session or session['role'] != 'homeowner':
        flash("Please login as a homeowner to book services.", "danger")
        return redirect('/user_login')
    
    service = viewListingController.viewListing(listing_id)
    if not service:
        flash("Service not found.", "warning")
        return redirect('/browse_services')
    
    if request.method == 'POST':
        service_date = request.form['service_date']
        notes = request.form.get('notes', '')
        
        # Get cleaner_id from the service
        cleaner_id = service['user_id']
        
        # Create the booking
        result = bookServiceController.createBooking(
            listing_id=listing_id,
            cleaner_id=cleaner_id,
            homeowner_id=session['user_id'],
            service_date=service_date,
            notes=notes
        )
        
        if result:
            flash("Service booked successfully!", "success")
            return redirect(url_for('viewHomeownerHistoryPage.viewHomeownerHistory'))
        else:
            flash("Failed to book service. Please try again.", "danger")
    
    today = date.today().strftime('%Y-%m-%d')
    return render_template('book_service.html', service=service, today_date=today)
