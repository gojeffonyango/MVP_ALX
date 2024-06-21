from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from models import mongo, Report
from datetime import datetime

class ReportService:
    @staticmethod
    def generate_report():
        user_id = get_jwt_identity()

        transactions = mongo.db.transactions.find({"user_id": user_id})
        budgets = mongo.db.budgets.find({"user_id": user_id})

        total_income = sum(t['amount'] for t in transactions if t['amount'] > 0)
        total_expenses = sum(t['amount'] for t in transactions if t['amount'] < 0)

        categories = {}
        for t in transactions:
            if t['category'] in categories:
                categories[t['category']] += t['amount']
            else:
                categories[t['category']] = t['amount']

        report_data = {
            "user_id": user_id,
            "generated_at": datetime.utcnow(),
            "total_income": total_income,
            "total_expenses": total_expenses,
            "categories": [{"category": k, "spent": v} for k, v in categories.items()]
        }

        new_report = Report(**report_data)
        mongo.db.reports.insert_one(new_report.__dict__)

        return jsonify(report_data), 200

