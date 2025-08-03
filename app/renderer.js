// =============================================================================
// SECTION A: FIREBASE & AUTHENTICATION
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
        initializeAppUI(user);
    } else {
        window.electronAPI.navigate('login');
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
        name: authUser.displayName || "User",
    };
    let sessionCoinsUsed = 0; // Corrected to be a number
    let selectedFilesStore = {};

    const pageTitle = document.getElementById('pageTitle');
    const statusMessage = document.getElementById('statusMessage');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const chatMessages = document.getElementById('chatMessages'); // Moved up for global access

    // =========================================================================
    // SECTION 2: CORE APP INITIALIZATION & HELPERS
    // =========================================================================

    function initialize() {
        try {
            log('info', `Initializing app for user: ${currentUser.name}`);
            setupNavigationAndTabs();
            setupDashboard();
            setupConversionStudio();
            setupImageStudio();
            setupFileManagement();
            setupWebScrapers();
            setupChatbot();
            setupHelp();
            
            window.electronAPI.onScriptReply(handleScriptReply);

            window.addEventListener('beforeunload', () => {
                log('info', `App closing. Total session coin usage: ${sessionCoinsUsed}`);
                if (sessionCoinsUsed > 0) {
                    window.electronAPI.updateFinalCoinBalance({
                        uid: currentUser.uid,
                        sessionCoinUsage: sessionCoinsUsed
                    });
                }
            });
            log('info', 'App initialized and all event listeners are active.');
        } catch (error) {
            log('error', 'A critical error occurred during UI initialization:', error);
            showStatus('A fatal error occurred. Please restart the application.', true, 10000);
        }
    }

    const log = (level, message, data = '') => {
        const logData = data ? JSON.stringify(data) : '';
        window.electronAPI.log(level, `${message} ${logData}`);
    };

    function showStatus(message, isError = false, duration = 4000) {
        statusMessage.textContent = message;
        statusMessage.className = isError ? 'status-error' : 'status-success';
        statusMessage.classList.remove('hidden');
        // Ensure the status message is visible above everything
        statusMessage.style.zIndex = 1001; 
        setTimeout(() => statusMessage.classList.add('hidden'), duration);
    }

    // Generic function to render file lists for knowledge base or canvas
    function renderFileList(containerId, filesArray, showDelete = false) {
        const container = document.getElementById(containerId);
        if (!container) return; // Guard clause
        container.innerHTML = ''; // Clear existing list

        if (filesArray && filesArray.length > 0) {
            filesArray.forEach(file => {
                const fileItem = document.createElement('div');
                fileItem.className = 'knowledge-file-item'; // Reusing class for visual consistency
                const fileNameSpan = document.createElement('span');
                fileNameSpan.textContent = file.name || file; // Assuming 'file' might be just path string
                fileItem.appendChild(fileNameSpan);

                if (showDelete) {
                    const deleteBtn = document.createElement('button');
                    deleteBtn.className = 'delete-knowledge-file-btn';
                    deleteBtn.textContent = '×';
                    deleteBtn.title = `Remove ${file.name || file}`;
                    deleteBtn.dataset.filepath = file.path || file; // Store path for removal
                    fileItem.appendChild(deleteBtn);
                }
                container.appendChild(fileItem);
            });
        } else {
            container.innerHTML = '<p style="text-align: center; color: #888;">No files added yet.</p>';
        }

        // Add event listeners for delete buttons (if present)
        if (showDelete) {
            container.querySelectorAll('.delete-knowledge-file-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const filePathToRemove = e.target.dataset.filepath;
                    log('info', `Attempting to remove file: ${filePathToRemove}`);
                    // You'll need to call a function here to manage the removal
                    // For now, let's just log and visually remove
                    const parentDiv = e.target.closest('.knowledge-file-item');
                    if (parentDiv) parentDiv.remove();
                    showStatus(`File removed: ${filePathToRemove.split('\\').pop().split('/').pop()}`);
                    // TODO: Trigger IPC call to main process to update actual knowledge base
                });
            });
        }
    }


    // =========================================================================
    // SECTION 3: NAVIGATION & VIEW MANAGEMENT
    // =========================================================================
    function setupNavigationAndTabs() {
        const navContainer = document.querySelector('.nav-items');
        navContainer.addEventListener('click', (event) => {
            const navItem = event.target.closest('.nav-item');
            if (!navItem) return;
            if (navItem.classList.contains('nav-toggle')) {
                event.preventDefault();
                navItem.closest('.nav-category').classList.toggle('open');
                return;
            }
            if (navItem.dataset.view) {
                document.querySelectorAll('.nav-item').forEach(link => link.classList.remove('active'));
                navItem.classList.add('active');
                if (navItem.classList.contains('sub-item')) {
                    navItem.closest('.nav-category').querySelector('.nav-toggle').classList.add('active');
                }
                showView(navItem.dataset.view, navItem.dataset.title);
            }
        });

        document.querySelectorAll('.studio-tabs').forEach(tabContainer => {
            tabContainer.addEventListener('click', (event) => {
                const tabLink = event.target.closest('.tab-link');
                if (!tabLink) return;
                const tabId = tabLink.dataset.tab;
                const studioContainer = tabLink.closest('.view-section');
                studioContainer.querySelectorAll('.tab-link').forEach(link => link.classList.remove('active'));
                tabLink.classList.add('active');
                studioContainer.querySelectorAll('.studio-tab-content').forEach(content => content.classList.remove('active'));
                studioContainer.querySelector(`#${tabId}`).classList.add('active');
            });
        });
    }

    // Moved 'viewAccountBtn' listener into setupDashboard,
    // as it's directly related to the dashboard view.

    function showView(viewId, title) {
        document.querySelectorAll('.view-section').forEach(section => section.classList.remove('active'));
        const activeView = document.getElementById(viewId + 'View');
        if (activeView) {
            activeView.classList.add('active');
            pageTitle.textContent = title;
        }
    }

   // =========================================================================
    // SECTION 4: FEATURE SETUP
    // =========================================================================
    
    async function setupDashboard() {
        const outputPathSpan = document.getElementById('outputPath');
        const coinCountSpan = document.getElementById('coinCount');
        const shredOnExitCheckbox = document.getElementById('shredOnExit');
        const dashboardKnowledgeFilesList = document.getElementById('dashboard-knowledge-files-list');

        try {
            outputPathSpan.textContent = await window.electronAPI.getStoreValue('outputPath');
            // Load shred on exit preference
            const shredOnExitValue = await window.electronAPI.getStoreValue('shredOnExit');
            shredOnExitCheckbox.checked = shredOnExitValue !== undefined ? shredOnExitValue : true;

            const userData = await window.electronAPI.getUserData();
            if (userData) {
                currentUser.name = userData.name;
                const initialCoins = parseFloat(userData.coins) || 0; // Ensure it's a number
                sessionStorage.setItem('userCoins', initialCoins); // Store initial balance
                coinCountSpan.textContent = initialCoins.toFixed(4); // Display initial balance
            } else {
                 throw new Error("User data from main process was null or incomplete.");
            }

            // Initial render of knowledge files (if any)
            const knowledgeFilesReply = await window.electronAPI.runScript({functionName: 'list_chatbot_files', payload: {}});
            if (knowledgeFilesReply.success && knowledgeFilesReply.data) {
                const parsedData = JSON.parse(knowledgeFilesReply.data);
                if (parsedData.files) {
                    renderFileList('dashboard-knowledge-files-list', parsedData.files, true); // True to show delete
                }
            }


        } catch (error) {
            log('error', 'Failed to setup dashboard data:', error);
            showStatus('Could not load dashboard settings or user data.', true);
            coinCountSpan.textContent = 'Error';
        }

        // Event Listeners
        document.getElementById('openOutputFolderBtn').addEventListener('click', () => {
            log('info', 'User clicked "Open Output Folder"');
            window.electronAPI.openPath(outputPathSpan.textContent);
        });
        document.getElementById('changeOutputBtn').addEventListener('click', async () => {
            log('info', 'User clicked "Change Output Folder"');
            const result = await window.electronAPI.showOpenDirectoryDialog();
            if (result && !result.canceled && result.filePaths.length > 0) {
                const newPath = result.filePaths[0];
                await window.electronAPI.setStoreValue('outputPath', newPath);
                outputPathSpan.textContent = newPath;
                showStatus(`Output path changed to: ${newPath}`);
            }
        });
        document.getElementById('resetOutputBtn').addEventListener('click', async () => {
            log('info', 'User clicked "Reset Output Folder"');
            const defaultPath = await window.electronAPI.getDefaultPath();
            await window.electronAPI.setStoreValue('outputPath', defaultPath);
            outputPathSpan.textContent = defaultPath;
            showStatus('Output path reset to default.');
        });

        // Shred on Exit checkbox listener
        shredOnExitCheckbox.addEventListener('change', async () => {
            log('info', `Shred on exit preference changed to: ${shredOnExitCheckbox.checked}`);
            await window.electronAPI.setStoreValue('shredOnExit', shredOnExitCheckbox.checked);
            showStatus(`Shred on exit is now ${shredOnExitCheckbox.checked ? 'enabled' : 'disabled'}.`);
        });

        document.getElementById('shredNowBtn').addEventListener('click', async () => {
            log('info', 'User clicked "Shred Output Folder Now"');
            const result = await window.electronAPI.showConfirmDialog({ type: 'warning', buttons: ['Cancel', 'Shred'], defaultId: 0, title: 'Confirm Shred', message: 'Are you sure you want to permanently delete everything in the output folder? This cannot be undone.' });
            if (result.response === 1) {
                window.electronAPI.runScript({ functionName: 'shred_folder_adapter', payload: { folder_path: outputPathSpan.textContent } });
            }
        });
        document.getElementById('viewAccountBtn').addEventListener('click', () => {
            log('info', 'User clicked "View Account Details", navigating to account page.');
            window.electronAPI.loadAccountPage();
        });

        document.getElementById('addToKnowledgeBtn').addEventListener('click', async () => {
            log('info', 'User clicked "Add Knowledge File(s)"');
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'], filters: [{ name: 'Markdown Files', extensions: ['md'] }] });
            if (result && !result.canceled && result.filePaths.length > 0) {
                showLoadingFeedback('Adding Knowledge...', 'Processing files for knowledge base...', true);
                window.electronAPI.runScript({ functionName: 'manage_chatbot_files', payload: { action: 'add', files: result.filePaths, uid: currentUser.uid } });
            }
        });
        document.getElementById('clearKnowledgeBtn').addEventListener('click', async () => {
            log('info', 'User clicked "Clear All Knowledge"');
            const result = await window.electronAPI.showConfirmDialog({type: 'warning', buttons: ['Cancel', 'Clear'], defaultId: 0, title: 'Confirm Clear Knowledge Base', message: 'Are you sure you want to remove all files from the chatbot knowledge base? This will clear the vector store.'});
            if (result.response === 1) {
                showLoadingFeedback('Clearing Knowledge...', 'Removing files from knowledge base...', true);
                window.electronAPI.runScript({ functionName: 'manage_chatbot_files', payload: { action: 'clear', uid: currentUser.uid } });
            }
        });

    }

    function setupImageStudio() {
        // --- AI Generation Tab ---
        const toolCards = document.querySelectorAll('.tool-card');
        const dynamicControls = document.getElementById('dynamic-controls-area');
        const toolTitle = document.getElementById('tool-title');
        const toolInstructions = document.getElementById('tool-instructions');
        const textInputContainer = document.getElementById('text-input-container');
        const imageInputContainer = document.getElementById('image-input-container');
        let activeTool = null;

        toolCards.forEach(card => {
            card.addEventListener('click', () => {
                activeTool = card.dataset.tool;
                log('info', `User selected AI Image tool: ${activeTool}`);
                
                toolCards.forEach(c => c.classList.remove('active'));
                card.classList.add('active');

                // Configure UI based on selected tool
                toolTitle.textContent = card.textContent.replace(/Premium$/, '');
                dynamicControls.classList.remove('hidden');
                
                // Show/hide inputs based on tool requirements
                const needsText = ['text2img', 'ghibli-style'];
                const needsImage = ['toonify', 'image-editor', 'torch-srgan', 'waifu2x', 'background-remover'];

                textInputContainer.classList.toggle('hidden', !needsText.includes(activeTool));
                imageInputContainer.classList.toggle('hidden', !needsImage.includes(activeTool));

                // Clear previous image/text input on tool change
                document.getElementById('imagePromptInput').value = '';
                document.getElementById('selectedAiImagePath').textContent = 'No file selected.';
                document.getElementById('generatedImage').classList.add('hidden');
                document.getElementById('imageResultContainer').querySelector('span').classList.remove('hidden'); // Show placeholder
            });
        });

        document.getElementById('selectAiImageBtn').addEventListener('click', async () => {
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile'], filters: [{ name: 'Images', extensions: ['png', 'jpg', 'jpeg'] }] });
            if (result && !result.canceled && result.filePaths.length > 0) {
                selectedFilesStore.ai_image_input = result.filePaths[0];
                document.getElementById('selectedAiImagePath').textContent = selectedFilesStore.ai_image_input.split('\\').pop().split('/').pop();
            }
        });

        document.getElementById('runAiToolBtn').addEventListener('click', () => {
            const payload = { tool: activeTool };
            const needsText = ['text2img', 'ghibli-style'];
            const needsImage = ['toonify', 'image-editor', 'torch-srgan', 'waifu2x', 'background-remover'];

            if (needsText.includes(activeTool)) {
                payload.prompt = document.getElementById('imagePromptInput').value;
                if (!payload.prompt) return showStatus('Please enter a prompt.', true);
            }
            if (needsImage.includes(activeTool)) {
                payload.image_path = selectedFilesStore.ai_image_input;
                if (!payload.image_path) return showStatus('Please select an input image.', true);
            }

            window.electronAPI.runScript({ functionName: 'generate_image', payload });
        });

        // --- Image Conversion Tab ---
        const convertImageBtn = document.getElementById('convertImageBtn');
        document.getElementById('selectImageBtn').addEventListener('click', async () => {
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'], filters: [{ name: 'Images', extensions: ['png', 'jpg', 'jpeg', 'gif', 'bmp'] }] });
            if (result && !result.canceled && result.filePaths.length > 0) {
                selectedFilesStore.image_conversion = result.filePaths;
                document.getElementById('selectedImagePaths').textContent = `Selected files: ${result.filePaths.length}`;
                convertImageBtn.disabled = false;
            }
        });

        convertImageBtn.addEventListener('click', () => {
            const format = document.getElementById('outputFormatImageSelect').value;
            const width = document.getElementById('resizeWidth').value;
            const height = document.getElementById('resizeHeight').value;
            const aspect = document.getElementById('preserveAspect').checked;

            const payload = { 
                files: selectedFilesStore.image_conversion, 
                format: format,
                resize: {
                    width: width ? parseInt(width) : null,
                    height: height ? parseInt(height) : null,
                    preserve_aspect: aspect
                }
            };
            window.electronAPI.runScript({ functionName: 'convert_image', payload });
        });
    }

    function setupFileManagement() {
        const mergeFilesBtn = document.getElementById('mergeFilesBtn');
        const shredFilesBtn = document.getElementById('shredFilesBtn');

        document.getElementById('selectMergeFilesBtn').addEventListener('click', async () => {
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'] });
            if (result && !result.canceled && result.filePaths.length > 0) {
                selectedFilesStore.merge = result.filePaths;
                document.getElementById('selectedMergePaths').textContent = `Selected files: ${result.filePaths.length}`;
                mergeFilesBtn.disabled = false;
            }
        });
        mergeFilesBtn.addEventListener('click', () => {
            const mode = document.querySelector('input[name="mergeMode"]:checked').value;
            window.electronAPI.runScript({ functionName: 'merge_files', payload: { files: selectedFilesStore.merge, mode: mode } });
        });

        // --- File Shredder ---
        document.getElementById('selectShredFilesBtn').addEventListener('click', async () => {
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'] });
            if (result && !result.canceled && result.filePaths.length > 0) {
                selectedFilesStore.shred = result.filePaths;
                document.getElementById('selectedShredPaths').textContent = `Selected files: ${result.filePaths.length}`;
                shredFilesBtn.disabled = false;
            }
        });
        shredFilesBtn.addEventListener('click', async () => {
            const result = await window.electronAPI.showConfirmDialog({type: 'warning', buttons: ['Cancel', 'Shred'], defaultId: 0, title: 'Confirm Shred', message: 'Are you sure you want to permanently shred the selected files?'});
            if (result.response === 1) {
                window.electronAPI.runScript({ functionName: 'shred_files_adapter', payload: { files: selectedFilesStore.shred } });
            }
        });
        document.getElementById('shredFolderBtn').addEventListener('click', async () => {
            const result = await window.electronAPI.showOpenDirectoryDialog();
            if (result && !result.canceled && result.filePaths.length > 0) {
                const confirmResult = await window.electronAPI.showConfirmDialog({type: 'warning', buttons: ['Cancel', 'Shred'], defaultId: 0, title: 'Confirm Shred', message: `Are you sure you want to shred the entire folder: ${result.filePaths[0]}?`});
                if (confirmResult.response === 1) {
                    window.electronAPI.runScript({ functionName: 'shred_folder_adapter', payload: { folder_path: result.filePaths[0] } });
                }
            }
        });
    }


    function setupWebScrapers() {
        const formatUrl = (input) => {
            if (!input) return '';
            if (!/^https?:\/\//i.test(input)) return `https://${input}`;
            return input;
        };
        document.getElementById('scrapeSinglePageBtn').addEventListener('click', () => {
            const url = formatUrl(document.getElementById('singlePageUrlInput').value);
            if (!url) return showStatus('Please enter a URL.', true);
            window.electronAPI.runScript({ functionName: 'scrape_single_page', payload: { url } });
        });
        document.getElementById('scrapeSitemapBtn').addEventListener('click', () => {
            const url = formatUrl(document.getElementById('sitemapUrlInput').value);
            if (!url) return showStatus('Please enter a sitemap URL.', true);
            window.electronAPI.runScript({ functionName: 'scrape_sitemap', payload: { sitemap_url: url } });
        });
        document.getElementById('downloadFilesBtn').addEventListener('click', () => {
            const url = formatUrl(document.getElementById('fileDownloaderUrlInput').value);
            const fileType = document.getElementById('fileTypeSelect').value;
            if (!url) return showStatus('Please enter a URL.', true);
            window.electronAPI.runScript({ functionName: 'download_files_from_page', payload: { url, file_type: fileType } });
        });
        document.getElementById('downloadWebsiteBtn').addEventListener('click', () => {
            const url = formatUrl(document.getElementById('downloadWebsiteUrlInput').value);
            if (!url) return showStatus('Please enter a URL.', true);
            window.electronAPI.runScript({ functionName: 'download_website_adapter', payload: { url } });
        });
    }
    function setupConversionStudio() {
        const setupConverter = (type) => {
            const typeLower = type.toLowerCase();
            const convertButton = document.getElementById(`convert${type}Btn`); // Get reference to button
            document.getElementById(`select${type}Btn`).addEventListener('click', async () => {
                const extensions = { Pdf: ['pdf'], Json: ['json'], Markdown: ['md'] };
                const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'], filters: [{ name: type, extensions: extensions[type] }] });
                if (result && !result.canceled && result.filePaths.length > 0) {
                    selectedFilesStore[typeLower] = result.filePaths;
                    document.getElementById(`selected${type}Paths`).textContent = `Selected files: ${result.filePaths.length}`;
                    convertButton.disabled = false; // Enable convert button
                }
            });
            convertButton.addEventListener('click', () => { // Attach listener to the button reference
                const format = document.getElementById(`${typeLower}OutputFormatSelect`).value;
                window.electronAPI.runScript({ functionName: `convert_${typeLower}`, payload: { files: selectedFilesStore[typeLower], format: format } });
            });
        };
        setupConverter('Pdf');
        setupConverter('Json');
        setupConverter('Markdown');
    }

    function setupChatbot() {
        const chatInput = document.getElementById('chatInput');
        const sendMessageBtn = document.getElementById('sendMessageBtn');
        const clearChatHistoryBtn = document.getElementById('clearChatHistoryBtn');
        const ephemeralFilesDisplay = document.getElementById('ephemeral-files-display');
        const ephemeralFilesList = document.getElementById('ephemeral-files-list');
        const clearEphemeralFilesBtn = document.getElementById('clearEphemeralFilesBtn');
        const addToCanvasBtn = document.getElementById('addToCanvasBtn');
        const clearCanvasBtn = document.getElementById('clearCanvasBtn');
        const attachFileBtn = document.getElementById('attachFileBtn');

        // Initial render of canvas files (if any)
        async function loadInitialCanvasFiles() {
            try {
                const canvasFilesReply = await window.electronAPI.runScript({functionName: 'list_chatbot_files', payload: { scope: 'canvas' }});
                if (canvasFilesReply.success && canvasFilesReply.data) {
                    const parsedData = JSON.parse(canvasFilesReply.data);
                    if (parsedData.files) {
                        renderFileList('canvas-files-list', parsedData.files, true); // True to show delete
                    }
                }
            } catch (error) {
                log('error', `Failed to load initial canvas files: ${error.message}`);
            }
        }
        loadInitialCanvasFiles(); // Call this on chatbot setup

        // Helper to render chat messages
        const appendChatMessage = (role, content) => {
            const messageEl = document.createElement('div');
            messageEl.classList.add('chat-message', `${role}-message`); 
            messageEl.innerHTML = marked.parse(content);
            chatMessages.appendChild(messageEl);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        };

        // --- Handles sending a message ---
        const sendMessage = () => {
            const message = chatInput.value.trim();
            if (!message) return;

            appendChatMessage('user', message); // Immediately show user's message
            log('info', 'User sent a chatbot message.');
            
            const payload = {
                uid: currentUser.uid,
                message: message,
                ephemeral_files: selectedFilesStore.ephemeral_chat_files || []
            };

            window.electronAPI.runScript({
                functionName: 'get_chatbot_response',
                payload: payload
            });
            chatInput.value = '';
            selectedFilesStore.ephemeral_chat_files = []; // Clear ephemeral files after sending
            ephemeralFilesDisplay.classList.add('hidden');
            ephemeralFilesList.textContent = '';
        };

        // --- Event Listeners ---
        sendMessageBtn.addEventListener('click', sendMessage);
        chatInput.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' && !event.shiftKey) {
                event.preventDefault();
                sendMessage();
            }
        });

        clearChatHistoryBtn.addEventListener('click', async () => {
            log('info', 'User clicked "Clear History".');
            const result = await window.electronAPI.showConfirmDialog({type: 'info', buttons: ['Cancel', 'Clear'], defaultId: 0, title: 'Confirm Clear Chat History', message: 'Are you sure you want to clear your chat history for this session?'});
            if (result.response === 1) {
                showLoadingFeedback('Clearing History...', 'Please wait...', true);
                window.electronAPI.runScript({
                    functionName: 'clear_chat_history',
                    payload: { uid: currentUser.uid }
                });
            }
        });

        attachFileBtn.addEventListener('click', async () => {
            log('info', 'User clicked "Attach File to Chat".');
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'] });
            if (result && !result.canceled && result.filePaths.length > 0) {
                selectedFilesStore.ephemeral_chat_files = result.filePaths;
                ephemeralFilesList.textContent = result.filePaths.map(p => p.split('\\').pop().split('/').pop()).join(', ');
                ephemeralFilesDisplay.classList.remove('hidden');
                showStatus(`Attached ${result.filePaths.length} file(s) for next message.`);
            }
        });
        clearEphemeralFilesBtn.addEventListener('click', () => {
            log('info', 'User cleared attached chat files.');
            selectedFilesStore.ephemeral_chat_files = [];
            ephemeralFilesDisplay.classList.add('hidden');
            ephemeralFilesList.textContent = '';
            showStatus('Attached files cleared.');
        });
        
        addToCanvasBtn.addEventListener('click', async () => {
            log('info', 'User clicked "Add File(s) to Canvas".');
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'], filters: [{ name: 'Document Files', extensions: ['pdf', 'docx', 'txt', 'md'] }] });
            if (result && !result.canceled && result.filePaths.length > 0) {
                showLoadingFeedback('Adding to Canvas...', 'Processing files for canvas...', true);
                window.electronAPI.runScript({ functionName: 'manage_chatbot_files', payload: { action: 'add_to_canvas', files: result.filePaths, uid: currentUser.uid } });
            }
        });

        clearCanvasBtn.addEventListener('click', async () => {
            log('info', 'User clicked "Clear Canvas".');
            const result = await window.electronAPI.showConfirmDialog({type: 'warning', buttons: ['Cancel', 'Clear'], defaultId: 0, title: 'Confirm Clear Canvas', message: 'Are you sure you want to remove all files from the chatbot canvas? This will clear all context for the current session.'});
            if (result.response === 1) {
                showLoadingFeedback('Clearing Canvas...', 'Removing files from canvas...', true);
                window.electronAPI.runScript({ functionName: 'manage_chatbot_files', payload: { action: 'clear_canvas', uid: currentUser.uid } });
            }
        });
    }
    
    function setupHelp() {
        document.getElementById('supportEmailBtn').addEventListener('click', () => {
            window.electronAPI.openExternalLink('mailto:support@applymytech.ai?subject=App Support Request');
        });
        document.getElementById('privacyEmailBtn').addEventListener('click', () => {
            window.electronAPI.openExternalLink('mailto:support@applymytech.ai?subject=App Privacy Request');
        });
    }

    // =========================================================================
    // SECTION 5: CENTRAL SCRIPT REPLY & PROGRESS HANDLERS
    // =========================================================================
    function handleScriptReply(reply) {
        log('debug', `Received script reply:`, reply); 

        const { source, success, data, error } = reply;

        let parsedData = {};
        let isProgressUpdate = false;

        try {
            parsedData = JSON.parse(data);
            if (parsedData && parsedData.progress) {
                isProgressUpdate = true;
            }
        } catch (e) {
            log('warn', `Non-JSON or invalid JSON response from '${source}': ${data}`);
            // If data is not JSON, use it as a simple message.
            parsedData = { message: data.trim() || `${source} completed.` };
        }

        if (isProgressUpdate) {
            updateProgress(parsedData.progress.percent, parsedData.progress.message);
            if (parsedData.progress.percent >= 100) {
            }
            return; // Exit here for progress updates
        }

        // --- If we reach here, it's a final reply (or initial reply not progress) ---

        if (!success) {
            log('error', `Error from '${source}':`, error);
            showStatus(`Error during ${source}: ${error || 'Unknown error'}`, true);
            return;
        }
        
        // Handle coin deduction
        if (parsedData.coins_used !== undefined && parsedData.coins_used !== null) {
            const cost = parseFloat(parsedData.coins_used);
            if (cost > 0) {
                sessionCoinsUsed += cost;
                const coinCountSpan = document.getElementById('coinCount');
                const initialBalance = parseFloat(sessionStorage.getItem('userCoins') || '0');
                const newDisplayBalance = initialBalance - sessionCoinsUsed;
                coinCountSpan.textContent = newDisplayBalance.toFixed(4);
                log('info', `Deducted ${cost.toFixed(4)} AI Coins. Current Session Usage: ${sessionCoinsUsed.toFixed(4)}. Display Balance: ${newDisplayBalance.toFixed(4)}`);
            }
        }
        
        // Determine the message to show to the user
        let statusMessageText = parsedData.message; // Prefer message from parsedData

        // Specific UI updates based on source function
        if (source === 'shred_folder_adapter' || source === 'shred_files_adapter') {
            statusMessageText = 'Files shredded successfully!';
            // Re-render knowledge/canvas lists if shredding affects them
            if (source === 'shred_folder_adapter' && parsedData.shredded_output_folder) {
                // Potentially clear or update relevant file lists if they were in the shredded folder
            }
        } else if (source === 'get_ai_log_summary') {
            statusMessageText = 'AI Log Summary generated and saved.';
        } else if (source === 'generate_image') {
            if (parsedData.image_url) {
                const generatedImage = document.getElementById('generatedImage');
                const imageResultContainer = document.getElementById('imageResultContainer');
                generatedImage.src = parsedData.image_url;
                generatedImage.classList.remove('hidden');
                const placeholderSpan = imageResultContainer.querySelector('span');
                if (placeholderSpan) placeholderSpan.classList.add('hidden'); 
                statusMessageText = 'Image generated successfully!';
            } else {
                statusMessageText = 'Image generation completed, but no image URL received.';
                showStatus(statusMessageText, true); 
                return; 
            }
        } else if (source.startsWith('convert_')) {
            statusMessageText = `${source.replace('convert_', '').toUpperCase()} conversion completed!`;
        } else if (source.startsWith('scrape_') || source.startsWith('download_')) {
            statusMessageText = `Web operation completed: ${parsedData.message || 'Check output folder.'}`;
        } else if (source === 'get_chatbot_response') {
            if (parsedData.chat_history) { 
                 chatMessages.innerHTML = ''; 
                 parsedData.chat_history.forEach(msg => {
                     const messageEl = document.createElement('div');
                     messageEl.classList.add('chat-message', `${msg.role}-message`); 
                     messageEl.innerHTML = marked.parse(msg.content);
                     chatMessages.appendChild(messageEl);
                 });
                 chatMessages.scrollTop = chatMessages.scrollHeight; 
            } else if (parsedData.message) { 
                 appendChatMessage('bot', parsedData.message); // Use append helper for just a new message
            }
            statusMessageText = 'Chatbot responded.';
        } else if (source === 'clear_chat_history') {
            if (chatMessages) chatMessages.innerHTML = ''; 
            statusMessageText = 'Chat history cleared.';
        } else if (source === 'manage_chatbot_files') {
            statusMessageText = parsedData.message || 'Knowledge base updated.';
            if (parsedData.action_performed === 'add' || parsedData.action_performed === 'clear') {
                // Re-list knowledge files after add/clear operations
                // We need to fetch the updated list from the backend
                window.electronAPI.runScript({functionName: 'list_chatbot_files', payload: {}}).then(reply => {
                    if (reply.success && reply.data) {
                        const filesData = JSON.parse(reply.data);
                        if (filesData.files) {
                            renderFileList('dashboard-knowledge-files-list', filesData.files, true);
                        }
                    }
                }).catch(err => log('error', 'Failed to refresh knowledge file list:', err));
            } else if (parsedData.action_performed === 'add_to_canvas' || parsedData.action_performed === 'clear_canvas') {
                 window.electronAPI.runScript({functionName: 'list_chatbot_files', payload: { scope: 'canvas' }}).then(reply => {
                    if (reply.success && reply.data) {
                        const filesData = JSON.parse(reply.data);
                        if (filesData.files) {
                            renderFileList('canvas-files-list', filesData.files, true);
                        }
                    }
                }).catch(err => log('error', 'Failed to refresh canvas file list:', err));
            }
        } else if (source === 'list_chatbot_files') {
            // This reply is often for initial load, or triggered by manage_chatbot_files
            // The renderFileList is called directly within the setup function or manage_chatbot_files handler
            // So, no need to show a status message for a list operation unless it's an error.
            return; // Don't show generic status for pure list operations
        }


        // Fallback for any function that doesn't have a specific message
        if (!statusMessageText) {
             statusMessageText = `${source} completed successfully!`;
        }
        showStatus(statusMessageText, false); 
    }

    // =========================================================================
    // SECTION 6: START THE APP
    // =========================================================================
    initialize();
}