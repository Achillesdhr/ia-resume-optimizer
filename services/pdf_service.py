from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from io import BytesIO
from services.ai_service import generate_personalized_resume

def gerar_curriculo_personalizado_pdf(curriculo_original, titulo_vaga, empresa, descricao_vaga):
    """Gera um PDF personalizado do currículo baseado na vaga"""
    print("=== INICIANDO GERAÇÃO DO PDF ===")
    try:
        # Gera o currículo personalizado com IA
        print("Chamando IA para personalizar currículo...")
        dados_curriculo = generate_personalized_resume(
            curriculo_original, 
            titulo_vaga, 
            empresa, 
            descricao_vaga
        )
        
        if not dados_curriculo:
            print("ERRO: Dados do currículo estão vazios")
            return None
        
        print(f"Dados do currículo: {dados_curriculo}")
        
        # Cria o PDF
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        story = []
        
        # Estilos
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=12,
            textColor=colors.darkblue
        )
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=8,
            textColor=colors.darkblue
        )
        
        # Cabeçalho
        story.append(Paragraph(f"<b>{dados_curriculo.get('nome', 'Nome')}</b>", title_style))
        story.append(Paragraph(f"Email: {dados_curriculo.get('email', '')} | Telefone: {dados_curriculo.get('telefone', '')}", styles['Normal']))
        story.append(Spacer(1, 12))
        
        # Resumo
        if dados_curriculo.get('resumo'):
            story.append(Paragraph("<b>RESUMO PROFISSIONAL</b>", heading_style))
            story.append(Paragraph(dados_curriculo['resumo'], styles['Normal']))
            story.append(Spacer(1, 12))
        
        # Experiências
        if dados_curriculo.get('experiencias'):
            story.append(Paragraph("<b>EXPERIÊNCIA PROFISSIONAL</b>", heading_style))
            for exp in dados_curriculo['experiencias']:
                story.append(Paragraph(f"<b>{exp.get('cargo', '')}</b> - {exp.get('empresa', '')} ({exp.get('periodo', '')})", styles['Normal']))
                story.append(Paragraph(exp.get('descricao', ''), styles['Normal']))
                story.append(Spacer(1, 6))
            story.append(Spacer(1, 12))
        
        # Educação
        if dados_curriculo.get('educacao'):
            story.append(Paragraph("<b>EDUCAÇÃO</b>", heading_style))
            for edu in dados_curriculo['educacao']:
                story.append(Paragraph(f"<b>{edu.get('curso', '')}</b> - {edu.get('instituicao', '')} ({edu.get('periodo', '')})", styles['Normal']))
            story.append(Spacer(1, 12))
        
        # Habilidades
        if dados_curriculo.get('habilidades'):
            story.append(Paragraph("<b>HABILIDADES</b>", heading_style))
            habilidades_text = ", ".join(dados_curriculo['habilidades'])
            story.append(Paragraph(habilidades_text, styles['Normal']))
        
        # Gera o PDF
        print("Gerando PDF...")
        doc.build(story)
        buffer.seek(0)
        print("PDF gerado com sucesso!")
        return buffer
        
    except Exception as e:
        print(f"Erro ao gerar PDF: {e}")
        return None 