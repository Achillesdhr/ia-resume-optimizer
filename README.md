# JobMatch AI 🤖

> **Plataforma inteligente de otimização de currículos com IA**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![Firebase](https://img.shields.io/badge/Firebase-Auth%20%7C%20Firestore-orange.svg)](https://firebase.google.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Visão Geral

O JobMatch AI é uma plataforma inovadora que utiliza Inteligência Artificial para conectar candidatos às melhores oportunidades de emprego. O sistema analisa currículos, busca vagas relevantes e gera versões personalizadas dos currículos para cada oportunidade.

### ✨ Principais Funcionalidades

- 🔐 **Autenticação Segura** - Login com Firebase Auth
- 📄 **Upload Inteligente** - Suporte a PDF e DOCX
- 🔍 **Busca de Vagas** - Integração com múltiplas plataformas
- 🎯 **Otimização de Currículos** - IA personalizada por vaga
- 📱 **Interface Responsiva** - Design moderno e intuitivo
- 🔄 **Validação de Tokens** - Segurança automática

## 🛠️ Tecnologias

### Frontend
- **HTML5** + **CSS3** + **JavaScript (ES6+)**
- **Tailwind CSS** - Framework de estilização
- **Font Awesome** - Ícones
- **Google Fonts** - Tipografia

### Backend
- **Python 3.11+** - Linguagem principal
- **Flask** - Framework web
- **Firebase** - Autenticação e banco de dados
- **pdfplumber** - Processamento de PDFs
- **python-docx** - Processamento de DOCX

### Serviços
- **Firebase Authentication** - Sistema de login
- **Firestore** - Banco de dados NoSQL
- **Google Cloud** - Infraestrutura

## ⚡ Instalação Rápida

### Pré-requisitos
- Python 3.11+
- Conta Firebase
- Git

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/resume-optimizer.git
cd resume-optimizer
```

### 2. Configure o Ambiente
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Linux/Mac)
source venv/bin/activate

# Ativar ambiente (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configure o Firebase
1. Crie um projeto no [Firebase Console](https://console.firebase.google.com)
2. Ative Authentication e Firestore
3. Configure as credenciais em `static/js/auth.js`

### 4. Execute a Aplicação
```bash
python app.py
```

Acesse: **http://localhost:5000** 🎉

## 📁 Estrutura do Projeto

```
resume-optimizer/
├── app.py                      # Aplicação principal
├── routes/                     # Rotas da aplicação
├── services/                   # Serviços de negócio
├── utils/                      # Utilitários
├── static/                     # Arquivos estáticos
│   ├── css/
│   ├── js/
│   └── uploads/
├── templates/                  # Templates HTML
├── requirements.txt            # Dependências Python
└── docs/                      # Documentação
```

## 🔐 Autenticação

### Estados do Sistema

#### Usuário Não Autenticado
- ✅ Botão "Login" visível
- ✅ Botão de upload **visível mas desabilitado**
- ✅ Mensagem informativa sobre login
- ✅ Modal de login/cadastro funcional

#### Usuário Autenticado
- ✅ Dropdown com nome do usuário
- ✅ Botão de upload **habilitado e funcional**
- ✅ Opção de logout disponível
- ✅ Token validado automaticamente

### Funcionalidades de Segurança
- **Validação de Token**: Verificação automática de expiração
- **Refresh Automático**: Renovação a cada 55 minutos
- **Logout Automático**: Em caso de token inválido
- **Persistência**: Manutenção de sessão após recarga

## 🎨 Interface

### Design Responsivo
- **Mobile First** - Otimizado para dispositivos móveis
- **Tailwind CSS** - Framework moderno de estilização
- **Animações Suaves** - Transições elegantes
- **Acessibilidade** - Suporte a leitores de tela

### Componentes Principais
- **Header**: Navegação e autenticação
- **Hero Section**: Apresentação do produto
- **Upload Section**: Área de envio de currículos
- **Results Section**: Exibição de resultados
- **Footer**: Informações de contato

## 📊 Funcionalidades

### Upload de Currículos
- **Formatos**: PDF, DOCX
- **Tamanho**: Máximo 5MB
- **Validação**: Tipo e conteúdo
- **Processamento**: Extração automática de texto

### Busca de Vagas
- **Integração**: Múltiplas APIs de emprego
- **Filtros**: Tipo, localização, experiência
- **Matching**: Algoritmo de compatibilidade
- **Resultados**: Personalizados por perfil

### Otimização de Currículos
- **Análise IA**: Identificação de habilidades
- **Personalização**: Adaptação por vaga
- **Geração**: Versões otimizadas
- **Comparação**: Múltiplas versões

## 🧪 Testes

### Guia de Testes
Consulte o arquivo [TEST_BUTTON_BEHAVIOR.md](TEST_BUTTON_BEHAVIOR.md) para um guia completo de testes.

### Cenários Principais
1. **Estado Inicial**: Verificar botão de login e upload desabilitado
2. **Após Login**: Verificar dropdown e upload habilitado
3. **Após Logout**: Verificar restauração do estado inicial
4. **Recarga**: Verificar persistência de sessão

### Comandos de Teste
```javascript
// Verificar estado atual
console.log('Usuário logado:', currentUser);
console.log('Token válido:', userToken);

// Verificar interface
const loginBtn = document.getElementById('loginBtn');
console.log('Texto do botão:', loginBtn.textContent);
```

## 📚 Documentação

### Documentação Completa
- **[DOCUMENTACAO_COMPLETA.md](DOCUMENTACAO_COMPLETA.md)** - Documentação técnica completa
- **[AUTH_IMPLEMENTATION.md](AUTH_IMPLEMENTATION.md)** - Implementação de autenticação
- **[TEST_BUTTON_BEHAVIOR.md](TEST_BUTTON_BEHAVIOR.md)** - Guia de testes

### Seções Principais
- **Arquitetura**: Visão geral do sistema
- **Instalação**: Configuração passo a passo
- **Autenticação**: Sistema de segurança
- **Interface**: Design e componentes
- **API**: Endpoints e integrações
- **Deploy**: Configuração de produção

## 🚀 Deploy

### Configuração de Produção
```bash
# Variáveis de ambiente
FLASK_ENV=production
FLASK_DEBUG=0
SECRET_KEY=sua-chave-secreta

# Servidor
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Serviços Recomendados
- **Heroku** - Deploy simples
- **Google Cloud** - Integração nativa com Firebase
- **AWS** - Escalabilidade
- **DigitalOcean** - Custo-benefício

## 🤝 Contribuição

### Como Contribuir
1. **Fork** o repositório
2. **Clone** seu fork
3. **Crie** uma branch para sua feature
4. **Commit** suas mudanças
5. **Push** para a branch
6. **Abra** um Pull Request

### Padrões de Código
- **Python**: PEP 8
- **JavaScript**: ESLint
- **HTML/CSS**: Prettier
- **Commits**: Conventional Commits

### Áreas de Contribuição
- 🐛 **Bug Fixes** - Correção de problemas
- ✨ **Features** - Novas funcionalidades
- 📚 **Documentação** - Melhorias na docs
- 🎨 **UI/UX** - Melhorias na interface
- 🧪 **Testes** - Cobertura de testes

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Suporte

### Contato
- **Email**: contato@jobmatchai.com
- **GitHub**: [Issues](https://github.com/seu-usuario/resume-optimizer/issues)
- **Discord**: [Comunidade](https://discord.gg/jobmatchai)

### Recursos
- **Documentação**: [docs.jobmatchai.com](https://docs.jobmatchai.com)
- **Demo**: [demo.jobmatchai.com](https://demo.jobmatchai.com)
- **Roadmap**: [GitHub Projects](https://github.com/seu-usuario/resume-optimizer/projects)

---

## 🎯 Roadmap

### v1.1 - Melhorias de UX
- [ ] Dashboard do usuário
- [ ] Histórico de buscas
- [ ] Favoritos de vagas
- [ ] Comparação de currículos

### v1.2 - Funcionalidades Avançadas
- [ ] IA para análise de compatibilidade
- [ ] Recomendações personalizadas
- [ ] Integração com LinkedIn
- [ ] Sistema de feedback

### v2.0 - Plataforma Completa
- [ ] Portal para recrutadores
- [ ] Sistema de candidaturas
- [ ] Analytics avançado
- [ ] API pública

---

<div align="center">

**⭐ Se este projeto te ajudou, considere dar uma estrela! ⭐**

*Desenvolvido com ❤️ pela equipe JobMatch AI*

</div> 