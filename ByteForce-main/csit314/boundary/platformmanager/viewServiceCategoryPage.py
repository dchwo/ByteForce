from flask import Blueprint, render_template, redirect, session, flash
from csit314.controller.platformmanager.viewServiceCategoryController import ViewServiceCategoryController

viewServiceCategoryPage = Blueprint('viewServiceCategoryPage', __name__, template_folder='../templates', static_folder='../static')
viewServiceCategoryController = ViewServiceCategoryController()

@viewServiceCategoryPage.route('/categories')
def viewAllCategories():
    if 'user_id' not in session or session['role'] != 'platformmanager':
        return redirect('/user_login')
    
    categories = viewServiceCategoryController.getAllCategories()
    return render_template('categories.html', categories=categories, name=session.get('first_name'))

@viewServiceCategoryPage.route('/category/<int:id>')
def viewCategory(id):
    if 'user_id' not in session or session['role'] != 'platformmanager':
        return redirect('/user_login')
    
    category = viewServiceCategoryController.getCategory(id)
    if not category:
        flash("Category not found.", "warning")
        return redirect('/categories')
    
    return render_template('category_detail.html', category=category)