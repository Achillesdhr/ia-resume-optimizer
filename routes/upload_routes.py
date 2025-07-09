from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from config import Config
from utils.text_extractor import extract_text_from_pdf, extract_text_from_docx
from services.ai_service import extract_with_gemini
from services.job_service import search_jobs_by_keywords

# Blueprint para rotas de upload
upload_bp = Blueprint('upload', __name__)

# Variável global para armazenar o currículo original
curriculo_original = None

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    """Rota para upload e processamento de currículos"""
    global curriculo_original
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and file.filename and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # Extrai texto baseado na extensão
        ext = filename.rsplit('.', 1)[1].lower()
        if ext == 'pdf':
            text = extract_text_from_pdf(filepath)
        elif ext == 'docx':
            text = extract_text_from_docx(filepath)
        else:
            text = ''
        
        # Armazena o currículo original globalmente
        curriculo_original = text[:6000]
        
        # Extração via Gemini
        gemini_result = extract_with_gemini(text[:6000])
        
        # Busca vagas baseada nas palavras-chave extraídas
        vagas_encontradas = []
        if 'palavras_chave' in gemini_result and isinstance(gemini_result['palavras_chave'], list):
            # Pega os parâmetros do frontend
            employment_type = request.form.get('employment_type', '').strip()
            workplace_type = request.form.get('workplace_type', '').strip()
            
            # Converte valores vazios para None
            employment_type = employment_type if employment_type else None
            workplace_type = workplace_type if workplace_type else None
            
            vagas_encontradas = search_jobs_by_keywords(
                gemini_result['palavras_chave'],
                num_pages=3,  # Busca 3 páginas para ter mais vagas
                employment_type=employment_type,
                workplace_type=workplace_type
            )
        
        return jsonify({
            'message': 'Arquivo recebido com sucesso',
            'filename': filename,
            'resultado_gemini': gemini_result,
            'vagas_encontradas': vagas_encontradas,
        }), 200
    else:
        return jsonify({'error': 'Tipo de arquivo não permitido'}), 400

def get_curriculo_original():
    """Retorna o currículo original armazenado"""
    global curriculo_original
    return curriculo_original 