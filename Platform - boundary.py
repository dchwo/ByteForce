from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from csit314.platform_manager.platform_manager_controller import PlatformManagerController

platform_manager_bp = Blueprint('platform_manager', __name__, template_folder='../templates', static_folder='../static')
controller = PlatformManagerController()

# Manager authentication
@platform_manager_bp.route('/manager_login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return controller.login(request.form['username'], request.form['password'])
    return render_template('manager_login.html')

@platform_manager_bp.route('/manager_logout')
def logout():
    return controller.logout()

# Check if manager is logged in
def manager_required(func):
    def wrapper(*args, **kwargs):
        if 'manager_id' not in session:
            flash("Manager login required.", "warning")
            return redirect(url_for('platform_manager.login'))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

# Category management
@platform_manager_bp.route('/categories', methods=['GET'])
@manager_required
def categories():
    query = request.args.get('query')
    status = request.args.get('status')
    categories = controller.list_categories(query, status)
    return render_template('categories.html', 
                           categories=categories, 
                           username=session.get('manager_username'),
                           selected_status=status)

@platform_manager_bp.route('/category/add', methods=['GET', 'POST'])
@manager_required
def add_category():
    if request.method == 'POST':
        if controller.create_category(
            request.form['name'],
            request.form['description'],
            request.form['min_price'],
            request.form['max_price']
        ):
            return redirect(url_for('platform_manager.categories'))
        return render_template('category_form.html', action='Add', category={})
    return render_template('category_form.html', action='Add', category={})

@platform_manager_bp.route('/category/edit/<int:id>', methods=['GET', 'POST'])
@manager_required
def edit_category(id):
    category = controller.entity.get_category(id)
    if not category:
        flash("Category not found.", "warning")
        return redirect(url_for('platform_manager.categories'))
    
    if request.method == 'POST':
        if controller.update_category(
            id,
            request.form['name'],
            request.form['description'],
            request.form['min_price'],
            request.form['max_price']
        ):
            return redirect(url_for('platform_manager.categories'))
        return render_template('category_form.html', action='Update', category=category)
    
    return render_template('category_form.html', action='Update', category=category)

@platform_manager_bp.route('/category/delete/<int:id>')
@manager_required
def delete_category(id):
    controller.delete_category(id)
    return redirect(url_for('platform_manager.categories'))

@platform_manager_bp.route('/category/suspend/<int:id>')
@manager_required
def suspend_category(id):
    controller.suspend_category(id)
    return redirect(url_for('platform_manager.categories'))

@platform_manager_bp.route('/category/activate/<int:id>')
@manager_required
def activate_category(id):
    controller.activate_category(id)
    return redirect(url_for('platform_manager.categories'))