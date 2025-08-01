// main.js

// =============================================================================
// SECTION 1: DEPENDENCIES (Must Load First)
// =============================================================================
const { app, BrowserWindow, ipcMain, Menu, shell, dialog } = require('electron');
const path = require('path');
const fs = require('fs');
const os = require('os');
const { spawn, spawnSync } = require('child_process');
const log = require('electron-log');
const express = require('express');

// Firebase Admin SDK for secure backend operations (like updating user tokens)
const admin = require('firebase-admin');

require('dotenv').config({ path: path.join(__dirname, '.env') });


// =============================================================================
// SECTION 2: GLOBAL CONFIGURATION & SETUP
// =============================================================================
log.errorHandler.startCatching();

log.transports.file.resolvePathFn = () => path.join(__dirname, 'logs/main.log');
log.info('Application starting...');

let mainWindow;
let Store;
let store;

const getDefaultPath = () => path.join(app.getPath('appData'), 'appliedai-companion', 'conversions');

// Initialize Firebase Admin SDK (for server-side operations like updating Firestore)
try {
    const serviceAccountBase64 = process.env.FIREBASE_PRIVATE_KEY_BASE64;
    if (!serviceAccountBase64) {
        throw new Error("FIREBASE_PRIVATE_KEY_BASE64 not found in .env. Firebase Admin SDK cannot be initialized.");
    }
    const serviceAccount = JSON.parse(Buffer.from(serviceAccountBase64, 'base64').toString('ascii'));

    admin.initializeApp({
        credential: admin.credential.cert(serviceAccount),
    });
    log.info('[Main Process] Firebase Admin SDK initialized successfully.');
} catch (error) {
    log.error('[Main Process] Failed to initialize Firebase Admin SDK:', error);
}


