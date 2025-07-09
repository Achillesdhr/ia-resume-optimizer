# 🔥 Configuração do Firebase Authentication

Este guia explica como configurar o Firebase Authentication no seu projeto JobMatch AI.

## 📋 Pré-requisitos

1. Conta no Google Cloud Console
2. Projeto Firebase criado
3. Python 3.8+ instalado

## 🚀 Passo a Passo

### 1. Criar Projeto Firebase

1. Acesse [Firebase Console](https://console.firebase.google.com/)
2. Clique em "Criar projeto"
3. Digite o nome do projeto (ex: "jobmatch-ai")
4. Siga os passos de configuração

### 2. Configurar Authentication

1. No console Firebase, vá para "Authentication"
2. Clique em "Get started"
3. Vá para a aba "Sign-in method"
4. Habilite "Email/Password"
5. **Habilite "Google"** (importante para login social)
6. Clique em "Save"

#### 2.1 Configurar Google Sign-In

1. Na seção "Google", clique em "Editar"
2. Selecione um "Project support email"
3. Clique em "Save"
4. **Importante**: Anote o "Web client ID" que aparecerá

### 3. Obter Configurações do Projeto

1. No console Firebase, clique na engrenagem ⚙️ (Configurações)
2. Selecione "Configurações do projeto"
3. Role até "Seus aplicativos"
4. Clique em "Adicionar app" e selecione "Web"
5. Registre o app e copie as configurações

### 4. Configurar Variáveis de Ambiente

1. Crie um arquivo `.env` na raiz do projeto
2. Copie o conteúdo de `env_example.txt`
3. Substitua os valores pelas suas configurações do Firebase:

```env
# Configurações do Firebase
FIREBASE_API_KEY=sua-api-key-aqui
FIREBASE_AUTH_DOMAIN=seu-projeto.firebaseapp.com
FIREBASE_PROJECT_ID=seu-projeto-id
FIREBASE_STORAGE_BUCKET=seu-projeto.appspot.com
FIREBASE_MESSAGING_SENDER_ID=123456789
FIREBASE_APP_ID=1:123456789:web:abcdef123456

# Secret key para sessões Flask
SECRET_KEY=sua-secret-key-super-secreta-aqui

# Outras configurações
DEBUG=True
```

### 5. Atualizar Configuração no Frontend

1. Abra `templates/index.html`
2. Localize a seção de configuração do Firebase (linha ~120)
3. Substitua `firebaseConfig` com suas configurações:

```javascript
const firebaseConfig = {
    apiKey: "sua-api-key-aqui",
    authDomain: "seu-projeto.firebaseapp.com",
    projectId: "seu-projeto-id",
    storageBucket: "seu-projeto.appspot.com",
    messagingSenderId: "123456789",
    appId: "1:123456789:web:abcdef123456"
};
```

### 6. Configurar Firebase Admin SDK (Opcional)

Para funcionalidades avançadas no backend:

1. No console Firebase, vá para "Configurações do projeto"
2. Aba "Contas de serviço"
3. Clique em "Gerar nova chave privada"
4. Salve o arquivo JSON como `serviceAccountKey.json`
5. Adicione o caminho no `.env`:

```env
FIREBASE_CREDENTIALS_PATH=serviceAccountKey.json
```

## 🧪 Testando

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o projeto:
```bash
python app.py
```

3. Acesse `http://localhost:5000`
4. Clique em "Login" no cabeçalho
5. Teste tanto o login com email/senha quanto com Google

## 📁 Estrutura de Arquivos

```
resume-optimizer/
├── firebase_config.py          # Configuração do Firebase Admin
├── routes/auth_routes.py       # Rotas de autenticação
├── templates/index.html        # Frontend com Firebase SDK
├── .env                        # Variáveis de ambiente
├── env_example.txt            # Exemplo de configuração
└── FIREBASE_SETUP.md          # Este arquivo
```

## 🔧 Funcionalidades Implementadas

- ✅ Login com email/senha
- ✅ **Login com Google** (novo!)
- ✅ Logout
- ✅ Verificação de estado de autenticação
- ✅ Menu de usuário logado
- ✅ Integração com sessões Flask
- ✅ Tratamento de erros
- ✅ Notificações de feedback

## 🛡️ Segurança

- Tokens JWT verificados no backend
- Sessões seguras com secret key
- Validação de entrada
- Tratamento de erros de autenticação
- **OAuth 2.0** para login com Google

## 🚨 Troubleshooting

### Erro: "Firebase not initialized"
- Verifique se as configurações do Firebase estão corretas
- Confirme se o Firebase SDK está carregado

### Erro: "Invalid API key"
- Verifique se a API key está correta
- Confirme se o domínio está autorizado no Firebase

### Erro: "User not found"
- Verifique se o usuário foi criado no Firebase
- Confirme se o email está correto

### Erro: "Popup blocked"
- Permita popups para o seu domínio
- Verifique se o bloqueador de popups está desabilitado

### Erro: "Google Sign-In not configured"
- Verifique se o provedor Google está habilitado no Firebase
- Confirme se o "Web client ID" está correto

## 📞 Suporte

Se encontrar problemas:
1. Verifique o console do navegador para erros JavaScript
2. Verifique os logs do Flask para erros do backend
3. Confirme se todas as configurações estão corretas
4. Verifique se o provedor Google está habilitado no Firebase 