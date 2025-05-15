from flask import session, redirect, url_for, flash, render_template, request
from csit314.entity.userAccount import UserAccount

class UserLoginController:
    def __init__(self):
        self.entity = UserAccount()
    
    def verifyAccount(self, email, password, role):
        return self.entity.getUser(email, password, role)