async function initializeStore() {
    try {
        Store = (await import('electron-store')).default;
        store = new Store();
        log.info('[Main Process] Electron-store initialized successfully.');
        
        if (!store.get('outputPath')) {
            const defaultPath = getDefaultPath();
            store.set('outputPath', defaultPath);
            log.info(`[Main Process] Set default output path to: ${defaultPath}`);
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
            preload: path.join(__dirname, 'app', 'renderer.js'),
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
app.on('before-quit', () => {
    log.info('[Main Process] Initiating shutdown sequence.');

    // --- Shredding Output Folder on Exit ---
    const shredOnExit = store.get('shredOnExit', true);
    if (shredOnExit) {
        log.info('[Main Process] Shred on exit enabled. Shredding output folder synchronously.');
        const scriptPath = path.join(__dirname, 'scripts', 'api_handler.py');
        const outputPath = store.get('outputPath');
        const payload = { folder_path: outputPath };
        const scriptArgs = [scriptPath, 'shred_folder', '', JSON.stringify(payload), outputPath];
        const result = spawnSync('python', scriptArgs, { env: { ...process.env, SHRED: 'true' }, encoding: 'utf8' });
        if (result.status !== 0) {
            log.error(`[Main Process] Shred on exit failed: ${result.stderr.toString()}`);
        } else {
            log.info('[Main Process] Shred on exit completed successfully.');
        }
    }

    // --- Generating App Health Summary ---
    log.info('[Main Process] Generating final app health summary.');
    const scriptPath = path.join(__dirname, 'scripts', 'api_handler.py');
    const logFilePath = log.transports.file.getFile().path;

    const scriptArgs = [scriptPath, 'summarize_log', '', JSON.stringify({ log_file_path: logFilePath }), ''];
    const result = spawnSync('python', scriptArgs, { env: { ...process.env }, encoding: 'utf8' });

    if (result.status !== 0) {
        log.error(`[Main Process] Health summary generation failed: ${result.stderr.toString()}`);
    } else {
        log.info('[Main Process] Health summary generated successfully.');
        try {
            const summaryData = JSON.parse(result.stdout.trim());
            const summaryContent = summaryData.summary;
            const tokensUsed = summaryData.tokens_used;

            if (summaryContent) {
                const now = new Date();
                const month = String(now.getMonth() + 1).padStart(2, '0');
                const day = String(now.getDate()).padStart(2, '0');
                const hours = String(now.getHours()).padStart(2, '0');
                const minutes = String(now.getMinutes()).padStart(2, '0');
                const year = String(now.getFullYear()).slice(2);

                let errorStatus = "good";
                if (summaryContent.toLowerCase().includes("error") || summaryContent.toLowerCase().includes("failure") || summaryContent.toLowerCase().includes("fatal")) {
                    errorStatus = "fatal_errors";
                } else if (summaryContent.toLowerCase().includes("warning")) {
                    errorStatus = "check";
                }

                const filename = `${month}.${minutes} ${day}${month}${year} log summary (${errorStatus}).md`;
                
                // CHANGED: Save the summary in the project's 'logs' directory
                const logDir = path.join(__dirname, 'logs');
                fs.mkdirSync(logDir, { recursive: true });
                const filePath = path.join(logDir, filename);

                fs.writeFileSync(filePath, summaryContent, 'utf-8');
                log.info(`[Main Process] App health summary saved to: ${filePath} (Tokens: ${tokensUsed})`);
            }
        } catch (parseError) {
            log.error(`[Main Process] Failed to parse health summary output: ${parseError}`);
            log.error(`[Main Process] Raw summary output that caused error: ${result.stdout.trim()}`);
        }
    }
});


// =============================================================================
// SECTION 5: APPLICATION MENU
// =============================================================================
const menu = Menu.buildFromTemplate([
    {
        label: 'File',
        submenu: [{ label: 'Logout', click: () => mainWindow.loadURL('http://localhost:3000/login.html') }, { role: 'quit' }]
    },
    { label: 'View', submenu: [{ role: 'reload' }, { role: 'toggleDevTools' }] }
]);
Menu.setApplicationMenu(menu);


// =============================================================================
// SECTION 6: IPC HANDLERS
// =============================================================================
ipcMain.on('load-account-page', (event) => BrowserWindow.fromWebContents(event.sender)?.loadURL('http://localhost:3000/account.html'));
ipcMain.on('start-main-app', (event) => BrowserWindow.fromWebContents(event.sender)?.loadURL('http://localhost:3000/app/index.html'));
ipcMain.on('return-to-login', (event) => BrowserWindow.fromWebContents(event.sender)?.loadURL('http://localhost:3000/login.html'));

ipcMain.handle('get-token-balance', () => store.get('userTokens'));
ipcMain.on('update-token-balance', async (event, { uid, newBalance }) => {
    try {
        if (!admin.apps.length) {
            log.error('[Main Process] Firebase Admin SDK not initialized. Cannot update token balance.');
            return;
        }
        const userDocRef = admin.firestore().collection('artifacts').doc('appliedai-companion').collection('users').doc(uid);
        await userDocRef.update({ tokens: newBalance });
        log.info(`[Main Process] Firestore token balance updated for ${uid} to: ${newBalance}`);
    } catch (error) {
        log.error(`[Main Process] Failed to update Firestore token balance for ${uid}:`, error);
    }
});

ipcMain.handle('get-output-path', () => store.get('outputPath'));
ipcMain.on('open-output-folder', () => shell.openPath(store.get('outputPath')));
ipcMain.on('change-output-folder', async (event) => {
    const result = await dialog.showOpenDialog(mainWindow, { properties: ['openDirectory'] });
    if (!result.canceled && result.filePaths.length > 0) {
        const newPath = result.filePaths[0];
        store.set('outputPath', newPath);
        event.sender.send('output-path-changed', newPath);
    }
});
ipcMain.on('reset-output-folder', (event) => {
    const defaultPath = getDefaultPath();
    store.set('outputPath', defaultPath);
    fs.mkdirSync(defaultPath, { recursive: true });
    event.sender.send('output-path-changed', defaultPath);
});
ipcMain.handle('select-files', (event, options) => dialog.showOpenDialog(mainWindow, options).then(result => result.filePaths));
ipcMain.handle('select-folder', () => dialog.showOpenDialog(mainWindow, { properties: ['openDirectory'] }).then(result => result.filePaths[0]));
ipcMain.handle('show-confirm-dialog', (event, options) => {
    const dialogOptions = {
        type: 'question',
        buttons: ['Cancel', 'OK'],
        defaultId: 1,
        title: options.title || 'Confirm',
        message: options.message || 'Are you sure?',
        detail: options.detail || ''
    };
    const result = dialog.showMessageBoxSync(mainWindow, dialogOptions);
    return result === 1; 
});

ipcMain.on('log', (event, { level, message }) => log[level](`[Renderer] ${message}`));
ipcMain.on('open-external-link', (event, url) => shell.openExternal(url));

ipcMain.on('run-script', async (event, args) => {
    const { functionName, payload = {} } = args;
    const outputPath = store.get('outputPath');
    
    fs.mkdirSync(outputPath, { recursive: true });

    log.info(`[Main Process] Running script for function: ${functionName}`);
    const scriptPath = path.join(__dirname, 'scripts', 'api_handler.py');
    let processEnv = { ...process.env };
    if (functionName.includes('shred')) {
        processEnv.SHRED = 'true';
    }

    processEnv.AIML_API_KEY = process.env.AIML_API_KEY || '';
    processEnv.DEEP_AI_KEY = process.env.DEEP_AI_KEY || '';

    const scriptArgs = [scriptPath, functionName, "UNUSED_API_KEY", JSON.stringify(payload), outputPath];
    
    log.info(`[Main Process] Executing command for function: ${functionName}`);
    const pyProcess = spawn('python', scriptArgs, { env: processEnv });
    
    let resultData = '', errorData = '';
    pyProcess.stdout.on('data', (data) => resultData += data.toString());
    pyProcess.stderr.on('data', (data) => errorData += data.toString());
    
    pyProcess.on('close', (code) => {
        if (errorData) log.error(`[Python STDERR - ${functionName}] ${errorData.trim()}`);
        event.sender.send('script-reply', {
            success: code === 0,
            data: resultData.trim(),
            error: errorData.trim() || 'Unknown Python error',
            source: functionName
        });
    });
});