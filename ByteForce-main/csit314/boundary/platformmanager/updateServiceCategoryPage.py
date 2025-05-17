from flask import Blueprint, render_template, request, redirect, session, flash
from csit314.controller.platformmanager.updateServiceCategoryController import UpdateServiceCategoryController
from csit314.controller.platformmanager.viewServiceCategoryController import ViewServiceCategoryController

updateServiceCategoryPage = Blueprint('updateServiceCategoryPage', __name__, template_folder='../templates', static_folder='../static')
updateServiceCategoryController = UpdateServiceCategoryController()
viewServiceCategoryController = ViewServiceCategoryController()

@updateServiceCategoryPage.route('/category/edit/<int:id>', methods=['GET', 'POST'])
def updateServiceCategory(id):
    if 'user_id' not in session or session['role'] != 'platformmanager':
        return redirect('/user_login')
    
    category = viewServiceCategoryController.getCategory(id)
    if not category:
        flash("Category not found.", "warning")
        return redirect('/categories')
    
    if request.method == 'POST':
        updateServiceCategoryController.updateServiceCategory(
            id,
            request.form['name'],
            request.form.get('description', ''),
            request.form.get('min_price'),
            request.form.get('max_price')
        )
        flash("Category updated successfully.", "success")
        return redirect('/categories')
    
    return render_template('category_form.html', action='Update', category=category)