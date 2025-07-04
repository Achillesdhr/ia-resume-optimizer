// Variáveis globais
let currentPage = 1;
let jobsPerPage = 5;
let allJobs = [];

// Elementos do DOM
const fileInput = document.getElementById('fileInput');
const fileLabel = document.getElementById('fileLabel');
const uploadBtn = document.getElementById('uploadBtn');
const resultsDiv = document.getElementById('results');
const jobsContainer = document.getElementById('jobsContainer');
const paginationContainer = document.getElementById('pagination');

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    fileInput.addEventListener('change', handleFileSelect);
    uploadBtn.addEventListener('click', handleUpload);
});

// Manipulação de arquivo selecionado
function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        fileLabel.textContent = `Arquivo selecionado: ${file.name}`;
        fileLabel.style.background = 'linear-gradient(45deg, #28a745, #20c997)';
        uploadBtn.disabled = false;
    } else {
        fileLabel.textContent = 'Clique para selecionar um arquivo (PDF ou DOCX)';
        fileLabel.style.background = 'linear-gradient(45deg, #667eea, #764ba2)';
        uploadBtn.disabled = true;
    }
}

// Upload do arquivo
async function handleUpload() {
    const file = fileInput.files[0];
    if (!file) {
        alert('Por favor, seleciona um arquivo primeiro.');
        return;
    }

    // Mostra loading
    showLoading();
    
    const formData = new FormData();
    formData.append('file', file);
    
    // Adiciona filtros se selecionados
    const employmentType = document.getElementById('employmentType').value;
    const workplaceType = document.getElementById('workplaceType').value;
    
    if (employmentType) formData.append('employment_type', employmentType);
    if (workplaceType) formData.append('workplace_type', workplaceType);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        
        if (response.ok) {
            displayResults(result);
        } else {
            showError(result.error || 'Erro no upload');
        }
    } catch (error) {
        console.error('Erro:', error);
        showError('Erro de conexão');
    }
}

// Exibe resultados
function displayResults(result) {
    resultsDiv.innerHTML = '';
    
    // Resultado da IA
    if (result.resultado_gemini) {
        const aiResult = createResultCard('Análise da IA', result.resultado_gemini);
        resultsDiv.appendChild(aiResult);
    }
    
    // Vagas encontradas
    if (result.vagas_encontradas && result.vagas_encontradas.data) {
        allJobs = result.vagas_encontradas.data;
        displayJobs();
    } else if (result.vagas_encontradas && result.vagas_encontradas.erro) {
        showError(`Erro na busca de vagas: ${result.vagas_encontradas.erro}`);
    }
}

// Cria card de resultado
function createResultCard(title, data) {
    const card = document.createElement('div');
    card.className = 'result-card fade-in';
    
    const titleEl = document.createElement('h3');
    titleEl.textContent = title;
    card.appendChild(titleEl);
    
    if (typeof data === 'object') {
        for (const [key, value] of Object.entries(data)) {
            if (value && value.length > 0) {
                const section = document.createElement('div');
                section.innerHTML = `<strong>${key.replace('_', ' ').toUpperCase()}:</strong> `;
                
                if (Array.isArray(value)) {
                    section.innerHTML += value.join(', ');
                } else {
                    section.innerHTML += value;
                }
                card.appendChild(section);
            }
        }
    } else {
        card.innerHTML += `<p>${data}</p>`;
    }
    
    return card;
}

// Exibe vagas
function displayJobs() {
    if (!allJobs || allJobs.length === 0) {
        jobsContainer.innerHTML = '<p>Nenhuma vaga encontrada.</p>';
        return;
    }
    
    const startIndex = (currentPage - 1) * jobsPerPage;
    const endIndex = startIndex + jobsPerPage;
    const currentJobs = allJobs.slice(startIndex, endIndex);
    
    jobsContainer.innerHTML = '';
    
    currentJobs.forEach(job => {
        const jobCard = createJobCard(job);
        jobsContainer.appendChild(jobCard);
    });
    
    updatePagination();
}

