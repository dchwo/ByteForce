from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from csit314.controller.platformmanager.createServiceCategoryController import CreateServiceCategoryController

createServiceCategoryPage = Blueprint('createServiceCategoryPage', __name__, template_folder='../templates', static_folder='../static')
createServiceCategoryController = CreateServiceCategoryController()

@createServiceCategoryPage.route('/category/add', methods=['GET', 'POST'])
def createServiceCategory():
    if 'user_id' not in session or session['role'] != 'platformmanager':
        return redirect('/user_login')
    
    if request.method == 'POST':
        createServiceCategoryController.createServiceCategory(
            request.form['name'],
            request.form.get('description', ''),
            request.form.get('min_price'),
            request.form.get('max_price')
        )
        flash("Category added successfully.", "success")
        return redirect('/categories')
    
    return render_template('category_form.html', action='Add', category={})