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
    let sessionCoinsUsed = 0; // Tracks all AI Coin spending in this session
    let selectedFilesStore = {};

    // --- Main UI Elements ---
    const pageTitle = document.getElementById('pageTitle');
    const statusMessage = document.getElementById('statusMessage');
    const loadingIndicator = document.getElementById('loadingIndicator');

    // --- Progress Modal Elements ---
    const progressModal = document.getElementById('progressModal');
    const progressTitle = document.getElementById('progress-title');
    const progressMessage = document.getElementById('progress-message');
    const progressBarInner = document.getElementById('progress-bar-inner');
    const progressPercentage = document.getElementById('progress-percentage');

    // =========================================================================
    // SECTION 2: CORE APP INITIALIZATION & HELPERS
    // =========================================================================

    function initialize() {
        log('info', `Initializing app for user: ${currentUser.name}`);
        setupNavigation();
        setupDashboard();
        setupFileFeatures();
        setupImageStudio();
        setupFileManagement();
        setupWebScrapers();
        setupChatbot();
        setupHelp();
        
        window.electronAPI.onScriptReply(handleScriptReply);
        window.electronAPI.onProgressUpdate(handleProgressUpdate);

        // Final step: Save coin balance to Firebase when the user closes the app
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

    // --- Progress Bar Functions ---
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
    function setupNavigation() {
        const navContainer = document.querySelector('.nav-items');
        navContainer.addEventListener('click', (event) => {
            const navItem = event.target.closest('.nav-item');
            if (navItem && navItem.classList.contains('nav-toggle')) {
                event.preventDefault();
                log('info', 'User toggled a navigation category.');
                const category = navItem.closest('.nav-category');
                category.classList.toggle('open');
                return;
            }
            if (navItem && navItem.dataset.view) {
                log('info', `User clicked nav item, switching to view: ${navItem.dataset.view}`);
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
        document.querySelectorAll('.view-section').forEach(section => {
            section.classList.remove('active');
        });
        const activeView = document.getElementById(viewId + 'View');
        if (activeView) {
            activeView.classList.add('active');
            pageTitle.textContent = title;
            if (viewId === 'dashboard') {
                refreshKnowledgeFiles();
            }
        } else {
            log('error', `View section not found for ID: ${viewId + 'View'}`);
        }
    }

    // =========================================================================
    // SECTION 4: FEATURE SETUP (WITH LOGGING)
    // =========================================================================
    
    async function setupDashboard() {
        const outputPathSpan = document.getElementById('outputPath');
        const coinCountSpan = document.getElementById('coinCount');
        
        outputPathSpan.textContent = await window.electronAPI.getStoreValue('outputPath');
        
        const initialCoins = await window.electronAPI.getUserData(currentUser.uid).coins;
        sessionStorage.setItem('userCoins', initialCoins || 0);
        coinCountSpan.textContent = (initialCoins || 0).toFixed(4);

        document.getElementById('openOutputFolderBtn').addEventListener('click', () => {
            log('info', 'User clicked "Open Output Folder"');
            window.electronAPI.openPath(outputPathSpan.textContent);
        });
        document.getElementById('changeOutputBtn').addEventListener('click', async () => {
            log('info', 'User clicked "Change Output Folder"');
            const result = await window.electronAPI.showOpenDirectoryDialog();
            if (!result.canceled && result.filePaths.length > 0) {
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
            const confirmed = await window.electronAPI.showConfirmDialog({ message: 'Are you sure you want to permanently delete everything in the output folder?' });
            if (confirmed) {
                showLoading(true);
                window.electronAPI.runScript({ functionName: 'shred_folder', payload: { folder_path: outputPathSpan.textContent } });
            }
        });
        
        document.getElementById('addToKnowledgeBtn').addEventListener('click', async () => {
            log('info', 'User clicked "Add Knowledge File"');
            const result = await window.electronAPI.showOpenFileDialog({ properties: ['openFile', 'multiSelections'], filters: [{ name: 'Markdown', extensions: ['md'] }] });
            if (!result.canceled && result.filePaths.length > 0) {
                showLoading(true);
                window.electronAPI.runScript({ functionName: 'manage_chatbot_files', payload: { uid: currentUser.uid, action: 'save', files: result.filePaths } });
            }
        });
        document.getElementById('clearKnowledgeBtn').addEventListener('click', async () => {
            log('info', 'User clicked "Clear All Knowledge"');
            const confirmed = await window.electronAPI.showConfirmDialog({ message: 'Are you sure you want to delete all knowledge files?' });
            if (confirmed) {
                showLoading(true);
                window.electronAPI.runScript({ functionName: 'manage_chatbot_files', payload: { uid: currentUser.uid, action: 'delete_all' } });
            }
        });
    }

    // ... Continue adding comprehensive logging to every addEventListener in the remaining setup functions ...
    // e.g. setupFileFeatures(), setupImageStudio(), etc.

    // =========================================================================
    // SECTION 5: CENTRAL SCRIPT REPLY & PROGRESS HANDLERS
    // =========================================================================
    function handleScriptReply(reply) {
        showLoading(false);
        hideProgressModal(); // Hide progress bar on task completion
        const { source, success, data, error } = reply;

        if (!success) {
            log('error', `Error from '${source}':`, error);
            showStatus(`Error during ${source}: ${error}`, true);
            return;
        }
        
        let jsonData = {};
        try {
            jsonData = JSON.parse(data);
        } catch (e) {
            log('warn', `Non-JSON response from '${source}': ${data}`);
            jsonData = { message: data };
        }

        // --- AI Coin Calculation ---
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

        // --- Handle Specific Function Replies ---
        switch (source) {
            case 'get_chatbot_response':
                renderChatHistory(jsonData.history);
                break;
            // ... other cases
            default:
                showStatus(jsonData.message || `${source} completed successfully!`);
        }
    }

    function handleProgressUpdate(update) {
        const { percent, message } = update;
        updateProgress(percent, message);
    }

    // =========================================================================
    // SECTION 6: START THE APP
    // =========================================================================
    initialize();
}
