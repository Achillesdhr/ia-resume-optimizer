import requests
from config import Config

def search_jobs_by_keywords(keywords, num_pages=1, employment_type=None, workplace_type=None):
    """Busca vagas usando as palavras-chave extraídas com JSearch API"""
    if not keywords:
        return []
    
    # Combina as palavras-chave em uma query de busca seguindo o padrão JSearch
    query = '+'.join(keywords[:2]).replace(' ', '+')   # Limita a 3 palavras-chave e usa + como separador
    
    headers = {
        'X-RapidAPI-Key': Config.RAPIDAPI_KEY,
        'X-RapidAPI-Host': Config.RAPIDAPI_HOST
    }
    
    # Parâmetros para JSearch API
    params = {
        'query': query,
        'num_pages': num_pages,
        'country': 'BR'  # Brasil
    }
    
    # Adiciona parâmetros opcionais se fornecidos
    if employment_type:
        # Se não for vazio, usa o valor selecionado, senão usa todos os tipos
        if employment_type:
            params['employment_types'] = employment_type
        else:
            params['employment_types'] = 'FULLTIME,CONTRACTOR,PARTTIME,INTERN'
    if workplace_type:
        params['work_from_home'] = 'true' if workplace_type == 'REMOTE' else 'false'
    
    try:
        print(f"Buscando vagas com query: {query}")
        print(f"Parâmetros: {params}")
        
        response = requests.get(Config.JSEARCH_URL, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {'erro': f'Erro na API: {response.status_code}', 'detalhes': response.text}
    except Exception as e:
        return {'erro': f'Erro na requisição: {str(e)}'}

def search_jobs_direct(query):
    """Busca vagas diretamente por query"""
    headers = {
        'X-RapidAPI-Key': Config.RAPIDAPI_KEY,
        'X-RapidAPI-Host': Config.RAPIDAPI_HOST
    }
    params = {
        'query': query,
        'num_pages': 1,
        'country': 'BR'
    }
    
    try:
        response = requests.get(Config.JSEARCH_URL, headers=headers, params=params)
        return response.json(), response.status_code
    except Exception as e:
        return {'erro': f'Erro na requisição: {str(e)}'}, 500 