// Variáveis globais
let currentPage = 1;
let jobsPerPage = 6;
let allJobs = [];

// Elementos do DOM
const fileInput = document.getElementById('fileInput');
const uploadBtn = document.getElementById('uploadBtn');
const uploadProgress = document.getElementById('uploadProgress');
const progressBar = document.getElementById('progressBar');
const progressPercent = document.getElementById('progressPercent');
const uploadSuccess = document.getElementById('uploadSuccess');
const resultsDiv = document.getElementById('results');
const jobsContainer = document.getElementById('jobsContainer');
const paginationContainer = document.getElementById('pagination');

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    fileInput.addEventListener('change', handleFileSelect);
    // Removido: uploadBtn.addEventListener('click', handleUpload); - conflito com onclick no HTML
    
    // Drag and drop functionality
    setupDragAndDrop();
});

// Configura drag and drop
function setupDragAndDrop() {
    const dropZone = document.querySelector('.file-upload label div');
    
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, preventDefaults, false);
    });
    
    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }
    
    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, highlight, false);
    });
    
    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, unhighlight, false);
    });
    
    function highlight(e) {
        dropZone.classList.add('border-indigo-500', 'bg-indigo-50');
    }
    
    function unhighlight(e) {
        dropZone.classList.remove('border-indigo-500', 'bg-indigo-50');
    }
    
    dropZone.addEventListener('drop', handleDrop, false);
    
    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        
        if (files.length > 0) {
            fileInput.files = files;
            handleFileSelect({ target: { files: files } });
        }
    }
}

// Manipulação de arquivo selecionado
function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        // Validação do arquivo
        const validTypes = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
        const maxSize = 5 * 1024 * 1024; // 5MB
        
        if (!validTypes.includes(file.type)) {
            showNotification('Por favor, selecione um arquivo PDF ou DOCX.', 'error');
            return;
        }
        
        if (file.size > maxSize) {
            showNotification('O arquivo é muito grande. O tamanho máximo permitido é 5MB.', 'error');
            return;
        }
        
        // Atualiza a interface
        const dropZone = document.querySelector('.file-upload label div');
        dropZone.innerHTML = `
            <i class="fas fa-check-circle text-green-500 text-4xl mb-4"></i>
            <h4 class="text-lg font-medium text-gray-700 mb-2">Arquivo selecionado</h4>
            <p class="text-gray-500 mb-4">${file.name}</p>
            <p class="text-sm text-gray-400">Clique em "Analisar Currículo" para continuar</p>
        `;
        
        uploadBtn.classList.remove('bg-gray-400');
        uploadBtn.classList.add('bg-indigo-600');
    } else {
        uploadBtn.classList.add('bg-gray-400');
        uploadBtn.classList.remove('bg-indigo-600');
    }
}

// Upload do arquivo
async function handleUpload() {
    const file = fileInput.files[0];

    // Mostra progresso
    showUploadProgress();
    
    const formData = new FormData();
    formData.append('file', file);
    
    // Adiciona filtros se selecionados
    const employmentType = document.getElementById('employmentType').value;
    const workplaceType = document.getElementById('workplaceType').value;
    
    if (employmentType) formData.append('employment_type', employmentType);
    if (workplaceType) formData.append('workplace_type', workplaceType);

    try {
        // Simula progresso de upload
        simulateProgress();
        
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        
        if (response.ok) {
            showUploadSuccess();
            setTimeout(() => {
                displayResults(result);
                // Esconde o progresso após mostrar os resultados
                hideUploadProgress();
            }, 1500);
        } else {
            showNotification(result.error || 'Erro no upload', 'error');
            hideUploadProgress();
        }
    } catch (error) {
        console.error('Erro:', error);
        showNotification('Erro de conexão', 'error');
        hideUploadProgress();
    }
}

// Simula progresso de upload
function simulateProgress() {
    let progress = 0;
    const interval = setInterval(() => {
        progress += Math.floor(Math.random() * 10) + 1;
        if (progress > 100) progress = 100;
        
        progressBar.style.width = `${progress}%`;
        progressPercent.textContent = `${progress}%`;
        
        if (progress === 100) {
            clearInterval(interval);
        }
    }, 300);
}

// Mostra progresso de upload
function showUploadProgress() {
    uploadProgress.classList.remove('hidden');
    uploadBtn.disabled = true;
    uploadBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i> Processando...';
}