// Cria card de vaga
function createJobCard(job) {
    const card = document.createElement('div');
    card.className = 'job-card fade-in';
    
    card.innerHTML = `
        <div class="job-title">${job.job_title || 'Título não disponível'}</div>
        <div class="job-company">${job.employer_name || 'Empresa não disponível'}</div>
        <div class="job-location">📍 ${job.job_city || 'Localização não disponível'}</div>
        <div class="job-description">${job.job_description || 'Descrição não disponível'}</div>
        <div class="job-actions">
            <a href="${job.job_apply_link || '#'}" target="_blank" class="job-link">Ver Vaga</a>
            <button class="generate-resume-btn" onclick="generateResume('${escapeString(job.job_title || '')}', '${escapeString(job.employer_name || '')}', '${escapeString(job.job_description || '')}')">
                📄 Gerar CV Personalizado
            </button>
        </div>
    `;
    
    return card;
}

// Escapa strings para uso em atributos HTML
function escapeString(text) {
    if (!text) return '';
    return text
        .replace(/\\/g, '\\\\')
        .replace(/'/g, "\\'")
        .replace(/"/g, '\\"')
        .replace(/\n/g, '\\n')
        .replace(/\r/g, '\\r')
        .replace(/\t/g, '\\t');
}

// Atualiza paginação
function updatePagination() {
    const totalPages = Math.ceil(allJobs.length / jobsPerPage);
    
    paginationContainer.innerHTML = '';
    
    if (totalPages <= 1) return;
    
    // Botão anterior
    const prevBtn = document.createElement('button');
    prevBtn.className = 'pagination-btn';
    prevBtn.textContent = '← Anterior';
    prevBtn.disabled = currentPage === 1;
    prevBtn.onclick = () => changePage(currentPage - 1);
    paginationContainer.appendChild(prevBtn);
    
    // Informação da página
    const pageInfo = document.createElement('div');
    pageInfo.className = 'page-info';
    pageInfo.textContent = `Página ${currentPage} de ${totalPages}`;
    paginationContainer.appendChild(pageInfo);
    
    // Botão próximo
    const nextBtn = document.createElement('button');
    nextBtn.className = 'pagination-btn';
    nextBtn.textContent = 'Próxima →';
    nextBtn.disabled = currentPage === totalPages;
    nextBtn.onclick = () => changePage(currentPage + 1);
    paginationContainer.appendChild(nextBtn);
}

// Muda página
function changePage(page) {
    currentPage = page;
    displayJobs();
}

// Gera currículo personalizado
async function generateResume(tituloVaga, empresa, descricaoVaga) {
    console.log('=== GERANDO CURRÍCULO PERSONALIZADO ===');
    console.log('Título da vaga:', tituloVaga);
    console.log('Empresa:', empresa);
    console.log('Descrição da vaga:', descricaoVaga);
    
    const button = event.target;
    const originalText = button.textContent;
    
    try {
        button.disabled = true;
        button.textContent = '⏳ Gerando...';
        
        const response = await fetch('/gerar_curriculo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                titulo_vaga: tituloVaga,
                empresa: empresa,
                descricao_vaga: descricaoVaga
            })
        });
        
        console.log('Resposta recebida:', response);
        
        if (response.ok) {
            // Cria blob para download
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            
            // Cria link de download
            const a = document.createElement('a');
            a.href = url;
            a.download = `curriculo_${empresa.replace(/\s+/g, '_')}.pdf`;
            document.body.appendChild(a);
            a.click();
            
            // Limpa
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
            
            button.textContent = '✅ Baixado!';
            setTimeout(() => {
                button.textContent = originalText;
                button.disabled = false;
            }, 3000);
        } else {
            const errorData = await response.json();
            console.error('Erro na resposta:', errorData);
            alert(`Erro ao gerar currículo: ${errorData.erro || 'Erro desconhecido'}`);
            button.textContent = originalText;
            button.disabled = false;
        }
    } catch (error) {
        console.error('Erro na requisição:', error);
        alert('Erro de conexão ao gerar currículo');
        button.textContent = originalText;
        button.disabled = false;
    }
}

// Mostra loading
function showLoading() {
    resultsDiv.innerHTML = `
        <div class="loading">
            <div class="spinner"></div>
            <p>Processando arquivo e buscando vagas...</p>
        </div>
    `;
}

// Mostra erro
function showError(message) {
    resultsDiv.innerHTML = `
        <div class="result-card error">
            <h3>Erro</h3>
            <p class="error-message">${message}</p>
        </div>
    `;
} 