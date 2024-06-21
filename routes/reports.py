from flask import Blueprint
from flask_jwt_extended import jwt_required
from services.report_service import ReportService

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/', methods=['GET'])
@jwt_required()
def generate_report():
    return ReportService.generate_report()

