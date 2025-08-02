const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    // --- Specific functions for Login/Account flow ---
    loadAccountPage: () => ipcRenderer.send('load-account-page'),
    startMainApp: () => ipcRenderer.send('start-main-app'),
    returnToLogin: () => ipcRenderer.send('return-to-login'),

    // --- Generic Navigation for Main App ---
    navigate: (page) => ipcRenderer.send('navigate', page),
    
    // --- User & Firebase Data ---
    getUserData: () => ipcRenderer.invoke('get-user-data'), // <-- THIS WAS THE MISSING FUNCTION
    updateFinalCoinBalance: (data) => ipcRenderer.send('update-final-coin-balance', data),
    firebaseConfig: {
        apiKey: process.env.FIREBASE_API_KEY,
        authDomain: process.env.FIREBASE_AUTH_DOMAIN,
        projectId: process.env.FIREBASE_PROJECT_ID,
        storageBucket: process.env.FIREBASE_STORAGE_BUCKET,
        messagingSenderId: process.env.FIREBASE_MESSAGING_SENDER_ID,
        appId: process.env.FIREBASE_APP_ID
    },
    
    // --- Core App Functionality ---
    runScript: (args) => ipcRenderer.send('run-script', args),
    onScriptReply: (callback) => ipcRenderer.on('script-reply', (_event, value) => callback(value)),

    // --- Settings & Store ---
    getStoreValue: (key) => ipcRenderer.invoke('store:get', key),
    setStoreValue: (key, value) => ipcRenderer.send('store:set', { key, value }),
    getDefaultPath: () => ipcRenderer.invoke('get-default-path'),

    // --- Dialogs & System ---
    showOpenFileDialog: (options) => ipcRenderer.invoke('dialog:openFile', options),
    showOpenDirectoryDialog: () => ipcRenderer.invoke('dialog:openDirectory'),
    showConfirmDialog: (options) => ipcRenderer.invoke('dialog:showMessageBox', options),
    openPath: (path) => ipcRenderer.send('shell:openPath', path),
    openExternalLink: (url) => ipcRenderer.send('shell:openExternal', url),
    
    // --- General Utilities ---
    log: (level, message) => ipcRenderer.send('log:log', { level, message }),
});
