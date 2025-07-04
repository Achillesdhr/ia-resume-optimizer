# 🚀 Otimizador de Currículos com IA

Uma aplicação Flask que utiliza inteligência artificial para otimizar currículos e buscar vagas de emprego relevantes.

## 📁 Estrutura do Projeto

```
workspace/
├── app.py                 # Aplicação principal Flask
├── config.py             # Configurações da aplicação
├── requirements.txt      # Dependências Python
├── README.md            # Documentação
├── .env                 # Variáveis de ambiente (criar)
├── uploads/             # Diretório para arquivos enviados
├── templates/
│   └── index.html       # Template HTML principal
├── static/
│   ├── css/
│   │   └── style.css    # Estilos CSS
│   └── js/
│       └── app.js       # JavaScript da aplicação
├── utils/
│   ├── __init__.py
│   └── text_extractor.py # Extração de texto de arquivos
├── services/
│   ├── __init__.py
│   ├── ai_service.py    # Serviços de IA (Gemini)
│   ├── job_service.py   # Serviços de busca de vagas
│   └── pdf_service.py   # Geração de PDFs
└── routes/
    ├── __init__.py
    ├── upload_routes.py # Rotas de upload
    ├── job_routes.py    # Rotas de vagas
    └── resume_routes.py # Rotas de currículos
```

## 🛠️ Funcionalidades

- **Upload de Currículos**: Suporte para arquivos PDF e DOCX
- **Análise com IA**: Extração de experiências, habilidades e palavras-chave usando Google Gemini
- **Busca de Vagas**: Integração com JSearch API para encontrar vagas relevantes
- **Filtros Avançados**: Por tipo de emprego e local de trabalho
- **Paginação**: Navegação por páginas das vagas encontradas
- **Currículo Personalizado**: Geração de PDF personalizado para cada vaga
- **Interface Moderna**: Design responsivo e intuitivo

## 🚀 Como Executar

1. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar variáveis de ambiente**:
   Criar arquivo `.env` com:
   ```
   GOOGLE_API_KEY=sua_chave_api_gemini
   SECRET_KEY=sua_chave_secreta
   FLASK_DEBUG=True
   ```

3. **Executar a aplicação**:
   ```bash
   python app.py
   ```

4. **Acessar no navegador**:
   ```
   http://localhost:5000
   ```

## 📋 Dependências

- Flask
- google-genai
- python-docx
- pdfplumber
- reportlab
- requests
- python-dotenv

## 🔧 Configuração das APIs

### Google Gemini
1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crie uma API key
3. Adicione no arquivo `.env`

### JSearch (RapidAPI)
- A API key já está configurada no código
- Para usar sua própria chave, edite `config.py`

## 🎨 Estrutura Modular

### Configuração (`config.py`)
Centraliza todas as configurações da aplicação.

### Utilitários (`utils/`)
- **text_extractor.py**: Extração de texto de PDFs e DOCXs

### Serviços (`services/`)
- **ai_service.py**: Integração com Google Gemini
- **job_service.py**: Busca de vagas via JSearch API
- **pdf_service.py**: Geração de PDFs personalizados

### Rotas (`routes/`)
- **upload_routes.py**: Processamento de uploads
- **job_routes.py**: Busca direta de vagas
- **resume_routes.py**: Geração de currículos

### Frontend (`static/`)
- **style.css**: Estilos CSS responsivos
- **app.js**: Lógica JavaScript da aplicação

## 🔄 Fluxo da Aplicação

1. Usuário faz upload do currículo
2. Sistema extrai texto do arquivo
3. IA analisa e extrai informações relevantes
4. Sistema busca vagas baseado nas palavras-chave
5. Usuário pode filtrar e navegar pelas vagas
6. Usuário pode gerar currículo personalizado para cada vaga

## 🎯 Melhorias Implementadas

- ✅ Separação de responsabilidades
- ✅ Código modular e reutilizável
- ✅ Configuração centralizada
- ✅ Estrutura de blueprints Flask
- ✅ Frontend organizado (CSS/JS separados)
- ✅ Documentação clara
- ✅ Tratamento de erros melhorado

## 🐛 Solução de Problemas

### Erro de API Key
- Verifique se o arquivo `.env` existe
- Confirme se a API key do Google está correta

### Erro de Upload
- Verifique se o diretório `uploads/` existe
- Confirme se o arquivo é PDF ou DOCX

### Erro de Geração de PDF
- Verifique os logs do console
- Confirme se o currículo foi carregado

## 📝 Licença

Este projeto é de uso livre para fins educacionais e comerciais. 