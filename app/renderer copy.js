const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    // --- Authentication & Page Navigation ---
    loadAccountPage: () => ipcRenderer.send('load-account-page'),
    startMainApp: () => ipcRenderer.send('start-main-app'),
    returnToLogin: () => ipcRenderer.send('return-to-login'),
    openExternalLink: (url) => ipcRenderer.send('shell:openExternal', url),
    openPath: (path) => ipcRenderer.send('shell:openPath', path),
    navigate: (page) => ipcRenderer.send('navigate', page),
    
    // --- User & Firebase Data ---
    getUserData: () => ({
        uid: sessionStorage.getItem('userUID'),
        name: sessionStorage.getItem('userName'),
        email: sessionStorage.getItem('userEmail'),
        tokens: sessionStorage.getItem('userTokens')
    }),
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

    // --- File & Folder Operations ---
    getOutputPath: () => ipcRenderer.invoke('get-output-path'),
    openOutputFolder: () => ipcRenderer.send('open-output-folder'),
    changeOutputFolder: () => ipcRenderer.send('change-output-folder'),
    resetOutputFolder: () => ipcRenderer.send('reset-output-folder'),
    onOutputPathChanged: (callback) => ipcRenderer.on('output-path-changed', (_event, value) => callback(value)),
    selectFiles: (options) => ipcRenderer.invoke('select-files', options),
    selectFolder: () => ipcRenderer.invoke('select-folder'),
    
    // ADDED: Expose the confirmation dialog function
    showConfirmDialog: (options) => ipcRenderer.invoke('show-confirm-dialog', options),

    // --- General Utilities ---
    openExternalLink: (url) => ipcRenderer.send('open-external-link', url),
    log: (level, message) => ipcRenderer.send('log', { level, message }),
    updateFinalCoinBalance: (data) => ipcRenderer.send('update-final-coin-balance', data),

});