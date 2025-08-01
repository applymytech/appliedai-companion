// account.js

// =============================================================================
// SECTION 1: IMPORTS & FIREBASE INITIALIZATION
// =============================================================================
import { getFirestore, doc, getDoc, onSnapshot } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js";
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";

// --- Crucial Preload Script Check ---
if (!window.electronAPI) {
    throw new Error("FATAL: The 'electronAPI' object is not available. The preload script may have failed to run.");
}

const firebaseConfig = window.electronAPI.firebaseConfig;
if (!firebaseConfig || !firebaseConfig.apiKey) {
    throw new Error("FATAL: Firebase configuration is missing or invalid. Check your .env file and the preload script.");
}

// --- Initialize Firebase Services ---
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app); // Get the auth instance


// =============================================================================
// SECTION 2: CORE LOGIC & AUTH STATE LISTENER
// =============================================================================

// onAuthStateChanged is the gatekeeper. The code inside only runs AFTER
// Firebase has determined the user's authentication status.
onAuthStateChanged(auth, (user) => {
    const loadingSpinner = document.getElementById('loadingSpinner');
    const loadingMessage = document.getElementById('loadingMessage');
    const accountContainer = document.getElementById('accountContainer');
    const startAppBtn = document.getElementById('startAppBtn');

    if (user) {
        // --- USER IS LOGGED IN ---
        console.log(`[Account Page] Auth state confirmed for user: ${user.uid}`);
        
        // Now that we have the authenticated user, we can safely fetch their data.
        initializeAccountPage(user.uid);

    } else {
        // --- USER IS NOT LOGGED IN ---
        console.error('[Account Page] No authenticated user found. Redirecting to login.');
        loadingSpinner.classList.add('hidden');
        accountContainer.querySelector('h1').textContent = 'Authentication Error';
        loadingMessage.textContent = 'No user session found. Please log in again.';
        loadingMessage.classList.remove('hidden');
        
        // Redirect back to login after a short delay
        setTimeout(() => {
            window.electronAPI.returnToLogin();
        }, 2000);
    }
});


/**
 * Initializes the account page after authentication is confirmed.
 * Fetches data and sets up listeners.
 * @param {string} uid The authenticated user's ID.
 */
async function initializeAccountPage(uid) {
    // --- Element References ---
    const userNameSpan = document.getElementById('userName');
    const userEmailSpan = document.getElementById('userEmail');
    const userTokensSpan = document.getElementById('userTokens');
    const accountInfo = document.getElementById('accountInfo');
    const startAppBtn = document.getElementById('startAppBtn');
    const accountContainer = document.getElementById('accountContainer');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const loadingMessage = document.getElementById('loadingMessage');

    // --- Firestore Document References ---
    const userDocRef = doc(db, "artifacts", "appliedai-companion", "users", uid);
    const appConfigDocRef = doc(db, "app_config", "announcement");

    // --- Real-time Listener for User Tokens ---
    const unsubscribe = onSnapshot(userDocRef, (docSnap) => {
        if (docSnap.exists()) {
            userTokensSpan.textContent = docSnap.data().tokens;
        }
    }, (error) => {
        console.error(`[Account Page] Real-time listener failed: ${error.message}`);
    });

// --- Initial Data Fetch & UI Setup ---
    try {
        const userDocSnap = await getDoc(userDocRef);
        if (userDocSnap.exists()) {
            const data = userDocSnap.data();
            
            // Populate UI
            userNameSpan.textContent = data.name || "User";
            userEmailSpan.textContent = data.email;
            userTokensSpan.textContent = data.tokens;

            // FIX: Store the fetched data in sessionStorage for the main app.
            // This prepares the necessary data for the next page (companion_renderer.js).
            sessionStorage.setItem('userUID', uid);
            sessionStorage.setItem('userName', data.name || "User");
            sessionStorage.setItem('userEmail', data.email);
            sessionStorage.setItem('userTokens', data.tokens);

            // Show account info and hide loading indicators
            loadingSpinner.classList.add('hidden');
            loadingMessage.classList.add('hidden');
            accountContainer.querySelector('h1').textContent = 'Account Dashboard';
            accountInfo.classList.remove('hidden');
            startAppBtn.classList.remove('hidden');

            // Fetch announcement
            const announcementDocSnap = await getDoc(appConfigDocRef);
            if (announcementDocSnap.exists() && announcementDocSnap.data().is_active) {
                const message = announcementDocSnap.data().message;
                const announcementDiv = document.createElement('div');
                announcementDiv.className = 'announcement-banner';
                announcementDiv.textContent = message;
                accountContainer.prepend(announcementDiv);
            }

        } else {
            throw new Error("Your user data could not be found in the database.");
        }
    } catch (error) {
        console.error(`[Account Page] Error loading initial data: ${error.message}`);
        loadingSpinner.classList.add('hidden');
        accountContainer.querySelector('h1').textContent = 'Loading Error';
        loadingMessage.textContent = `An error occurred: ${error.message}`;
        loadingMessage.classList.remove('hidden');
        startAppBtn.disabled = true;
    }

    // --- Button Event Listener ---
    startAppBtn.addEventListener('click', () => {
        unsubscribe(); // Detach the real-time listener before leaving the page
        window.electronAPI.startMainApp();
    });
}
