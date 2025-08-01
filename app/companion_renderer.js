// =============================================================================
// SECTION A: FIREBASE & AUTHENTICATION (The Security Guard)
// =============================================================================
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js";

// --- Crucial Preload Script Check ---
if (!window.electronAPI) {
    throw new Error("FATAL: The 'electronAPI' object is not available. The preload script may have failed to run.");
}

// --- Initialize Firebase to get the auth context ---
const firebaseConfig = window.electronAPI.firebaseConfig;
if (!firebaseConfig || !firebaseConfig.apiKey) {
    throw new Error("FATAL: Firebase configuration is missing or invalid.");
}
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);


// --- Authentication Gatekeeper ---
onAuthStateChanged(auth, (user) => {
    if (user) {
        console.log(`[Companion Renderer] Auth state confirmed for user: ${user.uid}`);
        initializeAppUI(user);
    } else {
        console.error("[Companion Renderer] No authenticated user found. Redirecting to login.");
        window.electronAPI.returnToLogin();
    }
});


// =============================================================================
// SECTION B: MAIN APPLICATION UI INITIALIZATION
// =============================================================================

function initializeAppUI(authUser) {

    // =========================================================================
    // SECTION 1: GLOBAL STATE & ELEMENT REFERENCES
    // =========================================================================
    let currentUser = {
        uid: authUser.uid,
        name: authUser.displayName,
        email: authUser.email,
        tokens: 'Loading...'
    };

    let selectedFilesStore = {};
    let ephemeralChatFiles = [];

    const pageTitle = document.getElementById('pageTitle');
    const statusMessage = document.getElementById('statusMessage');
    const loadingIndicator = document.getElementById('loadingIndicator');

    // =========================================================================
    // SECTION 2: CORE APP INITIALIZATION & HELPERS
    // =========================================================================

    function initialize() {
        log('info', `Initializing app for user: ${currentUser.name}`);
        setupNavigation();
        setupDashboard();
        setupToolbox(); // CHANGED: Added handler for the toolbox button
        setupFileFeatures();
        setupImageStudio();
        setupFileManagement();
        setupWebScrapers();
        setupChatbot();
        // REMOVED: setupChatbotManager(); - No longer needed
        setupHelp();
        document.querySelectorAll('.output-shortcut').forEach(btn => {
            btn.addEventListener('click', () => {
                log('info', "User clicked output folder shortcut icon");
                window.electronAPI.openOutputFolder();
            });
        });
        window.electronAPI.onScriptReply(handleScriptReply);
        log('info', 'App initialized and all event listeners are active.');
    }

    const log = (level, message, data = '') => {
        const logData = data ? JSON.stringify(data) : '';
        window.electronAPI.log(level, `${message} ${logData}`);
    };
    function showLoading(show) {
        loadingIndicator.classList.toggle('hidden', !show);
    }
    function showStatus(message, isError = false, duration = 4000) {
        statusMessage.textContent = message;
        statusMessage.className = isError ? 'status-error' : 'status-success';
        statusMessage.classList.remove('hidden');
        setTimeout(() => statusMessage.classList.add('hidden'), duration);
    }

    // =========================================================================
    // SECTION 3: NAVIGATION
    // =========================================================================
    function setupNavigation() {
        const navContainer = document.querySelector('.nav-items');
        navContainer.addEventListener('click', (event) => {
            const navItem = event.target.closest('.nav-item');
            if (navItem && navItem.classList.contains('nav-toggle')) {
                event.preventDefault();
                const category = navItem.closest('.nav-category');
                category.classList.toggle('open');
                return;
            }
            if (navItem && navItem.dataset.view) {
                // REMOVED: Logic to handle chatbotManager view
                if (navItem.dataset.view === 'chatbotManager') {
                    return; // Do nothing for the old button
                }
                document.querySelectorAll('.nav-item').forEach(link => link.classList.remove('active'));
                navItem.classList.add('active');
                if (navItem.classList.contains('sub-item')) {
                    navItem.closest('.nav-category').querySelector('.nav-toggle').classList.add('active');
                }
                showView(navItem.dataset.view, navItem.dataset.title);
            }
        });
    }

    function showView(viewId, title) {
        log('info', `Switching view to: ${viewId}`);
        document.querySelectorAll('.view-section').forEach(section => {
    section.classList.remove('active');
    section.classList.add('hidden'); // Ensure all sections are hidden first
});

const viewToShow = (viewId === 'imageGeneration' || viewId === 'imageConversions') ? 'aiImageStudio' : viewId;
const activeView = document.getElementById(viewToShow + 'View');

if (activeView) {
    activeView.classList.remove('hidden'); // Explicitly remove hidden class
    activeView.classList.add('active');   // Add active class to display it
    pageTitle.textContent = title;
} else {
    log('error', `View section not found for ID: ${viewToShow + 'View'}`);
}
    }

    // =========================================================================
    // SECTION 4: FEATURE SETUP
    // =========================================================================
    async function setupDashboard() {
        const outputPathSpan = document.getElementById('outputPath');
        const tokenCountSpan = document.getElementById('tokenCount');
        outputPathSpan.textContent = await window.electronAPI.getOutputPath();
        const userTokens = sessionStorage.getItem('userTokens');
        if (userTokens) {
            currentUser.tokens = userTokens;
            tokenCountSpan.textContent = userTokens;
        } else {
            log('warn', 'Could not find userTokens in sessionStorage.');
            tokenCountSpan.textContent = 'N/A';
        }
        document.getElementById('openOutputFolderBtn').addEventListener('click', () => window.electronAPI.openOutputFolder());
        document.getElementById('changeOutputBtn').addEventListener('click', () => window.electronAPI.changeOutputFolder());
        document.getElementById('resetOutputBtn').addEventListener('click', () => window.electronAPI.resetOutputFolder());
        document.getElementById('shredNowBtn').addEventListener('click', async () => {
            const currentPath = await window.electronAPI.getOutputPath();
            const confirmed = await window.electronAPI.showConfirmDialog({
                title: 'Confirm Shred',
                message: `Are you sure you want to permanently delete everything inside:\n${currentPath}`,
            });
            if (confirmed) {
                showLoading(true);
                window.electronAPI.runScript({ functionName: 'shred_folder', payload: { folder_path: currentPath } });
            }
        });
        window.electronAPI.onOutputPathChanged(newPath => {
            outputPathSpan.textContent = newPath;
            showStatus(`Output path changed to: ${newPath}`);
        });

        // CHANGED: Moved Knowledge Base logic from chatbotManager to here
        const addToKnowledgeBtn = document.getElementById('addToKnowledgeBtn');
        const clearKnowledgeBtn = document.getElementById('clearKnowledgeBtn');

        async function addFilesToKnowledgeBase() {
            // Only allow markdown files
            const files = await window.electronAPI.selectFiles({ 
                properties: ['openFile', 'multiSelections'], 
                title: 'Add to Knowledge Base', 
                filters: [{ name: 'Markdown', extensions: ['md'] }] 
            });
            if (files && files.length > 0) {
                showLoading(true);
                window.electronAPI.runScript({ functionName: 'manage_chatbot_files', payload: { uid: currentUser.uid, action: 'save', files: files } });
            }
        }
        async function clearKnowledgeBase() {
            const confirmed = await window.electronAPI.showConfirmDialog({ title: 'Confirm Deletion', message: 'Are you sure you want to delete all files from your permanent knowledge repository?' });
            if (confirmed) {
                showLoading(true);
                window.electronAPI.runScript({ functionName: 'manage_chatbot_files', payload: { uid: currentUser.uid, action: 'delete_all' } });
            }
        }

        if(addToKnowledgeBtn) addToKnowledgeBtn.addEventListener('click', addFilesToKnowledgeBase);
        if(clearKnowledgeBtn) clearKnowledgeBtn.addEventListener('click', clearKnowledgeBase);
        
        // Refresh knowledge files list when dashboard is shown
        refreshKnowledgeFiles();
    }

    // CHANGED: Added function to handle the toolbox button
    function setupToolbox() {
        // This assumes you have a button with id="toolboxBtn" in your index.html
        const toolboxBtn = document.getElementById('toolboxBtn');
        if (toolboxBtn) {
            toolboxBtn.addEventListener('click', () => {
                // Assuming the toolbox view has an id of "toolboxView"
                showView('toolbox', 'Toolbox'); 
            });
        }
    }


    function setupFileFeatures() {
        const fileFeatures = [
            { key: 'pdf', select: 'selectPdfBtn', display: 'selectedPdfPaths', action: 'convertPdfBtn', format: 'outputFormatSelect', func: 'convert_pdf' },
            { key: 'image', select: 'selectImageBtn', display: 'selectedImagePaths', action: 'convertImageBtn', format: 'outputFormatImageSelect', func: 'convert_image' },
            { key: 'json', select: 'selectJsonBtn', display: 'selectedJsonPaths', action: 'convertJsonBtn', format: 'jsonOutputFormatSelect', func: 'convert_json' },
            { key: 'markdown', select: 'selectMarkdownBtn', display: 'selectedMarkdownPaths', action: 'convertMarkdownBtn', format: 'markdownOutputFormatSelect', func: 'convert_markdown' },
        ];
        fileFeatures.forEach(f => {
            setupFileSelectionLogic(f.select, f.display, f.action, f.key);
            setupConversionButton(f.action, f.key, f.format, f.func);
        });
    }

    function setupFileSelectionLogic(selectBtnId, pathDisplayId, actionBtnId, fileTypeKey) {
        const selectBtn = document.getElementById(selectBtnId);
        selectBtn.addEventListener('click', async () => {
            const files = await window.electronAPI.selectFiles({ properties: ['openFile', 'multiSelections'] });
            if (files && files.length > 0) {
                selectedFilesStore[fileTypeKey] = files;
                document.getElementById(pathDisplayId).textContent = `Selected files: ${files.length}`;
                document.getElementById(actionBtnId).disabled = false;
            }
        });
    }

    function setupConversionButton(actionBtnId, fileTypeKey, formatSelectId, funcName) {
        document.getElementById(actionBtnId).addEventListener('click', async () => {
            const files = selectedFilesStore[fileTypeKey];
            const format = document.getElementById(formatSelectId).value;
            if (!files || files.length === 0) {
                showStatus('No files selected.', true);
                return;
            }
            if (funcName === 'convert_pdf' || files.length > 5) {
                const confirmed = await window.electronAPI.showConfirmDialog({
                    title: 'Large Task Warning',
                    message: `You are about to process ${files.length} file(s). This may take some time.`,
                    detail: 'The application may be unresponsive during this period. Please wait for it to complete.'
                });
                if (!confirmed) return;
            }
            
            showLoading(true);
            const payload = { files, format };
            if (fileTypeKey === 'image') {
                payload.width = document.getElementById('resizeWidth').value || null;
                payload.height = document.getElementById('resizeHeight').value || null;
                payload.preserve_aspect = document.getElementById('preserveAspect').checked;
            }
            window.electronAPI.runScript({ functionName: funcName, payload: payload });
        });
    }

    function setupImageStudio() {
        const toolCards = document.querySelectorAll('#aiImageStudioView .tool-card');
        const dynamicControls = document.getElementById('dynamic-controls-area');
        const toolTitle = document.getElementById('tool-title');
        const toolInstructions = document.getElementById('tool-instructions');
        const textInputContainer = document.getElementById('text-input-container');
        const imageInputContainer = document.getElementById('image-input-container');
        const runAiToolBtn = document.getElementById('runAiToolBtn');
        const selectAiImageBtn = document.getElementById('selectAiImageBtn');
        const selectedAiImagePath = document.getElementById('selectedAiImagePath');
        const generatedImage = document.getElementById('generatedImage');
        const imagePromptInput = document.getElementById('imagePromptInput');

        let activeTool = null;
        let selectedImagePath = null;

        const toolConfig = {
            'text2img': { title: 'Text to Image', instructions: 'Enter a descriptive prompt.', needsText: true, needsImage: false },
            'ghibli-style': { title: 'Animation Style', instructions: 'Enter a prompt to create an animation-style image.', needsText: true, needsImage: false },
            'toonify': { title: 'Toonify', instructions: 'Select an image to turn it into a cartoon.', needsText: false, needsImage: true },
            'image-editor': { title: 'AI Photo Editor', instructions: 'Select an image and provide instructions on how to edit it.', needsText: true, needsImage: true },
            'torch-srgan': { title: 'Super Resolution', instructions: 'Select a low-resolution image to upscale.', needsText: false, needsImage: true },
            'waifu2x': { title: 'Premium Upscaler', instructions: 'Select an anime-style image to upscale.', needsText: false, needsImage: true },
            'background-remover': { title: 'Background Remover', instructions: 'Select an image to remove the background.', needsText: false, needsImage: true }
        };

        document.querySelectorAll('#aiImageStudioView .tab-link').forEach(tab => {
            tab.addEventListener('click', () => {
                document.querySelectorAll('#aiImageStudioView .tab-link, #aiImageStudioView .studio-tab-content').forEach(el => el.classList.remove('active'));
                tab.classList.add('active');
                document.getElementById(tab.dataset.tab).classList.add('active');
            });
        });

        toolCards.forEach(card => {
            card.addEventListener('click', () => {
                toolCards.forEach(c => c.classList.remove('active'));
                card.classList.add('active');
                activeTool = card.dataset.tool;
                selectedImagePath = null;
                selectedAiImagePath.textContent = 'No file selected.';
                const config = toolConfig[activeTool];
                toolTitle.textContent = config.title;
                toolInstructions.textContent = config.instructions;
                textInputContainer.classList.toggle('hidden', !config.needsText);
                imageInputContainer.classList.toggle('hidden', !config.needsImage);
                dynamicControls.classList.remove('hidden');
            });
        });

        selectAiImageBtn.addEventListener('click', async () => {
            const files = await window.electronAPI.selectFiles({ properties: ['openFile'] });
            if (files && files.length > 0) {
                selectedImagePath = files[0];
                selectedAiImagePath.textContent = selectedImagePath.split(/[\\/]/).pop();
            }
        });

        runAiToolBtn.addEventListener('click', () => {
            if (!activeTool) return;
            const config = toolConfig[activeTool];
            const payload = {};
            if (config.needsText) {
                const prompt = imagePromptInput.value.trim();
                if (!prompt) { showStatus('Please enter a prompt or instruction.', true); return; }
                payload.text = prompt;
            }
            if (config.needsImage) {
                if (!selectedImagePath) { showStatus('Please select an image file.', true); return; }
                payload.image = selectedImagePath;
            }
            showLoading(true);
            imageResultContainer.querySelector('span').textContent = 'Generating...';
            generatedImage.classList.add('hidden');
            window.electronAPI.runScript({ functionName: 'generate_image', payload: { type: activeTool, params: payload } });
        });
    }

    function setupFileManagement() {
        setupFileSelectionLogic('selectMergeFilesBtn', 'selectedMergePaths', 'mergeFilesBtn', 'merge');
        document.getElementById('mergeFilesBtn').addEventListener('click', async () => {
            const files = selectedFilesStore['merge'];
            if (!files || files.length === 0) { showStatus('No files selected for merging.', true); return; }
            if (document.querySelector('input[name="mergeMode"]:checked').value === 'with_contents') {
                const confirmed = await window.electronAPI.showConfirmDialog({ title: 'AI-Powered Merge Cost', message: 'This action uses AI and will use tokens. Proceed?' });
                if (!confirmed) return;
            }
            showLoading(true);
            window.electronAPI.runScript({ functionName: 'merge_files', payload: { files, mode: document.querySelector('input[name="mergeMode"]:checked').value } });
        });

        setupFileSelectionLogic('selectShredFilesBtn', 'selectedShredPaths', 'shredFilesBtn', 'shred');
        document.getElementById('shredFilesBtn').addEventListener('click', async () => {
            const files = selectedFilesStore['shred'];
            if (!files || files.length === 0) { showStatus('No files selected for shredding.', true); return; }
            const confirmed = await window.electronAPI.showConfirmDialog({ title: 'Confirm Shred', message: `Permanently shred ${files.length} selected file(s)? This cannot be undone.` });
            if (confirmed) {
                showLoading(true);
                window.electronAPI.runScript({ functionName: 'shred_files', payload: { files } });
            }
        });
        document.getElementById('shredFolderBtn').addEventListener('click', async () => {
            const folderPath = await window.electronAPI.selectFolder();
            if (folderPath) {
                const confirmed = await window.electronAPI.showConfirmDialog({ title: 'Confirm Shred', message: `Permanently shred the entire folder?\n${folderPath}\nThis cannot be undone.` });
                if (confirmed) {
                    showLoading(true);
                    window.electronAPI.runScript({ functionName: 'shred_folder', payload: { folder_path: folderPath } });
                }
            }
        });
    }

    function setupWebScrapers() {
        document.getElementById('scrapeSinglePageBtn').addEventListener('click', () => { /* ... */ });
        document.getElementById('scrapeSitemapBtn').addEventListener('click', () => { /* ... */ });
        document.getElementById('downloadFilesBtn').addEventListener('click', () => { /* ... */ });
        document.getElementById('downloadFromSitemapBtn').addEventListener('click', () => { /* ... */ });
    }

    function setupChatbot() {
        let ephemeralChatFiles = [];
        let canvasFiles = [];
        const sendMessageBtn = document.getElementById('sendMessageBtn');
        const chatInput = document.getElementById('chatInput');
        const attachFileBtn = document.getElementById('attachFileBtn');
        const clearEphemeralFilesBtn = document.getElementById('clearEphemeralFilesBtn');
        const addToCanvasBtn = document.getElementById('addToCanvasBtn');
        const clearCanvasBtn = document.getElementById('clearCanvasBtn');
        const canvasFilesList = document.getElementById('canvas-files-list');
        const allowedFileTypes = { name: 'Text & Code Files', extensions: ['txt', 'md', 'py', 'js', 'html', 'css', 'json', 'xml'] };

        function sendMessage() {
            const message = chatInput.value.trim();
            if (!message && ephemeralChatFiles.length === 0) return;
            appendMessageToChat('user', message || "Analyzing file(s)...");
            chatInput.value = '';
            showLoading(true);
            window.electronAPI.runScript({
                functionName: 'chatbot_request',
                payload: {
                    uid: currentUser.uid, message: message,
                    attached_files: ephemeralChatFiles, canvas_files: canvasFiles.map(f => f.path),
                    // REMOVED: personality has been removed from the call
                }
            });
            clearEphemeralFileList();
        }
        async function addFilesToCanvas() {
            const files = await window.electronAPI.selectFiles({ properties: ['openFile', 'multiSelections'], title: 'Add Files to Focus Canvas', filters: [allowedFileTypes] });
            if (files) {
                files.forEach(path => {
                    if (!canvasFiles.some(f => f.path === path)) canvasFiles.push({ path: path, name: path.split(/[\\/]/).pop() });
                });
                renderCanvasFiles();
            }
        }
        function renderCanvasFiles() {
            canvasFilesList.innerHTML = '';
            if (canvasFiles.length === 0) {
                canvasFilesList.innerHTML = '<p style="font-size: 12px; color: #888;">No files in canvas.</p>';
            } else {
                canvasFiles.forEach(file => {
                    const item = document.createElement('div');
                    item.className = 'knowledge-file-item';
                    item.textContent = file.name;
                    const deleteBtn = document.createElement('button');
                    deleteBtn.className = 'delete-knowledge-file-btn';
                    deleteBtn.textContent = '×';
                    deleteBtn.onclick = () => {
                        canvasFiles = canvasFiles.filter(f => f.path !== file.path);
                        renderCanvasFiles();
                    };
                    item.appendChild(deleteBtn);
                    canvasFilesList.appendChild(item);
                });
            }
        }
        function clearCanvas() { canvasFiles = []; renderCanvasFiles(); }
        async function attachChatFile() {
            const files = await window.electronAPI.selectFiles({ properties: ['openFile', 'multiSelections'], title: 'Attach Files to this Message', filters: [allowedFileTypes] });
            if (files) { ephemeralChatFiles.push(...files); updateEphemeralFilesDisplay(); }
        }
        function updateEphemeralFilesDisplay() {
            const list = document.getElementById('ephemeral-files-list');
            document.getElementById('ephemeral-files-display').classList.toggle('hidden', ephemeralChatFiles.length === 0);
            list.textContent = ephemeralChatFiles.map(f => f.split(/[\\/]/).pop()).join(', ');
        }
        function clearEphemeralFileList() { ephemeralChatFiles = []; updateEphemeralFilesDisplay(); }
        
        sendMessageBtn.addEventListener('click', sendMessage);
        chatInput.addEventListener('keypress', (e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); } });
        document.getElementById('clearChatHistoryBtn').addEventListener('click', () => {
            showLoading(true);
            window.electronAPI.runScript({ functionName: 'clear_chat_history', payload: { uid: currentUser.uid } });
        });
        addToCanvasBtn.addEventListener('click', addFilesToCanvas);
        clearCanvasBtn.addEventListener('click', clearCanvas);
        attachFileBtn.addEventListener('click', attachChatFile);
        clearEphemeralFilesBtn.addEventListener('click', clearEphemeralFileList);
        renderCanvasFiles();
    }
    
    // REMOVED: function setupChatbotManager() - This entire function is no longer needed
    
    function setupHelp() {
        document.getElementById('supportEmailBtn').addEventListener('click', () => window.electronAPI.openExternalLink('mailto:support@example.com'));
        document.getElementById('privacyEmailBtn').addEventListener('click', () => window.electronAPI.openExternalLink('mailto:privacy@example.com'));
    }

    // --- SHARED HELPER FUNCTIONS ---
    function appendMessageToChat(role, content) {
        const messagesDiv = document.getElementById('chatMessages');
        // CHANGED: Keep user scroll position unless they are at the bottom
        const isScrolledToBottom = messagesDiv.scrollHeight - messagesDiv.clientHeight <= messagesDiv.scrollTop + 1;

        const messageElement = document.createElement('div');
        messageElement.classList.add('chat-message', `${role}-message`);
        messageElement.innerHTML = window.marked.parse(content);
        messagesDiv.appendChild(messageElement);

        if (isScrolledToBottom) {
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }
    }

    function renderChatHistory(history) {
        const messagesDiv = document.getElementById('chatMessages');
        messagesDiv.innerHTML = '';
        if (!history || history.length === 0) {
            appendMessageToChat('assistant', 'Meet Gemma! Your built-in AI helper.');
        } else {
            history.forEach(msg => appendMessageToChat(msg.role, msg.content));
        }
    }

    function refreshKnowledgeFiles() {
        window.electronAPI.runScript({ functionName: 'list_chatbot_files', payload: { uid: currentUser.uid } });
    }

    function renderKnowledgeFiles(files) {
        // CHANGED: Now renders in the dashboard, not a separate manager view
        const listDiv = document.getElementById('dashboard-knowledge-files-list'); // Assumes this ID exists in the dashboard view
        if (!listDiv) return;

        listDiv.innerHTML = '';
        if (!files || files.length === 0) {
            listDiv.innerHTML = '<p style="font-size: 12px; color: #888;">No knowledge files uploaded.</p>';
            return;
        }
        files.forEach(file => {
            const item = document.createElement('div');
            item.className = 'knowledge-file-item';
            item.textContent = file;
            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-knowledge-file-btn';
            deleteBtn.textContent = '×';
            deleteBtn.onclick = async () => {
                const confirmed = await window.electronAPI.showConfirmDialog({ title: 'Confirm Deletion', message: `Are you sure you want to delete ${file} from your knowledge base?`});
                if (confirmed) {
                    showLoading(true);
                    window.electronAPI.runScript({ functionName: 'manage_chatbot_files', payload: { uid: currentUser.uid, action: 'delete_one', files: [file] } });
                }
            };
            item.appendChild(deleteBtn);
            listDiv.appendChild(item);
        });
    }

    // =========================================================================
    // SECTION 5: CENTRAL SCRIPT REPLY HANDLER
    // =========================================================================
    function handleScriptReply(reply) {
        showLoading(false);
        const { source, success, data, error } = reply;
        if (!success) {
            log('error', `Error from '${source}':`, error);
            if (source === 'chatbot_request') {
                appendMessageToChat('bot-error', `Backend Error: ${error}`);
            } else {
                showStatus(`Error during ${source}: ${error}`, true);
            }
            return;
        }
        let jsonData = {};
        try { jsonData = JSON.parse(data); } catch (e) { jsonData = { message: data }; }
        if (jsonData.tokens_used) {
            const tokenCountSpan = document.getElementById('tokenCount');
            const newBalance = parseFloat(tokenCountSpan.textContent) - jsonData.tokens_used;
            tokenCountSpan.textContent = newBalance.toFixed(4);
            currentUser.tokens = newBalance;
        }
        switch (source) {
            case 'chatbot_request':
                if (Array.isArray(jsonData.history)) renderChatHistory(jsonData.history);
                else if (jsonData.error) appendMessageToChat('bot-error', `API Error: ${jsonData.error}`);
                else appendMessageToChat('bot-error', 'Invalid response from server.');
                break;
            case 'clear_chat_history':
                renderChatHistory([]);
                showStatus(jsonData.message || data);
                break;
            case 'list_chatbot_files':
                renderKnowledgeFiles(jsonData.files);
                break;
            case 'manage_chatbot_files':
                showStatus(jsonData.message || data);
                refreshKnowledgeFiles(); // Refresh the list on the dashboard
                break;
            case 'generate_image':
                document.getElementById('generatedImage').src = `data:image/png;base64,${jsonData.image_base64}`;
                document.getElementById('generatedImage').classList.remove('hidden');
                document.getElementById('imageResultContainer').querySelector('span').classList.add('hidden');
                showStatus('Image generated successfully!');
                break;
            default:
                showStatus(jsonData.message || data || `${source} completed successfully!`);
                if (source.startsWith('convert') || source.startsWith('merge')) {
                    window.electronAPI.openOutputFolder();
                }
        }
    }

    // =========================================================================
    // SECTION 6: START THE APP
    // =========================================================================
    initialize();
}