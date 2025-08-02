// =============================================================================
// SECTION 1: DEPENDENCIES & SETUP
// =============================================================================
const { app, BrowserWindow, ipcMain, shell, dialog } = require('electron');
const path = require('path');
const fs = require('fs');
const { spawn, spawnSync } = require('child_process');
const log = require('electron-log');
const express = require('express');
const admin = require('firebase-admin');

require('dotenv').config({ path: path.join(__dirname, '.env') });

// =============================================================================
// SECTION 2: GLOBAL CONFIGURATION & INITIALIZATION
// =============================================================================
log.transports.file.resolvePathFn = () => path.join(__dirname, 'logs/main.log');
log.info('Application starting...');

let mainWindow;
let Store;
let store;

const getDefaultPath = () => path.join(app.getPath('appData'), 'appliedai-companion', 'conversions');

// Initialize Firebase Admin SDK
try {
    const serviceAccountBase64 = process.env.FIREBASE_PRIVATE_KEY_BASE64;
    if (!serviceAccountBase64) throw new Error("FIREBASE_PRIVATE_KEY_BASE64 not found in .env.");
    const serviceAccount = JSON.parse(Buffer.from(serviceAccountBase64, 'base64').toString('ascii'));
    admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
    log.info('[Main Process] Firebase Admin SDK initialized successfully.');
} catch (error) {
    log.error('[Main Process] Failed to initialize Firebase Admin SDK:', error);
}

async function initializeStore() {
    try {
        Store = (await import('electron-store')).default;
        store = new Store();
        if (!store.get('outputPath')) {
            store.set('outputPath', getDefaultPath());
        }
        const outputPath = store.get('outputPath');
        fs.mkdirSync(outputPath, { recursive: true });
        log.info(`[Main Process] Using output path: ${outputPath}`);
    } catch (error) {
        log.error('[Main Process] Failed to initialize electron-store:', error);
    }
}

// =============================================================================
// SECTION 3: APPLICATION LIFECYCLE & WINDOW MANAGEMENT
// =============================================================================
function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1300,
        height: 900,
        webPreferences: {
            preload: path.join(__dirname, 'app', 'preload.js'),
            contextIsolation: true,
            nodeIntegration: false,
        }
    });
    mainWindow.loadURL('http://localhost:3000/login.html');
}

app.whenReady().then(async () => {
    await initializeStore();
    
    const expressApp = express();
    expressApp.use(express.static(__dirname));
    expressApp.use('/app', express.static(path.join(__dirname, 'app')));
    expressApp.use(express.static(path.join(__dirname, 'src')));
    expressApp.listen(3000, () => log.info('[Main Process] Local server started on http://localhost:3000'));
    
    setupIpcHandlers(); 
    log.info('\n--- NEW APPLICATION SESSION STARTED ---\n'); 
    createWindow();
    
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});

// =============================================================================
// SECTION 4: APPLICATION SHUTDOWN SEQUENCE
// =============================================================================
app.on('before-quit', () => {
    log.info('[Main Process] Initiating shutdown sequence.');
    const shredOnExit = store.get('shredOnExit', true);
    if (shredOnExit) {
        const scriptPath = path.join(__dirname, 'scripts', 'script_router.py');
        const outputPath = store.get('outputPath');
        const payload = { folder_path: outputPath };
        const result = spawnSync('python', [scriptPath, 'shred_folder_adapter', '', JSON.stringify(payload), outputPath], { encoding: 'utf8' });
        if (result.status !== 0) {
            log.error(`[Main Process] Shred on exit failed: ${result.stderr}`);
        } else {
            log.info('[Main Process] Shred on exit completed successfully.');
        }
    }
    const healthSummaryScriptPath = path.join(__dirname, 'scripts', 'script_router.py');
    const mainLogFile = log.transports.file.getFile();
    const logDirectory = path.dirname(mainLogFile.path);
    const healthSummaryPayload = { log_file_path: mainLogFile.path };
    const summaryResult = spawnSync('python', [healthSummaryScriptPath, 'get_ai_log_summary', '', JSON.stringify(healthSummaryPayload), ''], { encoding: 'utf8' });
    if (summaryResult.status !== 0) {
        log.error(`[Main Process] Health summary generation failed: ${summaryResult.stderr}`);
    } else {
        const summaryContent = summaryResult.stdout;
        const summaryFileName = `health_summary_${Date.now()}.md`;
        const summaryFilePath = path.join(logDirectory, summaryFileName);
        try {
            fs.writeFileSync(summaryFilePath, summaryContent);
            log.info(`[Main Process] Health summary generated and saved to: ${summaryFilePath}`);
         } catch (error) {
            log.error(`[Main Process] Failed to write health summary file: ${error}`);
        }
    }
});

