// login.js

// =============================================================================
// SECTION 1: IMPORTS & FIREBASE INITIALIZATION
// =============================================================================
import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js";
import { getFirestore, doc, setDoc, getDoc } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";

// --- Crucial Preload Script Check ---
if (!window.electronAPI) {
    throw new Error("FATAL: The 'electronAPI' object is not available. The preload script may have failed to run.");
}

// --- Firebase Configuration ---
const firebaseConfig = window.electronAPI.firebaseConfig;
if (!firebaseConfig || !firebaseConfig.apiKey) {
    throw new Error("FATAL: Firebase configuration is missing or invalid. Check your .env file and the preload script.");
}

// --- Initialize Firebase Services ---
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const googleProvider = new GoogleAuthProvider();


// =============================================================================
// SECTION 2: UI HELPER
// =============================================================================

/**
 * Displays a status message to the user.
 * @param {string} message - The message to display.
 * @param {boolean} [isError=false] - If true, styles the message as an error.
 */
function updateStatus(message, isError = false) {
    const statusMessage = document.getElementById('statusMessage');
    statusMessage.textContent = message;
    statusMessage.className = isError ? 'status-error' : 'status-success';
    statusMessage.classList.remove('hidden');
}


// =============================================================================
// SECTION 3: CORE LOGIC
// =============================================================================
document.addEventListener('DOMContentLoaded', () => {
    const googleLoginBtn = document.getElementById('googleLoginBtn');

    googleLoginBtn.addEventListener('click', async () => {
        googleLoginBtn.disabled = true;
        updateStatus("Awaiting Google Sign-in...");

        try {
            const result = await signInWithPopup(auth, googleProvider);
            const user = result.user;

            updateStatus("Login successful, checking user data...");

            // Check if the user is new. If so, create their document in Firestore.
            const userDocRef = doc(db, "artifacts", "appliedai-companion", "users", user.uid);
            const userDocSnap = await getDoc(userDocRef);

            if (!userDocSnap.exists()) {
                console.log(`[Login] Creating new user document for UID: ${user.uid}`);
                await setDoc(userDocRef, {
                    name: user.displayName || "New User",
                    email: user.email,
                    tokens: 2 // Set initial token balance for new users
                });
            }
            
            updateStatus("Redirecting to account dashboard...");
            // Simply tell Electron to load the next page.
            window.electronAPI.loadAccountPage();

        } catch (error) {
            console.error(`[Login] Google sign-in error: ${error.code} - ${error.message}`);
            updateStatus(`Login Error: ${error.message}`, true);
            googleLoginBtn.disabled = false; // Re-enable button on error
        }
    });
});