// Esconde progresso de upload
function hideUploadProgress() {
    uploadProgress.classList.add('hidden');
    uploadSuccess.classList.add('hidden');
    uploadBtn.disabled = false;
    uploadBtn.innerHTML = '<i class="fas fa-upload mr-2"></i> Analisar Currículo e Buscar Vagas';
    uploadBtn.classList.remove('bg-gray-400');
    uploadBtn.classList.add('bg-indigo-600');
}

// Mostra sucesso do upload
function showUploadSuccess() {
    uploadSuccess.classList.remove('hidden');
    progressPercent.textContent = '100%';
    progressBar.style.width = '100%';
}

// Exibe resultados
function displayResults(result, retryCount = 0) {
    resultsDiv.classList.remove('hidden');
    resultsDiv.innerHTML = '';
    
    // Resultado da IA
    if (result.resultado_gemini) {
        const aiResult = createModernResultCard('Análise da IA', result.resultado_gemini);
        resultsDiv.appendChild(aiResult);
        // Scroll para a seção "Análise da IA" após um pequeno delay
        setTimeout(() => {
            aiResult.scrollIntoView({ 
                behavior: 'smooth', 
                block: 'start',
                inline: 'nearest'
            });
        }, 100);
    }
    
    // Vagas encontradas
    if (result.vagas_encontradas && result.vagas_encontradas.data) {
        allJobs = result.vagas_encontradas.data;
        if (allJobs.length === 0 && retryCount < 2) {
            // Retry automático
            showNotification('Nenhuma vaga encontrada. Tentando novamente...', 'info');
            // Refaz a requisição com os mesmos dados do último upload
            setTimeout(() => {
                retryLastUpload(retryCount + 1);
            }, 1200);
            return;
        }
        displayModernJobs();
        if (allJobs.length === 0 && retryCount >= 2) {
            showNotification('Nenhuma vaga encontrada após múltiplas tentativas.', 'warning');
        }
    } else if (result.vagas_encontradas && result.vagas_encontradas.erro) {
        showNotification(`Erro na busca de vagas: ${result.vagas_encontradas.erro}`, 'error');
    }
}

// Função para refazer o upload e buscar vagas novamente
async function retryLastUpload(retryCount) {
    const file = fileInput.files[0];
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);
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
        displayResults(result, retryCount);
    } catch (error) {
        showNotification('Erro ao tentar novamente buscar vagas.', 'error');
    }
}

// Cria card de resultado moderno
function createModernResultCard(title, data) {
    const card = document.createElement('div');
    card.className = 'bg-white rounded-xl shadow-lg p-6 mb-6 fade-in';
    
    const titleEl = document.createElement('h3');
    titleEl.className = 'text-xl font-bold text-gray-800 mb-4 flex items-center';
    titleEl.innerHTML = '<i class="fas fa-brain text-indigo-500 mr-3"></i>' + title;
    card.appendChild(titleEl);
    
    if (typeof data === 'object') {
        const content = document.createElement('div');
        content.className = 'space-y-3';
        
        for (const [key, value] of Object.entries(data)) {
            if (value && value.length > 0) {
                const section = document.createElement('div');
                section.className = 'bg-gray-50 p-4 rounded-lg';
                
                const sectionTitle = document.createElement('h4');
                sectionTitle.className = 'font-semibold text-gray-700 mb-2 capitalize';
                sectionTitle.textContent = key.replace('_', ' ');
                section.appendChild(sectionTitle);
                
                const sectionContent = document.createElement('div');
                sectionContent.className = 'text-gray-600';
                
                if (Array.isArray(value)) {
                    sectionContent.innerHTML = value.map(item => 
                        `<span class="inline-block bg-indigo-100 text-indigo-800 text-sm px-2 py-1 rounded mr-2 mb-2">${item}</span>`
                    ).join('');
                } else {
                    sectionContent.textContent = value;
                }
                
                section.appendChild(sectionContent);
                content.appendChild(section);
            }
        }
        
        card.appendChild(content);
    } else {
        const content = document.createElement('p');
        content.className = 'text-gray-600 leading-relaxed';
        content.textContent = data;
        card.appendChild(content);
    }
    
    return card;
}

