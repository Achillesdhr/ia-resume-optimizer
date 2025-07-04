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

## 🔄 Fluxo da Aplicação

1.  O usuário faz o **upload** do currículo.
2.  O sistema **extrai o texto** do arquivo.
3.  A **IA (Gemini)** analisa e extrai informações relevantes.
4.  O sistema busca **vagas** com base nas palavras-chave.
5.  O usuário pode **filtrar e navegar** pelas vagas.
6.  O usuário pode **gerar um currículo personalizado** para cada vaga.

---

## ✅ Melhorias para implementar

* **Autenticação de Usuário**:
    * Implementar **login** e **cadastro** para proteger os currículos e dados sensíveis do usuário, garantindo privacidade e segurança.
* **Dashboard do Usuário**:
    * Criar uma área personalizada onde o usuário poderá **visualizar, editar e gerenciar** todos os seus currículos enviados e otimizados de forma centralizada.
* **Feedback Detalhado da IA**:
    * Aprimorar a inteligência artificial para fornecer **sugestões de melhoria mais detalhadas** para cada seção do currículo (ex: experiência, habilidades, resumo), indicando pontos fortes e fracos.
* **Comparação de Currículos**:
    * Permitir que o usuário **compare diferentes versões** do currículo, visualizando as alterações antes e depois da otimização pela IA.
* **Sugestão de Vagas Personalizadas**:
    * Aprofundar a integração com **APIs de vagas de emprego** para sugerir oportunidades ainda mais personalizadas, baseadas no perfil detalhado do currículo otimizado.
* **Análise de Palavras-chave**:
    * Implementar uma funcionalidade para **destacar palavras-chave importantes** que podem estar faltando no currículo, de acordo com os requisitos da vaga desejada.
* **Exportação para LinkedIn**:
    * Desenvolver a capacidade de **exportar o currículo otimizado diretamente para o perfil do LinkedIn** do usuário, facilitando a atualização online.
* **Histórico de Alterações**:
    * Manter um **histórico completo das otimizações** realizadas em cada currículo, permitindo ao usuário revisar as edições anteriores.
* **Interface Responsiva e Moderna**:
    * Continuar aprimorando o **design da interface** para garantir que seja ainda mais intuitiva, visualmente agradável e totalmente responsiva em todos os dispositivos móveis.
* **Suporte Multilíngue**:
    * Adicionar a capacidade de **otimizar currículos em diferentes idiomas**, expandindo o alcance e a utilidade da ferramenta.
* **Envio Automático para Recrutadores**:
    * Explorar a implementação de uma funcionalidade para **enviar currículos otimizados diretamente** para recrutadores ou empresas através da plataforma.
* **Sistema de Notificações**:
    * Integrar um sistema de **notificações** para alertar o usuário sobre novas vagas relevantes, sugestões de melhoria para o currículo ou o status do processamento de documentos.
* **Testes Automatizados**:
    * Fortalecer a qualidade do código com a adição de **testes unitários e de integração** abrangentes, garantindo maior estabilidade e minimizando bugs.
* **Documentação Completa**:
    * Melhorar e expandir a **documentação do projeto**, facilitando a compreensão e a contribuição de novos desenvolvedores.

---

## 🐛 Solução de Problemas Comuns

* **Erro de API Key**: Verifique o arquivo `.env` e confirme a chave do Google API.
* **Erro de Upload**: Certifique-se de que o diretório `uploads/` existe e que o arquivo é PDF ou DOCX.
* **Erro de Geração de PDF**: Consulte os logs do console e verifique se o currículo foi carregado.

---

## 📝 Licença

Este projeto é de uso livre para fins educacionais e comerciais.
