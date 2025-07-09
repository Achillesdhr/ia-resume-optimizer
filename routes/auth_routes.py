from flask import Blueprint, request, jsonify, session
from firebase_config import initialize_firebase, verify_firebase_token
from firebase_admin import auth as firebase_auth, firestore
from google.cloud.firestore_v1 import SERVER_TIMESTAMP

auth_bp = Blueprint('auth', __name__)

# Inicializa Firebase
initialize_firebase()

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    """Endpoint para login com Firebase"""
    try:
        data = request.get_json()
        
        if not data or 'idToken' not in data:
            return jsonify({
                'success': False,
                'error': 'Token de autenticação não fornecido'
            }), 400
        
        # Verifica o token do Firebase
        result = verify_firebase_token(data['idToken'])
        
        if result['success']:
            uid = result['user_id']
            # Consulta o Firestore para garantir que o usuário existe
            db = firestore.client()
            user_ref = db.collection('users').document(uid)
            user_doc = user_ref.get()
            if not user_doc.exists:
                return jsonify({
                    'success': False,
                    'error': 'Usuário não encontrado no banco de dados'
                }), 404
            user_data = user_doc.to_dict()
            # Armazena dados do usuário na sessão
            session['user_id'] = uid
            session['user_email'] = user_data.get('email')
            session['user_name'] = user_data.get('name')
            return jsonify({
                'success': True,
                'message': 'Login realizado com sucesso',
                'user': {
                    'id': uid,
                    'email': user_data.get('email'),
                    'name': user_data.get('name'),
                    'picture': result['picture']
                }
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Token inválido ou expirado'
            }), 401
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Erro interno do servidor: {str(e)}'
        }), 500

@auth_bp.route('/api/auth/logout', methods=['POST'])
def logout():
    """Endpoint para logout"""
    try:
        # Limpa a sessão
        session.clear()
        
        return jsonify({
            'success': True,
            'message': 'Logout realizado com sucesso'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Erro interno do servidor: {str(e)}'
        }), 500

@auth_bp.route('/api/auth/verify', methods=['GET'])
def verify_session():
    """Verifica se o usuário está logado"""
    try:
        if 'user_id' in session:
            return jsonify({
                'success': True,
                'authenticated': True,
                'user': {
                    'id': session['user_id'],
                    'email': session.get('user_email'),
                    'name': session.get('user_name')
                }
            })
        else:
            return jsonify({
                'success': True,
                'authenticated': False
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Erro interno do servidor: {str(e)}'
        }), 500

@auth_bp.route('/api/auth/user', methods=['GET'])
def get_user_info():
    """Retorna informações do usuário logado"""
    try:
        if 'user_id' not in session:
            return jsonify({
                'success': False,
                'error': 'Usuário não autenticado'
            }), 401
        
        return jsonify({
            'success': True,
            'user': {
                'id': session['user_id'],
                'email': session.get('user_email'),
                'name': session.get('user_name')
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Erro interno do servidor: {str(e)}'
        }), 500 

from flask import Blueprint, request, jsonify, session
from firebase_config import initialize_firebase, verify_firebase_token
from firebase_admin import auth as firebase_auth, firestore
from google.cloud.firestore_v1 import SERVER_TIMESTAMP

auth_bp = Blueprint('auth', __name__)

# ... outras rotas ...

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    try:
        
        data = request.get_json()
        print(data)
        uid = data.get('uid')
        name = data.get('name')
        email = data.get('email')

        if not uid or not name or not email:
            return jsonify({'success': False, 'error': 'Dados incompletos'}), 400

        # Atualiza o nome do usuário no Firebase
        try:
            firebase_auth.update_user(uid, display_name=name)
        except Exception as e:
            print(f'Erro ao atualizar nome do usuário: {e}')

        # Salva no Firestore
        db = firestore.client()
        user_ref = db.collection('users').document(uid)
        user_ref.set({
            'uid': uid,
            'name': name,
            'email': email,
            'created_at': SERVER_TIMESTAMP
        }, merge=True)

        return jsonify({'success': True, 'message': 'Usuário registrado com sucesso!'})

    except Exception as e:
        return jsonify({'success': False, 'error': f'Erro interno: {str(e)}'}), 500