// =============================================================================
// SECTION 5: IPC HANDLERS (SINGLE SETUP FUNCTION)
// =============================================================================
function setupIpcHandlers() {
    // --- Page Navigation for Login/Account Flow ---
    ipcMain.on('load-account-page', (event) => {
        BrowserWindow.fromWebContents(event.sender)?.loadURL('http://localhost:3000/account.html');
    });
    ipcMain.on('start-main-app', (event) => {
        BrowserWindow.fromWebContents(event.sender)?.loadURL('http://localhost:3000/app/index.html');
    });
    ipcMain.on('return-to-login', (event) => {
        BrowserWindow.fromWebContents(event.sender)?.loadURL('http://localhost:3000/login.html');
    });

    // --- Generic Navigation for Main App ---
    ipcMain.on('navigate', (event, page) => {
        BrowserWindow.fromWebContents(event.sender)?.loadURL(`http://localhost:3000/${page}.html`);
    });

    // --- System, Dialogs, Store ---
    ipcMain.on('shell:openPath', (event, path) => shell.openPath(path));
    ipcMain.on('shell:openExternal', (event, url) => shell.openExternal(url));
    ipcMain.on('log:log', (event, { level, message }) => log[level](`[Renderer] ${message}`));
    ipcMain.handle('dialog:openFile', (event, options) => dialog.showOpenDialog(mainWindow, options));
    ipcMain.handle('dialog:openDirectory', () => dialog.showOpenDialog(mainWindow, { properties: ['openDirectory'] }));
    ipcMain.handle('dialog:showMessageBox', (event, options) => dialog.showMessageBox(mainWindow, options));
    ipcMain.handle('get-default-path', () => getDefaultPath());
    ipcMain.handle('store:get', (event, key) => store.get(key));
    ipcMain.on('store:set', (event, { key, value }) => store.set(key, value));
    
    // --- User Data & Coins ---
    ipcMain.handle('get-user-data', (event) => {
        return event.sender.executeJavaScript('({uid: sessionStorage.getItem("userUID"), name: sessionStorage.getItem("userName"), email: sessionStorage.getItem("userEmail"), coins: sessionStorage.getItem("userCoins")})', true);
    });
    ipcMain.on('update-final-coin-balance', async (event, { uid, sessionCoinUsage }) => {
        if (sessionCoinUsage > 0) {
            log.info(`[Main Process] Saving final coin balance for ${uid}. Session usage: ${sessionCoinUsage}`);
            try {
                if (!admin.apps.length) throw new Error("Firebase Admin SDK not initialized.");
                const userDocRef = admin.firestore().collection('artifacts').doc('appliedai-companion').collection('users').doc(uid);
                await admin.firestore().runTransaction(async (transaction) => {
                    const userDoc = await transaction.get(userDocRef);
                    if (!userDoc.exists) throw new Error("User document not found in Firestore!");
                    const currentBalance = userDoc.data().coins || 0;
                    const newBalance = currentBalance - sessionCoinUsage;
                    transaction.update(userDocRef, { coins: newBalance });
                    log.info(`[Main Process] Firestore coin balance for ${uid} updated from ${currentBalance} to ${newBalance}`);
                });
            } catch (error) {
                log.error(`[Main Process] FAILED to update final coin balance for ${uid}:`, error);
            }
        }
    });

     // --- Script Executor ---
ipcMain.handle('run-script', async (event, { functionName, payload = {} }) => { // Changed to handle and async
    const outputPath = store.get('outputPath');
    log.info(`[Main Process] Executing script: '${functionName}'`);
    const scriptPath = path.join(__dirname, 'scripts', 'script_router.py');
    const env = { ...process.env, PYTHONIOENCODING: 'utf-8' };
    // Ensure payload is a string
    const payloadString = JSON.stringify(payload);
    const scriptArgs = [scriptPath, functionName, "UNUSED_API_KEY", payloadString, outputPath];
    const pyProcess = spawn('python', scriptArgs, { env });

    let scriptOutput = '';
    let scriptError = '';

    // Capture stdout data (should be the final JSON result)
    pyProcess.stdout.on('data', (data) => {
        scriptOutput += data.toString();
    });

    // Capture stderr data (should be Python log messages or actual errors)
    pyProcess.stderr.on('data', (data) => {
        const stderrLine = data.toString().trim();
        if (stderrLine) {
            if (stderrLine.startsWith('2025-08-02') && (stderrLine.includes('INFO') || stderrLine.includes('WARNING') || stderrLine.includes('ERROR'))) { 
                 log.info(`[Python LOG - ${functionName}] ${stderrLine}`);
            } else {
                 log.error(`[Python STDERR - ${functionName}] ${stderrLine}`);
                 scriptError += stderrLine + '\n'; 
            }
        }
    });

    return new Promise((resolve, reject) => {
        pyProcess.on('close', (code) => {
            if (code !== 0) {
                log.warn(`[Main Process] Script '${functionName}' finished with non-zero exit code: ${code}`);
                // If there's an accumulated scriptError, send it. Otherwise, send generic error.
                resolve({ success: false, error: scriptError || `Script exited with code ${code}`, source: functionName }); // Resolve with failure
            } else {
                // Try to parse the final stdout as JSON. If it fails, something is wrong with Python output.
                try {
                    const finalData = scriptOutput.trim();
                    // This JSON.parse() is a validation step. The 'data' passed to renderer is the string.
                    JSON.parse(finalData); 
                    resolve({ success: true, data: finalData, source: functionName }); // Resolve with success
                } catch (e) {
                    log.error(`[Main Process] Script '${functionName}' returned non-JSON output on stdout or was empty: "${scriptOutput.trim()}". Error: ${e.message}`);
                    resolve({ success: false, error: `Invalid response format from script: ${e.message}. Check logs.`, source: functionName }); // Resolve with failure
                }
            }
        });

        pyProcess.on('error', (err) => { // Handle process spawn errors
            log.error(`[Main Process] Failed to start script process '${functionName}': ${err.message}`);
            resolve({ success: false, error: `Failed to start script: ${err.message}`, source: functionName });
        });
    });
});
}
