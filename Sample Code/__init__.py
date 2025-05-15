from flask import Flask

# Cleaner
from csit314.boundary.cleaner.searchCleanerListingPage import searchCleanerListingPage
from csit314.boundary.cleaner.updateCleanerListingPage import updateCleanerListingPage
from csit314.boundary.cleaner.createCleanerListingPage import createCleanerListingPage
from csit314.boundary.cleaner.deleteCleanerListingPage import deleteCleanerListingPage
from csit314.boundary.cleaner.viewServiceHistoryPage import viewServiceHistoryPage
from csit314.boundary.cleaner.searchServiceHistoryPage import searchServiceHistoryPage

# Home Owner
from csit314.boundary.homeowner.viewListingPage     import viewListingPage
from csit314.boundary.homeowner.searchListingPage   import searchListingPage
from csit314.boundary.homeowner.toggleShortlistPage import toggleShortlistPage
from csit314.boundary.homeowner.viewHomeownerHistoryPage import viewHomeownerHistoryPage
from csit314.boundary.homeowner.searchHomeownerHistoryPage import searchHomeownerHistoryPage

# User Account
from csit314.boundary.user.userLoginPage  import userLoginPage
from csit314.boundary.user.userLogoutPage import userLogoutPage

# Platform Manager
from csit314.boundary.platformmanager.createServiceCategoryPage import createServiceCategoryPage
from csit314.boundary.platformmanager.viewServiceCategoryPage import viewServiceCategoryPage
from csit314.boundary.platformmanager.updateServiceCategoryPage import updateServiceCategoryPage
from csit314.boundary.platformmanager.deleteServiceCategoryPage import deleteServiceCategoryPage
from csit314.boundary.platformmanager.suspendServiceCategoryPage import suspendServiceCategoryPage
from csit314.boundary.platformmanager.searchServiceCategoryPage import searchServiceCategoryPage

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecret'  # Replace with a strong secret key

    # Home Owner
    app.register_blueprint(viewListingPage)
    app.register_blueprint(searchListingPage)
    app.register_blueprint(toggleShortlistPage)
    app.register_blueprint(viewHomeownerHistoryPage)
    app.register_blueprint(searchHomeownerHistoryPage)
    
    # Cleaner
    app.register_blueprint(searchCleanerListingPage)
    app.register_blueprint(updateCleanerListingPage)
    app.register_blueprint(createCleanerListingPage)
    app.register_blueprint(deleteCleanerListingPage)
    app.register_blueprint(viewServiceHistoryPage)
    app.register_blueprint(searchServiceHistoryPage)

    # User Account
    app.register_blueprint(userLoginPage)
    app.register_blueprint(userLogoutPage)
    
    # Platform Manager
    app.register_blueprint(createServiceCategoryPage)
    app.register_blueprint(viewServiceCategoryPage)
    app.register_blueprint(updateServiceCategoryPage)
    app.register_blueprint(deleteServiceCategoryPage)
    app.register_blueprint(suspendServiceCategoryPage)
    app.register_blueprint(searchServiceCategoryPage)
    return app
