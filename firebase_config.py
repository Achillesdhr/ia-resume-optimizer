import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração do Firebase
def initialize_firebase():
    """Inicializa o Firebase Admin SDK"""
    try:
        # Verifica se já foi inicializado
        firebase_admin.get_app()
        return True
    except ValueError:
        # Se não foi inicializado, inicializa
        try:
            # Tenta usar arquivo de credenciais
            cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
            if cred_path and os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
            else:
                # Usa credenciais padrão (para desenvolvimento)
                firebase_admin.initialize_app()
            return True
        except Exception as e:
            print(f"Erro ao inicializar Firebase: {e}")
            return False

def verify_firebase_token(id_token):
    """Verifica um token do Firebase e retorna os dados do usuário"""
    try:
        decoded_token = auth.verify_id_token(id_token)
        return {
            'success': True,
            'user_id': decoded_token['uid'],
            'email': decoded_token.get('email'),
            'name': decoded_token.get('name'),
            'picture': decoded_token.get('picture')
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def create_custom_token(uid):
    """Cria um token customizado para um usuário"""
    try:
        custom_token = auth.create_custom_token(uid)
        return {
            'success': True,
            'token': custom_token.decode('utf-8')
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def get_user_by_email(email):
    """Busca usuário por email"""
    try:
        user = auth.get_user_by_email(email)
        return {
            'success': True,
            'user': {
                'uid': user.uid,
                'email': user.email,
                'display_name': user.display_name,
                'photo_url': user.photo_url
            }
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        } 