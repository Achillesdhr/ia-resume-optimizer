# Guia de Teste - Comportamento do Botão de Login

## Cenários de Teste

### 1. Estado Inicial (Não Autenticado)

**Comportamento Esperado:**
- ✅ Botão exibe "Login"
- ✅ Clique no botão abre modal de login
- ✅ Botão de upload está **visível mas desabilitado**
- ✅ Mensagem "Faça login para enviar seu currículo" aparece

**Como Testar:**
1. Abra a página sem estar logado
2. Verifique se o botão mostra "Login"
3. Clique no botão e confirme que o modal abre
4. Verifique se o botão de upload está visível mas desabilitado
5. Verifique se a mensagem "Faça login para enviar seu currículo" aparece

### 2. Após Login (Autenticado)

**Comportamento Esperado:**
- ✅ Botão exibe nome do usuário (ou primeira parte do email)
- ✅ Clique no botão NÃO abre modal de login
- ✅ Hover sobre o botão mostra dropdown
- ✅ Dropdown contém informações do usuário
- ✅ Dropdown tem opção de logout
- ✅ Botão de upload está **habilitado e funcional**
- ✅ Mensagem de login necessária foi removida

**Como Testar:**
1. Faça login com uma conta
2. Verifique se o botão mostra o nome do usuário
3. Clique no botão e confirme que NÃO abre modal
4. Passe o mouse sobre o botão e verifique o dropdown
5. Verifique se o dropdown mostra nome e email
6. Verifique se o botão de upload está habilitado
7. Verifique se a mensagem de login foi removida
8. Clique em "Sair" e confirme o logout

### 3. Após Logout

**Comportamento Esperado:**
- ✅ Botão volta a exibir "Login"
- ✅ Clique no botão volta a abrir modal de login
- ✅ Botão de upload volta a ficar **desabilitado**
- ✅ Mensagem "Faça login para enviar seu currículo" volta a aparecer

**Como Testar:**
1. Faça logout
2. Verifique se o botão volta a mostrar "Login"
3. Clique no botão e confirme que o modal abre
4. Verifique se o botão de upload está desabilitado
5. Verifique se a mensagem "Faça login para enviar seu currículo" aparece

### 4. Recarga da Página

**Comportamento Esperado:**
- ✅ Se logado: mantém nome do usuário no botão
- ✅ Se não logado: mantém "Login" no botão
- ✅ Funcionalidade correta após recarga

**Como Testar:**
1. Faça login
2. Recarregue a página (F5)
3. Verifique se o nome do usuário ainda aparece
4. Faça logout e recarregue
5. Verifique se volta a mostrar "Login"

## Verificação no Console

### Logs Esperados

**Ao Fazer Login:**
```
Estado de autenticação alterado: Logado
Token válido para usuário: usuario@email.com
Usuário autenticado: usuario@email.com
```

**Ao Fazer Logout:**
```
Estado de autenticação alterado: Não logado
Usuário não logado
```

**Ao Recarregar Página:**
```
Sistema de autenticação inicializado
Estado de autenticação alterado: Logado (se logado)
```

## Testes de Edge Cases

### 1. Usuário sem displayName
- ✅ Deve usar primeira parte do email
- ✅ Exemplo: "usuario" para "usuario@email.com"

### 2. Usuário com displayName
- ✅ Deve usar displayName completo
- ✅ Exemplo: "João Silva" para usuário com displayName

### 3. Token Expirado
- ✅ Deve fazer logout automático
- ✅ Deve restaurar botão de login
- ✅ Deve mostrar notificação

### 4. Erro de Rede
- ✅ Deve mostrar notificação de erro
- ✅ Deve manter estado anterior se possível

## Comandos de Teste no Console

```javascript
// Verificar estado atual
console.log('Usuário logado:', currentUser);
console.log('Token válido:', userToken);

// Simular logout (para testes)
handleLogout();

// Verificar interface
const loginBtn = document.getElementById('loginBtn');
console.log('Texto do botão:', loginBtn.textContent);
console.log('Event listener:', loginBtn.onclick);
```

## Checklist de Validação

### ✅ Funcionalidades Básicas
- [ ] Botão mostra "Login" quando não autenticado
- [ ] Botão mostra nome do usuário quando autenticado
- [ ] Clique abre modal apenas quando não autenticado
- [ ] Dropdown aparece no hover quando autenticado
- [ ] Logout funciona corretamente

### ✅ Botão de Upload
- [ ] Botão sempre visível (não oculto)
- [ ] Botão desabilitado quando não autenticado
- [ ] Botão habilitado quando autenticado
- [ ] Mensagem informativa aparece quando não autenticado
- [ ] Mensagem é removida quando autenticado
- [ ] Aparência visual correta (opacidade, cursor)
- [ ] Animações funcionam corretamente

### ✅ Estados de Transição
- [ ] Login remove event listener
- [ ] Logout restaura event listener
- [ ] Recarga mantém estado correto
- [ ] Token expirado faz logout automático

### ✅ Interface Visual
- [ ] Dropdown tem estilo correto
- [ ] Informações do usuário são exibidas
- [ ] Opção de logout está presente
- [ ] Animações funcionam suavemente

### ✅ Tratamento de Erros
- [ ] Erros de rede são tratados
- [ ] Tokens inválidos são detectados
- [ ] Notificações são exibidas
- [ ] Estado é mantido consistente 