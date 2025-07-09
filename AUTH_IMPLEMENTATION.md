# Implementação de Autenticação com Firebase

## Visão Geral

Esta implementação fornece um sistema completo de autenticação usando Firebase Authentication, incluindo validação de token, refresh automático e gerenciamento de estado do usuário.

## Funcionalidades Implementadas

### 1. Validação do Usuário Autenticado

- **`validateUserToken(user)`**: Valida o token do usuário usando `currentUser.getIdToken(true)`
- Verifica se o token não expirou comparando com o tempo atual
- Automaticamente faz logout se o token for inválido ou expirado
- Retorna `true` se o token for válido, `false` caso contrário

### 2. Atualização Dinâmica do Botão de Login

- **Interface do usuário logado**: Exibe o nome do usuário em um dropdown elegante
- **Fallback para email**: Se `displayName` estiver vazio, usa a primeira parte do email
- **Dropdown com informações**: Mostra nome completo, email e opção de logout
- **Interface responsiva**: Funciona bem em dispositivos móveis e desktop

### 3. Sistema de Logout

- **Botão de logout**: Integrado no dropdown do usuário
- **Limpeza de estado**: Remove tokens e timers ao fazer logout
- **Feedback visual**: Notificações informativas durante o processo

### 4. Comportamento na Recarga da Página

- **Persistência de sessão**: Mantém o usuário logado após recarregar
- **Validação automática**: Verifica token ao carregar a página
- **Interface consistente**: Restaura o estado correto da interface

## Estrutura de Arquivos

```
static/js/
├── auth.js          # Lógica principal de autenticação
└── app.js           # Outras funcionalidades da aplicação

templates/
└── index.html       # Template principal com modais e estrutura
```

## Componentes Principais

### Firebase Configuration
```javascript
const firebaseConfig = {
    apiKey: "AIzaSyCRM3sURZj8RyqDaR9r20i2RLE3lqg_qqE",
    authDomain: "jobmatchia.firebaseapp.com",
    projectId: "jobmatchia",
    // ... outras configurações
};
```

### Validação de Token
```javascript
async function validateUserToken(user) {
    try {
        const token = await user.getIdToken(true); // Força refresh
        const decodedToken = await user.getIdTokenResult();
        
        // Verifica expiração
        const currentTime = Date.now() / 1000;
        if (decodedToken.expirationTime < currentTime) {
            await auth.signOut();
            return false;
        }
        
        return true;
    } catch (error) {
        // Tratamento de erros
        return false;
    }
}
```

### Refresh Automático de Token
```javascript
function setupTokenRefresh(user) {
    const tokenRefreshInterval = 55 * 60 * 1000; // 55 minutos
    
    tokenRefreshTimer = setTimeout(async () => {
        await user.getIdToken(true);
        setupTokenRefresh(user); // Recursivo
    }, tokenRefreshInterval);
}
```

### Atualização da Interface
```javascript
function updateUserInterface(user) {
    if (user) {
        // Usuário logado - alterar comportamento do botão
        const displayName = user.displayName || user.email.split('@')[0];
        
        // Remover event listener anterior
        loginBtn.onclick = null;
        
        // Alterar texto e comportamento do botão
        // Cria dropdown com nome e opções
    } else {
        // Usuário não logado - restaurar botão de login original
        // Restaurar event listener para abrir modal
        loginBtn.onclick = openLoginModal;
    }
}
```

## Estados de Autenticação

### Usuário Não Logado
- Botão "Login" visível
- Botão de upload **visível mas desabilitado**
- Mensagem informativa sobre necessidade de login
- Modais de login/cadastro funcionais

### Usuário Logado
- **Botão alterado**: Remove event listener de login, exibe nome do usuário
- **Dropdown com informações**: Nome completo, email e opção de logout
- **Menu de logout**: Integrado no dropdown do usuário
- **Botão de upload habilitado**: Funcional para usuários autenticados
- **Mensagem removida**: Informação de login necessária é removida
- **Token validado**: Renovado automaticamente

## Comportamento do Botão de Login

