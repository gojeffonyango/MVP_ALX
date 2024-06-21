from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('config.Config')
mongo = PyMongo(app)

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class Transaction:
    def __init__(self, user_id, amount, category, date, description):
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

class Budget:
    def __init__(self, user_id, category, limit, spent):
        self.user_id = user_id
        self.category = category
        self.limit = limit
        self.spent = spent

class Report:
    def __init__(self, user_id, generated_at, total_income, total_expenses, categories):
        self.user_id = user_id
        self.generated_at = generated_at
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.categories = categories
