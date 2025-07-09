from flask import Blueprint, request, jsonify, send_file
from services.pdf_service import gerar_curriculo_personalizado_pdf
from routes.upload_routes import get_curriculo_original

# Blueprint para rotas de currículos
resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/gerar_curriculo', methods=['POST'])
def gerar_curriculo():
    """Rota para gerar currículo personalizado em PDF"""
    print("=== ROTA /gerar_curriculo CHAMADA ===")
    
    curriculo_original = get_curriculo_original()
    print(f"Currículo original existe: {curriculo_original is not None}")
    
    if not curriculo_original:
        print("ERRO: Nenhum currículo carregado")
        return jsonify({'erro': 'Nenhum currículo carregado'}), 400
    
    try:
        print("Processando dados da requisição...")
        data = request.get_json()
        print(f"Dados recebidos: {data}")
        
        titulo_vaga = data.get('titulo_vaga', '')
        empresa = data.get('empresa', '')
        descricao_vaga = data.get('descricao_vaga', '')
        
        print(f"Título da vaga: {titulo_vaga}")
        print(f"Empresa: {empresa}")
        print(f"Descrição da vaga: {descricao_vaga[:100]}...")  # Primeiros 100 chars
        
        # Gera o PDF personalizado
        print("Chamando função para gerar PDF...")
        pdf_buffer = gerar_curriculo_personalizado_pdf(
            curriculo_original, 
            titulo_vaga, 
            empresa, 
            descricao_vaga
        )
        
        print(f"PDF buffer recebido: {pdf_buffer is not None}")
        if pdf_buffer:
            print("Retornando PDF para download...")
            return send_file(
                pdf_buffer,
                mimetype='application/pdf',
                as_attachment=True,
                download_name=f'curriculo_{empresa.replace(" ", "_")}.pdf'
            )
        else:
            print("ERRO: PDF buffer é None")
            return jsonify({'erro': 'Erro ao gerar PDF'}), 500
            
    except Exception as e:
        print(f"Erro na rota gerar_curriculo: {e}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500 