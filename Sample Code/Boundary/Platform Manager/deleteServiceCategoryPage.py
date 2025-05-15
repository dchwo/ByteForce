from flask import Blueprint, redirect, session, flash
from csit314.controller.platformmanager.deleteServiceCategoryController import DeleteServiceCategoryController

deleteServiceCategoryPage = Blueprint('deleteServiceCategoryPage', __name__, template_folder='../templates', static_folder='../static')
deleteServiceCategoryController = DeleteServiceCategoryController()

@deleteServiceCategoryPage.route('/category/delete/<int:id>')
def deleteServiceCategory(id):
    if 'user_id' not in session or session['role'] != 'platformmanager':
        return redirect('/user_login')
    
    deleteServiceCategoryController.deleteServiceCategory(id)
    flash("Category deleted successfully.", "info")
    return redirect('/categories')