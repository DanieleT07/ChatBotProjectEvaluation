const API_URL = 'http://localhost:8000';
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const clearButton = document.getElementById('clear-button');
const sidebar = document.getElementById('sidebar');
const sidebarToggle = document.getElementById('sidebar-toggle');
const contextContent = document.getElementById('context-content');
const mainContent = document.querySelector('.main-content');

// Configure marked options
marked.setOptions({
    gfm: true,
    breaks: true,
    headerIds: true,
    mangle: false,
    sanitize: false,
    smartLists: true,
    smartypants: true,
    xhtml: false
});

// Handle clicks outside sidebar to close it
document.addEventListener('click', (e) => {
    if (!sidebar.contains(e.target) && 
        !sidebarToggle.contains(e.target) && 
        sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
        mainContent.classList.remove('sidebar-open');
    }
});

// Sidebar toggle functionality
sidebarToggle.addEventListener('click', (e) => {
    e.stopPropagation(); // Prevent document click handler
    sidebar.classList.toggle('open');
    mainContent.classList.toggle('sidebar-open');
});

function addMessage(message, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message${isUser ? ' user' : ''}`;
    
    const headerDiv = document.createElement('div');
    headerDiv.className = 'message-header';
    headerDiv.innerHTML = `
        <div class="message-avatar"></div>
        <span>${isUser ? 'You' : 'Assistant'}</span>
    `;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'markdown-body';
    contentDiv.innerHTML = marked.parse(message);
    
    messageDiv.appendChild(headerDiv);
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    messageDiv.scrollIntoView({ behavior: 'smooth', block: 'end' });
}

function addLoadingMessage() {
    const loadingDiv = document.createElement('div');
    loadingDiv.id = 'loading-message';
    loadingDiv.className = 'message';
    loadingDiv.innerHTML = `
        <div class="message-header">
            <div class="message-avatar"></div>
            <span>Assistant</span>
        </div>
        <div class="loading-dots">
            <div></div>
            <div></div>
            <div></div>
        </div>
    `;
    chatMessages.appendChild(loadingDiv);
    loadingDiv.scrollIntoView({ behavior: 'smooth', block: 'end' });
}

function removeLoadingMessage() {
    const loadingMessage = document.getElementById('loading-message');
    if (loadingMessage) {
        loadingMessage.remove();
    }
}

function showContext(context) {
    if (context && context.length > 0) {
        contextContent.innerHTML = context.map(c => `
            <div style="margin-bottom: 16px; padding: 8px; background: var(--color-canvas-subtle); border-radius: 6px;">
                ${marked.parse(c)}
            </div>
        `).join('');
        sidebar.classList.add('open');
        mainContent.classList.add('sidebar-open');
    }
}

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    userInput.disabled = true;
    sendButton.disabled = true;

    addMessage(message, true);
    userInput.value = '';
    addLoadingMessage();

    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                clear_history: false
            })
        });

        const data = await response.json();
        
        removeLoadingMessage();
        addMessage(data.response);
        showContext(data.context);
    } catch (error) {
        removeLoadingMessage();
        addMessage('Error: Unable to get response from server');
        console.error('Error:', error);
    }

    userInput.disabled = false;
    sendButton.disabled = false;
    userInput.focus();
}

async function clearChat() {
    while (chatMessages.children.length > 1) {
        chatMessages.removeChild(chatMessages.lastChild);
    }
    
    sidebar.classList.remove('open');
    mainContent.classList.remove('sidebar-open');
    contextContent.innerHTML = '';
    userInput.value = '';
    
    try {
        await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: '',
                clear_history: true
            })
        });
    } catch (error) {
        console.error('Error clearing history:', error);
        addMessage('Error: Unable to clear chat history');
    }
}

// Event Listeners
sendButton.addEventListener('click', sendMessage);
clearButton.addEventListener('click', clearChat);

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// Prevent sidebar from closing when clicking inside it
sidebar.addEventListener('click', (e) => {
    e.stopPropagation();
});

// Focus input on page load
userInput.focus();

// Handle window resize
window.addEventListener('resize', () => {
    if (window.innerWidth <= 768) {
        sidebar.classList.remove('open');
        mainContent.classList.remove('sidebar-open');
    }
});

// Error handling for network issues
window.addEventListener('online', () => {
    addMessage('Connection restored');
});

window.addEventListener('offline', () => {
    addMessage('Connection lost. Please check your internet connection.');
});