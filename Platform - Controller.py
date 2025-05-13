from flask import session, redirect, url_for, flash, render_template, request
from csit314.platform_manager.platform_manager_entity import PlatformManagerEntity

class PlatformManagerController:
    def __init__(self):
        self.entity = PlatformManagerEntity()
    
    # Authentication methods
    def login(self, username, password):
        user = self.entity.get_manager(username, password)
        if user:
            session['manager_id'] = user['user_id']
            session['manager_username'] = user['username']
            flash("Logged in as manager!", "success")
            return redirect(url_for('platform_manager.categories'))
        flash("Invalid credentials", "danger")
        return redirect(url_for('platform_manager.login'))
    
    def logout(self):
        session.clear()
        flash("Logged out.", "info")
        return redirect(url_for('platform_manager.login'))
    
    # Category management methods
    def list_categories(self, query=None, status=None):
        return self.entity.get_categories(query, status)
    
    def create_category(self, name, description, min_price, max_price):
        try:
            self.entity.add_category(name, description, min_price, max_price)
            flash("Category added successfully.", "success")
            return True
        except Exception as e:
            flash(f"Error adding category: {str(e)}", "danger")
            return False
    
    def update_category(self, category_id, name, description, min_price, max_price):
        try:
            self.entity.update_category(category_id, name, description, min_price, max_price)
            flash("Category updated successfully.", "success")
            return True
        except Exception as e:
            flash(f"Error updating category: {str(e)}", "danger")
            return False
    
    def delete_category(self, category_id):
        self.entity.delete_category(category_id)
        flash("Category deleted.", "info")
    
    def suspend_category(self, category_id):
        self.entity.suspend_category(category_id)
        flash("Category suspended.", "info")
    
    def activate_category(self, category_id):
        self.entity.activate_category(category_id)
        flash("Category activated.", "success")