// Exibe vagas com design moderno
function displayModernJobs() {
    if (!allJobs || allJobs.length === 0) {
        jobsContainer.innerHTML = `
            <div class="text-center py-12">
                <i class="fas fa-search text-4xl text-gray-400 mb-4"></i>
                <h3 class="text-xl font-semibold text-gray-600 mb-2">Nenhuma vaga encontrada</h3>
                <p class="text-gray-500">Tente ajustar os filtros ou enviar um currículo diferente.</p>
            </div>
        `;
        jobsContainer.classList.remove('hidden');
        return;
    }
    
    const startIndex = (currentPage - 1) * jobsPerPage;
    const endIndex = startIndex + jobsPerPage;
    const currentJobs = allJobs.slice(startIndex, endIndex);
    
    jobsContainer.innerHTML = `
        <div class="mb-6">
            <h3 class="text-2xl font-bold text-gray-800 mb-2">Vagas encontradas</h3>
            <p class="text-gray-600">${allJobs.length} oportunidades compatíveis com seu perfil</p>
        </div>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            ${currentJobs.map(job => createModernJobCard(job)).join('')}
        </div>
    `;
    
    jobsContainer.classList.remove('hidden');
    updateModernPagination();
}

// Cria card de vaga moderno
function createModernJobCard(job) {
    const matchScore = Math.floor(Math.random() * 30) + 70; // Simula score de compatibilidade
    
    return `
        <div class="bg-white rounded-xl shadow-md p-6 hover:shadow-lg transition-all duration-300 card-hover">
            <div class="flex justify-between items-start mb-4">
                <h4 class="text-lg font-bold text-gray-800 line-clamp-2">${job.job_title || 'Título não disponível'}</h4>
                <span class="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded-full whitespace-nowrap">
                    ${matchScore}% match
                </span>
            </div>
            
            <p class="text-indigo-600 font-medium mb-2">${job.employer_name || 'Empresa não disponível'}</p>
            <p class="text-gray-500 text-sm mb-4 flex items-center">
                <i class="fas fa-map-marker-alt mr-2"></i>
                ${job.job_city || 'Localização não disponível'}
            </p>
            
            <p class="text-gray-600 text-sm mb-4 line-clamp-3">
                ${job.job_description ? job.job_description.substring(0, 150) + '...' : 'Descrição não disponível'}
            </p>
            
            <div class="flex space-x-3">
                <a href="${job.job_apply_link || '#'}" target="_blank" 
                   class="bg-indigo-600 text-white font-medium py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors duration-200 flex-1 text-center text-sm">
                    <i class="fas fa-external-link-alt mr-2"></i> Ver Vaga
                </a>
                <button onclick="generateResume('${escapeString(job.job_title || '')}', '${escapeString(job.employer_name || '')}', '${escapeString(job.job_description || '')}')"
                        class="border border-indigo-600 text-indigo-600 font-medium py-2 px-4 rounded-lg hover:bg-indigo-50 transition-colors duration-200 text-sm">
                    <i class="fas fa-file-pdf"></i>
                </button>
            </div>
        </div>
    `;
}

