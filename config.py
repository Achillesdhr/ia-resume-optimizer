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
    JSEARCH_URL = 
    RAPIDAPI_KEY = 
    RAPIDAPI_HOST = 
    
    # Configurações da API Google Gemini
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    
    # Configurações do Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true' 
