from google import genai
import json
import re
from config import Config

# Inicializa o cliente Gemini
if Config.GOOGLE_API_KEY:
    client = genai.Client()
else:
    client = None

def extract_with_gemini(text):
    """Extrai informações do currículo usando IA Gemini"""
    if not client:
        return {'erro': 'Cliente Gemini não inicializado'}
    
    prompt = (
        "Extraia do texto abaixo as experiências profissionais, habilidades e palavras-chave mais relevantes para o mercado de trabalho de tecnologia. Se limite a apenas 3 palavras-chave"
        "Responda em JSON com os campos: experiencias, habilidades, palavras_chave.\n\nTexto:\n" + text
    )
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        # Tenta extrair JSON da resposta
        match = re.search(r'\{.*\}', response.text or '', re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except Exception:
                return {'erro': 'Falha ao decodificar JSON da resposta da IA', 'resposta': response.text}
        return {'erro': 'Resposta inesperada da IA', 'resposta': response.text}
    except Exception as e:
        return {'erro': f'Erro na chamada da IA: {str(e)}'}

def generate_personalized_resume(curriculo_original, titulo_vaga, empresa, descricao_vaga):
    """Gera currículo personalizado usando IA"""
    if not client:
        return None
    
    prompt = f"""
    Com base no currículo original abaixo e na descrição da vaga, crie uma versão personalizada do currículo que destaque as experiências e habilidades mais relevantes para esta posição específica.

    TÍTULO DA VAGA: {titulo_vaga}
    EMPRESA: {empresa}
    DESCRIÇÃO DA VAGA: {descricao_vaga}

    CURRÍCULO ORIGINAL:
    {curriculo_original}

    Responda em JSON com os campos:
    {{
        "nome": "Nome completo",
        "email": "Email",
        "telefone": "Telefone",
        "resumo": "Resumo profissional personalizado para a vaga",
        "experiencias": [
            {{
                "cargo": "Cargo",
                "empresa": "Empresa",
                "periodo": "Período",
                "descricao": "Descrição das responsabilidades e conquistas"
            }}
        ],
        "educacao": [
            {{
                "curso": "Curso",
                "instituicao": "Instituição",
                "periodo": "Período"
            }}
        ],
        "habilidades": ["Lista de habilidades relevantes para a vaga"]
    }}
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        # Extrai o JSON da resposta
        match = re.search(r'\{.*\}', response.text or '', re.DOTALL)
        if not match:
            return None
        
        return json.loads(match.group(0))
    except Exception as e:
        print(f"Erro ao gerar currículo personalizado: {e}")
        return None 