from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from models import mongo, Transaction

class TransactionService:
    @staticmethod
    def get_transactions():
        user_id = get_jwt_identity()
        transactions = mongo.db.transactions.find({"user_id": user_id})
        return jsonify([transaction for transaction in transactions]), 200

    @staticmethod
    def add_transaction(data):
        user_id = get_jwt_identity()
        new_transaction = Transaction(
            user_id=user_id,
            amount=data['amount'],
            category=data['category'],
            date=data['date'],
            description=data.get('description', '')
        )
        mongo.db.transactions.insert_one(new_transaction.__dict__)
        return jsonify({"msg": "Transaction added successfully"}), 201

    @staticmethod
    def update_transaction(transaction_id, data):
        user_id = get_jwt_identity()
        update_data = {
            "amount": data['amount'],
            "category": data['category'],
            "date": data['date'],
            "description": data.get('description', '')
        }
        mongo.db.transactions.update_one(
            {"_id": transaction_id, "user_id": user_id},
            {"$set": update_data}
        )
        return jsonify({"msg": "Transaction updated successfully"}), 200

    @staticmethod
    def delete_transaction(transaction_id):
        user_id = get_jwt_identity()
        mongo.db.transactions.delete_one({"_id": transaction_id, "user_id": user_id})
        return jsonify({"msg": "Transaction deleted successfully"}), 200

