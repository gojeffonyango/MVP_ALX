from flask import Flask
from config import Config
from models import mongo
from routes.auth import auth_bp
from routes.transactions import transactions_bp
from routes.budgets import budgets_bp
from routes.reports import reports_bp
from utils.jwt import init_jwt

app = Flask(__name__)
app.config.from_object(Config)

mongo.init_app(app)
jwt = init_jwt(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(transactions_bp, url_prefix='/api/transactions')
app.register_blueprint(budgets_bp, url_prefix='/api/budgets')
app.register_blueprint(reports_bp, url_prefix='/api/reports')

if __name__ == '__main__':
    app.run(debug=True)
