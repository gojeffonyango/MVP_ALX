from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from services.transaction_service import TransactionService

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/', methods=['GET'])
@jwt_required()
def get_transactions():
    return TransactionService.get_transactions()

@transactions_bp.route('/', methods=['POST'])
@jwt_required()
def add_transaction():
    data = request.get_json()
    return TransactionService.add_transaction(data)

@transactions_bp.route('/<transaction_id>', methods=['PUT'])
@jwt_required()
def update_transaction(transaction_id):
    data = request.get_json()
    return TransactionService.update_transaction(transaction_id, data)

@transactions_bp.route('/<transaction_id>', methods=['DELETE'])
@jwt_required()
def delete_transaction(transaction_id):
    return TransactionService.delete_transaction(transaction_id)

