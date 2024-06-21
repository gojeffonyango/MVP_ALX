from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from models import mongo, Budget

class BudgetService:
    @staticmethod
    def get_budgets():
        user_id = get_jwt_identity()
        budgets = mongo.db.budgets.find({"user_id": user_id})
        return jsonify([budget for budget in budgets]), 200

    @staticmethod
    def add_budget(data):
        user_id = get_jwt_identity()
        new_budget = Budget(
            user_id=user_id,
            category=data['category'],
            limit=data['limit'],
            spent=data.get('spent', 0)
        )
        mongo.db.budgets.insert_one(new_budget.__dict__)
        return jsonify({"msg": "Budget added successfully"}), 201

    @staticmethod
    def update_budget(budget_id, data):
        user_id = get_jwt_identity()
        update_data = {
            "category": data['category'],
            "limit": data['limit'],
            "spent": data.get('spent', 0)
        }
        mongo.db.budgets.update_one(
            {"_id": budget_id, "user_id": user_id},
            {"$set": update_data}
        )
        return jsonify({"msg": "Budget updated successfully"}), 200

    @staticmethod
    def delete_budget(budget_id):
        user_id = get_jwt_identity()
        mongo.db.budgets.delete_one({"_id": budget_id, "user_id": user_id})
        return jsonify({"msg": "Budget deleted successfully"}), 200

