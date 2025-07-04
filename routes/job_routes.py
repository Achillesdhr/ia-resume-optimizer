from flask import Blueprint, request, jsonify
from services.job_service import search_jobs_direct

# Blueprint para rotas de vagas
job_bp = Blueprint('job', __name__)

@job_bp.route('/search_jobs', methods=['POST'])
def search_jobs():
    """Rota para busca direta de vagas"""
    data = request.get_json()
    query = data.get('q', '')
    
    if not query:
        return jsonify({'error': 'Query não fornecida'}), 400
    
    result, status_code = search_jobs_direct(query)
    return jsonify(result), status_code 