// Escapa strings para uso em atributos HTML
function escapeString(text) {
    if (!text) return '';
    const maxLength = 200;
    if (text.length > maxLength) {
        text = text.substring(0, maxLength) + '...';
    }
    return text
        .replace(/\\/g, '\\\\')
        .replace(/'/g, "\\'")
        .replace(/"/g, '\\"')
        .replace(/\n/g, '\\n')
        .replace(/\r/g, '\\r')
        .replace(/\t/g, '\\t')
        .replace(/\s+/g, ' ');
}

// Atualiza paginação moderna
function updateModernPagination() {
    const totalPages = Math.ceil(allJobs.length / jobsPerPage);
    
    if (totalPages <= 1) {
        paginationContainer.classList.add('hidden');
        return;
    }
    
    paginationContainer.classList.remove('hidden');
    paginationContainer.innerHTML = `
        <div class="flex justify-center items-center space-x-4 mt-8">
            <button onclick="changePage(${currentPage - 1})" 
                    ${currentPage === 1 ? 'disabled' : ''}
                    class="px-4 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200">
                <i class="fas fa-chevron-left mr-2"></i> Anterior
            </button>
            
            <div class="flex space-x-2">
                ${generatePageNumbers(currentPage, totalPages)}
            </div>
            
            <button onclick="changePage(${currentPage + 1})" 
                    ${currentPage === totalPages ? 'disabled' : ''}
                    class="px-4 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200">
                Próxima <i class="fas fa-chevron-right ml-2"></i>
            </button>
        </div>
    `;
}

// Gera números das páginas
function generatePageNumbers(current, total) {
    let pages = [];
    const maxVisible = 5;
    
    if (total <= maxVisible) {
        for (let i = 1; i <= total; i++) {
            pages.push(i);
        }
    } else {
        if (current <= 3) {
            for (let i = 1; i <= 4; i++) {
                pages.push(i);
            }
            pages.push('...');
            pages.push(total);
        } else if (current >= total - 2) {
            pages.push(1);
            pages.push('...');
            for (let i = total - 3; i <= total; i++) {
                pages.push(i);
            }
        } else {
            pages.push(1);
            pages.push('...');
            for (let i = current - 1; i <= current + 1; i++) {
                pages.push(i);
            }
            pages.push('...');
            pages.push(total);
        }
    }
    
    return pages.map(page => {
        if (page === '...') {
            return '<span class="px-3 py-2 text-gray-500">...</span>';
        }
        
        const isActive = page === current;
        return `
            <button onclick="changePage(${page})" 
                    class="px-3 py-2 text-sm font-medium rounded-lg transition-colors duration-200 ${
                        isActive 
                            ? 'bg-indigo-600 text-white' 
                            : 'text-gray-500 bg-white border border-gray-300 hover:bg-gray-50'
                    }">
                ${page}
            </button>
        `;
    }).join('');
}

// Muda página
function changePage(page) {
    currentPage = page;
    displayModernJobs();
    window.scrollTo({ top: jobsContainer.offsetTop - 100, behavior: 'smooth' });
}

// Gera currículo personalizado
async function generateResume(tituloVaga, empresa, descricaoVaga) {
    const button = event.target;
    const originalHTML = button.innerHTML;
    
    try {
        button.disabled = true;
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        
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
        
        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            
            const a = document.createElement('a');
            a.href = url;
            a.download = `curriculo_${empresa.replace(/\s+/g, '_')}.pdf`;
            document.body.appendChild(a);
            a.click();
            
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
            
            button.innerHTML = '<i class="fas fa-check text-green-500"></i>';
            showNotification('Currículo gerado com sucesso!', 'success');
            
            setTimeout(() => {
                button.innerHTML = originalHTML;
                button.disabled = false;
            }, 3000);
        } else {
            const errorData = await response.json();
            showNotification(`Erro ao gerar currículo: ${errorData.erro || 'Erro desconhecido'}`, 'error');
            button.innerHTML = originalHTML;
            button.disabled = false;
        }
    } catch (error) {
        console.error('Erro na requisição:', error);
        showNotification('Erro de conexão ao gerar currículo', 'error');
        button.innerHTML = originalHTML;
        button.disabled = false;
    }
}

// Mostra notificação
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `fixed top-4 right-4 z-50 p-4 rounded-lg shadow-lg transition-all duration-300 transform translate-x-full`;
    
    const colors = {
        success: 'bg-green-500 text-white',
        error: 'bg-red-500 text-white',
        info: 'bg-blue-500 text-white',
        warning: 'bg-yellow-500 text-white'
    };
    
    notification.className += ` ${colors[type]}`;
    notification.innerHTML = `
        <div class="flex items-center">
            <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : type === 'warning' ? 'exclamation-triangle' : 'info-circle'} mr-3"></i>
            <span>${message}</span>
            <button onclick="this.parentElement.parentElement.remove()" class="ml-4 hover:opacity-75">
                <i class="fas fa-times"></i>
            </button>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Anima entrada
    setTimeout(() => {
        notification.classList.remove('translate-x-full');
    }, 100);
    
    // Remove automaticamente após 5 segundos
    setTimeout(() => {
        notification.classList.add('translate-x-full');
        setTimeout(() => {
            if (notification.parentElement) {
                notification.remove();
            }
        }, 300);
    }, 5000);
}

// Adiciona CSS para line-clamp
const style = document.createElement('style');
style.textContent = `
    .line-clamp-2 {
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    
    .line-clamp-3 {
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
`;
document.head.appendChild(style); 