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
    let sessionCoinsUsed = 0;
    let selectedFilesStore = {};

    const pageTitle = document.getElementById('pageTitle');
    const statusMessage = document.getElementById('statusMessage');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const progressModal = document.getElementById('progressModal');
    const progressTitle = document.getElementById('progress-title');
    const progressMessage = document.getElementById('progress-message');
    const progressBarInner = document.getElementById('progress-bar-inner');
    const progressPercentage = document.getElementById('progress-percentage');

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
        setTimeout(() => statusMessage.classList.add('hidden'), duration);
    }
    function showProgressModal(title, message) {
        progressTitle.textContent = title;
        progressMessage.textContent = message;
        progressBarInner.style.width = '0%';
        progressPercentage.textContent = '0%';
        progressModal.classList.remove('hidden');
    }
    function updateProgress(percent, message) {
        progressBarInner.style.width = `${percent}%`;
        progressPercentage.textContent = `${percent}%`;
        if (message) {
            progressMessage.textContent = message;
        }
    }
    function hideProgressModal() {
        progressModal.classList.add('hidden');
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

    document.getElementById('viewAccountBtn').addEventListener('click', () => {
            log('info', 'User clicked "View Account Details", navigating to account page.');
            window.electronAPI.loadAccountPage();
        });

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
        
        try {
            outputPathSpan.textContent = await window.electronAPI.getStoreValue('outputPath');
            const userData = await window.electronAPI.getUserData();
            if (userData) {
                currentUser.name = userData.name;
                const initialCoins = userData.coins || 0;
                sessionStorage.setItem('userCoins', initialCoins);
                coinCountSpan.textContent = parseFloat(initialCoins).toFixed(4);
            } else {
                 throw new Error("User data from main process was null.");
            }
        } catch (error) {
            log('error', 'Failed to setup dashboard data:', error);
            showStatus('Could not load dashboard settings.', true);
            coinCountSpan.textContent = 'Error';
        }

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
        document.getElementById('shredNowBtn').addEventListener('click', async () => {
            log('info', 'User clicked "Shred Output Folder Now"');
            const result = await window.electronAPI.showConfirmDialog({ type: 'warning', buttons: ['Cancel', 'Shred'], defaultId: 0, title: 'Confirm Shred', message: 'Are you sure you want to permanently delete everything in the output folder? This cannot be undone.' });
            if (result.response === 1) {
                showProgressModal('Shredding...', 'Securely deleting files...');
                window.electronAPI.runScript({ functionName: 'shred_folder_adapter', payload: { folder_path: outputPathSpan.textContent } });
            }
        });
        // Logic for the new "View Account Details" button
        document.getElementById('viewAccountBtn').addEventListener('click', () => {
            log('info', 'User clicked "View Account Details", navigating to account page.');
            window.electronAPI.loadAccountPage();
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
            });
        });

        document.getElementById('selectAiImageBtn').addEventListener('click', async () => {
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile'], filters: [{ name: 'Images', extensions: ['png', 'jpg', 'jpeg'] }] });
            if (result && !result.canceled && result.filePaths.length > 0) {
                selectedFilesStore.ai_image_input = result.filePaths[0];
                document.getElementById('selectedAiImagePath').textContent = selectedFilesStore.ai_image_input;
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
            
            showProgressModal('Generating Image...', `Using ${toolTitle.textContent} tool...`);
            window.electronAPI.runScript({ functionName: 'generate_image', payload });
        });

        // --- Image Conversion Tab ---
        document.getElementById('selectImageBtn').addEventListener('click', async () => {
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'], filters: [{ name: 'Images', extensions: ['png', 'jpg', 'jpeg', 'gif', 'bmp'] }] });
            if (result && !result.canceled && result.filePaths.length > 0) {
                selectedFilesStore.image_conversion = result.filePaths;
                document.getElementById('selectedImagePaths').textContent = `Selected files: ${result.filePaths.length}`;
                document.getElementById('convertImageBtn').disabled = false;
            }
        });

        document.getElementById('convertImageBtn').addEventListener('click', () => {
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
            
            showProgressModal('Converting Images', `Converting to ${format}...`);
            window.electronAPI.runScript({ functionName: 'convert_image', payload });
        });
    }

    function setupFileManagement() {
        document.getElementById('selectMergeFilesBtn').addEventListener('click', async () => {
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'] });
            if (result && !result.canceled && result.filePaths.length > 0) {
                selectedFilesStore.merge = result.filePaths;
                document.getElementById('selectedMergePaths').textContent = `Selected files: ${result.filePaths.length}`;
                document.getElementById('mergeFilesBtn').disabled = false;
            }
        });
        document.getElementById('mergeFilesBtn').addEventListener('click', () => {
            const mode = document.querySelector('input[name="mergeMode"]:checked').value;
            showProgressModal('Merging Files', 'Combining selected files...');
            window.electronAPI.runScript({ functionName: 'merge_files', payload: { files: selectedFilesStore.merge, mode: mode } });
        });

        // --- File Shredder ---
        document.getElementById('selectShredFilesBtn').addEventListener('click', async () => {
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'] });
            if (result && !result.canceled && result.filePaths.length > 0) {
                selectedFilesStore.shred = result.filePaths;
                document.getElementById('selectedShredPaths').textContent = `Selected files: ${result.filePaths.length}`;
                document.getElementById('shredFilesBtn').disabled = false;
            }
        });
        document.getElementById('shredFilesBtn').addEventListener('click', async () => {
            const result = await window.electronAPI.showConfirmDialog({type: 'warning', buttons: ['Cancel', 'Shred'], defaultId: 0, title: 'Confirm Shred', message: 'Are you sure you want to permanently shred the selected files?'});
            if (result.response === 1) {
                showProgressModal('Shredding Files', 'Securely deleting selected files...');
                window.electronAPI.runScript({ functionName: 'shred_files_adapter', payload: { files: selectedFilesStore.shred } });
            }
        });
        document.getElementById('shredFolderBtn').addEventListener('click', async () => {
            const result = await window.electronAPI.showOpenDirectoryDialog();
            if (result && !result.canceled && result.filePaths.length > 0) {
                const confirmResult = await window.electronAPI.showConfirmDialog({type: 'warning', buttons: ['Cancel', 'Shred'], defaultId: 0, title: 'Confirm Shred', message: `Are you sure you want to shred the entire folder: ${result.filePaths[0]}?`});
                if (confirmResult.response === 1) {
                    showProgressModal('Shredding Folder', 'Securely deleting folder contents...');
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
            showProgressModal('Scraping Page', `Scraping content from ${url}...`);
            window.electronAPI.runScript({ functionName: 'scrape_single_page', payload: { url } });
        });
        document.getElementById('scrapeSitemapBtn').addEventListener('click', () => {
            const url = formatUrl(document.getElementById('sitemapUrlInput').value);
            if (!url) return showStatus('Please enter a sitemap URL.', true);
            showProgressModal('Scraping Sitemap', `Processing sitemap from ${url}...`);
            window.electronAPI.runScript({ functionName: 'scrape_sitemap', payload: { sitemap_url: url } });
        });
        document.getElementById('downloadFilesBtn').addEventListener('click', () => {
            const url = formatUrl(document.getElementById('fileDownloaderUrlInput').value);
            const fileType = document.getElementById('fileTypeSelect').value;
            if (!url) return showStatus('Please enter a URL.', true);
            showProgressModal('Downloading Files', `Searching for .${fileType} files...`);
            window.electronAPI.runScript({ functionName: 'download_files_from_page', payload: { url, file_type: fileType } });
        });
        document.getElementById('downloadWebsiteBtn').addEventListener('click', () => {
            const url = formatUrl(document.getElementById('downloadWebsiteUrlInput').value);
            if (!url) return showStatus('Please enter a URL.', true);
            showProgressModal('Downloading Website', 'Starting website snapshot...');
            window.electronAPI.runScript({ functionName: 'download_website_adapter', payload: { url } });
        });
    }
    function setupConversionStudio() {
        const setupConverter = (type) => {
            const typeLower = type.toLowerCase();
            document.getElementById(`select${type}Btn`).addEventListener('click', async () => {
                const extensions = { Pdf: ['pdf'], Json: ['json'], Markdown: ['md'] };
                const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'], filters: [{ name: type, extensions: extensions[type] }] });
                if (result && !result.canceled && result.filePaths.length > 0) {
                    selectedFilesStore[typeLower] = result.filePaths;
                    document.getElementById(`selected${type}Paths`).textContent = `Selected files: ${result.filePaths.length}`;
                    document.getElementById(`convert${type}Btn`).disabled = false;
                }
            });
            document.getElementById(`convert${type}Btn`).addEventListener('click', () => {
                const format = document.getElementById(`${typeLower}OutputFormatSelect`).value;
                showProgressModal(`Converting ${type}`, `Converting to ${format}...`);
                window.electronAPI.runScript({ functionName: `convert_${typeLower}`, payload: { files: selectedFilesStore[typeLower], format: format } });
            });
        };
        setupConverter('Pdf');
        setupConverter('Json');
        setupConverter('Markdown');
    }

    function setupChatbot() {
        const chatMessages = document.getElementById('chatMessages');
        const chatInput = document.getElementById('chatInput');
        const sendMessageBtn = document.getElementById('sendMessageBtn');
        const clearChatHistoryBtn = document.getElementById('clearChatHistoryBtn');
        const renderChatHistory = (history) => {
            chatMessages.innerHTML = '';
            if (history) {
                history.forEach(msg => {
                    const messageEl = document.createElement('div');
                    messageEl.classList.add('chat-message', `role-${msg.role}`);
                    // Use marked library to render Markdown from the model
                    messageEl.innerHTML = marked.parse(msg.content);
                    chatMessages.appendChild(messageEl);
                });
            }
            chatMessages.scrollTop = chatMessages.scrollHeight;
        };

        // --- Handles sending a message ---
        const sendMessage = () => {
            const message = chatInput.value.trim();
            if (!message) return;

            log('info', 'User sent a chatbot message.');
            showProgressModal('Gemma is thinking...', 'Please wait for a response.');
            
            window.electronAPI.runScript({
                functionName: 'get_chatbot_response',
                payload: {
                    uid: currentUser.uid,
                    message: message
                }
            });
            chatInput.value = '';
        };

        // --- Event Listeners ---
        sendMessageBtn.addEventListener('click', sendMessage);
        chatInput.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' && !event.shiftKey) {
                event.preventDefault();
                sendMessage();
            }
        });

        clearChatHistoryBtn.addEventListener('click', () => {
            log('info', 'User cleared chat history.');
            showProgressModal('Clearing History...', 'Please wait...');
            window.electronAPI.runScript({
                functionName: 'clear_chat_history',
                payload: { uid: currentUser.uid }
            });
        });
    
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
        try {
            const progressUpdate = JSON.parse(reply.data);
            if (progressUpdate && progressUpdate.progress) {
                updateProgress(progressUpdate.progress.percent, progressUpdate.progress.message);
                if (progressUpdate.progress.percent >= 100) {
                    setTimeout(hideProgressModal, 1000);
                }
                return;
            }
        } catch(e) { /* Not a progress update, continue */ }

        hideProgressModal();
        const { source, success, data, error } = reply;

        if (!success) {
            log('error', `Error from '${source}':`, error);
            showStatus(`Error during ${source}: ${error || 'Unknown error'}`, true);
            return;
        }
        
        let jsonData = {};
        try {
            jsonData = JSON.parse(data);
        } catch (e) {
            log('warn', `Non-JSON response from '${source}': ${data}`);
            jsonData = { message: data || `${source} completed.` };
        }

        if (jsonData.coins_used) {
            const cost = parseFloat(jsonData.coins_used);
            if (cost > 0) {
                sessionCoinsUsed += cost;
                const coinCountSpan = document.getElementById('coinCount');
                const initialBalance = parseFloat(sessionStorage.getItem('userCoins'));
                const newDisplayBalance = initialBalance - sessionCoinsUsed;
                coinCountSpan.textContent = newDisplayBalance.toFixed(4);
                log('info', `Deducted ${cost.toFixed(4)} AI Coins. New session usage: ${sessionCoinsUsed.toFixed(4)}`);
            }
        }
        
        showStatus(jsonData.message || `${source} completed successfully!`);
    }

    // =========================================================================
    // SECTION 6: START THE APP
    // =========================================================================
    initialize();
}}
