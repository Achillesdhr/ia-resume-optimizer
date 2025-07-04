import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configurações da aplicação
class Config:
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'docx'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Configurações da API JSearch
    JSEARCH_URL = 'https://jsearch.p.rapidapi.com/search'
    RAPIDAPI_KEY = 'b680b398d6mshc589a9ee9b324fcp175309jsn34141ab70dd5'
    RAPIDAPI_HOST = 'jsearch.p.rapidapi.com'
    
    # Configurações da API Google Gemini
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    
    # Configurações do Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true' 