from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.homeowner.createShortlistController import CreateShortlistController
from csit314.controller.homeowner.deleteShortlistController import DeleteShortlistController
from csit314.controller.homeowner.searchShortlistController import SearchShortlistController

toggleShortlistPage = Blueprint('toggleShortlistPage', __name__, template_folder='../templates', static_folder='../static')
createShortlistController = CreateShortlistController()
deleteShortlistController = DeleteShortlistController()
searchShortlistController = SearchShortlistController()

# toggleShortlistPage
# Save/Undo shortlist button
@toggleShortlistPage.route('/shortlist/<int:listing_id>/<int:fromShortlistPage>', methods=['POST'])
def toggleShortlist(listing_id, fromShortlistPage):
    if 'user_id' not in session:
        return redirect('/user_login')
    
    user_id = session['user_id']

    print(f"Page - Checking shortlist: user_id={user_id}, listing_id={listing_id}")
    if searchShortlistController.isShortlisted(user_id, listing_id):
        deleteShortlistController.deleteShortlist(user_id, listing_id)
        flash("Listing removed from shortlist.", "info")
    else:
        createShortlistController.createShortlist(user_id, listing_id)
        flash("Listing saved to shortlist.", "success")


    # Preserve shortlist filter if set
    if fromShortlistPage:
        return redirect('/my_shortlisted_services')
    elif request.args.get("shortlisted") or (request.referrer and "shortlisted=1" in request.referrer):
        return redirect('/browse_services?shortlisted=1')
    else: 
        return redirect('/browse_services')    
