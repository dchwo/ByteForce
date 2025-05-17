from flask import Blueprint, render_template, redirect, session, flash
from csit314.controller.cleaner.deleteCleanerListingController import DeleteCleanerListingController

deleteCleanerListingPage = Blueprint('deleteCleanerListingPage', __name__, template_folder='../templates', static_folder='../static')
deleteCleanerListingController = DeleteCleanerListingController()

# deleteCleanerListingPage
@deleteCleanerListingPage.route('/service/delete/<int:id>')
def deleteCleanerListing(id):
    if 'user_id' not in session:
        return redirect('/user_login')
    
    deleteCleanerListingController.deleteCleanerListing(id, session['user_id'])
    flash("Service deleted.", "info")

    return redirect('/services')