### Estado Não Autenticado
- **Texto**: "Login"
- **Event Listener**: `onclick = openLoginModal`
- **Funcionalidade**: Abre modal de login ao clicar

### Estado Autenticado
- **Texto**: Nome do usuário (ou primeira parte do email)
- **Event Listener**: Removido (`onclick = null`)
- **Funcionalidade**: Dropdown com informações do usuário
- **Menu**: Opção de logout integrada

### Transições
- **Login**: Remove event listener, altera texto, adiciona dropdown, habilita upload
- **Logout**: Restaura event listener, restaura texto original, desabilita upload

## Comportamento do Botão de Upload

### Estado Não Autenticado
- **Visibilidade**: Botão sempre visível
- **Estado**: Desabilitado (`disabled = true`)
- **Aparência**: Opacidade reduzida, cursor not-allowed
- **Mensagem**: "Faça login para enviar seu currículo"
- **Funcionalidade**: Clique não executa ação

### Estado Autenticado
- **Visibilidade**: Botão sempre visível
- **Estado**: Habilitado (`disabled = false`)
- **Aparência**: Opacidade normal, cursor pointer, animação pulse
- **Mensagem**: Removida automaticamente
- **Funcionalidade**: Clique executa upload (quando implementado)

### Transições de Estado
- **Login**: Desabilita → Habilita, adiciona animação, remove mensagem
- **Logout**: Habilita → Desabilita, remove animação, adiciona mensagem

## Event Listeners

### Auth State Changes
```javascript
auth.onAuthStateChanged(async (user) => {
    if (user) {
        const isTokenValid = await validateUserToken(user);
        if (isTokenValid) {
            // Configurar interface e refresh
        }
    } else {
        // Limpar estado e interface
    }
});
```

### Modal Management
- Clique fora para fechar
- Tecla ESC para fechar
- Transições suaves

## Funcionalidades de Segurança

### Validação de Token
- Verificação de expiração
- Refresh automático
- Logout automático em caso de token inválido

### Validação de Formulários
- Validação de email
- Verificação de senha
- Confirmação de senha
- Validação de campos obrigatórios

### Tratamento de Erros
- Mensagens específicas para cada tipo de erro
- Notificações visuais
- Logs detalhados no console

## CSS Customizado

### Dropdown Styles
```css
.user-dropdown {
    position: relative;
}

.dropdown-menu {
    position: absolute;
    opacity: 0;
    visibility: hidden;
    transition: all 0.2s ease;
}

.user-dropdown:hover .dropdown-menu {
    opacity: 1;
    visibility: visible;
}
```

## Como Usar

### 1. Incluir Scripts
```html
<!-- Firebase SDK -->
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-auth-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore-compat.js"></script>

<!-- Auth Script -->
<script src="{{ url_for('static', filename='js/auth.js') }}"></script>
```

### 2. Estrutura HTML Necessária
```html
<!-- Botão de login -->
<button id="loginBtn" onclick="openLoginModal()">Login</button>

<!-- Modais de login/cadastro -->
<div id="loginModal" class="modal-overlay">
    <!-- Conteúdo do modal -->
</div>

<div id="registerModal" class="modal-overlay">
    <!-- Conteúdo do modal -->
</div>
```

### 3. Verificar Estado do Usuário
```javascript
// Verificar se usuário está logado
if (currentUser) {
    // Usuário logado
    console.log('Usuário:', currentUser.email);
} else {
    // Usuário não logado
    console.log('Nenhum usuário logado');
}

// Verificar token
if (userToken) {
    // Token válido
    console.log('Token disponível');
} else {
    // Sem token
    console.log('Token não disponível');
}
```

## Logs e Debug

O sistema inclui logs detalhados para debug:
- Estado de autenticação
- Validação de token
- Refresh automático
- Erros de autenticação

## Considerações de Performance

- Refresh de token 5 minutos antes da expiração
- Limpeza automática de timers
- Validação assíncrona
- Interface responsiva

## Próximos Passos

1. Implementar upload de arquivos com validação de token
2. Adicionar mais provedores de autenticação
3. Implementar recuperação de senha
4. Adicionar verificação de email
5. Implementar roles e permissões 