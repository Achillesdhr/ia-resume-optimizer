# 🚀 Otimizador de Currículos com IA

Uma aplicação **Flask** poderosa que utiliza **Inteligência Artificial** para analisar e otimizar currículos, além de buscar vagas de emprego relevantes.

---

## 🌟 Funcionalidades Principais

* **Upload de Currículos**: Suporte para arquivos **PDF** e **DOCX**.
* **Análise com IA (Google Gemini)**: Extração inteligente de experiências, habilidades e palavras-chave.
* **Busca de Vagas (JSearch API)**: Encontra vagas de emprego relevantes com base no seu perfil.
* **Filtros Avançados**: Refine sua busca por tipo de emprego e local de trabalho.
* **Currículo Personalizado**: Geração de um PDF otimizado para cada vaga de interesse.
* **Interface Moderna**: Design responsivo e intuitivo para uma ótima experiência do usuário.

---

## 🛠️ Como Executar

Para colocar o projeto no ar, siga estes passos:

1.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Configure as variáveis de ambiente**:
    Crie um arquivo `.env` na raiz do projeto com as seguintes chaves:
    ```
    GOOGLE_API_KEY=sua_chave_api_gemini
    SECRET_KEY=sua_chave_secreta
    FLASK_DEBUG=True
    ```
3.  **Execute a aplicação**:
    ```bash
    python app.py
    ```
4.  **Acesse no navegador**:
    ```
    http://localhost:5000
    ```

---

## 📋 Dependências Essenciais

Este projeto utiliza as seguintes bibliotecas:

* **Flask**: Framework web.
* **google-genai**: Para integração com a API Gemini.
* **python-docx**: Para manipulação de arquivos DOCX.
* **pdfplumber**: Para extração de texto de PDFs.
* **reportlab**: Para geração de PDFs.
* **requests**: Para requisições HTTP (JSearch API).
* **python-dotenv**: Para carregar variáveis de ambiente.

---

## ⚙️ Estrutura Modular

O projeto é organizado de forma modular para facilitar a manutenção e escalabilidade:

* **`app.py`**: Aplicação principal Flask.
* **`config.py`**: Centraliza todas as configurações.
* **`uploads/`**: Diretório para arquivos enviados.
* **`templates/`**: Contém o HTML principal (`index.html`).
* **`static/`**: Arquivos CSS (`style.css`) e JavaScript (`app.js`).
* **`utils/`**: Utilitários como `text_extractor.py` (extração de texto).
* **`services/`**: Camada de serviços:
    * `ai_service.py`: Integração com **Google Gemini**.
    * `job_service.py`: Busca de vagas via **JSearch API**.
    * `pdf_service.py`: Geração de **PDFs**.
* **`routes/`**: Define as rotas da aplicação:
    * `upload_routes.py`: Rotas de upload.
    * `job_routes.py`: Rotas de busca de vagas.
    * `resume_routes.py`: Rotas de currículos.

---

## 🔄 Fluxo da Aplicação

1.  O usuário faz o **upload** do currículo.
2.  O sistema **extrai o texto** do arquivo.
3.  A **IA (Gemini)** analisa e extrai informações relevantes.
4.  O sistema busca **vagas** com base nas palavras-chave.
5.  O usuário pode **filtrar e navegar** pelas vagas.
6.  O usuário pode **gerar um currículo personalizado** para cada vaga.

---

## ✅ Melhorias Implementadas

* **Separação de responsabilidades** clara.
* **Código modular** e reutilizável.
* **Configuração centralizada**.
* Utilização de **blueprints Flask**.
* **Frontend organizado** (CSS/JS separados).
* **Documentação clara**.
* **Tratamento de erros** aprimorado.

---

## 🐛 Solução de Problemas Comuns

* **Erro de API Key**: Verifique o arquivo `.env` e confirme a chave do Google API.
* **Erro de Upload**: Certifique-se de que o diretório `uploads/` existe e que o arquivo é PDF ou DOCX.
* **Erro de Geração de PDF**: Consulte os logs do console e verifique se o currículo foi carregado.

---

## 📝 Licença

Este projeto é de uso livre para fins educacionais e comerciais.
