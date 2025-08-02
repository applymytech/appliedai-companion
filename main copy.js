// =============================================================================
// SECTION 1: DEPENDENCIES & SETUP
// =============================================================================
const { app, BrowserWindow, ipcMain, Menu, shell, dialog } = require('electron');
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

// Initialize Firebase Admin SDK for secure backend operations
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
            preload: path.join(__dirname, 'app', 'renderer.js'), // Using a dedicated preload script
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
    expressApp.listen(3000, () => log.info('[Main Process] Local server started on http://localhost:3000'));
    
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
app.on('before-quit', (event) => {
    log.info('[Main Process] Initiating shutdown sequence.');

    const shredOnExit = store.get('shredOnExit', true);
    if (shredOnExit) {
        log.info('[Main Process] Shred on exit enabled. Shredding output folder.');
        const scriptPath = path.join(__dirname, 'scripts', 'script_router.py');
        const outputPath = store.get('outputPath');
        const payload = { folder_path: outputPath };
        const scriptArgs = [scriptPath, 'shred_folder_adapter', '', JSON.stringify(payload), outputPath];
        const result = spawnSync('python', scriptArgs, { encoding: 'utf8' });
        if (result.status !== 0) {
            log.error(`[Main Process] Shred on exit failed: ${result.stderr}`);
        } else {
            log.info('[Main Process] Shred on exit completed successfully.');
        }
    }

    log.info('[Main Process] Generating final app health summary.');
const healthSummaryScriptPath = path.join(__dirname, 'scripts', 'script_router.py');
const mainLogFile = log.transports.file.getFile();
const logDirectory = path.dirname(mainLogFile.path);

const healthSummaryPayload = { log_file_path: mainLogFile.path };
const healthSummaryArgs = [healthSummaryScriptPath, 'get_ai_log_summary', '', JSON.stringify(healthSummaryPayload), ''];
const summaryResult = spawnSync('python', healthSummaryArgs, { encoding: 'utf8' });

if (summaryResult.status !== 0) {
    log.error(`[Main Process] Health summary generation failed: ${summaryResult.stderr}`);
    } else {
        const summaryContent = summaryResult.stdout;
        const summaryFileName = `health_summary_${Date.now()}.txt`;
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
// SECTION 5: IPC HANDLERS (COMMUNICATION WITH FRONTEND)
// =============================================================================
// --- Page Navigation ---
ipcMain.on('navigate', (event, page) => {
    const url = `http://localhost:3000/${page}.html`;
    log.info(`[Main Process] Navigating to ${url}`);
    BrowserWindow.fromWebContents(event.sender)?.loadURL(url);
});
ipcMain.on('load-account-page', (event) => {
    const win = BrowserWindow.fromWebContents(event.sender);
    if (win) {
        log.info('[Main Process] Navigating from login to account page.');
        win.loadURL('http://localhost:3000/account.html');
    }
});

ipcMain.on('start-main-app', (event) => {
    const win = BrowserWindow.fromWebContents(event.sender);
    if (win) {
        log.info('[Main Process] Navigating from account to main application.');
        win.loadURL('http://localhost:3000/app/index.html');
    }
});

ipcMain.on('return-to-login', (event) => {
    const win = BrowserWindow.fromWebContents(event.sender);
    if (win) {
        log.info('[Main Process] Navigating back to login page.');
        win.loadURL('http://localhost:3000/login.html');
    }
});

// Handles getting the initial user data from sessionStorage
ipcMain.handle('get-user-data', (event) => {
    return event.sender.executeJavaScript('({uid: sessionStorage.getItem("userUID"), name: sessionStorage.getItem("userName"), email: sessionStorage.getItem("userEmail"), coins: sessionStorage.getItem("userCoins")})', true);
});

// Handles getting the default path
ipcMain.handle('get-default-path', () => getDefaultPath());

// Handles getting a value from the electron-store
ipcMain.handle('store:get', (event, key) => store.get(key));

// --- File & Folder Dialogs ---
ipcMain.handle('dialog:openFile', (event, options) => dialog.showOpenDialog(mainWindow, options));
ipcMain.handle('dialog:openDirectory', (event, options) => dialog.showOpenDialog(mainWindow, options));
ipcMain.handle('dialog:showMessageBox', (event, options) => dialog.showMessageBoxSync(mainWindow, options));

// --- System Operations ---
ipcMain.on('shell:openPath', (event, path) => shell.openPath(path));
ipcMain.on('shell:openExternal', (event, url) => shell.openExternal(url));
ipcMain.on('log:log', (event, { level, message }) => log[level](`[Renderer] ${message}`));

// --- App Configuration ---
ipcMain.handle('store:get', (event, key) => store.get(key));
ipcMain.on('store:set', (event, { key, value }) => store.set(key, value));

// --- AI Coin Balance Management ---
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

// --- Central Script Executor ---
ipcMain.on('run-script', (event, { functionName, payload = {} }) => {
    const outputPath = store.get('outputPath');
    log.info(`[Main Process] Executing script: '${functionName}'`);
    const scriptPath = path.join(__dirname, 'scripts', 'script_router.py');
    
    const env = { ...process.env, PYTHONIOENCODING: 'utf-8' };
    const scriptArgs = [scriptPath, functionName, "UNUSED_API_KEY", JSON.stringify(payload), outputPath];
    
    const pyProcess = spawn('python', scriptArgs, { env });
    
    let resultData = '';
    let errorData = '';
    pyProcess.stdout.on('data', (data) => resultData += data.toString());
    pyProcess.stderr.on('data', (data) => errorData += data.toString());
    
    pyProcess.on('close', (code) => {
        if (errorData) log.error(`[Python STDERR - ${functionName}] ${errorData.trim()}`);
        
        event.sender.send('script-reply', {
            success: code === 0,
            data: resultData.trim(),
            error: errorData.trim(),
            source: functionName
        });
    });
});
