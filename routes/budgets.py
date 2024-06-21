from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from services.budget_service import BudgetService

budgets_bp = Blueprint('budgets', __name__)

@budgets_bp.route('/', methods=['GET'])
@jwt_required()
def get_budgets():
    return BudgetService.get_budgets()

@budgets_bp.route('/', methods=['POST'])
@jwt_required()
def add_budget():
    data = request.get_json()
    return BudgetService.add_budget(data)

@budgets_bp.route('/<budget_id>', methods=['PUT'])
@jwt_required()
def update_budget(budget_id):
    data = request.get_json()
    return BudgetService.update_budget(budget_id, data)

@budgets_bp.route('/<budget_id>', methods=['DELETE'])
@jwt_required()
def delete_budget(budget_id):
    return BudgetService.delete_budget(budget_id)

