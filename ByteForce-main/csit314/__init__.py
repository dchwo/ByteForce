from flask import Flask

# Cleaner
from csit314.boundary.cleaner.searchCleanerListingPage import searchCleanerListingPage
from csit314.boundary.cleaner.updateCleanerListingPage import updateCleanerListingPage
from csit314.boundary.cleaner.createCleanerListingPage import createCleanerListingPage
from csit314.boundary.cleaner.viewCleanerListingPage import viewCleanerListingPage
from csit314.boundary.cleaner.deleteCleanerListingPage import deleteCleanerListingPage
from csit314.boundary.cleaner.viewServiceHistoryPage import viewServiceHistoryPage
from csit314.boundary.cleaner.searchServiceHistoryPage import searchServiceHistoryPage
from csit314.boundary.cleaner.viewListingViewsPage import viewListingViewsPage
from csit314.boundary.cleaner.viewListingShortlistsPage import viewListingShortlistsPage

# Home Owner
from csit314.boundary.homeowner.viewListingPage     import viewListingPage
from csit314.boundary.homeowner.searchListingPage   import searchListingPage
from csit314.boundary.homeowner.toggleShortlistPage import toggleShortlistPage
from csit314.boundary.homeowner.viewHomeownerHistoryPage import viewHomeownerHistoryPage
from csit314.boundary.homeowner.searchHomeownerHistoryPage import searchHomeownerHistoryPage
from csit314.boundary.homeowner.viewShortlistedListingsPage import viewShortlistedListingsPage

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

# User Admin - User Accounts
from csit314.boundary.useradmin.userAccount.createUserAccountPage import createUserAccountPage
from csit314.boundary.useradmin.userAccount.viewUserAccountPage import viewUserAccountPage
from csit314.boundary.useradmin.userAccount.updateUserAccountPage import updateUserAccountPage
from csit314.boundary.useradmin.userAccount.suspendUserAccountPage import suspendUserAccountPage
from csit314.boundary.useradmin.userAccount.searchUserAccountPage import searchUserAccountPage

# User Admin - User Profile
from csit314.boundary.useradmin.userProfile.createUserProfilePage import createUserProfilePage
from csit314.boundary.useradmin.userProfile.viewUserProfilePage import viewUserProfilePage
from csit314.boundary.useradmin.userProfile.updateUserProfilePage import updateUserProfilePage
from csit314.boundary.useradmin.userProfile.suspendUserProfilePage import suspendUserProfilePage
from csit314.boundary.useradmin.userProfile.searchUserProfilePage import searchUserProfilePage

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecret'  # Replace with a strong secret key

    # Home Owner
    app.register_blueprint(viewListingPage)
    app.register_blueprint(searchListingPage)
    app.register_blueprint(toggleShortlistPage)
    app.register_blueprint(viewHomeownerHistoryPage)
    app.register_blueprint(searchHomeownerHistoryPage)
    app.register_blueprint(viewShortlistedListingsPage)

    # Cleaner
    app.register_blueprint(searchCleanerListingPage)
    app.register_blueprint(updateCleanerListingPage)
    app.register_blueprint(createCleanerListingPage)
    app.register_blueprint(viewCleanerListingPage)
    app.register_blueprint(deleteCleanerListingPage)
    app.register_blueprint(viewServiceHistoryPage)
    app.register_blueprint(searchServiceHistoryPage)
    app.register_blueprint(viewListingViewsPage)
    app.register_blueprint(viewListingShortlistsPage)

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

    #User Admin - User Account
    app.register_blueprint(createUserAccountPage)
    app.register_blueprint(viewUserAccountPage)
    app.register_blueprint(updateUserAccountPage)
    app.register_blueprint(suspendUserAccountPage)
    app.register_blueprint(searchUserAccountPage)

    # User Admin - User Profile
    app.register_blueprint(createUserProfilePage)
    app.register_blueprint(viewUserProfilePage)
    app.register_blueprint(updateUserProfilePage)
    app.register_blueprint(suspendUserProfilePage)
    app.register_blueprint(searchUserProfilePage)
    return app
