from io import BytesIO
from services.ai_service import generate_personalized_resume
from weasyprint import HTML, CSS

# CSS extraído/adaptado do codcurriculo2.html para currículo, sem borda nem sombra
CURRICULO2_CSS = '''
body {
  font-family: 'Segoe UI', sans-serif;
  color: #333;
  margin: 0px;
  line-height: 1.6;
  background-color: #f9f9f9;
}
.container {
  background: white;
  max-width: 900px;
  margin: auto;
  padding: 40px;
  /* border-radius: 12px; */
  /* box-shadow: 0 0 20px rgba(0,0,0,0.05); */
}
.header {
  display: flex;
  align-items: center;
  border-bottom: 2px solid #5B3DE2;
  padding-bottom: 20px;
  margin-bottom: 30px;
}
.header img {
  border-radius: 50%;
  width: 120px;
  height: 120px;
  object-fit: cover;
  margin-right: 30px;
}
h1 {
  margin: 0;
  font-size: 28px;
  color: #5B3DE2;
}
.contact {
  font-size: 14px;
  margin-top: 6px;
}
.section {
  margin-bottom: 30px;
}
.section h2 {
  border-left: 6px solid #30E27A;
  padding-left: 10px;
  font-size: 20px;
  color: #222;
  margin-bottom: 10px;
}
.section p, .section li {
  font-size: 15px;
}
ul {
  padding-left: 20px;
}
.job-title {
  font-weight: bold;
  margin-top: 5px;
}
.company {
  color: #777;
  font-size: 14px;
}
'''

def gerar_curriculo_personalizado_pdf(curriculo_original, titulo_vaga, empresa, descricao_vaga):
    """Gera um PDF personalizado do currículo baseado na vaga, usando HTML+CSS e WeasyPrint (estilo codcurriculo2.html)"""
    print("=== INICIANDO GERAÇÃO DO PDF (WeasyPrint, codcurriculo2) ===")
    try:
        # Gera o currículo personalizado com IA
        print("Chamando IA para personalizar currículo...")
        dados = generate_personalized_resume(
            curriculo_original, 
            titulo_vaga, 
            empresa, 
            descricao_vaga
        )
        if not dados:
            print("ERRO: Dados do currículo estão vazios")
            return None
        print(f"Dados do currículo: {dados}")

        # Monta HTML das experiências
        experiencias_html = ''
        for exp in dados.get('experiencias', []):
            experiencias_html += f'<p class="job-title">{exp.get("cargo", "")}</p>'
            experiencias_html += f'<p class="company">{exp.get("empresa", "")} ({exp.get("periodo", "")})</p>'
            if exp.get('descricao'):
                experiencias_html += '<ul>'
                for linha in exp['descricao'].split('\n'):
                    if linha.strip():
                        experiencias_html += f'<li>{linha.strip()}</li>'
                experiencias_html += '</ul>'

        # Monta HTML da educação
        educacao_html = ''
        for edu in dados.get('educacao', []):
            educacao_html += f'<p><strong>{edu.get("curso", "")}</strong><br/>{edu.get("instituicao", "")} ({edu.get("periodo", "")})</p>'

        # Monta HTML das habilidades
        habilidades_html = ''
        if dados.get('habilidades'):
            habilidades_html = '<ul>'
            for h in dados['habilidades']:
                habilidades_html += f'<li>{h}</li>'
            habilidades_html += '</ul>'

        # Monta o HTML final
        html = f'''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
          <meta charset="UTF-8" />
          <title>Currículo - JobTailor</title>
          <style>{CURRICULO2_CSS}</style>
        </head>
        <body>
          <div class="container">
            <div class="header">
              <img src="https://ui-avatars.com/api/?name={dados.get('nome','')}&background=5B3DE2&color=fff&size=256" alt="Foto de Perfil" />
              <div>
                <h1>{dados.get('nome','')}</h1>
                <div class="contact">
                  <p>Email: {dados.get('email','')}</p>
                  <p>Telefone: {dados.get('telefone','')}</p>
                </div>
              </div>
            </div>

            <div class="section">
              <h2>Resumo Profissional</h2>
              <p>{dados.get('resumo','')}</p>
            </div>

            <div class="section">
              <h2>Experiência Profissional</h2>
              {experiencias_html}
            </div>

            <div class="section">
              <h2>Educação</h2>
              {educacao_html}
            </div>

            <div class="section">
              <h2>Habilidades</h2>
              {habilidades_html}
            </div>
          </div>
        </body>
        </html>
        '''
        # Gera o PDF
        buffer = BytesIO()
        HTML(string=html).write_pdf(buffer)
        buffer.seek(0)
        print("PDF gerado com sucesso!")
        return buffer
    except Exception as e:
        print(f"Erro ao gerar PDF: {e}")
        return None 