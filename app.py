from flask import Flask, render_template
import os
from config import Config

# Importa os blueprints
from routes.upload_routes import upload_bp
from routes.job_routes import job_bp
from routes.resume_routes import resume_bp
from routes.auth_routes import auth_bp

def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__, static_folder='static')
    
    # Configurações
    app.config.from_object(Config)
    
    # Configura secret key para sessões
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Cria diretório de uploads se não existir
    if not os.path.exists(Config.UPLOAD_FOLDER):
        os.makedirs(Config.UPLOAD_FOLDER)
    
    # Registra os blueprints
    app.register_blueprint(upload_bp)
    app.register_blueprint(job_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(auth_bp)
    
    # Rota principal
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=Config.DEBUG) 